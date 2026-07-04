"""把生成结果写入约定的 Markdown 目录结构。

本模块负责路径计算、语言标题格式和原子替换。调用方决定何时写入，本模块保证每次写入尽量安全。
"""

from __future__ import annotations

import os
import re
from collections import OrderedDict
from dataclasses import dataclass
from pathlib import Path

from .dataset_loader import frontend_id_as_int


LANGUAGE_FENCES = {
    "cpp": "cpp",
    "python": "python",
    "python3": "python",
    "golang": "go",
    "javascript": "javascript",
    "typescript": "typescript",
    "java": "java",
    "c": "c",
    "csharp": "csharp",
    "rust": "rust",
    "ruby": "ruby",
    "php": "php",
    "swift": "swift",
    "kotlin": "kotlin",
    "scala": "scala",
    "dart": "dart",
    "racket": "racket",
    "erlang": "erlang",
    "elixir": "elixir",
}


@dataclass(frozen=True)
class ExistingSolutionSection:
    """已有 Markdown 中一个有效语言代码块。"""

    heading: str
    language: str | None
    code: str


def bucket_name(frontend_id: int) -> str:
    """返回每 100 题一个区间的目录名。"""

    start = ((frontend_id - 1) // 100) * 100 + 1
    end = start + 99
    return f"{start}-{end}"


def problem_output_path(problem: dict, output_root: Path) -> Path:
    """返回单题 Markdown 的目标路径。"""

    frontend_id = frontend_id_as_int(problem)
    difficulty = str(problem.get("difficulty", "")).lower()
    slug = str(problem.get("problem_slug", "")).strip()
    filename = f"{frontend_id:04d}-{slug}.md"
    return output_root / difficulty / bucket_name(frontend_id) / filename


def language_heading(language: str) -> str:
    """把语言 key 转成 Markdown 标题。"""

    if language == "cpp":
        return "Cpp"
    if language == "python3":
        return "Python3"
    return language[:1].upper() + language[1:]


def render_problem_markdown(problem: dict, solutions: dict[str, str]) -> str:
    """根据各语言代码渲染单题 Markdown。"""

    frontend_id = frontend_id_as_int(problem)
    title = str(problem.get("title", "")).strip()
    lines = [f"# {frontend_id:04d}. {title}", ""]
    for language, code in solutions.items():
        fence = LANGUAGE_FENCES.get(language, language)
        lines.extend(
            [
                f"## {language_heading(language)}",
                "",
                f"```{fence}",
                code.rstrip(),
                "```",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def write_atomic(path: Path, content: str) -> None:
    """通过临时兄弟文件替换目标文件，降低中断损坏风险。"""

    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    tmp_path.write_text(content, encoding="utf-8")
    os.replace(tmp_path, path)


def write_problem(path: Path, problem: dict, solutions: dict[str, str]) -> None:
    """渲染并原子写入单题 Markdown。"""

    write_atomic(path, render_problem_markdown(problem, solutions))


def read_existing_languages(path: Path) -> set[str]:
    """读取已有 Markdown 文件里带非空代码块的语言标题。"""

    return {section.heading for section in _read_existing_sections(path, [])}


def read_existing_language_order(path: Path, languages: list[str]) -> list[str]:
    """按文件中出现顺序读取带非空代码块的语言 key。"""

    return [section.language for section in _read_existing_sections(path, languages) if section.language is not None]


def read_existing_solutions(path: Path, languages: list[str]) -> OrderedDict[str, str]:
    """按预期语言顺序读取已有 Markdown 里的代码块。"""

    parsed = {
        section.language: section.code
        for section in _read_existing_sections(path, languages)
        if section.language is not None
    }
    return OrderedDict((language, parsed[language]) for language in languages if language in parsed)


def order_solutions(languages: list[str], solutions: dict[str, str]) -> OrderedDict[str, str]:
    """按数据集语言顺序排列已有和新生成的代码。"""

    return OrderedDict((language, solutions[language]) for language in languages if language in solutions)


def _read_existing_sections(path: Path, languages: list[str]) -> list[ExistingSolutionSection]:
    """解析已有 Markdown 中所有带非空代码块的语言 section。"""

    if not path.exists():
        return []

    text = path.read_text(encoding="utf-8")
    heading_to_language = {language_heading(language): language for language in languages}
    sections: list[ExistingSolutionSection] = []
    heading_matches = list(re.finditer(r"^##\s+(.+?)\s*$", text, flags=re.MULTILINE))

    for index, match in enumerate(heading_matches):
        heading = match.group(1)
        section_start = match.end()
        section_end = heading_matches[index + 1].start() if index + 1 < len(heading_matches) else len(text)
        section = text[section_start:section_end]
        code_match = re.search(r"```[^\n]*\n(.*?)\n```", section, flags=re.DOTALL)
        if code_match and code_match.group(1).strip():
            sections.append(
                ExistingSolutionSection(
                    heading=heading,
                    language=heading_to_language.get(heading),
                    code=code_match.group(1).rstrip(),
                )
            )

    return sections
