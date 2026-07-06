"""Integration tests for validate-pro case generation without LLM calls."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import generate_cases


class GenerateCasesNoLlmIntegrationTest(unittest.TestCase):
    """Run the generate_cases CLI against a tiny dataset fixture."""

    def test_cli_writes_cases_and_audit_reports(self) -> None:
        """The no-LLM path should retain dataset examples and write audit reports."""

        dataset = {
            "questions": [
                {
                    "frontend_id": "1",
                    "title": "Two Sum",
                    "problem_slug": "two-sum",
                    "difficulty": "Easy",
                    "description": "Return two indices.",
                    "constraints": "",
                    "examples": [{"example_text": "Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]"}],
                    "topics": ["Array"],
                    "hints": [],
                    "code_snippets": {"python3": "class Solution:\n    def twoSum(self, nums, target):\n        pass"},
                }
            ]
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dataset_path = root / "dataset.json"
            cases_dir = root / "cases"
            reports_dir = root / "reports"
            dataset_path.write_text(json.dumps(dataset), encoding="utf-8")
            argv = [
                "generate_cases.py",
                "--repo-root",
                str(root),
                "--dataset",
                str(dataset_path),
                "--cases-dir",
                str(cases_dir),
                "--reports-dir",
                str(reports_dir),
                "--no-llm",
            ]

            with patch.object(sys, "argv", argv):
                result = generate_cases.main()

            self.assertEqual(0, result)
            self.assertTrue((cases_dir / "0001-two-sum.json").exists())
            self.assertTrue((reports_dir / "adapter_support.md").exists())
            self.assertTrue((reports_dir / "generation_audit.md").exists())


if __name__ == "__main__":
    unittest.main()
