#!/usr/bin/env python
"""动态审计疑似异常的题解代码块，并生成 Markdown 报告。

这个脚本只读扫描 `easy/`、`medium/`、`hard/` 下已经生成的 Markdown 题解，
不会修改任何题解文件。它用于发现模型生成过程中可能出现的异常输出，例如：

- 某个语言代码块相对同难度、同语言的历史分布明显过长；
- 代码块里混入解释、复杂度分析、Markdown 标题或 fenced code block；
- 代码块内部存在明显重复段落，疑似模型绕进循环。

长度判断不使用固定阈值。脚本每次运行都会基于当前仓库已有代码动态统计，
优先使用 `难度 + 语言` 分组；样本不足时退化到 `语言` 分组；仍不足时使用
全局分布。这样后续题库逐步补全后，基线会随已有数据自动更新。

默认报告路径为 `migrate/suspicious_solutions_report.md`。该文件应被
`.gitignore` 忽略，因为它是本地审计产物，不是源码。
"""

from __future__ import annotations

import argparse
import re
import statistics
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


DIFFICULTIES = ("easy", "medium", "hard")
DEFAULT_REPORT = Path("migrate/suspicious_solutions_report.md")
MIN_GROUP_SIZE = 20
MIN_LANGUAGE_SIZE = 30
MAD_MULTIPLIER = 8.0
MIN_ABSOLUTE_CHARS = 2_000
MIN_ABSOLUTE_LINES = 80
NON_ALGORITHM_LANGUAGES = {
    "Bash",
    "MSSQL",
    "MySQL",
    "Mysql",
    "OracleSQL",
    "Oraclesql",
    "PostgreSQL",
    "Postgresql",
    "PythonData",
    "Pythondata",
}

NATURAL_LANGUAGE_PATTERNS = (
    re.compile(r"^\s*(time|space)\s+complexity\s*[:：]", re.IGNORECASE | re.MULTILINE),
    re.compile(r"^\s*(explanation|approach|algorithm)\s*[:：]", re.IGNORECASE | re.MULTILINE),
    re.compile(r"^\s*here\s+is\s+", re.IGNORECASE | re.MULTILINE),
    re.compile(r"^\s*this\s+solution\s+", re.IGNORECASE | re.MULTILINE),
    re.compile(r"^\s*we\s+can\s+", re.IGNORECASE | re.MULTILINE),
    re.compile(r"^\s*#{2,}\s+", re.MULTILINE),
    re.compile(r"```"),
)


@dataclass(frozen=True)
class CodeBlock:
    """题解 Markdown 中解析出的一个语言代码块。

    参数：
        path: 题解 Markdown 文件路径。
        difficulty: 难度目录名，统一为小写。
        language: Markdown 二级标题中的语言名。
        code: fenced code block 内部的代码文本，不包含外层 fence。
        chars: 代码字符数。
        lines: 代码行数。
    """

    path: Path
    difficulty: str
    language: str
    code: str
    chars: int
    lines: int


@dataclass(frozen=True)
class Baseline:
    """动态统计得到的长度基线。

    参数：
        scope: 使用的基线范围，可能是 `difficulty+language`、`language`
            或 `global`。
        count: 基线样本数。
        median_chars: 字符数中位数。
        mad_chars: 字符数 MAD。MAD 为 0 时会退化为 1，避免阈值等于中位数。
        median_lines: 行数中位数。
        mad_lines: 行数 MAD。
    """

    scope: str
    count: int
    median_chars: float
    mad_chars: float
    median_lines: float
    mad_lines: float

    def char_limit(self, mad_multiplier: float) -> float:
        """返回当前基线下的字符数异常阈值。"""

        return self.median_chars + mad_multiplier * max(self.mad_chars, 1.0)

    def line_limit(self, mad_multiplier: float) -> float:
        """返回当前基线下的行数异常阈值。"""

        return self.median_lines + mad_multiplier * max(self.mad_lines, 1.0)


