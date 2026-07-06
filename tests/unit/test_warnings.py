"""warning 清理相关测试。"""

from __future__ import annotations

import unittest

from scripts.generate_solutions import suppress_environment_warnings


class WarningFilterTest(unittest.TestCase):
    """验证环境 warning 过滤器可以安全安装。"""

    def test_suppress_environment_warnings_is_safe(self) -> None:
        """即使当前环境没有对应 warning 类型，也不应抛出异常。"""

        suppress_environment_warnings()


if __name__ == "__main__":
    unittest.main()
