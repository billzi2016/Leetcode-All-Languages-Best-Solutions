"""resume 的单元测试。"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from leetcode_solutions.markdown_writer import write_problem
from leetcode_solutions.resume import is_problem_complete, missing_languages


class ResumeTest(unittest.TestCase):
    """验证断点续跑的语言缺失判断。"""

    def test_complete_and_missing_languages(self) -> None:
        """完整文件应跳过，部分文件应返回缺失语言。"""

        problem = {"frontend_id": "1", "difficulty": "Easy", "problem_slug": "two-sum", "title": "Two Sum"}
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "0001-two-sum.md"
            write_problem(path, problem, {"python3": "code"})
            self.assertTrue(is_problem_complete(path, ["python3"]))
            self.assertEqual(["cpp"], missing_languages(path, ["python3", "cpp"]))

    def test_incomplete_sections_are_missing(self) -> None:
        """空代码块或只有标题的语言必须继续重跑。"""

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "0004-median-of-two-sorted-arrays.md"
            path.write_text(
                "# 0004. Median of Two Sorted Arrays\n\n"
                "## Cpp\n\n"
                "```cpp\n"
                "\n"
                "```\n\n"
                "## Kotlin\n\n",
                encoding="utf-8",
            )

            self.assertFalse(is_problem_complete(path, ["cpp", "kotlin"]))
            self.assertEqual(["cpp", "kotlin"], missing_languages(path, ["cpp", "kotlin"]))


if __name__ == "__main__":
    unittest.main()
