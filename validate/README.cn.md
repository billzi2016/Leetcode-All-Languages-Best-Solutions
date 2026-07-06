# 容器化题解验证

`validate/` 提供一个可复现的题解验证环境。它从 `dataset/merged_problems.json` 读取 LeetCode 样例，解析 `Leetcode-Easy/`、`Leetcode-Medium/`、`Leetcode-Hard/` 中已经生成的题解 Markdown，提取各语言代码块，按语言编译或运行，并按难度写出 CSV 矩阵。

CSV 输出：

```text
validate/reports/easy.csv
validate/reports/medium.csv
validate/reports/hard.csv
```

每一行是一道题。每个语言列只使用：

```text
1 = 样例通过
0 = 样例未通过
```

## 构建

在仓库根目录执行：

```bash
docker build -f validate/Dockerfile -t leetcode-solutions-validate .
```

## 运行

在仓库根目录执行：

```bash
docker run --rm -v "$PWD":/workspace leetcode-solutions-validate
```

默认输出到 `validate/reports/`。

## 参数

```bash
python validate/run_validation.py --repo-root /workspace
python validate/run_validation.py --repo-root /workspace --dataset dataset/merged_problems.json
python validate/run_validation.py --repo-root /workspace --reports-dir validate/reports
```

CSV 会保留 dataset 声明的语言列。内置可执行 runner 覆盖 Python、Python3、Cpp、Java 和 JavaScript，并支持从 dataset 样例解析出的题型。

## 和 `validate-pro/` 的关系

`validate/` 是快速验证层。它读取 `dataset/merged_problems.json` 中已经存在的 examples，运行支持的题解语言 section，并写出紧凑的 CSV 矩阵。

`validate-pro/` 是增强对数验证层。它会让 `gpt-oss:120b` 额外生成边界样例候选，再用 Python 参考解校验这些候选样例，只有确认可运行且答案正确的样例才会以 JSON 保存下来，然后再运行更大的验证集合。这个流程更重：运行时间更长，会产生更多本地文件，并且 ReAct 风格样例生成会把题面、constraints、examples、topics 和 starter signatures 都放进 prompt，因此 token 消耗会很大。

日常快速检查使用 `validate/`；需要更深的生成样例质量控制时使用 `validate-pro/`。

## 文件树

```text
validate/
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
