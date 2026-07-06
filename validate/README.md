# Containerized Solution Validation

`validate/` contains a reproducible validation environment for generated LeetCode solution Markdown files. It reads examples from `dataset/merged_problems.json`, extracts language sections from `Leetcode-Easy/`, `Leetcode-Medium/`, and `Leetcode-Hard/`, compiles or runs supported languages, and writes one CSV matrix per difficulty.

CSV output:

```text
validate/reports/easy.csv
validate/reports/medium.csv
validate/reports/hard.csv
```

Each row is a problem. Each language column uses:

```text
1 = sample cases passed
0 = sample cases not passed
```

## Build

Run from the repository root:

```bash
docker compose -f validate/compose.yaml build
```

## Run

Run from the repository root:

```bash
docker compose -f validate/compose.yaml run --rm validate
```

The default command writes CSV files under `validate/reports/`.

## Options

```bash
python validate/run_validation.py --repo-root /workspace
python validate/run_validation.py --repo-root /workspace --dataset dataset/merged_problems.json
python validate/run_validation.py --repo-root /workspace --reports-dir validate/reports
```

The CSV keeps the language columns declared by the dataset. The bundled executable runners cover Python, Python3, Cpp, Java, and JavaScript sections for supported problem shapes parsed from the dataset examples.

## Relationship With `validate-pro/`

`validate/` is the fast validation layer. It reads examples already present in `dataset/merged_problems.json`, runs supported solution sections, and writes compact CSV matrices.

`validate-pro/` is the extended differential-testing layer. It is designed to ask `gpt-oss:120b` for additional edge-case candidates, verify those candidates with Python reference solvers, store retained generated cases as JSON, and then run a larger validation set. That workflow is intentionally heavier: it can take much longer, create many local artifacts, and consume a large token budget because ReAct-style case generation includes problem statements, constraints, examples, topics, and starter signatures in the prompt.

Use `validate/` for quick checks and `validate-pro/` for deeper generated-case quality control.

## File Tree

```text
validate/
  compose.yaml
  Dockerfile
  README.md
  README.cn.md
  requirements.txt
  run_validation.py
  reports/
    easy.csv
    medium.csv
    hard.csv
  work/
```

`reports/` and `work/` are local generated artifacts.
