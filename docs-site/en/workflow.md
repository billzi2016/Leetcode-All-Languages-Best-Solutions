# End-to-End Workflow

This page explains how the generator, documentation site, and deployment workflow fit together.

The workflow is designed for long-running full generation: it can resume after interruption, keep failure data separate, and keep the documentation aligned with the repository's actual behavior.

## Generation Flow

```mermaid
flowchart TD
    A[Download merged_problems.json locally] --> B[Load questions]
    B --> C[Filter by difficulty or frontend id]
    C --> D[Order Easy / Medium / Hard]
    D --> E[Build shared problem prompt]
    E --> F[Iterate code_snippets languages]
    F --> G[Build language prompt]
    G --> H[Call Ollama]
    H --> I[Write Markdown solution file]
    I --> J[Skip completed file on next run]
```

## Runtime Intent

- `merged_problems.json` is downloaded locally and not committed, so the repository does not carry the large dataset file.
- The shared problem prompt uses useful problem fields but skips `images` because the current model is not multimodal.
- The language prompt contains only the target language and starter code, so switching languages changes the smallest possible input.
- Easy uses `low` think mode, Medium uses `medium`, and Hard uses `high`, matching reasoning effort to problem complexity.
- A failed language is retried up to three times. If it still fails, the failure is written to the failures log and the run continues.
- Existing target Markdown files are treated as completed output, so a second run can skip them and resume long tmux jobs.

## Prompt Reuse Path

```mermaid
flowchart TD
    A[SYSTEM_PROMPT globally fixed] --> B[Problem 0001 problem_prompt]
    B --> C[python3 language_prompt]
    B --> D[cpp language_prompt]
    B --> E[java language_prompt]
    C --> F[0001 Python3 code]
    D --> G[0001 C++ code]
    E --> H[0001 Java code]

    A --> I[Problem 0002 problem_prompt]
    I --> J[python3 / cpp / java ...]
```

The generator splits prompts into three layers so identical content stays near the request prefix. `SYSTEM_PROMPT` holds stable rules, `problem_prompt` holds shared data for one problem, and `language_prompt` holds the smallest language-specific delta. This supports three goals at once: better prefix reuse, easier debugging, and targeted reruns when one language fails.

Do not rebuild every request as a completely different block of mixed problem data, language requirements, and output rules. That reduces reuse and makes failures harder to diagnose.

## Background Generation With tmux

The tmux scripts are entry points for long-running generation jobs. `scripts/tmux_all.sh` generates all difficulties; `scripts/tmux_easy.sh`, `scripts/tmux_medium.sh`, and `scripts/tmux_hard.sh` generate Easy, Medium, and Hard respectively. Each script installs the root `requirements.txt` first, then starts the corresponding tmux session.

```mermaid
flowchart TD
    A[Run a tmux script] --> B[Enter repository root]
    B --> C[python -m pip install -r requirements.txt]
    C --> D{Script type}
    D -->|tmux_all.sh| E[Run all difficulties: leetcode-all]
    D -->|tmux_easy.sh| F[Run Easy: leetcode-easy]
    D -->|tmux_medium.sh| G[Run Medium: leetcode-medium]
    D -->|tmux_hard.sh| H[Run Hard: leetcode-hard]
    E --> I[Inspect with tmux attach]
    F --> I
    G --> I
    H --> I
    I --> J[Write logs under logs/datetime]
```

Dependency installation happens before tmux starts so environment failures appear in the current terminal. The actual generation then runs in the background.

Common commands:

```bash
scripts/tmux_all.sh
scripts/tmux_easy.sh
scripts/tmux_medium.sh
scripts/tmux_hard.sh
tmux ls
tmux attach -t leetcode-all
tmux attach -t leetcode-easy
tmux attach -t leetcode-medium
tmux attach -t leetcode-hard
tmux kill-session -t leetcode-all
tmux kill-session -t leetcode-easy
tmux kill-session -t leetcode-medium
tmux kill-session -t leetcode-hard
tmux kill-server
```

`tmux kill-session` cancels only this project's current generation task. `tmux kill-server` cancels every tmux session, so it should only be used when no other tmux work is running.

## Resume and Rerun Strategy

```mermaid
flowchart TD
    A[Prepare problem Markdown] --> B{Target file exists?}
    B -->|Yes| C[Skip problem]
    B -->|No| D[Iterate all languages]
    D --> E{Language generated?}
    E -->|Yes| F[Keep generated result in memory]
    E -->|No| G[Retry up to 3 times]
    G --> H{Still failed?}
    H -->|Yes| I[Write failures.jsonl and continue]
    H -->|No| F
    F --> J[Write Markdown by difficulty]
```

Easy and Medium write each problem Markdown once. Hard writes at language granularity. This reduces repeated I/O for normal cases while giving complex problems finer save points.

## Logs and Failure Handling

```mermaid
flowchart LR
    A[Generation task] --> B[stdout.log: normal progress]
    A --> C[stderr.log: warnings and error text]
    A --> D[failures.jsonl: structured failed units]
    D --> E[Rerun by problem id and language later]
```

stdout, stderr, and failures are separated to keep long-running output readable. Screen output is for progress, file logs preserve the run context, and `failures.jsonl` supports targeted reruns.

The log directory is timestamped, for example:

```text
logs/
  2026-07-03_031520/
    stdout.log
    stderr.log
    failures.jsonl
```

`stdout.log` stores normal progress and completion messages, `stderr.log` stores warnings, exceptions, and model-call error text, and `failures.jsonl` stores machine-readable failed units.

## Documentation Flow

```mermaid
flowchart TD
    A[English Markdown files] --> C[MkDocs Build]
    B[Chinese Markdown files] --> C
    C --> D[Static site artifact]
    D --> E[GitHub Pages deploy]
```

## GitHub Actions Flow

```mermaid
sequenceDiagram
    participant Dev as Developer
    participant GH as GitHub
    participant Action as GitHub Actions
    participant Pages as GitHub Pages

    Dev->>GH: Push docs-site changes
    GH->>Action: Trigger docs workflow
    Action->>Action: Install dependencies
    Action->>Action: Build MkDocs site
    Action->>Pages: Deploy static artifact
    Pages-->>Dev: Published documentation site
```

The site root provides language entry points, while `cn/` and `en/` hold the Chinese and English pages. GitHub Actions only builds and deploys documentation; solution generation depends on local Ollama and the local dataset file.
