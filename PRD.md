# PRD: LeetCode All Languages Best Solutions

## 目标

本项目目标是基于 `dataset/merged_problems.json` 中的 LeetCode 题目数据，使用 Ollama 本地模型 `gpt-oss:120b` 为每一道题生成所有可用编程语言的最优解，并按难度、题号区间和题目 slug 组织为 Markdown 文件。

最终产物不是题目集，而是题解集。每个题目的 Markdown 文件只保存各种语言的最优解代码，不重复放入题目正文。

## 模型与推理强度

使用 Ollama 调用 `gpt-oss:120b`。

根据题目难度设置模型 think 强度：

- Easy: `low`
- Medium: `medium`
- Hard: `high`

生成顺序固定为：

1. Easy
2. Medium
3. Hard

这样可以先完成简单题，快速验证流程和输出格式，再逐步处理更复杂的题目。

## 数据来源

输入数据来自：

- `dataset/merged_problems.json`

顶层字段为 `questions`，每个元素是一道题。生成时需要优先使用题目中对解法正确性有帮助的信息，包括：

- `title`
- `problem_id`
- `frontend_id`
- `difficulty`
- `problem_slug`
- `topics`
- `description`
- `examples`
- `constraints`
- `follow_ups`
- `hints`
- `solutions`
- `code_snippets`

其中 `solutions` 如果存在，可以作为 editorial 思路材料传给模型，以提升最优解正确性；如果不存在则跳过。

部分字段可能缺失，例如 `solutions`、`images`、`follow_ups`。生成逻辑必须把这些字段视为可选字段，不能因为缺失而中断。

`images` 字段只作为数据字段保留，不传入模型 prompt。`gpt-oss:120b` 不是多模态模型，不能直接理解图片 URL 或图片内容。

## Prompt 设计

Prompt 分为三层：

1. 固定 system prompt
2. 可缓存的题目公共信息 prompt
3. 每种语言单独的 user prompt

### System Prompt

System prompt 放入所有稳定要求，避免每种语言重复构造不同规则。

输入 prompt 可以使用 Markdown 或结构化文本组织信息，以帮助模型理解题目；输出必须严格限制为纯代码。

核心要求：

- 你是专业算法工程师和 LeetCode 题解生成器。
- 只生成目标语言的最优解。
- 优先选择时间复杂度和空间复杂度最优、可通过 LeetCode 的解法。
- 必须严格匹配 LeetCode 函数签名和 starter code 风格。
- 不要输出题目描述。
- 不要输出 Markdown 正文解释。
- 不要输出复杂度分析，除非未来明确需要。
- 不要输出测试代码、main 函数或额外 I/O。
- 最终输出只包含纯代码。
- 不要使用 Markdown 代码块包裹，不要输出 ``` 或 ```language。
- 如果题目有官方 editorial 或 solution 信息，可以参考其思路，但必须输出干净、可提交的代码。

System prompt 也负责固定输出质量要求：

- 代码必须完整。
- 代码必须能直接替换 LeetCode 编辑器中的 starter code。
- 不允许使用不存在的库或非 LeetCode 默认环境依赖。
- 不允许省略关键逻辑。
- 不允许输出伪代码。

### 可缓存题目公共 Prompt

题目公共 prompt 由题目有用信息拼接而成，对同一道题的所有语言都相同，因此可以缓存和复用。

缓存策略：

- System prompt 是全局稳定内容，跨题目、跨语言都应复用。
- 题目公共 prompt 包含除 `images` 之外的题目有效字段，同一道题的所有语言复用。
- 语言 user prompt 只包含目标语言和该语言 starter code。
- 即使切换题目，system prompt 仍保持相同，可以最大化模型侧 prompt cache 命中。
- 缺失字段直接跳过，不影响缓存结构和生成流程。

建议包含：

```text
Problem Metadata:
- title
- problem_id
- frontend_id
- difficulty
- problem_slug
- topics

Problem Statement:
- description

Examples:
- examples.example_num
- examples.example_text

Constraints:
- constraints

Follow Ups:
- follow_ups, if present

Hints:
- hints, if present

Editorial / Solution Reference:
- solutions, if present
```

