# 题解验证

验证体系集中放在 `Leetcode-QC/` 下，按从轻到重分为三层：先做静态审计，再跑官方样例 Docker 验证，最后使用增强对数验证补充更多边界样例。

## 第一层：静态审计

`migrate/audit_missing_solutions.py` 和 `migrate/audit_suspicious_solutions.py` 不运行题解代码，只扫描已经生成的 Markdown。它们用来检查缺失语言、可修复顺序异常、异常长代码块、Markdown 残留和重复生成输出。

## 第二层：基础 Docker 验证

`Leetcode-QC/validate/` 是快速 Docker 验证层。它从 `dataset/merged_problems.json` 读取 LeetCode 样例，从 `Leetcode-Easy/`、`Leetcode-Medium/`、`Leetcode-Hard/` 提取各语言代码块，运行支持的可执行语言 section，并按难度写出 CSV 矩阵：

```text
Leetcode-QC/validate/reports/easy.csv
Leetcode-QC/validate/reports/medium.csv
Leetcode-QC/validate/reports/hard.csv
```

每个 CSV 行是一道题。每个语言列使用 `1` 表示样例通过，使用 `0` 表示其它结果。

## Docker

在仓库根目录构建：

```bash
docker compose -f Leetcode-QC/validate/compose.yaml build
```

在仓库根目录运行：

```bash
docker compose -f Leetcode-QC/validate/compose.yaml run --rm validate
```

## 直接命令

```bash
python Leetcode-QC/validate/run_validation.py --repo-root .
python Leetcode-QC/validate/run_validation.py --repo-root . --dataset dataset/merged_problems.json
python Leetcode-QC/validate/run_validation.py --repo-root . --reports-dir Leetcode-QC/validate/reports
```

## 第三层：Validate Pro 增强对数验证

`Leetcode-QC/validate-pro/` 是增强对数验证层。这里的“对数验证”指的是：不只相信某一个生成结果，而是让 `gpt-oss:120b` 继续设计更多边界样例候选，再用本地 Python 参考解算出标准答案，只把通过校验的样例保存为 JSON，最后用更大的 Docker 验证集合检查各语言题解是否和标准答案一致。

Validate Pro 命令入口：

```bash
docker compose -f Leetcode-QC/validate-pro/compose.yaml build
docker compose -f Leetcode-QC/validate-pro/compose.yaml run --rm validate-pro
docker compose -f Leetcode-QC/validate-pro/compose.yaml run --rm generate-cases
```

详细设计：

- [Validate Pro 中文 PRD](validate-pro-prd.md)

`Leetcode-QC/validate-pro/` 是更深一层的验证，不替代 `Leetcode-QC/validate/`。
