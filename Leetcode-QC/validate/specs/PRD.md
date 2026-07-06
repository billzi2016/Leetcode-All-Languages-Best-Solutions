# Quick Validate PRD

`Leetcode-QC/validate/` is the fast Docker validation layer for generated LeetCode solution Markdown files.

It is designed to answer one practical question quickly: can the generated language sections run against the official examples already present in `dataset/merged_problems.json`?

## Goals

- Read problem examples from `dataset/merged_problems.json`.
- Locate generated solution Markdown files under `Leetcode-Easy/`, `Leetcode-Medium/`, and `Leetcode-Hard/`.
- Extract supported language code blocks from each Markdown file.
- Compile or run supported languages inside a reproducible Docker environment.
- Write one compact CSV matrix per difficulty.

## Non-Goals

- It does not generate new test cases.
- It does not replace `Leetcode-QC/validate-pro/`.
- It does not attempt to prove full correctness beyond the dataset examples.
- It does not modify generated solution Markdown files.

## Inputs

```text
dataset/merged_problems.json
Leetcode-Easy/**/*.md
Leetcode-Medium/**/*.md
Leetcode-Hard/**/*.md
```

The dataset provides problem metadata, examples, language declarations, starter signatures, and difficulty labels. The Markdown files provide generated code sections for each language.

## Outputs

```text
Leetcode-QC/validate/reports/easy.csv
Leetcode-QC/validate/reports/medium.csv
Leetcode-QC/validate/reports/hard.csv
```

Each row is a problem. Each language column uses:

```text
1 = official dataset examples passed
0 = official dataset examples did not pass
```

`reports/` and `work/` are local generated artifacts and are ignored by Git.

## Execution Model

The Docker image installs the language runtimes needed by the validation harness. The compose command mounts the repository root at `/workspace`, so the runner can read the dataset, generated Markdown files, and local output directories through the same paths used by repository scripts.

```bash
docker compose -f Leetcode-QC/validate/compose.yaml build
docker compose -f Leetcode-QC/validate/compose.yaml run --rm validate
```

The direct runner is also available:

```bash
python Leetcode-QC/validate/run_validation.py --repo-root /workspace
python Leetcode-QC/validate/run_validation.py --repo-root /workspace --dataset dataset/merged_problems.json
python Leetcode-QC/validate/run_validation.py --repo-root /workspace --reports-dir Leetcode-QC/validate/reports
```

## Relationship With Validate Pro

`Leetcode-QC/validate/` is the baseline layer. It uses the official examples that already exist in the dataset and is intended for quick feedback.

`Leetcode-QC/validate-pro/` is the deeper differential validation layer. It can ask `gpt-oss:120b` to propose additional edge-case candidates, verify those candidates with Python reference solvers, retain only verified JSON cases, and then run a larger validation set.

The two layers are complementary: quick validation checks whether generated solutions handle known examples, while Validate Pro expands coverage with verified generated cases.

## Acceptance Criteria

- Docker build uses `Leetcode-QC/validate/Dockerfile`.
- Compose runs from `Leetcode-QC/validate/compose.yaml` while mounting the repository root as `/workspace`.
- CSV reports are written under `Leetcode-QC/validate/reports/`.
- The runner keeps language columns declared by the dataset.
- The module remains read-only with respect to generated Markdown solution files.
