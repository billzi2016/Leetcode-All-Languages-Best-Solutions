"""logger 的单元测试。"""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from leetcode_solutions.logger import RunLogger


class LoggerTest(unittest.TestCase):
    """验证 stdout、stderr 和 failures 三类日志分流。"""

    def test_log_files_are_separated(self) -> None:
        """三类日志应写入同一个运行目录下的不同文件。"""

        with tempfile.TemporaryDirectory() as tmp:
            logger = RunLogger(Path(tmp), run_datetime="run")
            logger.info("hello stdout")
            logger.error("hello stderr")
            logger.failure({"frontend_id": "1", "error": "timeout"})
            logger.close()

            run_dir = Path(tmp) / "run"
            stdout_text = (run_dir / "stdout.log").read_text(encoding="utf-8")
            stderr_text = (run_dir / "stderr.log").read_text(encoding="utf-8")
            failure_line = (run_dir / "failures.jsonl").read_text(encoding="utf-8").strip()

        self.assertIn("hello stdout", stdout_text)
        self.assertIn("hello stderr", stderr_text)
        self.assertEqual("1", json.loads(failure_line)["frontend_id"])


if __name__ == "__main__":
    unittest.main()

