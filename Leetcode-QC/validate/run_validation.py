#!/usr/bin/env python3
"""运行题解样例验证并输出按难度拆分的 CSV 矩阵。

脚本从 `dataset/merged_problems.json` 读取题目和 LeetCode examples，
从仓库的 `Leetcode-Easy/`、`Leetcode-Medium/`、`Leetcode-Hard/`
目录读取已经生成的 Markdown 题解。
每个语言代码块会被包装成对应语言的最小 LeetCode 测试入口，并在临时
工作目录里编译或运行。

CSV 输出规则保持简单稳定：

- 每个难度一个 CSV；
- 每一行是一道题；
- 每个语言列只写 `1` 或 `0`；
- `1` 表示该语言代码通过该题内置样例；
- `0` 表示缺少代码、语言 runner 不支持、编译失败、运行失败或结果不一致。
"""

from __future__ import annotations

import argparse
import ast
import csv
import json
import re
import shutil
import subprocess
import textwrap
from dataclasses import dataclass
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any, Callable


DIFFICULTIES = ("Easy", "Medium", "Hard")
DIFFICULTY_DIRS = {
    "Easy": "Leetcode-Easy",
    "Medium": "Leetcode-Medium",
    "Hard": "Leetcode-Hard",
}
LANGUAGE_HEADINGS = {
    "Bash": "bash",
    "C": "c",
    "Cpp": "cpp",
    "Java": "java",
    "Javascript": "javascript",
    "JavaScript": "javascript",
    "Python": "python",
    "Python3": "python3",
}
SUPPORTED_LANGUAGES = {"cpp", "java", "javascript", "python", "python3"}


@dataclass(frozen=True)
class ValidationProblem:
    """从 dataset 读取出的验证题配置。

    参数：
        frontend_id: LeetCode 展示题号。
        title: 题目标题。
        difficulty: 题目难度。
        slug: Markdown 文件名中的 slug。
        method: 从 starter code 推导出的 LeetCode Solution 方法名。
        kind: runner 使用的题型模板；不支持的题型会保留 CSV 行并输出 0。
        languages: dataset 中该题声明的语言 key。
        cases: 从 examples.example_text 解析出的样例列表。
    """

    frontend_id: str
    title: str
    difficulty: str
    slug: str
    method: str
    kind: str
    languages: list[str]
    cases: list[dict[str, Any]]

    @property
    def padded_id(self) -> str:
        """返回四位补零题号。"""

        return f"{int(self.frontend_id):04d}"


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""

    parser = argparse.ArgumentParser(description="Validate generated solution Markdown with sample cases.")
    parser.add_argument("--repo-root", type=Path, default=Path.cwd(), help="Repository root path.")
    parser.add_argument(
        "--dataset",
        type=Path,
        default=Path("dataset/merged_problems.json"),
        help="Merged dataset JSON path, relative to repo root unless absolute.",
    )
    parser.add_argument(
        "--reports-dir",
        type=Path,
        default=Path("Leetcode-QC/validate/reports"),
        help="CSV output directory, relative to repo root unless absolute.",
    )
    parser.add_argument(
        "--work-dir",
        type=Path,
        default=None,
        help="Optional persistent work directory for generated harness files.",
    )
    parser.add_argument("--timeout", type=float, default=10.0, help="Compile/run timeout per language and problem.")
    return parser.parse_args()


