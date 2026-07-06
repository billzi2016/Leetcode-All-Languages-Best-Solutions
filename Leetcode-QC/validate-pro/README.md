# Validate Pro

`Leetcode-QC/validate-pro/` is the controlled-AI differential validation layer for generated LeetCode solutions.

Differential validation means the project does not only trust one generated solution. It asks `gpt-oss:120b` to design one additional edge-case candidate at a time, uses local Python reference adapters to calculate the expected answer, stores only verified JSON cases, and then runs a larger Docker validation set against generated Markdown solutions.

Docs:

- `specs/PRD.md`
- `specs/PRD.cn.md`

## Generate Cases

```bash
PYTHONPATH=Leetcode-QC/validate-pro/src python Leetcode-QC/validate-pro/generate_cases.py --repo-root . --frontend-ids 1 20 121
```

## Validate Retained Cases

```bash
PYTHONPATH=Leetcode-QC/validate-pro/src python Leetcode-QC/validate-pro/run_validation.py --repo-root .
```

## Docker Compose

```bash
docker compose -f Leetcode-QC/validate-pro/compose.yaml build
docker compose -f Leetcode-QC/validate-pro/compose.yaml run --rm validate-pro
```

Generate retained cases through Compose:

```bash
docker compose -f Leetcode-QC/validate-pro/compose.yaml run --rm generate-cases
```

## Artifacts

```text
Leetcode-QC/validate-pro/cases/
Leetcode-QC/validate-pro/reports/
Leetcode-QC/validate-pro/work/
```

These directories are local generated artifacts.

## File Tree

```text
Leetcode-QC/
  validate-pro/
    specs/
      PRD.md
      PRD.cn.md
    src/
      validate_pro/
        adapters/
        case_store.py
        dataset.py
        llm_case_generator.py
        markdown.py
        prompt_builder.py
        reference.py
        report.py
    tests/
      unit/
      integration/
      smoke/
    generate_cases.py
    run_validation.py
    Dockerfile
    requirements.txt
```