字段缺失时直接跳过，不写空字段占位。

如果示例中包含 `images`，生成 prompt 时跳过该字段，只使用文本形式的 `example_text`。

### 语言 User Prompt

语言 user prompt 只放每种语言不同的内容：

- 目标语言名称
- 该语言对应的 `code_snippets` starter code

示例结构：

```text
Target Language: python3

Use this LeetCode starter code signature and style:

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pass
```

Generate the optimal accepted solution for this language.
Return raw code only. Do not wrap the answer in Markdown code fences.
```

这样可以让 system prompt 和题目公共 prompt 保持一致，只有语言层输入变化，便于缓存、断点续跑和排查错误。

## 输出结构

生成结果按难度分为三个目录：

```text
easy/
medium/
hard/
```

每个难度目录内按 `frontend_id` 每 100 题分桶：

```text
easy/
  1-100/
    0001-two-sum.md
  101-200/
    0101-symmetric-tree.md

medium/
  1-100/
  101-200/

hard/
  1-100/
  101-200/
```

文件名格式：

```text
{frontend_id 四位补零}-{problem_slug}.md
```

示例：

```text
0001-two-sum.md
0011-container-with-most-water.md
```

如果 `frontend_id` 不是纯数字，需要记录为异常题目并跳过或单独处理。

## 单题 Markdown 格式

每个 `.md` 文件只包含各语言题解，不包含题目正文。

推荐格式：

````markdown
# 0001. Two Sum

## Python3

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ...
```

## Cpp

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        ...
    }
};
```
````

标题只保留题号和题名，用于定位文件内容；不放题目描述、examples、constraints、hints 或 editorial。

## 语言范围

语言列表来自每道题的 `code_snippets` 字段。

生成逻辑应遍历该对象中的所有语言 key，例如：

- `python3`
- `python`
- `cpp`
- `java`
- `c`
- `csharp`
- `javascript`
- `typescript`
- `php`
- `swift`
- `kotlin`
- `dart`
- `golang`
- `ruby`
- `scala`
- `rust`
- `racket`
- `erlang`
- `elixir`

不同题目的可用语言可能不完全一致，以该题实际存在的 `code_snippets` 为准。

## 进度条

生成进度用 `tqdm` 实现，按难度顺序串行处理：

1. Easy 题目进度跑完到 100%。
2. Medium 题目进度跑完到 100%。
3. Hard 题目进度跑完到 100%。

每个难度阶段使用一个外层 `tqdm`，统计当前难度下已完成的题目数。处理单题时，使用一个内层 `tqdm`，统计当前题目已完成的语言数。

伪代码结构：

```python
for difficulty in ["Easy", "Medium", "Hard"]:
    problems = get_problems_by_difficulty(difficulty)
    for problem in tqdm(problems, desc=difficulty):
        languages = get_languages(problem)
        for language in tqdm(languages, desc=problem["problem_slug"], leave=False):
            generate_solution(problem, language)
