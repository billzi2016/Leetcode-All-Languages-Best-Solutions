"""Tests for validate-pro report helpers."""

from __future__ import annotations

import csv
import tempfile
import unittest
from pathlib import Path

from validate_pro.report import write_empty_reports


class ReportTest(unittest.TestCase):
    """Validate CSV report helpers."""

    def test_write_empty_reports(self) -> None:
        """Report helper should create one CSV per difficulty."""

        with tempfile.TemporaryDirectory() as tmp:
            reports_dir = Path(tmp) / "reports"
            write_empty_reports(reports_dir, ["python3", "cpp"])
            with (reports_dir / "easy.csv").open(encoding="utf-8") as file:
                rows = list(csv.reader(file))
            medium_exists = (reports_dir / "medium.csv").exists()
            hard_exists = (reports_dir / "hard.csv").exists()

        self.assertEqual(["problem_id", "title", "python3", "cpp"], rows[0])
        self.assertTrue(medium_exists)
        self.assertTrue(hard_exists)


if __name__ == "__main__":
    unittest.main()
