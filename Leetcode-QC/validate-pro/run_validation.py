#!/usr/bin/env python3
"""Run validate-pro retained cases through the existing Docker-style validation harness."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from tempfile import TemporaryDirectory


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""

    parser = argparse.ArgumentParser(description="Validate generated solutions with validate-pro retained cases.")
    parser.add_argument("--repo-root", type=Path, default=Path.cwd(), help="Repository root path.")
    parser.add_argument("--cases-dir", type=Path, default=Path("Leetcode-QC/validate-pro/cases"), help="Retained case directory.")
    parser.add_argument("--reports-dir", type=Path, default=Path("Leetcode-QC/validate-pro/reports"), help="CSV report directory.")
    parser.add_argument("--work-dir", type=Path, default=None, help="Optional persistent work directory.")
    parser.add_argument("--timeout", type=float, default=10.0, help="Compile/run timeout per language and problem.")
    return parser.parse_args()


def resolve_path(repo_root: Path, path: Path) -> Path:
    """Resolve a path against repo root when needed."""

    return path if path.is_absolute() else repo_root / path


def load_base_validator(repo_root: Path):
    """Load the baseline validator as a module without requiring package changes."""

    validator_path = repo_root / "Leetcode-QC" / "validate" / "run_validation.py"
    spec = importlib.util.spec_from_file_location("base_validate_run_validation", validator_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load base validator: {validator_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def load_retained_case_documents(cases_dir: Path) -> list[dict]:
    """Load all retained case JSON files."""

    if not cases_dir.exists():
        return []
    return [json.loads(path.read_text(encoding="utf-8")) for path in sorted(cases_dir.glob("*.json"))]


def make_base_problem(base_module, document: dict):
    """Convert one retained case document into the base validator problem dataclass."""

    return base_module.ValidationProblem(
        frontend_id=str(document["frontend_id"]),
        title=str(document["title"]),
        difficulty=str(document["difficulty"]),
        slug=str(document["problem_slug"]),
        method=str(document["method"]),
        kind=str(document["kind"]),
        languages=[],
        cases=[{**case["input"], "expected": case["expected"]} for case in document.get("cases", [])],
    )


def main() -> int:
    """CLI entry point."""

    args = parse_args()
    repo_root = args.repo_root
    cases_dir = resolve_path(repo_root, args.cases_dir)
    reports_dir = resolve_path(repo_root, args.reports_dir)
    base = load_base_validator(repo_root)
    documents = load_retained_case_documents(cases_dir)
    problems = [make_base_problem(base, document) for document in documents]
    sections_by_problem = {
        problem.frontend_id: base.parse_markdown_sections(base.solution_path(repo_root, problem))
        for problem in problems
    }
    if args.work_dir:
        work_root = resolve_path(repo_root, args.work_dir)
        work_root.mkdir(parents=True, exist_ok=True)
        results = base.validate_all(problems, sections_by_problem, work_root, args.timeout)
    else:
        with TemporaryDirectory() as tmp:
            results = base.validate_all(problems, sections_by_problem, Path(tmp), args.timeout)
    base.write_csv_reports(problems, sections_by_problem, results, reports_dir)
    print(f"Wrote reports: {reports_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
