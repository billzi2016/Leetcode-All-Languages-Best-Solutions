"""Tests for validate-pro retained case generation helpers."""

from __future__ import annotations

import unittest

import generate_cases
from validate_pro.adapters import get_adapter
from validate_pro.dataset import Problem


class CaseGenerationTest(unittest.TestCase):
    """Validate generation helper behavior without calling an LLM."""

    def test_retained_dataset_examples(self) -> None:
        """Dataset examples should be verified through the reference adapter."""

        problem = Problem(
            frontend_id="1",
            title="Two Sum",
            slug="two-sum",
            difficulty="Easy",
            description="",
            constraints="",
            examples=[
                {
                    "input": {"nums": [2, 7, 11, 15], "target": 9},
                    "expected": [1, 0],
                    "source": "dataset",
                    "purpose": "dataset example",
                }
            ],
            topics=[],
            hints=[],
            code_snippets={},
            method="twoSum",
            kind="array_int_target_indices",
        )

        retained, events = generate_cases.retained_dataset_examples(problem, get_adapter(problem.kind))

        self.assertEqual([0, 1], retained[0]["expected"])
        self.assertEqual("retained", events[0].status)


if __name__ == "__main__":
    unittest.main()
