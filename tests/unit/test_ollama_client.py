"""ollama_client 的单元测试。"""

from __future__ import annotations

import unittest

from leetcode_solutions.config import MAX_OUTPUT_TOKENS, TEMPERATURE, THINK_BY_DIFFICULTY
from leetcode_solutions.ollama_client import OllamaClient, strip_code_fences


class OllamaClientTest(unittest.TestCase):
    """验证 think 映射、100_000 限制和输出清洗。"""

    def test_options_include_think_and_100_000_limit(self) -> None:
        """Easy/Medium/Hard 应映射到 low/medium/high，并包含 100_000 输出限制。"""

        client = OllamaClient(THINK_BY_DIFFICULTY)
        self.assertEqual(
            {"think": "low", "num_predict": MAX_OUTPUT_TOKENS, "temperature": TEMPERATURE},
            client.build_options("Easy"),
        )
        self.assertEqual("medium", client.build_options("Medium")["think"])
        self.assertEqual("high", client.build_options("Hard")["think"])
        self.assertEqual(0.1, client.build_options("Hard")["temperature"])

    def test_strip_code_fences(self) -> None:
        """模型误输出 Markdown 代码块时应清洗为纯代码。"""

        self.assertEqual("print('hi')", strip_code_fences("```python\nprint('hi')\n```"))

    def test_ollama_smoke_test_contract(self) -> None:
        """smoke test 约定使用 hello 覆盖三种 think 模式。"""

        prompts = [(difficulty, "hello", OllamaClient(THINK_BY_DIFFICULTY).build_options(difficulty)["think"]) for difficulty in THINK_BY_DIFFICULTY]
        self.assertEqual([("Easy", "hello", "low"), ("Medium", "hello", "medium"), ("Hard", "hello", "high")], prompts)


if __name__ == "__main__":
    unittest.main()
