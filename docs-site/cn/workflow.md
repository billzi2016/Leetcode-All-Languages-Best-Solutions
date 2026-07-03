# 端到端工作流

本文说明生成器、文档站点和部署流程如何配合。

这套工作流的目标是让全量生成可以长时间运行、可以中断后继续、可以定位失败原因，并且让文档站点始终解释当前仓库的真实行为。

## 生成流程

```mermaid
flowchart TD
    A[本地下载 merged_problems.json] --> B[读取 questions]
    B --> C[按难度或题号筛选]
    C --> D[按 Easy / Medium / Hard 排序]
    D --> E[构造题目公共 prompt]
    E --> F[遍历 code_snippets 语言]
    F --> G[构造语言 prompt]
    G --> H[调用 Ollama]
    H --> I[写入 Markdown 题解文件]
    I --> J[下次运行跳过已完成文件]
```

## 运行意图

- `merged_problems.json` 不提交到仓库，生成时由本地下载，避免把大数据文件放进 Git。
- 题目公共 prompt 使用题目有用字段，但跳过 `images`，因为当前模型不是多模态模型。
- 语言 prompt 只包含目标语言和 starter code，保证同一道题切换语言时只改变最小输入。
- Easy 使用 `low` think，Medium 使用 `medium` think，Hard 使用 `high` think，让推理强度和题目复杂度匹配。
- 单个语言失败后最多重试三次，仍失败则记录到 failures 日志并继续下一个语言或题目。
- 已存在的目标 Markdown 文件会被视为已完成，二次运行可以跳过，适合 tmux 长任务断点续跑。

## Prompt 复用路径

```mermaid
flowchart TD
    A[SYSTEM_PROMPT 全局固定] --> B[题目 0001 problem_prompt]
    B --> C[python3 language_prompt]
    B --> D[cpp language_prompt]
    B --> E[java language_prompt]
    C --> F[0001 Python3 代码]
    D --> G[0001 C++ 代码]
    E --> H[0001 Java 代码]

    A --> I[题目 0002 problem_prompt]
    I --> J[python3 / cpp / java ...]
```

生成器把 prompt 拆成三层，是为了让相同内容尽量出现在请求前缀里。`SYSTEM_PROMPT` 负责所有稳定规则，`problem_prompt` 负责同一道题共享的信息，`language_prompt` 负责最小的语言差异。这个结构同时服务三个目标：模型更容易复用前缀、日志更容易定位问题、单语言失败时更容易重跑。

不要把题目、语言、输出格式要求每次拼成完全不同的一大段文本。那样会降低复用，也会让失败排查变困难。

## tmux 后台生成

tmux 脚本是面向长时间生成任务的入口。`scripts/tmux_all.sh` 生成全部难度；`scripts/tmux_easy.sh`、`scripts/tmux_medium.sh`、`scripts/tmux_hard.sh` 分别生成 Easy、Medium、Hard。每个脚本都会先安装根目录 `requirements.txt`，再启动对应的 tmux session。

```mermaid
flowchart TD
    A[执行 tmux 脚本] --> B[进入仓库根目录]
    B --> C[python -m pip install -r requirements.txt]
    C --> D{脚本类型}
    D -->|tmux_all.sh| E[运行全部难度: leetcode-all]
    D -->|tmux_easy.sh| F[运行 Easy: leetcode-easy]
    D -->|tmux_medium.sh| G[运行 Medium: leetcode-medium]
    D -->|tmux_hard.sh| H[运行 Hard: leetcode-hard]
    E --> I[屏幕查看 tmux attach]
    F --> I
    G --> I
    H --> I
    I --> J[日志落盘到 logs/日期时间]
```

依赖安装放在 tmux 启动之前，是为了让缺依赖这类环境问题直接出现在当前终端；真正的生成任务再进入后台运行。

常用命令：

```bash
scripts/tmux_all.sh
scripts/tmux_easy.sh
scripts/tmux_medium.sh
scripts/tmux_hard.sh
tmux ls
tmux attach -t leetcode-all
tmux attach -t leetcode-easy
tmux attach -t leetcode-medium
tmux attach -t leetcode-hard
tmux kill-session -t leetcode-all
tmux kill-session -t leetcode-easy
tmux kill-session -t leetcode-medium
tmux kill-session -t leetcode-hard
tmux kill-server
```

`tmux kill-session` 只取消本项目的当前生成任务；`tmux kill-server` 会取消所有 tmux session，应只在确认没有其他 tmux 工作时使用。

## 断点续跑和重跑策略

```mermaid
flowchart TD
    A[准备生成某题 Markdown] --> B{目标文件已存在?}
    B -->|是| C[跳过该题]
    B -->|否| D[遍历该题所有语言]
    D --> E{语言生成成功?}
    E -->|是| F[暂存到内存结果]
    E -->|否| G[重试最多 3 次]
    G --> H{仍失败?}
    H -->|是| I[写 failures.jsonl 并继续]
    H -->|否| F
    F --> J[按难度写入 Markdown]
```

Easy 和 Medium 每个题目写一次 Markdown，Hard 按语言写入，目的是降低长时间运行时的重复 I/O，同时让复杂题在语言级别有更细的保存粒度。

## 日志和失败处理

```mermaid
flowchart LR
    A[生成任务] --> B[stdout.log: 正常进度]
    A --> C[stderr.log: 警告和错误文本]
    A --> D[failures.jsonl: 结构化失败项]
    D --> E[后续按题号和语言重跑]
```

stdout、stderr 和 failures 分开保存，是为了避免长时间运行后日志混在一起。屏幕输出用于观察进度；文件日志用于复盘；`failures.jsonl` 用于后续精确重跑。

日志目录按日期时间创建，例如：

```text
logs/
  2026-07-03_031520/
    stdout.log
    stderr.log
    failures.jsonl
```

`stdout.log` 保存正常进度和完成信息，`stderr.log` 保存 warning、异常和模型调用错误文本，`failures.jsonl` 保存机器可读的失败记录。

## 文档流程

```mermaid
flowchart TD
    A[英文 Markdown 文件] --> C[MkDocs 构建]
    B[中文 Markdown 文件] --> C
    C --> D[静态站点产物]
    D --> E[GitHub Pages 部署]
```

## GitHub Actions 流程

```mermaid
sequenceDiagram
    participant Dev as 开发者
    participant GH as GitHub
    participant Action as GitHub Actions
    participant Pages as GitHub Pages

    Dev->>GH: Push docs-site 变更
    GH->>Action: 触发文档工作流
    Action->>Action: 安装依赖
    Action->>Action: 构建 MkDocs 站点
    Action->>Pages: 部署静态产物
    Pages-->>Dev: 发布文档站点
```

文档站点根路径提供语言入口，`cn/` 和 `en/` 分别保存中文和英文页面。GitHub Actions 只负责构建和部署文档，不参与题解生成；题解生成依赖本地 Ollama 和本地数据文件。
