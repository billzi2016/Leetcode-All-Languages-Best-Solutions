"""CSV report helpers for validate-pro."""

from __future__ import annotations

import csv
from pathlib import Path

from .dataset import DIFFICULTY_ORDER


def write_empty_reports(reports_dir: Path, languages: list[str]) -> None:
    """Write empty per-difficulty CSV files with language columns."""

    reports_dir.mkdir(parents=True, exist_ok=True)
    for difficulty in DIFFICULTY_ORDER:
        path = reports_dir / f"{difficulty.lower()}.csv"
        with path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["problem_id", "title", *languages])