@dataclass(frozen=True)
class Finding:
    """单个疑似异常结果。

    参数：
        block: 触发异常的代码块。
        reason: 异常类别，例如长度异常、自然语言标记或重复内容。
        detail: 可打印到报告里的具体说明。
        baseline: 长度异常使用的动态基线；非长度类异常可以为 None。
    """

    block: CodeBlock
    reason: str
    detail: str
    baseline: Baseline | None = None


def parse_args() -> argparse.Namespace:
    """解析命令行参数。

    返回：
        argparse.Namespace: 包含仓库根目录、报告路径和统计参数。
    """

    parser = argparse.ArgumentParser(description="Audit suspicious generated solution code blocks.")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Project root path.")
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT, help="Markdown report output path.")
    parser.add_argument("--min-group-size", type=int, default=MIN_GROUP_SIZE, help="Minimum samples for difficulty+language baseline.")
    parser.add_argument("--min-language-size", type=int, default=MIN_LANGUAGE_SIZE, help="Minimum samples for language baseline.")
    parser.add_argument("--mad-multiplier", type=float, default=MAD_MULTIPLIER, help="MAD multiplier for length outliers.")
    return parser.parse_args()


def iter_markdown_files(root: Path) -> list[Path]:
    """返回所有难度目录下的题解 Markdown 文件。

    参数：
        root: 仓库根目录。

    返回：
        list[Path]: 排序后的题解文件路径列表，不包含各难度目录自己的 README。
    """

    files: list[Path] = []
    for difficulty in DIFFICULTIES:
        difficulty_dir = root / difficulty
        if not difficulty_dir.exists():
            continue
        files.extend(path for path in difficulty_dir.glob("*/*.md") if path.name.lower() != "readme.md")
    return sorted(files)


def parse_code_blocks(path: Path, root: Path) -> list[CodeBlock]:
    """从单个题解 Markdown 中解析语言代码块。

    参数：
        path: 题解 Markdown 文件路径。
        root: 仓库根目录，用于推导难度目录名。

    返回：
        list[CodeBlock]: 按文件出现顺序排列的代码块列表。
    """

    text = path.read_text(encoding="utf-8")
    difficulty = path.relative_to(root).parts[0]
    blocks: list[CodeBlock] = []
    headings = list(re.finditer(r"^##\s+(.+?)\s*$", text, flags=re.MULTILINE))
    for index, match in enumerate(headings):
        language = match.group(1).strip()
        section_start = match.end()
        section_end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        section = text[section_start:section_end]
        code_match = re.search(r"```[^\n]*\n(.*?)\n```", section, flags=re.DOTALL)
        if not code_match:
            continue
        code = code_match.group(1).strip("\n")
        if not code.strip():
            continue
        blocks.append(
            CodeBlock(
                path=path,
                difficulty=difficulty,
                language=language,
                code=code,
                chars=len(code),
                lines=code.count("\n") + 1,
            )
        )
    return blocks


def median_and_mad(values: list[int]) -> tuple[float, float]:
    """计算中位数和 MAD。

    参数：
        values: 数值样本。

    返回：
        tuple[float, float]: `(median, mad)`。MAD 是各样本到中位数距离的中位数。
    """

    median = statistics.median(values)
    deviations = [abs(value - median) for value in values]
    mad = statistics.median(deviations)
    return float(median), float(mad)


def make_baseline(scope: str, blocks: list[CodeBlock]) -> Baseline:
    """根据一组代码块构造长度基线。

    参数：
        scope: 基线范围说明。
        blocks: 用于统计的代码块样本。

    返回：
        Baseline: 字符数和行数的中位数/MAD 基线。
    """

    median_chars, mad_chars = median_and_mad([block.chars for block in blocks])
    median_lines, mad_lines = median_and_mad([block.lines for block in blocks])
    return Baseline(scope, len(blocks), median_chars, mad_chars, median_lines, mad_lines)


