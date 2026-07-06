# Containerized Solution Validation

`Leetcode-QC/validate/` is the fast validation layer inside the LeetCode quality-control toolkit. It reads examples from `dataset/merged_problems.json`, extracts language sections from `Leetcode-Easy/`, `Leetcode-Medium/`, and `Leetcode-Hard/`, compiles or runs supported languages, and writes one CSV matrix per difficulty.

CSV output:

```text
Leetcode-QC/validate/reports/easy.csv
Leetcode-QC/validate/reports/medium.csv
Leetcode-QC/validate/reports/hard.csv
```

Each row is a problem. Each language column uses:

```text
1 = sample cases passed
0 = sample cases not passed
```

## Build

Run from the repository root:

```bash
docker compose -f Leetcode-QC/validate/compose.yaml build
```

## Run

Run from the repository root:

```bash
docker compose -f Leetcode-QC/validate/compose.yaml run --rm validate
```

The default command writes CSV files under `Leetcode-QC/validate/reports/`.

## Options

```bash
python Leetcode-QC/validate/run_validation.py --repo-root /workspace
python Leetcode-QC/validate/run_validation.py --repo-root /workspace --dataset dataset/merged_problems.json
python Leetcode-QC/validate/run_validation.py --repo-root /workspace --reports-dir Leetcode-QC/validate/reports
```

The CSV keeps the language columns declared by the dataset. The bundled executable runners cover Python, Python3, Cpp, Java, and JavaScript sections for supported problem shapes parsed from the dataset examples.

## Relationship With `Leetcode-QC/validate-pro/`

`Leetcode-QC/validate/` is the fast validation layer. It reads examples already present in `dataset/merged_problems.json`, runs supported solution sections, and writes compact CSV matrices.

`Leetcode-QC/validate-pro/` is the extended differential validation layer. It asks `gpt-oss:120b` for additional edge-case candidates, verifies those candidates with Python reference solvers, stores retained generated cases as JSON, and then runs a larger validation set. That workflow is intentionally heavier because ReAct-style case generation includes problem statements, constraints, examples, topics, and starter signatures in the prompt.

Use `Leetcode-QC/validate/` for quick checks and `Leetcode-QC/validate-pro/` for deeper generated-case quality control.

## Specs

- `specs/PRD.md`
- `specs/PRD.cn.md`

## File Tree

```text
Leetcode-QC/
  validate/
    specs/
      PRD.md
      PRD.cn.md
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