```

先保持实现简单，不需要手写文本进度条，也不需要同时展示 Easy、Medium、Hard 三条进度。

进度统计以题目 Markdown 文件为主：

- 外层 `tqdm` 表示当前难度下的题目 `.md` 完成进度。
- 内层 `tqdm` 只表示当前题目的语言生成进度。
- Easy 和 Medium 在单题所有语言生成完成并写入 `.md` 后，外层进度加 1。
- Hard 每生成完一个语言就更新一次该题 `.md`，但外层进度仍然在该题所有语言完成后加 1。

## 断点续跑

生成过程可能很长，必须支持断点续跑。

建议策略：

- 如果目标 `.md` 已存在且包含所有目标语言标题，则跳过该题。
- 如果文件存在但语言不完整，只补生成缺失语言。
- Easy 和 Medium 题目：先在内存中收集该题所有语言结果，全部成功后一次性写入目标 `.md`，减少 SSD 写入次数。
- Hard 题目：每生成完成一种语言就更新一次目标 `.md`，降低长耗时任务中断后的损失。
- 写文件时使用临时文件再替换，避免中断导致文件损坏。

## 日志要求

日志必须同时满足排查问题和实时观察进度：

- 输出路径分为两条：一条打印到屏幕，另一条写入本次运行的日志目录。
- stdout 信息打印到屏幕 stdout，同时写入 `stdout.log`。
- stderr 信息打印到屏幕 stderr，同时写入 `stderr.log`。
- 日志目录使用 `logs/`，该目录不提交到 Git。
- 每次运行按日期时间创建独立日志目录。
- stdout 写入本次运行目录下的 `stdout.log`。
- stderr 写入本次运行目录下的 `stderr.log`。
- 失败记录写入本次运行目录下的 `failures.jsonl`。
- 每条日志必须包含日期时间。
- stdout、stderr、failure 三类信息必须分开写，不要混在同一个文件。
- 模型调用失败、重试、超时、返回格式异常、字段缺失跳过等都要写日志。

日志目录示例：

```text
logs/
  2026-07-03_03-30-00/
    stdout.log
    stderr.log
    failures.jsonl
```

stdout 日志示例：

```text
2026-07-03 03:15:20 [INFO] Starting Easy generation
2026-07-03 03:16:10 [INFO] Finished 0001-two-sum
```

stderr 日志示例：

```text
2026-07-03 03:15:24 [WARN] ollama warning: ...
2026-07-03 03:16:02 [ERROR] 0001-two-sum python3 retry=2 timeout
```

`failures.jsonl` 只保存结构化失败记录，不保存普通 stdout/stderr 文本。

## 错误处理

需要处理以下情况：

- 题目缺失 `code_snippets`：记录并跳过。
- 单个语言缺失 starter code：跳过该语言。
- 模型返回非代码块：记录失败并重试。
- 模型调用超时：重试，超过 3 次后记录失败。
- JSON 字段缺失：跳过缺失字段，不中断。
- `frontend_id` 无法解析为数字：记录异常。

每个语言最多 retry 3 次。3 次仍失败后，不阻塞主流程，必须：

1. 写入本次运行目录的 `stderr.log`。
2. 写入本次运行目录的 `failures.jsonl`。
3. 继续处理下一个题目或下一个可处理单元。

失败日志路径：

```text
logs/{run_datetime}/failures.jsonl
```

每行记录：

- `frontend_id`
- `problem_slug`
- `difficulty`
- `language`
- `error`
- `retry_count`

## 代码质量要求

实现代码必须保持长期可维护：

- 每个代码文件开头必须有意图注释，说明这个文件负责什么、不负责什么。
- 每个公开函数或核心函数必须有注释，说明输入、输出和副作用。
- 长逻辑、复杂条件、重试策略、断点续跑、文件替换、日志 tee 等关键位置必须有重点注释。
- 注释要解释意图和边界，不写无意义的逐行翻译。
- 模块设计必须遵循 SOLID 原则。
- 重复逻辑必须抽成函数或模块，遵循 DRY 原则。
- Prompt 构造、Ollama 调用、Markdown 写入、进度展示、日志记录、数据读取应拆分为独立模块。
- 单个模块只承担清晰职责，避免把全流程堆在一个大脚本里。

## 测试要求

所有单元测试统一放在 `tests/` 目录，并使用 Python 标准库 `unittest`。

运行 Python 命令时统一使用 `python`，不要在文档和脚本说明里写 `python3`。

测试需要覆盖：

- dataset 读取、字段缺失、难度筛选和题号排序。
- prompt 构造，特别是 `images` 跳过、`solutions` 可选、语言 starter code 拼接。
- Markdown 输出路径、题号分桶、文件名格式和语言章节格式。
- Easy/Medium 一题写一次、Hard 一语言写一次的写入策略。
- 断点续跑对完整题目和缺失语言的判断。
- stdout/stderr/failures 三类日志分流。
- retry 3 次失败后记录日志并继续处理下一个题目的行为。
- Ollama client 使用 Python `ollama` 库，不使用 `requests`。
- Ollama smoke test：用 `hello` 分别测试 `low`、`medium`、`high` 三种 think 模式能被本机 Ollama 识别。
- Ollama 调用参数测试：确认单次语言生成的最大输出限制为 100k tokens。
- CLI 参数测试：支持一次指定多个题号，例如 `--frontend-ids 1 2 4`。
- LeetCode 1 / 2 / 4 必须有正式流程测试，分别覆盖 Easy、Medium、Hard：
  - LeetCode 1 `Two Sum` -> `easy/1-100/0001-two-sum.md`
  - LeetCode 2 `Add Two Numbers` -> `medium/1-100/0002-add-two-numbers.md`
  - LeetCode 4 `Median of Two Sorted Arrays` -> `hard/1-100/0004-median-of-two-sorted-arrays.md`
- LeetCode 1 / 2 / 4 生成完成后必须再跑一次跳过测试：第二次运行应识别对应 `.md` 已完整存在，正常跳过，不重复调用模型。

## Git Commit 要求

提交时 commit message 必须清晰、详细、说明意图。不要只写 `update`、`fix`、`change` 这类模糊信息。

推荐 commit message 结构：

```text
实现 LeetCode 多语言题解生成器基础流程

