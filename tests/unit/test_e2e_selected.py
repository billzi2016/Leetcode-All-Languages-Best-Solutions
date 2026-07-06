"""LeetCode 1、2、4 正式流程和跳过行为测试。"""

from __future__ import annotations

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from leetcode_solutions.dataset_loader import find_by_frontend_id, load_questions
from leetcode_solutions.generator import SolutionGenerator

from tests.unit.test_generator import FakeClient, FakeLogger


class SelectedProblemsE2ETest(unittest.TestCase):
    """使用真实 dataset 中的 1/2/4 验证 Easy/Medium/Hard 生成链路。"""

    CASES = {
        "1": "Leetcode-Easy/0001-0100/0001-two-sum.md",
        "2": "Leetcode-Medium/0001-0100/0002-add-two-numbers.md",
        "4": "Leetcode-Hard/0001-0100/0004-median-of-two-sorted-arrays.md",
    }

    def test_selected_problems_formal_flow_then_skip(self) -> None:
        """第一次生成 1/2/4，第二次应识别完整文件并跳过模型调用。"""

        dataset = Path("dataset/merged_problems.json")
        if not dataset.exists():
            self.skipTest("dataset/merged_problems.json is not available locally")

        questions = load_questions(dataset)
        with TemporaryDirectory() as tmp:
            logger = FakeLogger()
            for frontend_id, expected_relative_path in self.CASES.items():
                problem = find_by_frontend_id(questions, frontend_id)
                self.assertIsNotNone(problem)

                first_client = FakeClient()
                output_path = SolutionGenerator(first_client, logger, Path(tmp)).generate_problem(problem)
                self.assertEqual(Path(tmp) / expected_relative_path, output_path)
                self.assertTrue(output_path.exists())
                self.assertEqual(len(problem["code_snippets"]), len(first_client.calls))

                second_client = FakeClient()
                SolutionGenerator(second_client, logger, Path(tmp)).generate_problem(problem)
                self.assertEqual([], second_client.calls)


if __name__ == "__main__":
    unittest.main()
