"""Tests for validate-pro LLM candidate parsing."""

from __future__ import annotations

import unittest

from validate_pro.llm_case_generator import parse_strict_json


class LlmCaseGeneratorTest(unittest.TestCase):
    """Validate strict JSON parsing."""

    def test_parse_strict_json(self) -> None:
        """A JSON object should parse as a candidate."""

        parsed = parse_strict_json('{"input": {"s": "()"}, "expected": true, "purpose": "basic"}')

        self.assertEqual("basic", parsed["purpose"])

    def test_reject_non_json_text(self) -> None:
        """Explanatory text around JSON should be rejected."""

        with self.assertRaises(Exception):
            parse_strict_json('Here is JSON: {"input": {}}')


if __name__ == "__main__":
    unittest.main()

