# 容器化题解验证

`Leetcode-QC/validate/` 是 LeetCode 质量检查工具中的快速验证层。它从 `dataset/merged_problems.json` 读取 LeetCode 样例，解析 `Leetcode-Easy/`、`Leetcode-Medium/`、`Leetcode-Hard/` 中已经生成的题解 Markdown，提取各语言代码块，按语言编译或运行，并按难度写出 CSV 矩阵。

CSV 输出：

```text
Leetcode-QC/validate/reports/easy.csv
Leetcode-QC/validate/reports/medium.csv
Leetcode-QC/validate/reports/hard.csv
```

每一行是一道题。每个语言列只使用：

```text
1 = 样例通过
0 = 样例未通过
```

## 构建

在仓库根目录执行：

```bash
docker compose -f Leetcode-QC/validate/compose.yaml build
```

## 运行

在仓库根目录执行：

```bash
docker compose -f Leetcode-QC/validate/compose.yaml run --rm validate
```

默认输出到 `Leetcode-QC/validate/reports/`。

## 参数

```bash
python Leetcode-QC/validate/run_validation.py --repo-root /workspace
python Leetcode-QC/validate/run_validation.py --repo-root /workspace --dataset dataset/merged_problems.json
python Leetcode-QC/validate/run_validation.py --repo-root /workspace --reports-dir Leetcode-QC/validate/reports
```

CSV 会保留 dataset 声明的语言列。内置可执行 runner 覆盖 Python、Python3、Cpp、Java 和 JavaScript，并支持从 dataset 样例解析出的题型。

## 和 `Leetcode-QC/validate-pro/` 的关系

`Leetcode-QC/validate/` 是快速验证层。它读取 `dataset/merged_problems.json` 中已经存在的 examples，运行支持的题解语言 section，并写出紧凑的 CSV 矩阵。

`Leetcode-QC/validate-pro/` 是增强对数验证层。它会让 `gpt-oss:120b` 额外生成边界样例候选，再用 Python 参考解校验这些候选样例，只有确认可运行且答案正确的样例才会以 JSON 保存下来，然后再运行更大的验证集合。这个流程更重，因为 ReAct 风格样例生成会把题面、constraints、examples、topics 和 starter signatures 都放进 prompt。

日常快速检查使用 `Leetcode-QC/validate/`；需要更深的生成样例质量控制时使用 `Leetcode-QC/validate-pro/`。

## 文件树

```text
Leetcode-QC/
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

`reports/` 和 `work/` 都是本地生成产物。
