# Project Structure

This document describes the recommended project layout and module responsibilities. Implementation should keep module boundaries clear and follow SOLID and DRY.

## Directory Tree

```text
.
├── README.md
├── README.cn.md
├── docs/
│   ├── PRD.md
│   ├── PRD.cn.md
│   ├── PROJECT_STRUCTURE.md
│   └── PROJECT_STRUCTURE.cn.md
├── requirements.txt
├── .gitignore
├── dataset/
│   ├── dataset.md
│   ├── dataset.cn.md
│   └── merged_problems.json        # downloaded locally, not committed to Git
├── src/
│   └── leetcode_solutions/
│       ├── __init__.py
│       ├── config.py               # model name, paths, retry count, timeout, and shared config
│       ├── dataset_loader.py       # load and validate merged_problems.json
│       ├── prompt_builder.py       # build system prompt, problem prompt, and language prompt
│       ├── ollama_client.py        # wrap Ollama calls
│       ├── markdown_writer.py      # create and update problem Markdown files
│       ├── logger.py               # screen and file logging
│       ├── resume.py               # resume detection and generated-language checks
│       └── generator.py            # orchestrate the generation flow
├── scripts/
│   └── generate_solutions.py       # CLI entry point
├── tests/
│   ├── unit/                       # unit tests for core modules and CLIs
│   │   ├── test_dataset_loader.py  # dataset loading and sorting tests
│   │   ├── test_prompt_builder.py  # prompt construction and missing-field tests
│   │   ├── test_markdown_writer.py # output path, filename, and Markdown format tests
│   │   ├── test_resume.py          # resume detection tests
│   │   ├── test_logger.py          # stdout/stderr/failures log separation tests
│   │   ├── test_ollama_client.py   # ollama library, think mode, and 100_000 limit tests
│   │   ├── test_cli.py             # CLI argument parsing tests
│   │   ├── test_generator.py       # main generator orchestration tests
│   │   └── test_e2e_selected.py    # LeetCode 1/2/4 formal-flow and skip tests
│   ├── integration/                # reserved for cross-module integration tests
│   └── smoke/                      # reserved for lightweight environment smoke tests
├── logs/                           # runtime logs, not committed to Git
├── Leetcode-Easy/                           # generated Easy solutions
├── Leetcode-Medium/                         # generated Medium solutions
└── Leetcode-Hard/                           # generated Hard solutions
```

## Module Responsibilities

- `config.py`: Centralizes model name, think mapping, input/output paths, timeout, retry count, temperature, and other shared config.
- `dataset_loader.py`: Reads JSON, parses `questions`, filters by difficulty, and sorts problems by id.
- `prompt_builder.py`: Builds prompts, skips missing fields, and excludes `images`.
- `ollama_client.py`: Calls Ollama, handles model options, and returns raw code.
- `markdown_writer.py`: Builds target paths, formats Markdown, and writes files atomically.
- `logger.py`: Handles log formatting and stdout/stderr/failures separation.
- `resume.py`: Determines whether a problem or language has already been generated.
- `generator.py`: Coordinates modules and runs Easy -> Medium -> Hard sequentially.

## Tests

All unit tests live in `tests/unit/` and use Python's standard `unittest` library.

Tests should cover:

- Dataset loading, missing fields, difficulty filtering, and problem-id sorting.
- Prompt construction, especially `images` exclusion, optional `solutions`, and language starter-code insertion.
- Markdown output paths, 100-problem buckets, filename format, and language section format.
- Easy/Medium write-once-per-problem behavior and Hard write-once-per-language behavior.
- Resume detection for complete problems and missing languages.
- stdout/stderr/failures log separation.
- Environment warning filtering for known requests dependency warnings.
- Retry-3 failure behavior that records logs and continues with the next problem.
- Ollama client usage through the Python `ollama` package, not `requests`.
- Ollama `hello` smoke tests for `low`, `medium`, and `high` think modes.
- Ollama options including a 100_000 token output limit and temperature `0.1`.
- CLI support for multiple problem ids, such as `--frontend-ids 1 2 4`.
- Formal-flow tests for LeetCode 1 / 2 / 4, covering Easy, Medium, and Hard, plus second-run skip behavior.

## SOLID

- Single Responsibility: each module handles one clear concern; prompt construction does not write files.
- Open/Closed: adding a model, output format, or language filter should usually be done through config or small modules, not by rewriting the main flow.
- Liskov Substitution: the model client should expose a stable interface so Ollama can be replaced without changing generation orchestration.
- Interface Segregation: callers should depend only on the methods they need.
- Dependency Inversion: orchestration depends on capabilities such as `ModelClient`, `Writer`, and `Logger`, not scattered low-level implementations.

## DRY

- The shared problem prompt is built once and reused across all languages for the same problem.
- Difficulty-to-think mapping is defined once in config.
- Output path and filename rules are implemented once in `markdown_writer.py`.
- Log formatting is defined once in `logger.py`.
- Resume checks are implemented once in `resume.py`.

Avoid copy-pasting path construction, prompt construction, retry logic, and Markdown formatting logic.
