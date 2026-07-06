"""输出查缺补漏审计测试。"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from leetcode_solutions.audit import audit_problem, audit_problems
from leetcode_solutions.markdown_writer import problem_output_path, write_problem


class AuditTest(unittest.TestCase):
    """验证缺失语言和顺序异常扫描。"""

    def test_audit_problem_reports_missing_languages(self) -> None:
        """只写出 Kotlin 的旧文件应报告前置语言缺失。"""

        problem = {
            "frontend_id": "4",
            "difficulty": "Hard",
            "problem_slug": "median-of-two-sorted-arrays",
            "title": "Median of Two Sorted Arrays",
            "code_snippets": {"cpp": "cpp starter", "java": "java starter", "kotlin": "kotlin starter"},
        }
        with tempfile.TemporaryDirectory() as tmp:
            output_root = Path(tmp)
            path = problem_output_path(problem, output_root)
            write_problem(path, problem, {"kotlin": "class ExistingKotlin {}"})
            result = audit_problem(problem, output_root)

        self.assertTrue(result.has_issues)
        self.assertEqual(["cpp", "java"], result.missing)
        self.assertFalse(result.order_mismatch)

    def test_audit_problem_reports_complete_wrong_order(self) -> None:
        """语言完整但顺序异常时应报告可修复顺序问题。"""

        problem = {
            "frontend_id": "4",
            "difficulty": "Hard",
            "problem_slug": "median-of-two-sorted-arrays",
            "title": "Median of Two Sorted Arrays",
            "code_snippets": {"cpp": "cpp starter", "kotlin": "kotlin starter"},
        }
        with tempfile.TemporaryDirectory() as tmp:
            output_root = Path(tmp)
            path = problem_output_path(problem, output_root)
            write_problem(path, problem, {"kotlin": "class ExistingKotlin {}", "cpp": "class ExistingCpp {}"})
            result = audit_problem(problem, output_root)

        self.assertTrue(result.has_issues)
        self.assertEqual([], result.missing)
        self.assertTrue(result.order_mismatch)
        self.assertEqual(["kotlin", "cpp"], result.existing_order)
        self.assertEqual(["cpp", "kotlin"], result.expected_order)

    def test_audit_problems_omits_clean_outputs(self) -> None:
        """完整且顺序正确的题目不应出现在审计结果中。"""

        problem = {
            "frontend_id": "1",
            "difficulty": "Easy",
            "problem_slug": "two-sum",
            "title": "Two Sum",
            "code_snippets": {"cpp": "cpp starter", "python3": "python starter"},
        }
        with tempfile.TemporaryDirectory() as tmp:
            output_root = Path(tmp)
            path = problem_output_path(problem, output_root)
            write_problem(path, problem, {"cpp": "cpp code", "python3": "python code"})
            results = audit_problems([problem], output_root)

        self.assertEqual([], results)


if __name__ == "__main__":
    unittest.main()
