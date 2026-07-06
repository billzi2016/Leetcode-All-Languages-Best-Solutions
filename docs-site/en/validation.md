# Validation

The validation system is organized under `Leetcode-QC/`. It has three layers, from lightweight static checks to deeper generated-case differential validation.

## Layer 1: Static Audits

`migrate/audit_missing_solutions.py` and `migrate/audit_suspicious_solutions.py` scan generated Markdown without running solution code. They check for missing language sections, repairable ordering issues, suspiciously long code blocks, Markdown leftovers, and repeated generated output.

## Layer 2: Baseline Docker Validation

`Leetcode-QC/validate/` is the fast Docker validation layer. It reads examples from `dataset/merged_problems.json`, extracts language code blocks from `Leetcode-Easy/`, `Leetcode-Medium/`, and `Leetcode-Hard/`, runs the supported executable sections, and writes CSV matrices by difficulty:

```text
Leetcode-QC/validate/reports/easy.csv
Leetcode-QC/validate/reports/medium.csv
Leetcode-QC/validate/reports/hard.csv
```

Each CSV row is a problem. Each language column uses `1` for passed sample cases and `0` for other outcomes.

## Docker

Build from the repository root:

```bash
docker compose -f Leetcode-QC/validate/compose.yaml build
```

Run from the repository root:

```bash
docker compose -f Leetcode-QC/validate/compose.yaml run --rm validate
```

## Direct Command

```bash
python Leetcode-QC/validate/run_validation.py --repo-root .
python Leetcode-QC/validate/run_validation.py --repo-root . --dataset dataset/merged_problems.json
python Leetcode-QC/validate/run_validation.py --repo-root . --reports-dir Leetcode-QC/validate/reports
```

## Layer 3: Validate Pro Differential Validation

`Leetcode-QC/validate-pro/` is the extended differential validation layer. Differential validation means the project does not only trust one generated solution: it asks `gpt-oss:120b` to design more edge-case candidates, uses local Python reference solvers to calculate the expected answers, stores only verified cases as JSON, and then runs a larger Docker validation set against the generated solutions.

Validate Pro entry points:

```bash
docker compose -f Leetcode-QC/validate-pro/compose.yaml build
docker compose -f Leetcode-QC/validate-pro/compose.yaml run --rm validate-pro
docker compose -f Leetcode-QC/validate-pro/compose.yaml run --rm generate-cases
```

Detailed design:

- [Validate Pro PRD](validate-pro-prd.md)

`Leetcode-QC/validate-pro/` is a deeper validation layer, not a replacement for `Leetcode-QC/validate/`.
