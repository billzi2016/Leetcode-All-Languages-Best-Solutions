"""Tests for validate-pro coverage and audit reports."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from validate_pro.coverage import GenerationEvent, adapter_support_rows, write_generation_audit_report
from validate_pro.dataset import Problem


class CoverageReportTest(unittest.TestCase):
    """Validate support matrix and audit report generation."""

    def test_adapter_support_rows_marks_supported_kind(self) -> None:
        """Known adapter kinds should be marked as supported."""

        problem = Problem("1", "Two Sum", "two-sum", "Easy", "", "", [], [], [], {}, "twoSum", "array_int_target_indices")

        rows = adapter_support_rows([problem])

        self.assertEqual("yes", rows[0]["supported"])
        self.assertEqual("array_int_target_indices", rows[0]["adapter"])

    def test_generation_audit_report_lists_failures(self) -> None:
        """Audit report should include detailed rejected candidate reasons."""

        problem = Problem("20", "Valid Parentheses", "valid-parentheses", "Easy", "", "", [], [], [], {}, "isValid", "string_bool")
        event = GenerationEvent("20", "Valid Parentheses", "Easy", "string_bool", "rejected", "llm_candidate:ValueError")
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "generation_audit.md"
            write_generation_audit_report(path, [problem], [event], Path(tmp) / "cases")

            content = path.read_text(encoding="utf-8")

        self.assertIn("llm_candidate:ValueError", content)
        self.assertIn("20 Valid Parentheses", content)


if __name__ == "__main__":
    unittest.main()