def is_non_algorithm_language(language: str) -> bool:
    """判断代码块语言是否属于 SQL、Shell 或 Python Data 这类非传统算法题。

    参数：
        language: Markdown 二级标题中的语言名。

    返回：
        bool: 非传统算法语言返回 True。
    """

    return language in NON_ALGORITHM_LANGUAGES


def choose_baseline(
    block: CodeBlock,
    by_group: dict[tuple[str, str], list[CodeBlock]],
    by_language: dict[str, list[CodeBlock]],
    algorithm_blocks: list[CodeBlock],
    non_algorithm_blocks: list[CodeBlock],
    all_blocks: list[CodeBlock],
    min_group_size: int,
    min_language_size: int,
) -> Baseline:
    """为某个代码块选择最合适的动态基线。

    参数：
        block: 待审计代码块。
        by_group: `(difficulty, language)` 到样本列表的映射。
        by_language: `language` 到样本列表的映射。
        algorithm_blocks: 普通算法语言样本。
        non_algorithm_blocks: SQL、Shell、Python Data 等非传统算法语言样本。
        all_blocks: 全部样本，用于极端情况下兜底。
        min_group_size: 使用难度+语言基线的最低样本数。
        min_language_size: 使用语言基线的最低样本数。

    返回：
        Baseline: 最细可用粒度的动态基线。
    """

    group_blocks = by_group[(block.difficulty, block.language)]
    if len(group_blocks) >= min_group_size:
        return make_baseline(f"{block.difficulty}+{block.language}", group_blocks)

    language_blocks = by_language[block.language]
    if len(language_blocks) >= min_language_size:
        return make_baseline(block.language, language_blocks)

    if is_non_algorithm_language(block.language) and non_algorithm_blocks:
        return make_baseline("non_algorithm_global", non_algorithm_blocks)

    if not is_non_algorithm_language(block.language) and algorithm_blocks:
        return make_baseline("algorithm_global", algorithm_blocks)

    return make_baseline("global", all_blocks)


def repeated_line_ratio(code: str) -> float:
    """计算代码中重复非空行的比例。

    参数：
        code: 代码文本。

    返回：
        float: 重复非空行数量 / 非空行总数。短行和常见括号行会被过滤，
        避免 C/Java/Rust 等语言的结构符号造成误报。
    """

    lines = [line.strip() for line in code.splitlines()]
    meaningful = [line for line in lines if len(line) >= 12 and line not in {"return nil", "return null"}]
    if len(meaningful) < 12:
        return 0.0
    unique = set(meaningful)
    return (len(meaningful) - len(unique)) / len(meaningful)


def natural_language_markers(code: str, language: str) -> list[str]:
    """查找代码块中疑似解释性文本或 Markdown 残留。

    参数：
        code: 代码文本。
        language: Markdown 二级标题中的语言名。SQL、Shell 和 Python Data
            会保留 Markdown 残留检查，但不使用普通算法代码的英文解释
            marker，避免数据库字段名、注释或查询别名造成误报。

    返回：
        list[str]: 命中的 marker 列表。
    """

    if is_non_algorithm_language(language):
        markdown_only_patterns = NATURAL_LANGUAGE_PATTERNS[-2:]
        return [pattern.pattern for pattern in markdown_only_patterns if pattern.search(code)]
    return [pattern.pattern for pattern in NATURAL_LANGUAGE_PATTERNS if pattern.search(code)]


