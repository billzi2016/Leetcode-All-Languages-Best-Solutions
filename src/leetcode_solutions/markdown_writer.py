"""把生成结果写入约定的 Markdown 目录结构。

本模块集中管理所有和题解 Markdown 文件有关的规则：

- 题目文件应该落到哪个难度目录、哪个 100 题分桶目录；
- 文件名如何使用四位补零题号和 problem_slug；
- LeetCode 语言 key 如何映射成 Markdown 标题和代码块 fence；
- 如何从已有 Markdown 中读回已经生成过的语言代码；
- 如何按 dataset 中的语言顺序重新排列已有代码；
- 如何通过临时同级文件加 `os.replace()` 做原子替换。

生成器只决定“什么时候写”和“写哪些语言”，不直接拼路径或解析 Markdown。
这样可以保证生成、断点续跑、审计和测试使用同一套文件格式规则。
"""

from __future__ import annotations

import os
import re
from collections import OrderedDict
from dataclasses import dataclass
from pathlib import Path

from .dataset_loader import frontend_id_as_int


LANGUAGE_FENCES = {
    "bash": "bash",
    "cpp": "cpp",
    "python": "python",
    "python3": "python",
    "pythondata": "python",
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
    "mysql": "sql",
    "mssql": "sql",
    "oraclesql": "sql",
    "postgresql": "sql",
}

SPECIAL_LANGUAGE_HEADINGS = {
    "mysql": "MySQL",
    "mssql": "MSSQL",
    "oraclesql": "OracleSQL",
    "postgresql": "PostgreSQL",
    "pythondata": "PythonData",
}


@dataclass(frozen=True)
class ExistingSolutionSection:
    """已有 Markdown 中解析出来的一个有效语言代码块。

    参数：
        heading: Markdown 二级标题文本，例如 `Python3` 或 `Cpp`。
        language: 标题反查到的 dataset 语言 key，例如 `python3`。
            如果标题不是预期语言，则为 None；这样调用方可以忽略未知段落。
        code: 非空代码块内容，不包含外层 ``` fence。
    """

    heading: str
    language: str | None
    code: str


