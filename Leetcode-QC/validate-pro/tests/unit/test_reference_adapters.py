"""Tests for validate-pro reference adapters."""

from __future__ import annotations

import unittest

from validate_pro.adapters import get_adapter
from validate_pro.adapters.core import CandidateError
from validate_pro.reference import dedupe_cases, verify_case


class ReferenceAdapterTest(unittest.TestCase):
    """Validate adapter solving, normalization, and rejection."""

    def test_two_sum_accepts_reversed_expected_pair(self) -> None:
        """Two Sum should normalize answer pair order."""

        adapter = get_adapter("array_int_target_indices")
        retained = verify_case(
            adapter,
            {"input": {"nums": [2, 7, 11, 15], "target": 9}, "expected": [1, 0], "purpose": "pair at front"},
        )

        self.assertEqual([0, 1], retained["expected"])

    def test_reject_bad_expected(self) -> None:
        """Incorrect expected output should be rejected."""

        adapter = get_adapter("string_bool")
        with self.assertRaises(CandidateError):
            verify_case(adapter, {"input": {"s": "()"}, "expected": False, "purpose": "basic true"})

    def test_dedupe_cases(self) -> None:
        """Duplicate retained cases should be removed."""

        cases = [
            {"input": {"s": "()"}, "expected": True, "purpose": "basic"},
            {"input": {"s": "()"}, "expected": True, "purpose": "basic"},
        ]

        self.assertEqual(1, len(dedupe_cases(cases)))


if __name__ == "__main__":
    unittest.main()

