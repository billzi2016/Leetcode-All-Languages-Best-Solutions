# Validation

The `validate/` directory provides a containerized validation environment for generated LeetCode solution Markdown files.

It reads examples from `dataset/merged_problems.json`, extracts language code blocks from `Leetcode-Easy/`, `Leetcode-Medium/`, and `Leetcode-Hard/`, runs the supported executable sections, and writes CSV matrices by difficulty:

```text
validate/reports/easy.csv
validate/reports/medium.csv
validate/reports/hard.csv
```

Each CSV row is a problem. Each language column uses `1` for passed sample cases and `0` for other outcomes.

## Docker

Build from the repository root:

```bash
docker compose -f validate/compose.yaml build
```

Run from the repository root:

```bash
docker compose -f validate/compose.yaml run --rm validate
```

## Direct Command

```bash
python validate/run_validation.py --repo-root .
python validate/run_validation.py --repo-root . --dataset dataset/merged_problems.json
python validate/run_validation.py --repo-root . --reports-dir validate/reports
```

## Validation Layers

The repository uses three complementary quality-control layers:

| Layer | Role | Output |
| --- | --- | --- |
| `migrate/` audits | Finds missing language sections, repairable ordering issues, suspiciously long code blocks, Markdown leftovers, and repeated generated output. | Terminal report or ignored local Markdown report |
| `validate/` | Fast Docker validation against examples already present in `dataset/merged_problems.json`. | `validate/reports/easy.csv`, `medium.csv`, `hard.csv` |
| `validate-pro/` | Extended differential-testing design. It asks `gpt-oss:120b` for additional edge-case candidates, verifies them with Python reference solvers, stores retained cases as JSON, and runs a larger Docker validation set. | `validate-pro/cases/*.json` and `validate-pro/reports/*.csv` |

`validate-pro/` is a deeper validation layer, not a replacement for `validate/`.
