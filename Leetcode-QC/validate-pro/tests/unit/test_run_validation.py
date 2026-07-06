"""Tests for validate-pro validation bridge."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import run_validation


class RunValidationBridgeTest(unittest.TestCase):
    """Validate conversion into the base validator format."""

    def test_make_base_problem(self) -> None:
        """Retained case JSON should convert to base validation problem."""

        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            validate_dir = repo / "Leetcode-QC" / "validate"
            validate_dir.mkdir(parents=True)
            (validate_dir / "run_validation.py").write_text(
                "from dataclasses import dataclass\n"
                "@dataclass\n"
                "class ValidationProblem:\n"
                "    frontend_id: str\n"
                "    title: str\n"
                "    difficulty: str\n"
                "    slug: str\n"
                "    method: str\n"
                "    kind: str\n"
                "    languages: list\n"
                "    cases: list\n",
                encoding="utf-8",
            )
            base = run_validation.load_base_validator(repo)
            problem = run_validation.make_base_problem(
                base,
                {
                    "frontend_id": "20",
                    "title": "Valid Parentheses",
                    "difficulty": "Easy",
                    "problem_slug": "valid-parentheses",
                    "method": "isValid",
                    "kind": "string_bool",
                    "cases": [{"input": {"s": "()"}, "expected": True}],
                },
            )

        self.assertEqual("20", problem.frontend_id)
        self.assertEqual([{"s": "()", "expected": True}], problem.cases)


if __name__ == "__main__":
    unittest.main()
