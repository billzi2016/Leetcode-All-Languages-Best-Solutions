"""Read and write retained validate-pro case files."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .dataset import Problem


def case_file_path(cases_dir: Path, problem: Problem) -> Path:
    """Return the retained-case JSON path for a problem."""

    return cases_dir / problem.case_filename


def load_case_file(path: Path) -> dict[str, Any] | None:
    """Load an existing retained-case file if it exists."""

    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def build_case_file(problem: Problem, cases: list[dict[str, Any]]) -> dict[str, Any]:
    """Build the JSON document stored for one problem."""

    return {
        "frontend_id": problem.frontend_id,
        "title": problem.title,
        "problem_slug": problem.slug,
        "difficulty": problem.difficulty,
        "method": problem.method,
        "kind": problem.kind,
        "cases": cases,
    }


def write_case_file(path: Path, document: dict[str, Any]) -> None:
    """Write one retained-case document as formatted JSON."""

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

