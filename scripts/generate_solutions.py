#!/usr/bin/env python
"""命令行入口。

本脚本负责把用户参数转换为生成器调用，不承载核心业务逻辑；核心逻辑放在 `src/leetcode_solutions/`。
"""

from __future__ import annotations

import argparse
from pathlib import Path

from leetcode_solutions.config import DIFFICULTY_ORDER, Paths, THINK_BY_DIFFICULTY
from leetcode_solutions.dataset_loader import filter_by_difficulty, find_by_frontend_id, load_questions
from leetcode_solutions.generator import SolutionGenerator
from leetcode_solutions.logger import RunLogger
from leetcode_solutions.ollama_client import OllamaClient


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""

    parser = argparse.ArgumentParser(description="Generate LeetCode all-language solutions.")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Project root path.")
    parser.add_argument("--only-frontend-id", help="Generate only one LeetCode frontend id, such as 1.")
    parser.add_argument("--frontend-ids", nargs="+", help="Generate multiple LeetCode frontend ids, such as 1 2 4.")
    parser.add_argument(
        "--difficulty",
        choices=DIFFICULTY_ORDER,
        help="Generate one difficulty only when --only-frontend-id is not set.",
    )
    return parser.parse_args()


def main() -> int:
    """执行生成流程并返回进程退出码。"""

    args = parse_args()
    paths = Paths.from_root(args.root)
    questions = load_questions(paths.dataset)
    logger = RunLogger(paths.logs_root)
    client = OllamaClient(THINK_BY_DIFFICULTY)
    generator = SolutionGenerator(client, logger, paths.output_root)

    try:
        requested_ids = []
        if args.only_frontend_id:
            requested_ids.append(args.only_frontend_id)
        if args.frontend_ids:
            requested_ids.extend(args.frontend_ids)

        if requested_ids:
            for frontend_id in requested_ids:
                problem = find_by_frontend_id(questions, frontend_id)
                if problem is None:
                    logger.error(f"Cannot find frontend_id={frontend_id}")
                    continue
                generator.generate_problem(problem)
            return 0

        difficulties = [args.difficulty] if args.difficulty else list(DIFFICULTY_ORDER)
        for difficulty in difficulties:
            generator.generate_many(filter_by_difficulty(questions, difficulty), difficulty)
        return 0
    finally:
        logger.close()


if __name__ == "__main__":
    raise SystemExit(main())
