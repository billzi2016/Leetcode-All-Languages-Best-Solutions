"""Markdown parsing helpers for generated solution files."""

from __future__ import annotations

import re
from pathlib import Path


DIFFICULTY_DIRS = {
    "Easy": "Leetcode-Easy",
    "Medium": "Leetcode-Medium",
    "Hard": "Leetcode-Hard",
}
LANGUAGE_HEADINGS = {
    "Bash": "bash",
    "C": "c",
    "Cpp": "cpp",
    "Java": "java",
    "Javascript": "javascript",
    "JavaScript": "javascript",
    "Python": "python",
    "Python3": "python3",
}


def bucket_name(frontend_id: int) -> str:
    """Return the fixed-width 100-problem bucket name."""

    start = ((frontend_id - 1) // 100) * 100 + 1
    return f"{start:04d}-{start + 99:04d}"


def solution_path(repo_root: Path, difficulty: str, frontend_id: str, slug: str) -> Path:
    """Return the Markdown solution path for a problem."""

    numeric_id = int(frontend_id)
    return (
        repo_root
        / DIFFICULTY_DIRS[difficulty]
        / bucket_name(numeric_id)
        / f"{numeric_id:04d}-{slug}.md"
    )


def parse_markdown_sections(path: Path) -> dict[str, str]:
    """Parse language code blocks from one solution Markdown file."""

    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    sections: dict[str, str] = {}
    headings = list(re.finditer(r"^##\s+(.+?)\s*$", text, flags=re.MULTILINE))
    for index, match in enumerate(headings):
        heading = match.group(1).strip()
        section_start = match.end()
        section_end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        section = text[section_start:section_end]
        code_match = re.search(r"```[^\n]*\n(.*?)\n```", section, flags=re.DOTALL)
        if not code_match:
            continue
        code = code_match.group(1).strip("\n")
        if code.strip():
            sections[LANGUAGE_HEADINGS.get(heading, heading.lower())] = code
    return sections