def bucket_name(frontend_id: int) -> str:
    """返回每 100 题一个固定宽度范围目录名。

    参数：
        frontend_id: LeetCode 数字题号。

    返回：
        str: 形如 `0001-0100`、`0101-0200`、`1301-1400` 的目录名。

    说明：
        旧的 `1-100`、`101-200` 在字符串排序下会和四位题号目录混在一起。
        固定宽度范围既保留了人类可读的区间语义，也能在 GitHub 和文件管理器
        里稳定按字典序排序。
    """

    start = ((frontend_id - 1) // 100) * 100 + 1
    end = start + 99
    return f"{start:04d}-{end:04d}"


def problem_output_path(problem: dict, output_root: Path) -> Path:
    """返回单题 Markdown 的目标路径。

    参数：
        problem: dataset 中的一道题，至少需要 `frontend_id`、`difficulty`
            和 `problem_slug`。
        output_root: 输出根目录，当前项目中通常是仓库根目录。

    返回：
        Path: 形如 `easy/0001-0100/0001-two-sum.md` 的完整路径。
    """

    frontend_id = frontend_id_as_int(problem)
    difficulty = str(problem.get("difficulty", "")).lower()
    slug = str(problem.get("problem_slug", "")).strip()
    filename = f"{frontend_id:04d}-{slug}.md"
    return output_root / difficulty / bucket_name(frontend_id) / filename


def language_heading(language: str) -> str:
    """把 dataset 语言 key 转成 Markdown 二级标题。

    参数：
        language: dataset `code_snippets` 中的语言 key，例如 `cpp`、
            `python3`、`golang`。

    返回：
        str: 写入 Markdown 的标题文本。少数语言需要特殊大小写，例如
        `cpp` 写成 `Cpp`，`python3` 写成 `Python3`。
    """

    if language == "cpp":
        return "Cpp"
    if language == "python3":
        return "Python3"
    if language in SPECIAL_LANGUAGE_HEADINGS:
        return SPECIAL_LANGUAGE_HEADINGS[language]
    return language[:1].upper() + language[1:]


def legacy_language_heading(language: str) -> str:
    """返回早期标题规则下的语言名，用于兼容已经生成的旧 Markdown。

    参数：
        language: dataset `code_snippets` 中的语言 key。

    返回：
        str: 旧实现使用的简单首字母大写标题，例如 `Mysql`、`Pythondata`。

    说明：
        新文件会写更准确的 `MySQL`、`PythonData` 等标题；但历史文件可能
        已经使用旧标题。读取时同时接受新旧标题，可以避免一次标题美化让
        审计脚本误判旧文件缺失语言。
    """

    if language == "cpp":
        return "Cpp"
    if language == "python3":
        return "Python3"
    return language[:1].upper() + language[1:]


def render_problem_markdown(problem: dict, solutions: dict[str, str]) -> str:
    """根据各语言代码渲染单题 Markdown 文本。

    参数：
        problem: dataset 中的一道题，用于生成一级标题。
        solutions: 已经生成或读回的语言代码。调用方应在传入前通过
            `order_solutions()` 保证顺序符合 dataset 语言顺序。

    返回：
        str: 完整 Markdown 文本，末尾保留一个换行，方便 Git diff。
    """

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
    """通过临时兄弟文件替换目标文件，降低中断损坏风险。

    参数：
        path: 最终目标文件路径。
        content: 要写入的完整文本。

    说明：
        先写 `xxx.md.tmp`，再用 `os.replace()` 替换目标文件。这样即使进程
        在写入期间被中断，已有的完整 `.md` 文件也不容易变成半截内容。
    """

    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    tmp_path.write_text(content, encoding="utf-8")
    os.replace(tmp_path, path)


def write_problem(path: Path, problem: dict, solutions: dict[str, str]) -> None:
    """渲染并原子写入单题 Markdown。

    参数：
        path: 目标 Markdown 文件路径。
        problem: dataset 中的一道题。
        solutions: 要写入的语言代码映射。
    """

    write_atomic(path, render_problem_markdown(problem, solutions))


def read_existing_languages(path: Path) -> set[str]:
    """读取已有 Markdown 文件里带非空代码块的语言标题。

    参数：
        path: 待检查的 Markdown 文件路径。

    返回：
        set[str]: 已经存在且代码块非空的 Markdown 标题集合，例如
        `{"Cpp", "Python3"}`。空代码块不算完成。
    """

    return {section.heading for section in _read_existing_sections(path, [])}


def read_existing_language_order(path: Path, languages: list[str]) -> list[str]:
    """按文件中出现顺序读取带非空代码块的语言 key。

    参数：
        path: 已有 Markdown 文件路径。
        languages: dataset 中该题的预期语言 key 顺序。

    返回：
        list[str]: 文件中实际出现的语言 key 顺序。未知标题会被忽略。
    """

    return [section.language for section in _read_existing_sections(path, languages) if section.language is not None]


def read_existing_solutions(path: Path, languages: list[str]) -> OrderedDict[str, str]:
    """按预期语言顺序读取已有 Markdown 里的代码块。

    参数：
        path: 已有 Markdown 文件路径。
        languages: dataset 中该题的预期语言 key 顺序。

    返回：
        OrderedDict[str, str]: 只包含已存在且非空的语言代码，并按 dataset
        语言顺序排列。这样旧文件即使顺序乱，写回时也能恢复标准顺序。
    """

    parsed = {
        section.language: section.code
        for section in _read_existing_sections(path, languages)
        if section.language is not None
    }
    return OrderedDict((language, parsed[language]) for language in languages if language in parsed)


def order_solutions(languages: list[str], solutions: dict[str, str]) -> OrderedDict[str, str]:
    """按数据集语言顺序排列已有和新生成的代码。

    参数：
        languages: dataset `code_snippets` 的语言 key 顺序。
        solutions: 语言到代码的映射，可能只包含部分语言。

    返回：
        OrderedDict[str, str]: 按 `languages` 顺序筛出的代码映射。
    """

    return OrderedDict((language, solutions[language]) for language in languages if language in solutions)


def _read_existing_sections(path: Path, languages: list[str]) -> list[ExistingSolutionSection]:
    """解析已有 Markdown 中所有带非空代码块的语言 section。

    参数：
        path: Markdown 文件路径。
        languages: 预期语言 key 列表，用于把标题反查回语言 key。

    返回：
        list[ExistingSolutionSection]: 按文件出现顺序排列的有效 section。

    实现说明：
        解析逻辑以二级标题 `## Language` 为 section 边界，再在每个 section
        里找第一个 fenced code block。这样可以容忍标题之间有空行或其它文本，
        但仍然要求代码块非空才算已经完成。
    """

    if not path.exists():
        return []

    text = path.read_text(encoding="utf-8")
    heading_to_language = {}
    for language in languages:
        heading_to_language[language_heading(language)] = language
        heading_to_language[legacy_language_heading(language)] = language
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
