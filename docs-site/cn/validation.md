# 题解验证

`validate/` 目录提供容器化题解验证环境，用于验证已经生成的 LeetCode 题解 Markdown 文件。

它从 `dataset/merged_problems.json` 读取 LeetCode 样例，从 `Leetcode-Easy/`、`Leetcode-Medium/`、`Leetcode-Hard/` 提取各语言代码块，运行支持的可执行语言 section，并按难度写出 CSV 矩阵：

```text
validate/reports/easy.csv
validate/reports/medium.csv
validate/reports/hard.csv
```

每个 CSV 行是一道题。每个语言列使用 `1` 表示样例通过，使用 `0` 表示其它结果。

## Docker

在仓库根目录构建：

```bash
docker build -f validate/Dockerfile -t leetcode-solutions-validate .
```

在仓库根目录运行：

```bash
docker run --rm -v "$PWD":/workspace leetcode-solutions-validate
```

## 直接命令

```bash
python validate/run_validation.py --repo-root .
python validate/run_validation.py --repo-root . --dataset dataset/merged_problems.json
python validate/run_validation.py --repo-root . --reports-dir validate/reports
```

## 验证层级

仓库使用三层互补的质量控制工具：

| 层级 | 作用 | 输出 |
| --- | --- | --- |
| `migrate/` 审计 | 查找缺失语言、可修复顺序异常、异常长代码块、Markdown 残留和重复生成输出。 | 终端报告或被忽略的本地 Markdown 报告 |
| `validate/` | 快速 Docker 验证，使用 `dataset/merged_problems.json` 中已有 examples。 | `validate/reports/easy.csv`、`medium.csv`、`hard.csv` |
| `validate-pro/` | 增强对数验证设计。它让 `gpt-oss:120b` 额外生成边界样例候选，用 Python 参考解校验后保存 JSON，再运行更大的 Docker 验证集合。 | `validate-pro/cases/*.json` 和 `validate-pro/reports/*.csv` |

`validate-pro/` 是更深一层的验证，不替代 `validate/`。
