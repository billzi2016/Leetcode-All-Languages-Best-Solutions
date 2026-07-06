"""Smoke tests for validate-pro command-line parsers."""

from __future__ import annotations

import sys
import unittest
from unittest.mock import patch

import generate_cases
import run_validation


class ValidateProCliSmokeTest(unittest.TestCase):
    """Validate that CLI parsers expose expected default paths."""

    def test_generate_cases_parser_defaults(self) -> None:
        """generate_cases should expose cases and reports defaults."""

        with patch.object(sys, "argv", ["generate_cases.py"]):
            args = generate_cases.parse_args()

        self.assertEqual("Leetcode-QC/validate-pro/cases", str(args.cases_dir))
        self.assertEqual("Leetcode-QC/validate-pro/reports", str(args.reports_dir))

    def test_run_validation_parser_defaults(self) -> None:
        """run_validation should expose retained-case report defaults."""

        with patch.object(sys, "argv", ["run_validation.py"]):
            args = run_validation.parse_args()

        self.assertEqual("Leetcode-QC/validate-pro/cases", str(args.cases_dir))
        self.assertEqual("Leetcode-QC/validate-pro/reports", str(args.reports_dir))


if __name__ == "__main__":
    unittest.main()
