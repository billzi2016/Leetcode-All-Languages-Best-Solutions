"""Tests for validate-pro prompt construction."""

from __future__ import annotations

import unittest

from validate_pro.dataset import Problem
from validate_pro.prompt_builder import build_case_prompt


class PromptBuilderTest(unittest.TestCase):
    """Validate controlled-AI prompt shape."""

    def test_prompt_contains_controlled_json_requirements(self) -> None:
        """Prompt should include strict JSON and context fields."""

        problem = Problem(
            frontend_id="1",
            title="Two Sum",
            slug="two-sum",
            difficulty="Easy",
            description="Find two numbers.",
            constraints="2 <= nums.length",
            examples=[],
            topics=["Array"],
            hints=[],
            code_snippets={"python3": "def twoSum(self, nums, target): pass"},
            method="twoSum",
            kind="array_int_target_indices",
        )
        prompt = build_case_prompt(problem, ["dataset example"], "negative and positive mix")

        self.assertIn("strict JSON only", prompt)
        self.assertIn("negative and positive mix", prompt)
        self.assertIn("starter_signatures", prompt)
        self.assertIn("covered_purposes", prompt)


if __name__ == "__main__":
    unittest.main()

