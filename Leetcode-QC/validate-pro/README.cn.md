# Validate Pro

`Leetcode-QC/validate-pro/` 是生成题解的可控 AI 对数验证层。

这里的“对数验证”指的是：不只相信某一个生成结果，而是让 `gpt-oss:120b` 一次提出一个新的边界样例候选，再用本地 Python 参考 adapter 算出标准答案并校验样例，只把通过校验的样例保存为 JSON，最后用更大的样例集合检查已经生成的 Markdown 题解是否和标准答案一致。

文档：

- `specs/PRD.md`
- `specs/PRD.cn.md`

## 生成样例

```bash
PYTHONPATH=Leetcode-QC/validate-pro/src python Leetcode-QC/validate-pro/generate_cases.py --repo-root . --frontend-ids 1 20 121
```

## 验证保留样例

```bash
PYTHONPATH=Leetcode-QC/validate-pro/src python Leetcode-QC/validate-pro/run_validation.py --repo-root .
```

## Docker Compose

```bash
docker compose -f Leetcode-QC/validate-pro/compose.yaml build
docker compose -f Leetcode-QC/validate-pro/compose.yaml run --rm validate-pro
```

通过 Compose 生成保留样例：

```bash
docker compose -f Leetcode-QC/validate-pro/compose.yaml run --rm generate-cases
```

## 本地产物

```text
Leetcode-QC/validate-pro/cases/
Leetcode-QC/validate-pro/reports/
Leetcode-QC/validate-pro/work/
```

这些目录都是本地生成产物。

## 文件树

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