说明本次提交为什么需要做：
- 使用 dataset/merged_problems.json 作为题目输入
- 按 Easy、Medium、Hard 顺序生成，降低全量任务验证风险
- 拆分 prompt 构造、模型调用、文件写入和日志模块，便于后续维护

说明本次提交具体改了什么：
- 新增 Ollama gpt-oss:120b 调用封装
- 新增按难度和题号分桶的 Markdown 输出
- 新增 tqdm 题目进度和语言子进度
- 新增 logs/failures.jsonl 失败记录

说明影响范围：
- 生成产物目录为 easy/、medium/、hard/
- dataset/merged_problems.json 仍然由用户自行下载，不提交到仓库
```

Commit message 要让后续维护者能直接看懂本次提交的目的、设计取舍和影响范围。

## Ollama 调用要求

模型调用需要支持：

- 模型名：`gpt-oss:120b`
- 使用 Python `ollama` 库调用模型，不直接使用 `requests` 调 HTTP。
- think 强度：根据难度传入 `low`、`medium`、`high`
- think 强度必须有 smoke test，确认本机 Ollama 能识别 `low`、`medium`、`high`
- system prompt
- 题目公共 prompt
- 语言 user prompt
- 单个问题或单次语言生成的最大输出限制为 100k tokens。
- 超时控制
- 重试控制，单个语言最多 retry 3 次

如果 Ollama API 对 think 参数的实际字段名不同，应在实现阶段以本机 Ollama 版本支持的 API 为准。

## 验收标准

第一阶段验收：

- 能读取 `dataset/merged_problems.json`。
- 能按 Easy -> Medium -> Hard 排序处理。
- 能按题目难度选择 think 强度。
- 能为单题所有 `code_snippets` 语言生成一个 `.md` 文件。
- 能按 `easy/1-100/0001-two-sum.md` 结构落盘。
- 能展示难度进度条和语言子进度条。
- Easy 和 Medium 每题只在所有语言完成后写一次 `.md`。
- Hard 每生成完成一种语言就更新一次 `.md`。
- stdout、stderr 分别同时输出到屏幕和本次运行日志目录。
- failures 结构化写入本次运行目录的 `failures.jsonl`。
- 核心模块有 `tests/` 下的 `unittest` 覆盖。
- Ollama client 测试覆盖 `ollama` 库调用、三种 think 模式和 100k tokens 输出限制。
- LeetCode 1 / 2 / 4 能通过正式流程生成，并能在第二次运行时正常跳过。
- 能跳过缺失字段。
- 能断点续跑。

第二阶段验收：

- 全量 Easy 题生成完成。
- 随机抽查题解可以直接粘贴到 LeetCode 对应语言提交。
- 失败日志可复跑。

第三阶段验收：

- Medium 全量完成。
- Hard 全量完成。
- 所有生成文件结构稳定，可被后续脚本索引、搜索或发布。
