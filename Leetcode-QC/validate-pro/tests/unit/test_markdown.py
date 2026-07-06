"""Tests for validate-pro Markdown parsing."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from validate_pro.markdown import parse_markdown_sections, solution_path


class MarkdownTest(unittest.TestCase):
    """Validate Markdown helper behavior."""

    def test_solution_path_uses_leetcode_directories(self) -> None:
        """Solution paths should use Leetcode-* difficulty directories."""

        self.assertEqual(
            Path("/repo/Leetcode-Easy/0001-0100/0001-two-sum.md"),
            solution_path(Path("/repo"), "Easy", "1", "two-sum"),
        )

    def test_parse_markdown_sections(self) -> None:
        """Language sections should be extracted from Markdown fences."""

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "solution.md"
            path.write_text(
                "# 0001. Two Sum\n\n## Python3\n\n```python\nclass Solution: pass\n```\n\n## Cpp\n\n```cpp\nclass Solution {};\n```\n",
                encoding="utf-8",
            )
            sections = parse_markdown_sections(path)

        self.assertEqual({"python3", "cpp"}, set(sections))
        self.assertIn("class Solution", sections["python3"])


if __name__ == "__main__":
    unittest.main()

