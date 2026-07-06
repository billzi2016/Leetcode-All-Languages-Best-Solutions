"""Candidate verification against trusted reference adapters."""

from __future__ import annotations

from typing import Any

from .adapters import Adapter
from .adapters.core import CandidateError


def verify_case(adapter: Adapter, candidate: dict[str, Any]) -> dict[str, Any]:
    """Verify one candidate and return the retained normalized case.

    Args:
        adapter: Reference adapter for the problem.
        candidate: Candidate JSON with `input`, optional `expected`, and `purpose`.

    Returns:
        A retained-case dictionary with verified `expected`.

    Raises:
        CandidateError: If the candidate cannot be retained.
    """

    if not isinstance(candidate, dict):
        raise CandidateError("candidate must be an object")
    case_input = candidate.get("input")
    if not isinstance(case_input, dict):
        raise CandidateError("candidate.input must be an object")
    purpose = candidate.get("purpose")
    if not isinstance(purpose, str) or not purpose.strip():
        raise CandidateError("candidate.purpose must be non-empty")

    adapter.validate_input(case_input)
    actual = adapter.solve(case_input)
    if "expected" in candidate and not adapter.equivalent(candidate["expected"], actual):
        raise CandidateError("candidate expected does not match reference output")

    return {
        "input": case_input,
        "expected": actual,
        "source": str(candidate.get("source", "gpt-oss:120b")),
        "purpose": purpose.strip(),
    }


def dedupe_cases(cases: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Remove duplicate cases by serialized input and purpose."""

    seen: set[tuple[str, str]] = set()
    output: list[dict[str, Any]] = []
    for case in cases:
        key = (repr(sorted(case["input"].items())), str(case.get("purpose", "")))
        if key in seen:
            continue
        seen.add(key)
        output.append(case)
    return output

