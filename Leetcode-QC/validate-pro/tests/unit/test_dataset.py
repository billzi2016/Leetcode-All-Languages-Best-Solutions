"""Tests for validate-pro dataset parsing."""

from __future__ import annotations

import unittest

from validate_pro.dataset import infer_kind, infer_method, parse_example_text, problem_from_question


class DatasetTest(unittest.TestCase):
    """Validate dataset parsing helpers."""

    def test_parse_example_text(self) -> None:
        """LeetCode examples should parse into input and expected fields."""

        parsed = parse_example_text("Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: sample")

        self.assertEqual({"nums": [2, 7, 11, 15], "target": 9}, parsed["input"])
        self.assertEqual([0, 1], parsed["expected"])
        self.assertEqual("dataset", parsed["source"])

    def test_problem_from_question_infers_method_and_kind(self) -> None:
        """Starter code should provide method and adapter kind."""

        problem = problem_from_question(
            {
                "frontend_id": "1",
                "title": "Two Sum",
                "problem_slug": "two-sum",
                "difficulty": "Easy",
                "description": "desc",
                "constraints": "constraints",
                "examples": [],
                "topics": ["Array"],
                "hints": [],
                "code_snippets": {"python3": "class Solution:\n    def twoSum(self, nums, target):\n        pass"},
            }
        )

        self.assertEqual("twoSum", problem.method)
        self.assertEqual("array_int_target_indices", problem.kind)
        self.assertEqual("0001-two-sum.json", problem.case_filename)

    def test_infer_helpers(self) -> None:
        """Method and kind inference should support common starter forms."""

        self.assertEqual("isValid", infer_method({"java": "class Solution { public boolean isValid(String s) { } }"}))
        self.assertEqual("string_bool", infer_kind("valid-parentheses", "isValid"))


if __name__ == "__main__":
    unittest.main()

