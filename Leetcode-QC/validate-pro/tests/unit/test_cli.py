"""Tests for validate-pro CLI parsing."""

from __future__ import annotations

import sys
import unittest
from unittest.mock import patch

import generate_cases
import run_validation


class CliTest(unittest.TestCase):
    """Validate command-line argument parsers."""

    def test_generate_cases_args(self) -> None:
        """generate_cases should parse selected ids and no-llm mode."""

        with patch.object(sys, "argv", ["generate_cases.py", "--frontend-ids", "1", "20", "--no-llm"]):
            args = generate_cases.parse_args()

        self.assertEqual(["1", "20"], args.frontend_ids)
        self.assertTrue(args.no_llm)

    def test_run_validation_args(self) -> None:
        """run_validation should parse report and timeout options."""

        with patch.object(sys, "argv", ["run_validation.py", "--reports-dir", "out", "--timeout", "3"]):
            args = run_validation.parse_args()

        self.assertEqual("out", str(args.reports_dir))
        self.assertEqual(3.0, args.timeout)


if __name__ == "__main__":
    unittest.main()

