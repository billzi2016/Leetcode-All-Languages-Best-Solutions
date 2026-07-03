# LeetCode All Languages Best Solutions

本项目用于基于本地 LeetCode 题目数据集，使用 Ollama `gpt-oss:120b` 为题目生成多语言最优解，并按难度、题号区间和题目 slug 输出为 Markdown 文件。

## 当前状态

当前已完成基础工程结构和核心流程：

- 数据集读取和按难度/题号筛选
- prompt 构造，并排除 `images` 字段
- Python `ollama` 库调用封装
- Easy / Medium / Hard 对应 think 模式：`low` / `medium` / `high`
- 单次语言生成 100k tokens 输出限制
- Markdown 输出路径和文件格式
- 断点续跑和已生成题目跳过
- stdout / stderr / failures 日志分流
- `unittest` 测试覆盖

## 数据集

本仓库不提交 `dataset/merged_problems.json`。如需运行生成流程，请先自行下载：

```bash
curl -L -o dataset/merged_problems.json https://raw.githubusercontent.com/neenza/leetcode-problems/master/merged_problems.json
```

数据字段说明见：

- `dataset/dataset.md`

## 安装依赖

```bash
python -m pip install -r requirements.txt
```

依赖包括：

- `ollama`
- `tqdm`

## 运行测试

```bash
PYTHONPATH=src python -m unittest discover -s tests
```

测试包含 LeetCode 1 / 2 / 4 的正式流程测试，分别覆盖 Easy、Medium、Hard，并验证第二次运行能正常跳过已生成文件。

## 生成单题

生成 LeetCode 1：

```bash
PYTHONPATH=src python scripts/generate_solutions.py --only-frontend-id 1
```

一次生成 LeetCode 1 / 2 / 4：

```bash
PYTHONPATH=src python scripts/generate_solutions.py --frontend-ids 1 2 4
```

生成某个难度：

```bash
PYTHONPATH=src python scripts/generate_solutions.py --difficulty Easy
```

生成 Medium：

```bash
PYTHONPATH=src python scripts/generate_solutions.py --difficulty Medium
```

生成 Hard：

```bash
PYTHONPATH=src python scripts/generate_solutions.py --difficulty Hard
```

生成全部难度：

```bash
PYTHONPATH=src python scripts/generate_solutions.py
```

输出目录示例：

```text
easy/1-100/0001-two-sum.md
medium/1-100/0002-add-two-numbers.md
hard/1-100/0004-median-of-two-sorted-arrays.md
```

## 文档

- `PRD.md`: 产品需求和实现约束
- `PROJECT_STRUCTURE.md`: 项目结构、模块职责、SOLID/DRY 和测试规划
- `dataset/dataset.md`: 数据集来源和字段说明
