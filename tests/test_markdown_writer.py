"""markdown_writer 的单元测试。"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from leetcode_solutions.markdown_writer import (
    bucket_name,
    problem_output_path,
    read_existing_languages,
    read_existing_solutions,
    write_problem,
)


class MarkdownWriterTest(unittest.TestCase):
    """验证路径分桶、文件名和 Markdown 格式。"""

    def test_bucket_and_path(self) -> None:
        """题号应按每 100 题分桶，并使用四位补零文件名。"""

        problem = {"frontend_id": "1", "difficulty": "Easy", "problem_slug": "two-sum"}
        path = problem_output_path(problem, Path("/tmp/out"))
        self.assertEqual("1-100", bucket_name(1))
        self.assertEqual(Path("/tmp/out/easy/1-100/0001-two-sum.md"), path)

    def test_write_and_read_languages(self) -> None:
        """写出的 Markdown 应能被 resume 逻辑读回语言标题。"""

        problem = {"frontend_id": "1", "difficulty": "Easy", "problem_slug": "two-sum", "title": "Two Sum"}
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "easy/1-100/0001-two-sum.md"
            write_problem(path, problem, {"python3": "class Solution:\n    pass"})
            text = path.read_text(encoding="utf-8")
            languages = read_existing_languages(path)

        self.assertIn("# 0001. Two Sum", text)
        self.assertIn("## Python3", text)
        self.assertIn("```python", text)
        self.assertEqual({"Python3"}, languages)

    def test_read_existing_solutions_preserves_language_order(self) -> None:
        """已有 Markdown 代码块应按数据集语言顺序读回。"""

        problem = {"frontend_id": "1", "difficulty": "Hard", "problem_slug": "two-sum", "title": "Two Sum"}
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "hard/1-100/0001-two-sum.md"
            write_problem(path, problem, {"python3": "python code", "cpp": "cpp code"})
            solutions = read_existing_solutions(path, ["cpp", "python3", "kotlin"])

        self.assertEqual(["cpp", "python3"], list(solutions.keys()))
        self.assertEqual("cpp code", solutions["cpp"])
        self.assertEqual("python code", solutions["python3"])

    def test_existing_language_requires_non_empty_code_block(self) -> None:
        """只有标题或空代码块不应被当作已完成语言。"""

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "hard/1-100/0004-median-of-two-sorted-arrays.md"
            path.parent.mkdir(parents=True)
            path.write_text(
                "# 0004. Median of Two Sorted Arrays\n\n"
                "## Cpp\n\n"
                "```cpp\n"
                "\n"
                "```\n\n"
                "## Kotlin\n\n"
                "## Java\n\n"
                "```java\n"
                "class Solution {}\n"
                "```\n",
                encoding="utf-8",
            )
            languages = read_existing_languages(path)
            solutions = read_existing_solutions(path, ["cpp", "kotlin", "java"])

        self.assertEqual({"Java"}, languages)
        self.assertEqual(["java"], list(solutions.keys()))


if __name__ == "__main__":
    unittest.main()