def audit_blocks(blocks: list[CodeBlock], min_group_size: int, min_language_size: int, mad_multiplier: float) -> list[Finding]:
    """审计所有代码块并返回疑似异常结果。

    参数：
        blocks: 全部已解析代码块。
        min_group_size: 难度+语言基线最低样本数。
        min_language_size: 语言基线最低样本数。
        mad_multiplier: MAD 阈值倍数。

    返回：
        list[Finding]: 按文件路径、语言和异常原因排序的结果。
    """

    by_group: dict[tuple[str, str], list[CodeBlock]] = defaultdict(list)
    by_language: dict[str, list[CodeBlock]] = defaultdict(list)
    for block in blocks:
        by_group[(block.difficulty, block.language)].append(block)
        by_language[block.language].append(block)

    algorithm_blocks = [block for block in blocks if not is_non_algorithm_language(block.language)]
    non_algorithm_blocks = [block for block in blocks if is_non_algorithm_language(block.language)]

    findings: list[Finding] = []
    for block in blocks:
        baseline = choose_baseline(
            block,
            by_group,
            by_language,
            algorithm_blocks,
            non_algorithm_blocks,
            blocks,
            min_group_size,
            min_language_size,
        )
        char_limit = baseline.char_limit(mad_multiplier)
        line_limit = baseline.line_limit(mad_multiplier)
        too_many_chars = block.chars >= MIN_ABSOLUTE_CHARS and block.chars > char_limit
        too_many_lines = block.lines >= MIN_ABSOLUTE_LINES and block.lines > line_limit
        if too_many_chars or too_many_lines:
            findings.append(
                Finding(
                    block=block,
                    reason="length_outlier",
                    detail=(
                        f"chars={block.chars}, lines={block.lines}, "
                        f"char_limit={char_limit:.1f}, line_limit={line_limit:.1f}"
                    ),
                    baseline=baseline,
                )
            )

        markers = natural_language_markers(block.code, block.language)
        if markers:
            findings.append(
                Finding(
                    block=block,
                    reason="natural_language_or_markdown_marker",
                    detail=", ".join(markers[:5]),
                )
            )

        duplicate_ratio = repeated_line_ratio(block.code)
        if duplicate_ratio >= 0.35:
            findings.append(
                Finding(
                    block=block,
                    reason="repeated_lines",
                    detail=f"repeated_line_ratio={duplicate_ratio:.2f}",
                )
            )

    return sorted(findings, key=lambda item: (item.block.path.as_posix(), item.block.language, item.reason))


def render_report(root: Path, blocks: list[CodeBlock], findings: list[Finding]) -> str:
    """渲染 Markdown 审计报告。

    参数：
        root: 仓库根目录。
        blocks: 全部扫描到的代码块。
        findings: 疑似异常结果。

    返回：
        str: Markdown 报告内容。
    """

    lines = [
        "# Suspicious Solution Audit Report",
        "",
        "This report is generated by `migrate/audit_suspicious_solutions.py`.",
        "The audit is read-only and does not modify solution Markdown files.",
        "",
        f"Scanned code blocks: {len(blocks)}",
        f"Suspicious findings: {len(findings)}",
        "",
    ]

    if not findings:
        lines.append("No suspicious code blocks found.")
        return "\n".join(lines).rstrip() + "\n"

    lines.extend(
        [
            "| File | Language | Reason | Size | Detail | Baseline |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for finding in findings:
        block = finding.block
        rel_path = block.path.relative_to(root).as_posix()
        baseline = "-"
        if finding.baseline is not None:
            baseline = (
                f"{finding.baseline.scope}; n={finding.baseline.count}; "
                f"median_chars={finding.baseline.median_chars:.1f}; mad_chars={finding.baseline.mad_chars:.1f}; "
                f"median_lines={finding.baseline.median_lines:.1f}; mad_lines={finding.baseline.mad_lines:.1f}"
            )
        lines.append(
            f"| `{rel_path}` | {block.language} | {finding.reason} | "
            f"{block.chars} chars / {block.lines} lines | {finding.detail} | {baseline} |"
        )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    """命令行入口。

    返回：
        int: 发现疑似异常返回 1；没有异常返回 0。
    """

    args = parse_args()
    root = args.root
    blocks: list[CodeBlock] = []
    for path in iter_markdown_files(root):
        blocks.extend(parse_code_blocks(path, root))

    findings = audit_blocks(blocks, args.min_group_size, args.min_language_size, args.mad_multiplier)
    report_path = args.report if args.report.is_absolute() else root / args.report
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(render_report(root, blocks, findings), encoding="utf-8")
    print(f"Wrote report: {report_path}")
    print(f"Suspicious findings: {len(findings)}")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
