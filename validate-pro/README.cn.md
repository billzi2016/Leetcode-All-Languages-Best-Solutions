# Validate Pro

`validate-pro/` 是生成题解的可控 AI 对数验证层。

它使用 `gpt-oss:120b` 一次提出一个边界样例候选，再用本地 Python 参考 adapter 校验候选样例，只把通过校验的样例保存为 JSON，最后用更大的样例集合验证已经生成的 Markdown 题解。

文档：

- `docs/PRD.md`
- `docs/PRD.cn.md`

## 生成样例

```bash
PYTHONPATH=validate-pro/src python validate-pro/generate_cases.py --repo-root . --frontend-ids 1 20 121
```

## 验证保留样例

```bash
PYTHONPATH=validate-pro/src python validate-pro/run_validation.py --repo-root .
```

## Docker Compose

```bash
docker compose -f validate-pro/compose.yaml build
docker compose -f validate-pro/compose.yaml run --rm validate-pro
```

通过 Compose 生成保留样例：

```bash
docker compose -f validate-pro/compose.yaml run --rm generate-cases
```

## 本地产物

```text
validate-pro/cases/
validate-pro/reports/
validate-pro/work/
```

这些目录都是本地生成产物。

## 文件树

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
