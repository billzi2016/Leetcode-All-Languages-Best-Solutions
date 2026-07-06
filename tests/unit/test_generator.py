"""generator 的单元测试。"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from leetcode_solutions.generator import SolutionGenerator


class FakeClient:
    """用于测试的模型客户端。"""

    def __init__(self) -> None:
        """记录调用次数并返回固定代码。"""

        self.calls: list[str] = []

    def generate(self, *, difficulty: str, system_prompt: str, problem_prompt: str, language_prompt: str) -> str:
        """模拟一次模型生成。"""

        self.calls.append(language_prompt)
        return "class Solution:\n    pass"


class FakeLogger:
    """用于测试的日志器。"""

    def __init__(self) -> None:
        """保存日志和失败记录。"""

        self.messages: list[str] = []
        self.failures: list[dict] = []

    def info(self, message: str) -> None:
        """记录普通信息。"""

        self.messages.append(message)

    def warn(self, message: str) -> None:
        """记录警告信息。"""

        self.messages.append(message)

    def error(self, message: str) -> None:
        """记录错误信息。"""

        self.messages.append(message)

    def failure(self, record: dict) -> None:
        """记录结构化失败。"""

        self.failures.append(record)


class GeneratorTest(unittest.TestCase):
    """验证生成器主流程。"""

    def test_generate_problem_writes_markdown(self) -> None:
        """单题生成应写出 Markdown 文件。"""

        problem = {
            "frontend_id": "1",
            "difficulty": "Easy",
            "problem_slug": "two-sum",
            "title": "Two Sum",
            "code_snippets": {"python3": "class Solution:\n    pass"},
        }
        with tempfile.TemporaryDirectory() as tmp:
            client = FakeClient()
            path = SolutionGenerator(client, FakeLogger(), Path(tmp)).generate_problem(problem)
            text = path.read_text(encoding="utf-8")

        self.assertEqual(1, len(client.calls))
        self.assertIn("## Python3", text)

    def test_hard_resume_keeps_existing_languages(self) -> None:
        """Hard 续跑补缺失语言时不应覆盖已有语言。"""

        problem = {
            "frontend_id": "4",
            "difficulty": "Hard",
            "problem_slug": "median-of-two-sorted-arrays",
            "title": "Median of Two Sorted Arrays",
            "code_snippets": {"cpp": "class Solution {};", "kotlin": "class Solution {}"},
        }
        with tempfile.TemporaryDirectory() as tmp:
            output_root = Path(tmp)
            existing_path = output_root / "Leetcode-Hard/0001-0100/0004-median-of-two-sorted-arrays.md"
            existing_path.parent.mkdir(parents=True)
            existing_path.write_text(
                "# 0004. Median of Two Sorted Arrays\n\n"
                "## Cpp\n\n"
                "```cpp\n"
                "class ExistingCpp {}\n"
                "```\n",
                encoding="utf-8",
            )

            client = FakeClient()
            path = SolutionGenerator(client, FakeLogger(), output_root).generate_problem(problem)
            text = path.read_text(encoding="utf-8")

        self.assertEqual(1, len(client.calls))
        self.assertIn("## Cpp", text)
        self.assertIn("class ExistingCpp {}", text)
        self.assertIn("## Kotlin", text)
        self.assertIn("class Solution:", text)

    def test_hard_resume_repairs_kotlin_only_old_file(self) -> None:
        """旧 bug 只留下 Kotlin 时，应补齐前置语言并恢复标准顺序。"""

        problem = {
            "frontend_id": "4",
            "difficulty": "Hard",
            "problem_slug": "median-of-two-sorted-arrays",
            "title": "Median of Two Sorted Arrays",
            "code_snippets": {
                "cpp": "class Solution {};",
                "java": "class Solution {}",
                "kotlin": "class Solution {}",
            },
        }
        with tempfile.TemporaryDirectory() as tmp:
            output_root = Path(tmp)
            existing_path = output_root / "Leetcode-Hard/0001-0100/0004-median-of-two-sorted-arrays.md"
            existing_path.parent.mkdir(parents=True)
            existing_path.write_text(
                "# 0004. Median of Two Sorted Arrays\n\n"
                "## Kotlin\n\n"
                "```kotlin\n"
                "class ExistingKotlin {}\n"
                "```\n",
                encoding="utf-8",
            )

            client = FakeClient()
            path = SolutionGenerator(client, FakeLogger(), output_root).generate_problem(problem)
            text = path.read_text(encoding="utf-8")

        self.assertEqual(2, len(client.calls))
        self.assertLess(text.index("## Cpp"), text.index("## Java"))
        self.assertLess(text.index("## Java"), text.index("## Kotlin"))
        self.assertIn("class ExistingKotlin {}", text)

    def test_complete_problem_with_wrong_language_order_is_rewritten(self) -> None:
        """完整但 Kotlin 在前的旧文件应无需模型调用直接修正顺序。"""

        problem = {
            "frontend_id": "4",
            "difficulty": "Hard",
            "problem_slug": "median-of-two-sorted-arrays",
            "title": "Median of Two Sorted Arrays",
            "code_snippets": {"cpp": "class Solution {};", "kotlin": "class Solution {}"},
        }
        with tempfile.TemporaryDirectory() as tmp:
            output_root = Path(tmp)
            existing_path = output_root / "Leetcode-Hard/0001-0100/0004-median-of-two-sorted-arrays.md"
            existing_path.parent.mkdir(parents=True)
            existing_path.write_text(
                "# 0004. Median of Two Sorted Arrays\n\n"
                "## Kotlin\n\n"
                "```kotlin\n"
                "class ExistingKotlin {}\n"
                "```\n\n"
                "## Cpp\n\n"
                "```cpp\n"
                "class ExistingCpp {}\n"
                "```\n",
                encoding="utf-8",
            )

            client = FakeClient()
            path = SolutionGenerator(client, FakeLogger(), output_root).generate_problem(problem)
            text = path.read_text(encoding="utf-8")

        self.assertEqual([], client.calls)
        self.assertLess(text.index("## Cpp"), text.index("## Kotlin"))
        self.assertIn("class ExistingCpp {}", text)
        self.assertIn("class ExistingKotlin {}", text)


if __name__ == "__main__":
    unittest.main()
