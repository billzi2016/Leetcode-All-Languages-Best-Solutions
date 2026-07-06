# 快速验证 PRD

`Leetcode-QC/validate/` 是生成题解 Markdown 的快速 Docker 验证层。

它要快速回答一个实际问题：已经生成的各语言代码块，能不能跑通 `dataset/merged_problems.json` 里已有的官方样例？

## 目标

- 从 `dataset/merged_problems.json` 读取题目样例。
- 在 `Leetcode-Easy/`、`Leetcode-Medium/`、`Leetcode-Hard/` 下定位已经生成的题解 Markdown。
- 从 Markdown 中提取支持语言的代码块。
- 在可复现的 Docker 环境里编译或运行支持的语言。
- 按难度写出紧凑的 CSV 矩阵。

## 非目标

- 不生成新的测试样例。
- 不替代 `Leetcode-QC/validate-pro/`。
- 不声称证明官方样例之外的完整正确性。
- 不修改已经生成的题解 Markdown。

## 输入

```text
dataset/merged_problems.json
Leetcode-Easy/**/*.md
Leetcode-Medium/**/*.md
Leetcode-Hard/**/*.md
```

dataset 提供题目信息、examples、语言声明、starter signatures 和难度；Markdown 文件提供各语言生成代码块。

## 输出

```text
Leetcode-QC/validate/reports/easy.csv
Leetcode-QC/validate/reports/medium.csv
Leetcode-QC/validate/reports/hard.csv
```

每一行是一道题。每个语言列只使用：

```text
1 = 通过官方 dataset examples
0 = 未通过官方 dataset examples
```

`reports/` 和 `work/` 是本地生成产物，并由 Git 忽略。

## 执行模型

Docker 镜像安装验证器需要的语言运行环境。compose 命令把仓库根目录挂载到 `/workspace`，因此 runner 可以用和仓库脚本一致的路径读取 dataset、生成的 Markdown 文件和本地输出目录。

```bash
docker compose -f Leetcode-QC/validate/compose.yaml build
docker compose -f Leetcode-QC/validate/compose.yaml run --rm validate
```

也可以直接运行 Python runner：

```bash
python Leetcode-QC/validate/run_validation.py --repo-root /workspace
python Leetcode-QC/validate/run_validation.py --repo-root /workspace --dataset dataset/merged_problems.json
python Leetcode-QC/validate/run_validation.py --repo-root /workspace --reports-dir Leetcode-QC/validate/reports
```

## 和 Validate Pro 的关系

`Leetcode-QC/validate/` 是基础验证层。它使用 dataset 里已经存在的官方 examples，适合快速反馈。

`Leetcode-QC/validate-pro/` 是更深的对数验证层。它可以让 `gpt-oss:120b` 额外提出边界样例候选，再用 Python 参考解校验候选，只保留通过校验的 JSON 样例，然后运行更大的验证集合。

两层互补：快速验证检查生成题解能否处理已知样例，Validate Pro 用经过校验的生成样例扩展覆盖面。

## 验收标准

- Docker 构建使用 `Leetcode-QC/validate/Dockerfile`。
- Compose 入口位于 `Leetcode-QC/validate/compose.yaml`，并把仓库根目录挂载为 `/workspace`。
- CSV 报告写入 `Leetcode-QC/validate/reports/`。
- runner 保留 dataset 声明的语言列。
- 该模块不会修改已经生成的题解 Markdown 文件。
