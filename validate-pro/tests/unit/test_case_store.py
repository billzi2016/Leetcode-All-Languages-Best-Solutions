"""Tests for validate-pro retained case storage."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from validate_pro.case_store import build_case_file, case_file_path, load_case_file, write_case_file
from validate_pro.dataset import Problem


class CaseStoreTest(unittest.TestCase):
    """Validate JSON case file helpers."""

    def test_write_and_load_case_file(self) -> None:
        """Retained cases should round-trip as JSON."""

        problem = Problem("1", "Two Sum", "two-sum", "Easy", "", "", [], [], [], {}, "twoSum", "array_int_target_indices")
        document = build_case_file(problem, [{"input": {"nums": [2, 7], "target": 9}, "expected": [0, 1], "purpose": "basic"}])
        with tempfile.TemporaryDirectory() as tmp:
            path = case_file_path(Path(tmp), problem)
            write_case_file(path, document)
            loaded = load_case_file(path)

        self.assertEqual("1", loaded["frontend_id"])
        self.assertEqual("0001-two-sum.json", path.name)
        self.assertEqual([0, 1], loaded["cases"][0]["expected"])


if __name__ == "__main__":
    unittest.main()

