# Project Structure

本文档描述项目推荐目录结构和模块职责。实现时应保持模块边界清晰，遵循 SOLID 和 DRY。

## 目录树

```text
.
├── PRD.md
├── PROJECT_STRUCTURE.md
├── requirements.txt
├── .gitignore
├── dataset/
│   ├── dataset.md
│   └── merged_problems.json        # 本地自行下载，不提交 Git
├── src/
│   └── leetcode_solutions/
│       ├── __init__.py
│       ├── config.py               # 模型名、路径、重试次数、超时等配置
│       ├── dataset_loader.py       # 读取和校验 merged_problems.json
│       ├── prompt_builder.py       # 构造 system prompt、题目公共 prompt、语言 prompt
│       ├── ollama_client.py        # 封装 Ollama API 调用
│       ├── markdown_writer.py      # 生成和更新题目 Markdown 文件
│       ├── progress.py             # tqdm 进度条封装
│       ├── logger.py               # 屏幕和文件双写日志
│       ├── resume.py               # 断点续跑和已生成语言检测
│       └── generator.py            # 串联生成流程
├── scripts/
│   └── generate_solutions.py       # CLI 入口
├── tests/
│   ├── test_dataset_loader.py      # dataset 读取和排序测试
│   ├── test_prompt_builder.py      # prompt 拼接和字段跳过测试
│   ├── test_markdown_writer.py     # 输出路径、文件名和 Markdown 格式测试
│   ├── test_resume.py              # 断点续跑检测测试
│   ├── test_logger.py              # stdout/stderr/failures 日志分流测试
│   ├── test_ollama_client.py       # ollama 库调用、think 模式和 100k 限制测试
│   ├── test_cli.py                 # CLI 参数解析测试
│   ├── test_generator.py           # 主流程调度测试
│   └── test_e2e_selected.py        # LeetCode 1/2/4 正式流程和跳过行为测试
├── logs/                           # 运行日志，不提交 Git
├── easy/                           # 生成的 Easy 题解
├── medium/                         # 生成的 Medium 题解
└── hard/                           # 生成的 Hard 题解
```

当前仓库可以先只保留文档和数据说明，代码实现时再逐步创建 `src/`、`scripts/`、`tests/`、`logs/`、`easy/`、`medium/`、`hard/`。

## 模块职责

- `config.py`: 集中管理模型名、think 强度映射、输入输出路径、超时、重试次数等配置。
- `dataset_loader.py`: 只负责读取 JSON、解析 `questions`、按难度筛选和排序题目。
- `prompt_builder.py`: 只负责 prompt 拼接，跳过缺失字段，并排除 `images`。
- `ollama_client.py`: 只负责请求 Ollama、处理超时、重试和模型返回。
- `markdown_writer.py`: 只负责生成目标路径、格式化 Markdown、原子写入文件。
- `progress.py`: 只负责封装 `tqdm`，提供难度题目进度和语言子进度。
- `logger.py`: 只负责日志格式、stderr tee、文件日志和屏幕输出。
- `resume.py`: 只负责判断题目或语言是否已经生成，支持断点续跑。
- `generator.py`: 只负责调度各模块，按 Easy -> Medium -> Hard 串行执行。

## Tests

所有单元测试统一放在 `tests/` 目录，并使用 Python 标准库 `unittest`。

测试应覆盖：

- dataset 读取、字段缺失、难度筛选和题号排序。
- prompt 构造，特别是 `images` 跳过、`solutions` 可选、语言 starter code 拼接。
- Markdown 输出路径、题号分桶、文件名格式和语言章节格式。
- Easy/Medium 一题写一次、Hard 一语言写一次的写入策略。
- 断点续跑对完整题目和缺失语言的判断。
- stdout/stderr/failures 三类日志分流。
- retry 3 次失败后记录日志并继续处理下一个题目的行为。
- Ollama client 使用 Python `ollama` 库，不使用 `requests`。
- Ollama client 能用 `hello` smoke test 验证 `low`、`medium`、`high` 三种 think 模式。
- Ollama client 调用参数包含 100k tokens 最大输出限制。
- CLI 支持一次指定多个题号，例如 `--frontend-ids 1 2 4`。
- LeetCode 1 / 2 / 4 的正式生成流程：从 dataset 读取真实题目，分别覆盖 Easy、Medium、Hard，走完整生成链路并产出对应 `.md`。
- LeetCode 1 / 2 / 4 已生成后的跳过行为：第二次运行应识别目标 `.md` 已完整存在，并正常跳过，不重复调用模型。

## SOLID

- 单一职责：每个模块只处理一个明确问题，例如 prompt 构造不负责写文件。
- 开闭原则：新增模型、输出格式或语言过滤规则时，应优先新增配置或小模块，避免改动主流程。
- 里氏替换：模型客户端应抽象为稳定接口，后续替换 Ollama 或模型时不影响生成流程。
- 接口隔离：调用方只依赖自己需要的方法，例如 Markdown 写入模块不暴露日志内部实现。
- 依赖倒置：主流程依赖抽象能力，如 `ModelClient`、`Writer`、`Logger`，不把底层实现散落到各处。

## DRY

- Prompt 公共部分只构造一次，同一道题的不同语言复用题目公共 prompt。
- 难度到 think 强度的映射只在配置中定义一次。
- 输出路径和文件名规则只在 `markdown_writer.py` 中实现一次。
- 日志格式只在 `logger.py` 中定义一次。
- 断点续跑判断只在 `resume.py` 中实现一次。

避免复制粘贴相同的路径拼接、prompt 拼接、重试逻辑和 Markdown 格式化逻辑。
