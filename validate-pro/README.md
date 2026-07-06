# Validate Pro

`validate-pro/` is the controlled-AI differential validation layer for generated LeetCode solutions.

It uses `gpt-oss:120b` to propose one edge-case candidate at a time, verifies candidates with local Python reference adapters, stores only retained JSON cases, and runs a larger Docker validation set against generated Markdown solutions.

Docs:

- `docs/PRD.md`
- `docs/PRD.cn.md`

## Generate Cases

```bash
PYTHONPATH=validate-pro/src python validate-pro/generate_cases.py --repo-root . --frontend-ids 1 20 121
```

## Validate Retained Cases

```bash
PYTHONPATH=validate-pro/src python validate-pro/run_validation.py --repo-root .
```

## Docker Compose

```bash
docker compose -f validate-pro/compose.yaml build
docker compose -f validate-pro/compose.yaml run --rm validate-pro
```

Generate retained cases through Compose:

```bash
docker compose -f validate-pro/compose.yaml run --rm generate-cases
```

## Artifacts

```text
validate-pro/cases/
validate-pro/reports/
validate-pro/work/
```

These directories are local generated artifacts.

## File Tree

```text
validate-pro/
  docs/
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
