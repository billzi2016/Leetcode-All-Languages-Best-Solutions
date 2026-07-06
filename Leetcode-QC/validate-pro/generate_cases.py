#!/usr/bin/env python3
"""Generate retained validate-pro cases with controlled AI and reference solvers."""

from __future__ import annotations

import argparse
from pathlib import Path

from validate_pro.adapters import get_adapter
from validate_pro.case_store import build_case_file, case_file_path, load_case_file, write_case_file
from validate_pro.dataset import load_problems, select_problems
from validate_pro.llm_case_generator import OllamaCaseGenerator
from validate_pro.prompt_builder import build_case_prompt
from validate_pro.reference import dedupe_cases, verify_case


DEFAULT_PURPOSES = [
    "minimum valid input",
    "duplicate values",
    "boundary numeric values",
    "negative and positive mix",
    "reverse ordered input",
    "failure path or false result",
    "multiple valid answers if allowed",
    "stress within reference budget",
]


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""

    parser = argparse.ArgumentParser(description="Generate validate-pro retained cases.")
    parser.add_argument("--repo-root", type=Path, default=Path.cwd(), help="Repository root path.")
    parser.add_argument("--dataset", type=Path, default=Path("dataset/merged_problems.json"), help="Dataset path.")
    parser.add_argument("--cases-dir", type=Path, default=Path("Leetcode-QC/validate-pro/cases"), help="Retained case output directory.")
    parser.add_argument("--difficulty", choices=["Easy", "Medium", "Hard"], help="Generate cases for one difficulty.")
    parser.add_argument("--frontend-ids", nargs="+", help="Generate cases for selected frontend ids.")
    parser.add_argument("--min-cases", type=int, default=10, help="Minimum retained cases per supported problem.")
    parser.add_argument("--max-cases", type=int, default=50, help="Maximum retained cases per supported problem.")
    parser.add_argument("--max-attempts-per-case", type=int, default=5, help="LLM attempts per missing case.")
    parser.add_argument("--max-reference-seconds", type=float, default=1.0, help="Reserved per-case reference budget.")
    parser.add_argument("--coverage-profile", default="balanced", help="Reserved coverage profile name.")
    parser.add_argument("--token-budget", type=int, default=0, help="Reserved LLM token budget; 0 means no explicit budget.")
    parser.add_argument("--no-llm", action="store_true", help="Retain only dataset examples verified by reference adapters.")
    return parser.parse_args()


def resolve_path(repo_root: Path, path: Path) -> Path:
    """Resolve a possibly relative path against repo root."""

    return path if path.is_absolute() else repo_root / path


def retained_dataset_examples(problem, adapter) -> list[dict]:
    """Verify and retain dataset examples for one problem."""

    retained = []
    for example in problem.examples:
        try:
            retained.append(verify_case(adapter, example))
        except Exception:
            continue
    return retained


def generate_for_problem(problem, adapter, retained: list[dict], min_cases: int, max_cases: int, max_attempts: int) -> list[dict]:
    """Use gpt-oss candidates to extend retained cases."""

    generator = OllamaCaseGenerator()
    purposes = [purpose for purpose in DEFAULT_PURPOSES if purpose not in {case.get("purpose") for case in retained}]
    purpose_index = 0
    while len(retained) < min_cases and len(retained) < max_cases and purpose_index < len(purposes):
        requested_purpose = purposes[purpose_index]
        purpose_index += 1
        covered = [str(case.get("purpose", "")) for case in retained]
        prompt = build_case_prompt(problem, covered, requested_purpose)
        for _ in range(max_attempts):
            try:
                candidate = generator.generate(prompt)
                candidate["source"] = "gpt-oss:120b"
                retained.append(verify_case(adapter, candidate))
                retained = dedupe_cases(retained)
                break
            except Exception:
                continue
    return retained[:max_cases]


def main() -> int:
    """CLI entry point."""

    args = parse_args()
    repo_root = args.repo_root
    dataset_path = resolve_path(repo_root, args.dataset)
    cases_dir = resolve_path(repo_root, args.cases_dir)
    problems = select_problems(load_problems(dataset_path), args.difficulty, args.frontend_ids)

    written = 0
    for problem in problems:
        adapter = get_adapter(problem.kind)
        if adapter is None:
            continue
        path = case_file_path(cases_dir, problem)
        existing = load_case_file(path)
        retained = list(existing.get("cases", [])) if existing else []
        retained.extend(retained_dataset_examples(problem, adapter))
        retained = dedupe_cases(retained)
        if not args.no_llm:
            retained = generate_for_problem(problem, adapter, retained, args.min_cases, args.max_cases, args.max_attempts_per_case)
        if retained:
            write_case_file(path, build_case_file(problem, retained))
            written += 1

    print(f"Wrote retained case files: {written}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
