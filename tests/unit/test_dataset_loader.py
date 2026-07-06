"""dataset_loader 的单元测试。"""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from leetcode_solutions.dataset_loader import filter_by_difficulty, find_by_frontend_id, load_questions, sort_questions


class DatasetLoaderTest(unittest.TestCase):
    """验证数据读取、查找和排序逻辑。"""

    def test_load_questions_and_sort(self) -> None:
        """读取 questions 后按数字 frontend_id 排序。"""

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "merged_problems.json"
            path.write_text(
                json.dumps(
                    {
                        "questions": [
                            {"frontend_id": "2", "difficulty": "Medium"},
                            {"frontend_id": "1", "difficulty": "Easy"},
                        ]
                    }
                ),
                encoding="utf-8",
            )
            questions = load_questions(path)

        self.assertEqual(["1", "2"], [q["frontend_id"] for q in sort_questions(questions)])

    def test_filter_and_find(self) -> None:
        """按难度筛选，并能根据 frontend_id 找到题目。"""

        questions = [
            {"frontend_id": "2", "difficulty": "Medium"},
            {"frontend_id": "1", "difficulty": "Easy"},
        ]
        self.assertEqual("1", filter_by_difficulty(questions, "Easy")[0]["frontend_id"])
        self.assertEqual("2", find_by_frontend_id(questions, "2")["frontend_id"])
        self.assertIsNone(find_by_frontend_id(questions, "999"))


if __name__ == "__main__":
    unittest.main()

