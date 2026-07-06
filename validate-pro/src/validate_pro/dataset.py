"""Dataset loading and LeetCode example parsing for validate-pro."""

from __future__ import annotations

import ast
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DIFFICULTY_ORDER = ("Easy", "Medium", "Hard")


@dataclass(frozen=True)
class Problem:
    """Problem metadata needed by validate-pro.

    Args:
        frontend_id: LeetCode display id.
        title: Problem title.
        slug: Problem slug used in Markdown filenames.
        difficulty: Easy, Medium, or Hard.
        description: Original problem statement.
        constraints: Constraint text from the dataset.
        examples: Parsed dataset examples.
        topics: Topic tags from the dataset.
        hints: Hints from the dataset.
        code_snippets: LeetCode starter code keyed by language.
        method: Inferred Solution method name.
        kind: Supported adapter kind or an unsupported marker.
    """

    frontend_id: str
    title: str
    slug: str
    difficulty: str
    description: str
    constraints: str
    examples: list[dict[str, Any]]
    topics: list[str]
    hints: list[str]
    code_snippets: dict[str, str]
    method: str
    kind: str

    @property
    def padded_id(self) -> str:
        """Return the four-digit LeetCode id."""

        return f"{int(self.frontend_id):04d}"

    @property
    def case_filename(self) -> str:
        """Return the retained-case filename for this problem."""

        return f"{self.padded_id}-{self.slug}.json"


def parse_literal(value: str) -> Any:
    """Parse a LeetCode example literal into a Python value."""

    value = value.strip()
    if value == "true":
        return True
    if value == "false":
        return False
    if value == "null":
        return None
    return ast.literal_eval(value)


def parse_input_values(input_text: str) -> dict[str, Any]:
    """Parse `Input:` assignments such as `nums = [1,2], target = 3`."""

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
    """Parse a dataset example into `input`, `expected`, and `purpose` fields."""

    input_match = re.search(r"Input:\s*(.*?)(?:\n|$)Output:", example_text, flags=re.DOTALL)
    output_match = re.search(r"Output:\s*(.*?)(?:\n(?:Explanation|Note):|$)", example_text, flags=re.DOTALL)
    if input_match is None or output_match is None:
        return None
    try:
        return {
            "input": parse_input_values(input_match.group(1).strip()),
            "expected": parse_literal(output_match.group(1).strip()),
            "source": "dataset",
            "purpose": "dataset example",
        }
    except (SyntaxError, ValueError):
        return None


def infer_method(code_snippets: dict[str, str]) -> str:
    """Infer the LeetCode Solution method name from starter code."""

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
    """Map supported Solution methods to reference adapter kinds."""

    by_method = {
        "twoSum": "array_int_target_indices",
        "addTwoNumbers": "linked_list_addition",
        "isValid": "string_bool",
        "mergeTwoLists": "merge_two_sorted_lists",
        "maxProfit": "array_int_result",
    }
    return by_method.get(method, f"unsupported:{slug}")


def problem_from_question(question: dict[str, Any]) -> Problem:
    """Build a `Problem` from one dataset question record."""

    snippets = question.get("code_snippets") or {}
    examples = [
        parsed
        for example in (question.get("examples") or [])
        if (parsed := parse_example_text(str(example.get("example_text", "")))) is not None
    ]
    slug = str(question.get("problem_slug", ""))
    method = infer_method(snippets)
    return Problem(
        frontend_id=str(question.get("frontend_id", "")),
        title=str(question.get("title", "")),
        slug=slug,
        difficulty=str(question.get("difficulty", "")),
        description=str(question.get("description", "")),
        constraints=str(question.get("constraints", "")),
        examples=examples,
        topics=[str(topic) for topic in (question.get("topics") or [])],
        hints=[str(hint) for hint in (question.get("hints") or [])],
        code_snippets={str(key): str(value) for key, value in snippets.items()},
        method=method,
        kind=infer_kind(slug, method),
    )


def load_problems(dataset_path: Path) -> list[Problem]:
    """Load all problems from `dataset/merged_problems.json`."""

    data = json.loads(dataset_path.read_text(encoding="utf-8"))
    questions = data.get("questions", data if isinstance(data, list) else [])
    return [problem_from_question(question) for question in questions]


def select_problems(
    problems: list[Problem],
    difficulty: str | None = None,
    frontend_ids: list[str] | None = None,
) -> list[Problem]:
    """Select problems by difficulty or explicit frontend ids."""

    if frontend_ids:
        wanted = {str(frontend_id) for frontend_id in frontend_ids}
        return [problem for problem in problems if problem.frontend_id in wanted]
    if difficulty:
        return [problem for problem in problems if problem.difficulty == difficulty]
    return problems

