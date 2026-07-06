"""prompt_builder 的单元测试。"""

from __future__ import annotations

import unittest

from leetcode_solutions.prompt_builder import build_language_prompt, build_problem_prompt


class PromptBuilderTest(unittest.TestCase):
    """验证 prompt 字段拼接和图片字段排除。"""

    def test_problem_prompt_uses_useful_fields_but_skips_images(self) -> None:
        """题目 prompt 应包含文本信息和 solution，同时排除 images。"""

        prompt = build_problem_prompt(
            {
                "title": "Two Sum",
                "problem_id": "1",
                "frontend_id": "1",
                "difficulty": "Easy",
                "problem_slug": "two-sum",
                "topics": ["Array", "Hash Table"],
                "description": "Find two numbers.",
                "examples": [{"example_num": 1, "example_text": "Input...", "images": ["http://image"]}],
                "constraints": ["2 <= nums.length"],
                "follow_ups": [],
                "hints": ["Use a map."],
                "solution": "<p>Hash map</p>",
            }
        )

        self.assertIn("Two Sum", prompt)
        self.assertIn("Hash Table", prompt)
        self.assertIn("Input...", prompt)
        self.assertIn("Hash map", prompt)
        self.assertNotIn("http://image", prompt)
        self.assertNotIn("images", prompt)

    def test_language_prompt_contains_language_and_starter(self) -> None:
        """语言 prompt 只补目标语言和 starter code。"""

        prompt = build_language_prompt("python3", "class Solution:\n    pass")
        self.assertIn("Target Language: python3", prompt)
        self.assertIn("class Solution", prompt)
        self.assertIn("Return raw code only", prompt)


if __name__ == "__main__":
    unittest.main()

