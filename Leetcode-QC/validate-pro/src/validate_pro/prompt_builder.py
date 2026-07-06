"""Prompt construction for controlled AI case generation."""

from __future__ import annotations

import json

from .dataset import Problem


def build_case_prompt(problem: Problem, covered_purposes: list[str], requested_purpose: str) -> str:
    """Build a strict JSON prompt for one candidate test case."""

    context = {
        "problem_id": problem.frontend_id,
        "title": problem.title,
        "difficulty": problem.difficulty,
        "topics": problem.topics,
        "description": problem.description,
        "constraints": problem.constraints,
        "examples": problem.examples,
        "starter_signatures": problem.code_snippets,
        "method": problem.method,
        "kind": problem.kind,
        "covered_purposes": covered_purposes,
        "requested_purpose": requested_purpose,
    }
    schema = {
        "input": "object matching the problem method arguments",
        "expected": "the expected output for the input",
        "purpose": "short reason this case is valuable",
    }
    return (
        "You are a controlled test-case proposer for LeetCode solution validation.\n"
        "Use ReAct-style reasoning internally, but the final answer must be strict JSON only.\n"
        "Generate exactly one candidate case. Keep it within constraints and small enough for a Python reference solver.\n"
        "Do not include Markdown, prose, or code fences in the final answer.\n\n"
        "Problem context:\n"
        f"{json.dumps(context, ensure_ascii=False, indent=2)}\n\n"
        "Required final JSON schema:\n"
        f"{json.dumps(schema, ensure_ascii=False, indent=2)}\n"
    )

