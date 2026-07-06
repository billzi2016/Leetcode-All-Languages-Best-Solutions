"""历史 Markdown 语言 section 规范化脚本测试。"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from migrate.normalize_markdown_language_sections import normalize_content, run


class NormalizeMarkdownLanguageSectionsTest(unittest.TestCase):
    """验证老版本 SQL/PythonData 标题和 fence 可以被独立迁移。"""

    def test_normalize_content_rewrites_legacy_database_sections(self) -> None:
        """旧标题和旧 fence 应改成 MkDocs 更稳定识别的新格式。"""

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "0175-combine-two-tables.md"
            path.write_text(
                "# 0175. Combine Two Tables\n\n"
                "## Mysql\n\n"
                "```mysql\n"
                "SELECT * FROM Person;\n"
                "```\n\n"
                "## Pythondata\n\n"
                "```pythondata\n"
                "import pandas as pd\n"
                "```\n",
                encoding="utf-8",
            )

            result = normalize_content(path)

        self.assertTrue(result.changed)
        self.assertEqual(2, result.heading_changes)
        self.assertEqual(2, result.fence_changes)
        self.assertIn("## MySQL", result.content)
        self.assertIn("```sql", result.content)
        self.assertIn("## PythonData", result.content)
        self.assertIn("```python", result.content)

    def test_run_dry_run_does_not_rewrite_files(self) -> None:
        """默认 dry-run 只打印计划，不应修改磁盘上的 Markdown。"""

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "Leetcode-Easy/0101-0200/0175-combine-two-tables.md"
            path.parent.mkdir(parents=True)
            original = "# 0175. Combine Two Tables\n\n## Mysql\n\n```mysql\nSELECT 1;\n```\n"
            path.write_text(original, encoding="utf-8")

            exit_code = run(root, apply=False)

            self.assertEqual(0, exit_code)
            self.assertEqual(original, path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
