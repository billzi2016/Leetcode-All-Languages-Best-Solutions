"""疑似异常题解审计测试。"""

from __future__ import annotations

import unittest
from pathlib import Path

from migrate.audit_suspicious_solutions import CodeBlock, audit_blocks, natural_language_markers


class SuspiciousSolutionAuditTest(unittest.TestCase):
    """验证异常审计对非传统算法题语言使用独立判断。"""

    def test_non_algorithm_language_uses_non_algorithm_baseline(self) -> None:
        """SQL 样本不足时应退到非算法全局基线，而不是普通算法全局基线。"""

        python_blocks = [
            CodeBlock(
                path=Path(f"Leetcode-Easy/0001-0100/{index:04d}-sample.md"),
                difficulty="easy",
                language="Python3",
                code="return x",
                chars=8,
                lines=1,
            )
            for index in range(1, 40)
        ]
        sql_block = CodeBlock(
            path=Path("Leetcode-Easy/0101-0200/0175-combine-two-tables.md"),
            difficulty="easy",
            language="MySQL",
            code="\n".join(["SELECT Person.firstName, Person.lastName, Address.city, Address.state"] * 90),
            chars=6_000,
            lines=90,
        )

        findings = audit_blocks(python_blocks + [sql_block], min_group_size=20, min_language_size=30, mad_multiplier=8.0)
        length_findings = [finding for finding in findings if finding.block is sql_block and finding.reason == "length_outlier"]

        self.assertEqual([], length_findings)

    def test_non_algorithm_language_ignores_plain_explanation_words(self) -> None:
        """SQL/Bash 只检查 Markdown 残留，避免字段名或注释文本触发算法题 marker。"""

        self.assertEqual([], natural_language_markers("-- explanation: legacy query note\nSELECT 1;", "MySQL"))
        self.assertEqual([], natural_language_markers("# this solution uses awk\nawk '{print $1}' file.txt", "Bash"))
        self.assertNotEqual([], natural_language_markers("## Explanation\nSELECT 1;", "MySQL"))


if __name__ == "__main__":
    unittest.main()
