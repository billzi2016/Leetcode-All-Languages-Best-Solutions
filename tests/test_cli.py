"""CLI 参数解析相关测试。"""

from __future__ import annotations

import unittest
from unittest.mock import patch

from scripts.generate_solutions import parse_args


class CliTest(unittest.TestCase):
    """验证 CLI 能接受多个题号。"""

    def test_parse_multiple_frontend_ids(self) -> None:
        """`--frontend-ids 1 2 4` 应解析为三个题号。"""

        with patch("sys.argv", ["generate_solutions.py", "--frontend-ids", "1", "2", "4"]):
            args = parse_args()

        self.assertEqual(["1", "2", "4"], args.frontend_ids)


if __name__ == "__main__":
    unittest.main()
