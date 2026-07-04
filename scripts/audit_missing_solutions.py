#!/usr/bin/env python
"""扫描生成输出，列出缺失语言和可自修复的顺序异常。

调用示例：

`PYTHONPATH=src python scripts/audit_missing_solutions.py`
`PYTHONPATH=src python scripts/audit_missing_solutions.py --difficulty Hard`
`PYTHONPATH=src python scripts/audit_missing_solutions.py --frontend-ids 4 10`

脚本只读扫描，不调用模型、不写输出文件、不修改题解 Markdown。退出码
`0` 表示没有发现缺失或顺序异常；退出码 `1` 表示打印了需要补跑或可修复
的题目清单，适合放进 shell/CI 检查。
"""

from __future__ import annotations

import argparse
from pathlib import Path

from leetcode_solutions.audit import ProblemAudit, audit_problems
from leetcode_solutions.config import DIFFICULTY_ORDER, Paths
from leetcode_solutions.dataset_loader import filter_by_difficulty, find_by_frontend_id, load_questions


def parse_args() -> argparse.Namespace:
    """解析命令行参数。

    `--difficulty` 用于大范围按难度扫描；`--frontend-ids` 用于小范围
    点查问题题号。两个参数同时出现时，以显式题号为准。
    """

    parser = argparse.ArgumentParser(description="Audit generated LeetCode solution Markdown files.")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Project root path.")
    parser.add_argument(
        "--difficulty",
        choices=DIFFICULTY_ORDER,
        help="Scan one difficulty only.",
    )
    parser.add_argument("--frontend-ids", nargs="+", help="Scan selected LeetCode frontend ids, such as 1 2 4.")
    return parser.parse_args()


def select_questions(args: argparse.Namespace) -> list[dict]:
    """按参数选择要扫描的题目。

    题目来源始终是本地 dataset，保证审计脚本和生成脚本使用完全相同
    的语言列表与题目路径规则。
    """

    paths = Paths.from_root(args.root)
    questions = load_questions(paths.dataset)
    if args.frontend_ids:
        selected = []
        for frontend_id in args.frontend_ids:
            problem = find_by_frontend_id(questions, frontend_id)
            if problem is None:
                print(f"MISSING_DATASET frontend_id={frontend_id}")
                continue
            selected.append(problem)
        return selected
    if args.difficulty:
        return filter_by_difficulty(questions, args.difficulty)
    selected: list[dict] = []
    for difficulty in DIFFICULTY_ORDER:
        selected.extend(filter_by_difficulty(questions, difficulty))
    return selected


def format_audit(result: ProblemAudit, root: Path) -> str:
    """把单题审计结果格式化成一行。

    一行包含题号、slug、难度、相对路径、缺失语言，以及顺序异常时的
    实际顺序和期望顺序，便于直接复制题号去执行小范围补跑。
    """

    relative_path = result.path.relative_to(root) if result.path.is_relative_to(root) else result.path
    parts = [
        f"{result.frontend_id} {result.problem_slug}",
        f"difficulty={result.difficulty}",
        f"path={relative_path}",
    ]
    if result.missing:
        parts.append(f"missing={','.join(result.missing)}")
    if result.order_mismatch:
        parts.append(f"order={','.join(result.existing_order)}")
        parts.append(f"expected={','.join(result.expected_order)}")
    return " | ".join(parts)


def main() -> int:
    """执行审计并返回适合 shell 使用的退出码。

    这里不做任何修复；真正修复发生在后续运行 `generate_solutions.py`
    时，由生成器按最小补跑策略处理。
    """

    args = parse_args()
    paths = Paths.from_root(args.root)
    results = audit_problems(select_questions(args), paths.output_root)
    if not results:
        print("OK no missing languages or repairable order issues found")
        return 0

    print(f"FOUND {len(results)} problem(s) with missing languages or repairable order issues")
    for result in results:
        print(format_audit(result, args.root))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
