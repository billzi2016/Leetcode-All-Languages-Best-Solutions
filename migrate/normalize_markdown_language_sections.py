#!/usr/bin/env python
"""规范化历史题解 Markdown 中的语言标题和代码块 fence。

这个脚本用于整理老版本生成器已经写出的 SQL、Shell 和 Python Data 题解。
老版本会把 `mysql` 写成 `## Mysql` + ```mysql，把 `pythondata` 写成
`## Pythondata` + ```pythondata。它们可以被仓库读取，但在 MkDocs 展示和
代码高亮上不够规范。

脚本只处理 Markdown 结构层面的兼容迁移：

- `## Mysql` / `## mysql` -> `## MySQL`
- `## Mssql` / `## mssql` -> `## MSSQL`
- `## Oraclesql` / `## oraclesql` -> `## OracleSQL`
- `## Postgresql` / `## postgresql` -> `## PostgreSQL`
- `## Pythondata` / `## pythondata` -> `## PythonData`
- 对应 SQL fence 统一改为 ```sql
- `pythondata` fence 统一改为 ```python

默认只打印会修改的文件，不写入磁盘。确认无误后加 `--apply` 才会真正
重写文件。脚本不会修改代码块内容本身，也不会调用模型。
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


DIFFICULTY_DIRS = ("easy", "medium", "hard")
HEADING_REWRITES = {
    "mysql": "MySQL",
    "mssql": "MSSQL",
    "oraclesql": "OracleSQL",
    "postgresql": "PostgreSQL",
    "pythondata": "PythonData",
}
FENCE_REWRITES = {
    "mysql": "sql",
    "mssql": "sql",
    "oraclesql": "sql",
    "postgresql": "sql",
    "pythondata": "python",
}


@dataclass(frozen=True)
class RewriteResult:
    """单个 Markdown 文件的规范化结果。

    参数：
        path: 被扫描的 Markdown 文件路径。
        content: 规范化后的完整文件内容。
        heading_changes: 语言标题改写次数。
        fence_changes: 代码块 fence 改写次数。
    """

    path: Path
    content: str
    heading_changes: int
    fence_changes: int

    @property
    def changed(self) -> bool:
        """文件内容是否发生变化。"""

        return self.heading_changes > 0 or self.fence_changes > 0


def parse_args() -> argparse.Namespace:
    """解析命令行参数。

    返回：
        argparse.Namespace: 包含仓库根目录和是否实际写入的开关。
    """

    parser = argparse.ArgumentParser(description="Normalize legacy Markdown language headings and fences.")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Project root path.")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually rewrite Markdown files. Without this flag the script only prints the plan.",
    )
    return parser.parse_args()


def iter_solution_markdown(root: Path) -> list[Path]:
    """返回所有题解 Markdown 文件。

    参数：
        root: 仓库根目录。

    返回：
        list[Path]: 排序后的题解文件路径，不包含各难度目录 README。
    """

    files: list[Path] = []
    for difficulty in DIFFICULTY_DIRS:
        difficulty_dir = root / difficulty
        if not difficulty_dir.exists():
            continue
        files.extend(path for path in difficulty_dir.glob("*/*.md") if path.name.lower() != "readme.md")
    return sorted(files)


def normalize_heading(match: re.Match[str]) -> str:
    """把旧语言标题改成规范标题。

    参数：
        match: `re.sub` 传入的标题匹配对象。

    返回：
        str: 规范化后的整行标题。
    """

    original = match.group(1)
    normalized = HEADING_REWRITES.get(original.strip().lower())
    if normalized is None:
        return match.group(0)
    return f"## {normalized}"


def normalize_fence(match: re.Match[str]) -> str:
    """把旧代码块 fence 改成 MkDocs 更容易识别的 fence。

    参数：
        match: `re.sub` 传入的 fence 匹配对象。

    返回：
        str: 规范化后的 fence 起始行。
    """

    original = match.group(1)
    normalized = FENCE_REWRITES.get(original.strip().lower())
    if normalized is None:
        return match.group(0)
    return f"```{normalized}"


def normalize_content(path: Path) -> RewriteResult:
    """规范化单个 Markdown 文件内容。

    参数：
        path: 待扫描的 Markdown 文件。

    返回：
        RewriteResult: 包含新内容和改写统计。
    """

    text = path.read_text(encoding="utf-8")
    heading_changes = 0
    fence_changes = 0

    def heading_replacer(match: re.Match[str]) -> str:
        nonlocal heading_changes
        replacement = normalize_heading(match)
        if replacement != match.group(0):
            heading_changes += 1
        return replacement

    def fence_replacer(match: re.Match[str]) -> str:
        nonlocal fence_changes
        replacement = normalize_fence(match)
        if replacement != match.group(0):
            fence_changes += 1
        return replacement

    text = re.sub(r"^##\s+([^\n#`]+?)\s*$", heading_replacer, text, flags=re.MULTILINE)
    text = re.sub(r"^```([A-Za-z0-9_+-]+)\s*$", fence_replacer, text, flags=re.MULTILINE)
    return RewriteResult(path=path, content=text, heading_changes=heading_changes, fence_changes=fence_changes)


def run(root: Path, apply: bool) -> int:
    """打印或执行 Markdown 语言 section 规范化。

    参数：
        root: 仓库根目录。
        apply: True 表示实际写回文件；False 表示只打印计划。

    返回：
        int: 成功返回 0。
    """

    results = [normalize_content(path) for path in iter_solution_markdown(root)]
    changed = [result for result in results if result.changed]
    if not changed:
        print("No Markdown language sections need normalization.")
        return 0

    for result in changed:
        relative_path = result.path.relative_to(root)
        print(
            f"{relative_path}: "
            f"headings={result.heading_changes}, fences={result.fence_changes}"
        )
        if apply:
            result.path.write_text(result.content, encoding="utf-8")

    if not apply:
        print("Dry run only. Re-run with --apply to rewrite Markdown files.")
    return 0


def main() -> int:
    """命令行入口。"""

    args = parse_args()
    return run(args.root, args.apply)


if __name__ == "__main__":
    raise SystemExit(main())