def bucket_name(frontend_id: int) -> str:
    """返回题号对应的固定宽度分桶目录名。"""

    start = ((frontend_id - 1) // 100) * 100 + 1
    end = start + 99
    return f"{start:04d}-{end:04d}"


def parse_literal(value: str) -> Any:
    """把 LeetCode example 文本中的值转换为 Python 对象。"""

    value = value.strip()
    if value == "true":
        return True
    if value == "false":
        return False
    if value == "null":
        return None
    return ast.literal_eval(value)


def parse_input_values(input_text: str) -> dict[str, Any]:
    """解析 `Input:` 后面的逗号分隔参数。"""

    values: dict[str, Any] = {}
    for match in re.finditer(r"(\w+)\s*=", input_text):
        name = match.group(1)
        value_start = match.end()
        next_match = re.search(r",\s*\w+\s*=", input_text[value_start:])
        value_end = value_start + next_match.start() if next_match else len(input_text)
        raw_value = input_text[value_start:value_end].strip().rstrip(",")
        values[name] = parse_literal(raw_value)
    return values


def parse_example_text(example_text: str) -> dict[str, Any] | None:
    """从 dataset 的 LeetCode example 文本中提取输入和输出。"""

    input_match = re.search(r"Input:\s*(.*?)(?:\n|$)Output:", example_text, flags=re.DOTALL)
    output_match = re.search(r"Output:\s*(.*?)(?:\n(?:Explanation|Note):|$)", example_text, flags=re.DOTALL)
    if input_match is None or output_match is None:
        return None
    try:
        parsed = parse_input_values(input_match.group(1).strip())
        parsed["expected"] = parse_literal(output_match.group(1).strip())
        return parsed
    except (SyntaxError, ValueError):
        return None


def infer_method(code_snippets: dict[str, str]) -> str:
    """从 starter code 中推导 Solution 方法名。"""

    for language in ("python3", "python", "cpp", "java", "javascript"):
        code = code_snippets.get(language, "")
        for pattern in (
            r"def\s+([A-Za-z_]\w*)\s*\(",
            r"\b(?:vector<[^>]+>|int|bool|string|ListNode\*?|TreeNode\*?)\s+([A-Za-z_]\w*)\s*\(",
            r"\b(?:public\s+)?(?:int\[\]|boolean|int|String|ListNode)\s+([A-Za-z_]\w*)\s*\(",
            r"(?:var|let|const|function)\s+([A-Za-z_]\w*)\s*=",
            r"function\s+([A-Za-z_]\w*)\s*\(",
        ):
            match = re.search(pattern, code)
            if match:
                return match.group(1)
    return ""


def infer_kind(slug: str, method: str) -> str:
    """把已支持的 LeetCode 方法归类为 runner 模板。"""

    by_method = {
        "twoSum": "array_int_target_indices",
        "addTwoNumbers": "linked_list_addition",
        "isValid": "string_bool",
        "mergeTwoLists": "merge_two_sorted_lists",
        "maxProfit": "array_int_result",
    }
    return by_method.get(method, f"unsupported:{slug}")


def load_validation_problems(path: Path) -> list[ValidationProblem]:
    """从 `dataset/merged_problems.json` 读取题目和样例。"""

    data = json.loads(path.read_text(encoding="utf-8"))
    questions = data.get("questions", data if isinstance(data, list) else [])
    problems: list[ValidationProblem] = []
    for question in questions:
        snippets = question.get("code_snippets") or {}
        examples = question.get("examples") or []
        cases = [
            parsed
            for example in examples
            if (parsed := parse_example_text(str(example.get("example_text", "")))) is not None
        ]
        method = infer_method(snippets)
        slug = str(question.get("problem_slug", ""))
        problems.append(
            ValidationProblem(
                frontend_id=str(question.get("frontend_id", "")),
                title=str(question.get("title", "")),
                difficulty=str(question.get("difficulty", "")),
                slug=slug,
                method=method,
                kind=infer_kind(slug, method),
                languages=list(snippets.keys()),
                cases=cases,
            )
        )
    return problems


def solution_path(repo_root: Path, problem: ValidationProblem) -> Path:
    """返回样例题对应的 Markdown 题解路径。"""

    frontend_id = int(problem.frontend_id)
    return (
        repo_root
        / DIFFICULTY_DIRS.get(problem.difficulty, problem.difficulty)
        / bucket_name(frontend_id)
        / f"{frontend_id:04d}-{problem.slug}.md"
    )


def parse_markdown_sections(path: Path) -> dict[str, str]:
    """解析 Markdown 中的语言代码块。

    参数：
        path: 单题 Markdown 文件路径。

    返回：
        dict[str, str]: 语言 key 到代码文本的映射。未知标题会保留为小写标题，
        方便 CSV 动态出现对应列。
    """

    if not path.exists():
        return {}

    text = path.read_text(encoding="utf-8")
    sections: dict[str, str] = {}
    headings = list(re.finditer(r"^##\s+(.+?)\s*$", text, flags=re.MULTILINE))
    for index, match in enumerate(headings):
        heading = match.group(1).strip()
        section_start = match.end()
        section_end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        section = text[section_start:section_end]
        code_match = re.search(r"```[^\n]*\n(.*?)\n```", section, flags=re.DOTALL)
        if not code_match:
            continue
        code = code_match.group(1).strip("\n")
        if not code.strip():
            continue
        language = LANGUAGE_HEADINGS.get(heading, heading.lower())
        sections[language] = code
    return sections


def run_command(command: list[str], cwd: Path, timeout: float) -> bool:
    """运行编译或执行命令，成功返回 True。"""

    try:
        completed = subprocess.run(
            command,
            cwd=cwd,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return False
    return completed.returncode == 0


def python_literal(value: Any) -> str:
    """把 JSON 值渲染成 Python 字面量。"""

    return repr(value)


def js_literal(value: Any) -> str:
    """把 JSON 值渲染成 JavaScript 字面量。"""

    return json.dumps(value)


def cpp_vector(value: list[Any]) -> str:
    """把整数列表渲染成 C++ vector 初始化表达式。"""

    return "{" + ", ".join(str(item).lower() for item in value) + "}"


def java_array(value: list[Any]) -> str:
    """把整数列表渲染成 Java int[] 初始化表达式。"""

    return "new int[]{" + ", ".join(str(item) for item in value) + "}"


def java_string(value: str) -> str:
    """把字符串渲染成 Java 字符串字面量。"""

    return json.dumps(value)


def python_expected_expr(problem: ValidationProblem, case: dict[str, Any]) -> str:
    """返回 Python harness 中的单个样例断言代码。"""

    expected = python_literal(case["expected"])
    if problem.kind == "array_int_target_indices":
        return (
            f"out = Solution().{problem.method}({python_literal(case['nums'])}, {case['target']})\n"
            f"assert sorted(out) == {expected}, out"
        )
    if problem.kind == "string_bool":
        return f"assert Solution().{problem.method}({python_literal(case['s'])}) == {expected}"
    if problem.kind == "array_int_result":
        array_key = "prices" if "prices" in case else "nums"
        return f"assert Solution().{problem.method}({python_literal(case[array_key])}) == {expected}"
    if problem.kind == "linked_list_addition":
        return (
            f"out = Solution().{problem.method}(build_list({python_literal(case['l1'])}), "
            f"build_list({python_literal(case['l2'])}))\n"
            f"assert list_to_array(out) == {expected}"
        )
    if problem.kind == "merge_two_sorted_lists":
        return (
            f"out = Solution().{problem.method}(build_list({python_literal(case['list1'])}), "
            f"build_list({python_literal(case['list2'])}))\n"
            f"assert list_to_array(out) == {expected}"
        )
    raise ValueError(f"unsupported problem kind for Python: {problem.kind}")


def build_python_harness(problem: ValidationProblem, code: str) -> str:
    """生成 Python/Python3 测试入口。"""

    assertions = "\n".join(textwrap.indent(python_expected_expr(problem, case), "    ") for case in problem.cases)
    return (
        "from __future__ import annotations\n"
        "from typing import List, Optional\n\n"
        "class ListNode:\n"
        "    def __init__(self, val=0, next=None):\n"
        "        self.val = val\n"
        "        self.next = next\n\n"
        "def build_list(values):\n"
        "    dummy = ListNode(0)\n"
        "    cur = dummy\n"
        "    for value in values:\n"
        "        cur.next = ListNode(value)\n"
        "        cur = cur.next\n"
        "    return dummy.next\n\n"
        "def list_to_array(node):\n"
        "    values = []\n"
        "    while node is not None:\n"
        "        values.append(node.val)\n"
        "        node = node.next\n"
        "    return values\n\n"
        f"{code}\n\n"
        "def main():\n"
        f"{assertions}\n\n"
        "if __name__ == '__main__':\n"
        "    main()\n"
    )


def validate_python(problem: ValidationProblem, code: str, work_dir: Path, timeout: float) -> bool:
    """运行 Python/Python3 题解样例。"""

    path = work_dir / "solution.py"
    path.write_text(build_python_harness(problem, code), encoding="utf-8")
    return run_command(["python", str(path)], work_dir, timeout)


def cpp_assertion(problem: ValidationProblem, case: dict[str, Any]) -> str:
    """返回 C++ harness 中的单个样例断言代码。"""

    if problem.kind == "array_int_target_indices":
        return (
            f"{{ vector<int> nums = {cpp_vector(case['nums'])}; "
            f"auto out = Solution().{problem.method}(nums, {case['target']}); "
            f"sort(out.begin(), out.end()); vector<int> expected = {cpp_vector(case['expected'])}; "
            "if (out != expected) return 1; }"
        )
    if problem.kind == "string_bool":
        expected = "true" if case["expected"] else "false"
        return f"if (Solution().{problem.method}({json.dumps(case['s'])}) != {expected}) return 1;"
    if problem.kind == "array_int_result":
        array_key = "prices" if "prices" in case else "nums"
        return (
            f"{{ vector<int> values = {cpp_vector(case[array_key])}; "
            f"if (Solution().{problem.method}(values) != {case['expected']}) return 1; }}"
        )
    if problem.kind == "linked_list_addition":
        return (
            f"if (toVector(Solution().{problem.method}(buildList({cpp_vector(case['l1'])}), "
            f"buildList({cpp_vector(case['l2'])}))) != vector<int>{cpp_vector(case['expected'])}) return 1;"
        )
    if problem.kind == "merge_two_sorted_lists":
        return (
            f"if (toVector(Solution().{problem.method}(buildList({cpp_vector(case['list1'])}), "
            f"buildList({cpp_vector(case['list2'])}))) != vector<int>{cpp_vector(case['expected'])}) return 1;"
        )
    raise ValueError(f"unsupported problem kind for Cpp: {problem.kind}")


def build_cpp_harness(problem: ValidationProblem, code: str) -> str:
    """生成 C++ 测试入口。"""

    assertions = "\n".join("    " + cpp_assertion(problem, case) for case in problem.cases)
    return (
        "#include <bits/stdc++.h>\n"
        "using namespace std;\n\n"
        "struct ListNode {\n"
        "    int val;\n"
        "    ListNode *next;\n"
        "    ListNode() : val(0), next(nullptr) {}\n"
        "    ListNode(int x) : val(x), next(nullptr) {}\n"
        "    ListNode(int x, ListNode *next) : val(x), next(next) {}\n"
        "};\n\n"
        "ListNode* buildList(vector<int> values) {\n"
        "    ListNode dummy(0);\n"
        "    ListNode* cur = &dummy;\n"
        "    for (int value : values) { cur->next = new ListNode(value); cur = cur->next; }\n"
        "    return dummy.next;\n"
        "}\n\n"
        "vector<int> toVector(ListNode* node) {\n"
        "    vector<int> values;\n"
        "    while (node) { values.push_back(node->val); node = node->next; }\n"
        "    return values;\n"
        "}\n\n"
        f"{code}\n\n"
        "int main() {\n"
        f"{assertions}\n"
        "    return 0;\n"
        "}\n"
    )


def validate_cpp(problem: ValidationProblem, code: str, work_dir: Path, timeout: float) -> bool:
    """编译并运行 C++ 题解样例。"""

    source = work_dir / "solution.cpp"
    binary = work_dir / "solution"
    source.write_text(build_cpp_harness(problem, code), encoding="utf-8")
    if not run_command(["g++", "-std=c++17", "-O2", str(source), "-o", str(binary)], work_dir, timeout):
        return False
    return run_command([str(binary)], work_dir, timeout)


def java_assertion(problem: ValidationProblem, case: dict[str, Any]) -> str:
    """返回 Java harness 中的单个样例断言代码。"""

    if problem.kind == "array_int_target_indices":
        return (
            f"{{ int[] nums = {java_array(case['nums'])}; "
            f"int[] out = new Solution().{problem.method}(nums, {case['target']}); "
            f"java.util.Arrays.sort(out); int[] expected = {java_array(case['expected'])}; "
            "if (!java.util.Arrays.equals(out, expected)) throw new RuntimeException(); }}"
        )
    if problem.kind == "string_bool":
        expected = "true" if case["expected"] else "false"
        return f"if (new Solution().{problem.method}({java_string(case['s'])}) != {expected}) throw new RuntimeException();"
    if problem.kind == "array_int_result":
        array_key = "prices" if "prices" in case else "nums"
        return (
            f"if (new Solution().{problem.method}({java_array(case[array_key])}) != {case['expected']}) "
            "throw new RuntimeException();"
        )
    if problem.kind == "linked_list_addition":
        return (
            f"if (!java.util.Arrays.equals(toArray(new Solution().{problem.method}(buildList({java_array(case['l1'])}), "
            f"buildList({java_array(case['l2'])}))), {java_array(case['expected'])})) throw new RuntimeException();"
        )
    if problem.kind == "merge_two_sorted_lists":
        return (
            f"if (!java.util.Arrays.equals(toArray(new Solution().{problem.method}(buildList({java_array(case['list1'])}), "
            f"buildList({java_array(case['list2'])}))), {java_array(case['expected'])})) throw new RuntimeException();"
        )
    raise ValueError(f"unsupported problem kind for Java: {problem.kind}")


def build_java_harness(problem: ValidationProblem, code: str) -> str:
    """生成 Java 测试入口。"""

    assertions = "\n".join("        " + java_assertion(problem, case) for case in problem.cases)
    return (
        "import java.util.*;\n\n"
        "class ListNode {\n"
        "    int val;\n"
        "    ListNode next;\n"
        "    ListNode() {}\n"
        "    ListNode(int val) { this.val = val; }\n"
        "    ListNode(int val, ListNode next) { this.val = val; this.next = next; }\n"
        "}\n\n"
        f"{code}\n\n"
        "public class Main {\n"
        "    static ListNode buildList(int[] values) {\n"
        "        ListNode dummy = new ListNode(0);\n"
        "        ListNode cur = dummy;\n"
        "        for (int value : values) { cur.next = new ListNode(value); cur = cur.next; }\n"
        "        return dummy.next;\n"
        "    }\n"
        "    static int[] toArray(ListNode node) {\n"
        "        ArrayList<Integer> values = new ArrayList<>();\n"
        "        while (node != null) { values.add(node.val); node = node.next; }\n"
        "        int[] out = new int[values.size()];\n"
        "        for (int i = 0; i < values.size(); i++) out[i] = values.get(i);\n"
        "        return out;\n"
        "    }\n"
        "    public static void main(String[] args) {\n"
        f"{assertions}\n"
        "    }\n"
        "}\n"
    )


def validate_java(problem: ValidationProblem, code: str, work_dir: Path, timeout: float) -> bool:
    """编译并运行 Java 题解样例。"""

    source = work_dir / "Main.java"
    source.write_text(build_java_harness(problem, code), encoding="utf-8")
    if not run_command(["javac", str(source)], work_dir, timeout):
        return False
    return run_command(["java", "-cp", str(work_dir), "Main"], work_dir, timeout)


def js_assertion(problem: ValidationProblem, case: dict[str, Any]) -> str:
    """返回 JavaScript harness 中的单个样例断言代码。"""

    if problem.kind == "array_int_target_indices":
        return (
            f"{{ const out = new Solution().{problem.method}({js_literal(case['nums'])}, {case['target']}).sort((a, b) => a - b); "
            f"assert.deepStrictEqual(out, {js_literal(case['expected'])}); }}"
        )
    if problem.kind == "string_bool":
        return f"assert.strictEqual(new Solution().{problem.method}({js_literal(case['s'])}), {str(case['expected']).lower()});"
    if problem.kind == "array_int_result":
        array_key = "prices" if "prices" in case else "nums"
        return f"assert.strictEqual(new Solution().{problem.method}({js_literal(case[array_key])}), {case['expected']});"
    if problem.kind == "linked_list_addition":
        return (
            f"assert.deepStrictEqual(toArray(new Solution().{problem.method}(buildList({js_literal(case['l1'])}), "
            f"buildList({js_literal(case['l2'])}))), {js_literal(case['expected'])});"
        )
    if problem.kind == "merge_two_sorted_lists":
        return (
            f"assert.deepStrictEqual(toArray(new Solution().{problem.method}(buildList({js_literal(case['list1'])}), "
            f"buildList({js_literal(case['list2'])}))), {js_literal(case['expected'])});"
        )
    raise ValueError(f"unsupported problem kind for JavaScript: {problem.kind}")


def build_javascript_harness(problem: ValidationProblem, code: str) -> str:
    """生成 JavaScript 测试入口。"""

    assertions = "\n".join(js_assertion(problem, case) for case in problem.cases)
    return (
        "const assert = require('assert');\n\n"
        "function ListNode(val, next) {\n"
        "  this.val = (val === undefined ? 0 : val);\n"
        "  this.next = (next === undefined ? null : next);\n"
        "}\n\n"
        "function buildList(values) {\n"
        "  const dummy = new ListNode(0);\n"
        "  let cur = dummy;\n"
        "  for (const value of values) { cur.next = new ListNode(value); cur = cur.next; }\n"
        "  return dummy.next;\n"
        "}\n\n"
        "function toArray(node) {\n"
        "  const values = [];\n"
        "  while (node) { values.push(node.val); node = node.next; }\n"
        "  return values;\n"
        "}\n\n"
        f"{code}\n\n"
        "class Solution {\n"
        "  twoSum(nums, target) { return typeof twoSum === 'function' ? twoSum(nums, target) : undefined; }\n"
        "  addTwoNumbers(l1, l2) { return typeof addTwoNumbers === 'function' ? addTwoNumbers(l1, l2) : undefined; }\n"
        "  isValid(s) { return typeof isValid === 'function' ? isValid(s) : undefined; }\n"
        "  mergeTwoLists(list1, list2) { return typeof mergeTwoLists === 'function' ? mergeTwoLists(list1, list2) : undefined; }\n"
        "  maxProfit(prices) { return typeof maxProfit === 'function' ? maxProfit(prices) : undefined; }\n"
        "}\n\n"
        f"{assertions}\n"
    )


def validate_javascript(problem: ValidationProblem, code: str, work_dir: Path, timeout: float) -> bool:
    """运行 JavaScript 题解样例。"""

    source = work_dir / "solution.js"
    source.write_text(build_javascript_harness(problem, code), encoding="utf-8")
    return run_command(["node", str(source)], work_dir, timeout)


VALIDATORS: dict[str, Callable[[ValidationProblem, str, Path, float], bool]] = {
    "cpp": validate_cpp,
    "java": validate_java,
    "javascript": validate_javascript,
    "python": validate_python,
    "python3": validate_python,
}


def validate_language(problem: ValidationProblem, language: str, code: str, work_root: Path, timeout: float) -> int:
    """验证单题单语言，返回 CSV 使用的 1 或 0。"""

    validator = VALIDATORS.get(language)
    if validator is None:
        return 0

    language_work_dir = work_root / problem.padded_id / language
    if language_work_dir.exists():
        shutil.rmtree(language_work_dir)
    language_work_dir.mkdir(parents=True, exist_ok=True)
    try:
        return 1 if validator(problem, code, language_work_dir, timeout) else 0
    except Exception:
        return 0


def collect_languages(problems: list[ValidationProblem], problem_sections: dict[str, dict[str, str]]) -> list[str]:
    """收集 CSV 需要展示的语言列。"""

    languages = set(SUPPORTED_LANGUAGES)
    for problem in problems:
        languages.update(problem.languages)
    for sections in problem_sections.values():
        languages.update(sections)
    return sorted(languages)


def write_csv_reports(
    problems: list[ValidationProblem],
    sections_by_problem: dict[str, dict[str, str]],
    results: dict[str, dict[str, int]],
    reports_dir: Path,
) -> None:
    """按难度写出 CSV 验证矩阵。"""

    reports_dir.mkdir(parents=True, exist_ok=True)
    languages = collect_languages(problems, sections_by_problem)
    for difficulty in DIFFICULTIES:
        path = reports_dir / f"{difficulty.lower()}.csv"
        rows = [problem for problem in problems if problem.difficulty == difficulty]
        with path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["problem_id", "title", *languages])
            for problem in rows:
                row_results = results.get(problem.frontend_id, {})
                writer.writerow(
                    [
                        problem.padded_id,
                        problem.title,
                        *[row_results.get(language, 0) for language in languages],
                    ]
                )


def run_validation(repo_root: Path, dataset_path: Path, reports_dir: Path, work_dir: Path | None, timeout: float) -> None:
    """执行样例验证并写出 CSV。"""

    dataset_path = dataset_path if dataset_path.is_absolute() else repo_root / dataset_path
    reports_dir = reports_dir if reports_dir.is_absolute() else repo_root / reports_dir
    problems = load_validation_problems(dataset_path)
    sections_by_problem = {
        problem.frontend_id: parse_markdown_sections(solution_path(repo_root, problem))
        for problem in problems
    }
    if work_dir is not None:
        work_root = work_dir if work_dir.is_absolute() else repo_root / work_dir
        work_root.mkdir(parents=True, exist_ok=True)
        results = validate_all(problems, sections_by_problem, work_root, timeout)
    else:
        with TemporaryDirectory() as tmp:
            results = validate_all(problems, sections_by_problem, Path(tmp), timeout)
    write_csv_reports(problems, sections_by_problem, results, reports_dir)


def validate_all(
    problems: list[ValidationProblem],
    sections_by_problem: dict[str, dict[str, str]],
    work_root: Path,
    timeout: float,
) -> dict[str, dict[str, int]]:
    """验证全部样例题并返回题号到语言结果的映射。"""

    results: dict[str, dict[str, int]] = {}
    languages = collect_languages(problems, sections_by_problem)
    for problem in problems:
        sections = sections_by_problem.get(problem.frontend_id, {})
        row: dict[str, int] = {}
        for language in languages:
            code = sections.get(language)
            row[language] = validate_language(problem, language, code, work_root, timeout) if code and problem.cases else 0
        results[problem.frontend_id] = row
    return results


def main() -> int:
    """命令行入口。"""

    args = parse_args()
    run_validation(args.repo_root, args.dataset, args.reports_dir, args.work_dir, args.timeout)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
