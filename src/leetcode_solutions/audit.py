"""扫描已有输出，报告缺失语言和可修复的顺序异常。

本模块只做只读审计，不调用模型、不写 Markdown、不修复文件。生成器、
命令行脚本和测试都通过这里复用同一套缺失语言和顺序异常判断，避免
审计逻辑和断点续跑逻辑分叉。
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .dataset_loader import Problem
from .markdown_writer import problem_output_path, read_existing_language_order
from .resume import missing_languages


@dataclass(frozen=True)
class ProblemAudit:
    """单题输出审计结果。

    `missing` 表示需要重新调用模型补齐的语言；`order_mismatch` 表示
    语言代码块已经齐全，但文件顺序不是数据集顺序，生成器可直接重写
    Markdown 修复，不需要重新生成代码。
    """

    frontend_id: str
    problem_slug: str
    difficulty: str
    path: Path
    missing: list[str]
    existing_order: list[str]
    expected_order: list[str]

    @property
    def exists(self) -> bool:
        """目标 Markdown 文件是否已经存在。"""

        return self.path.exists()

    @property
    def has_issues(self) -> bool:
        """是否存在缺失语言或语言顺序异常。"""

        return bool(self.missing) or self.order_mismatch

    @property
    def order_mismatch(self) -> bool:
        """完整语言集合存在但顺序和数据集语言顺序不同。"""

        return not self.missing and self.existing_order != self.expected_order


def audit_problem(problem: Problem, output_root: Path) -> ProblemAudit:
    """扫描单题目标文件，计算缺失语言和已有语言顺序。

    调用方传入 dataset 中的一道题和输出根目录；本函数按同一套路径规则
    找到目标 Markdown，并复用 resume/markdown_writer 的解析逻辑判断
    该题是否需要补跑或只需要顺序修复。
    """

    path = problem_output_path(problem, output_root)
    languages = list((problem.get("code_snippets") or {}).keys())
    existing_order = read_existing_language_order(path, languages)
    missing = missing_languages(path, languages)
    expected_order = [language for language in languages if language not in missing]
    return ProblemAudit(
        frontend_id=str(problem.get("frontend_id", "")),
        problem_slug=str(problem.get("problem_slug", "")),
        difficulty=str(problem.get("difficulty", "")),
        path=path,
        missing=missing,
        existing_order=existing_order,
        expected_order=expected_order,
    )


def audit_problems(problems: list[Problem], output_root: Path) -> list[ProblemAudit]:
    """返回所有有缺失语言或顺序异常的题目。

    返回列表只包含有问题的题目，方便 CLI 直接打印报告，也方便测试
    对结果做精确断言。
    """

    return [result for result in (audit_problem(problem, output_root) for problem in problems) if result.has_issues]
