# LeetCode All Languages Best Solutions

本项目用于生成和整理 LeetCode 所有支持语言的准确最优解，并按难度、题号区间和题目 slug 输出为 Markdown 文件。

文档站点：

- https://billzi2016.github.io/Leetcode-All-Languages-Best-Solutions/

## 支持语言

本项目覆盖 LeetCode 数据集中提供 starter code 的全部语言。算法语言示例来自 LeetCode 1 `Two Sum`；数据库和 Pandas 示例来自 LeetCode 175 `Combine Two Tables`；Bash 示例来自 LeetCode 192 `Word Frequency`。

| 语言 | 简介 | Starter Code 示例 |
| --- | --- | --- |
| C | 面向系统编程、嵌入式、数据库内核和高性能基础库，能展示指针、数组长度、返回数组分配和底层边界控制。 | `int* twoSum(int* nums, int numsSize, int target, int* returnSize)` |
| C++ | 面向性能敏感工程、游戏引擎、交易系统、图形计算和竞赛算法，常用 `class Solution`、STL 容器和复杂数据结构。 | `class Solution { public: vector<int> twoSum(vector<int>& nums, int target) }` |
| Java | 面向企业后端、服务端系统和 Android 生态，提交入口稳定，集合库成熟，适合标准工程风格算法实现。 | `class Solution { public int[] twoSum(int[] nums, int target) }` |
| Python | 面向脚本、自动化、数据处理和快速原型开发，表达简洁，但旧版入口需要注意迭代器、整数除法和性能边界。 | `class Solution(object): def twoSum(self, nums, target)` |
| Python3 | 当前主流 Python 版本，常用于后端脚本、机器学习、数据分析、自动化和算法原型，通常带类型标注。 | `class Solution: def twoSum(self, nums: List[int], target: int) -> List[int]` |
| C# | 面向 .NET 平台、企业应用、桌面工具、游戏开发、后端服务和云系统，使用强类型、泛型和 .NET 集合。 | `public class Solution { public int[] TwoSum(int[] nums, int target) }` |
| JavaScript | Web 前端、Node.js 后端、自动化脚本和全栈开发核心语言，数组和对象灵活，但要注意动态类型和数字精度。 | `var twoSum = function(nums, target)` |
| TypeScript | JavaScript 的类型增强版本，常用于大型前端、Node.js 服务和可维护全栈项目，能明确数组、对象、返回值和辅助结构类型。 | `function twoSum(nums: number[], target: number): number[]` |
| PHP | 常见于 Web 后端、CMS、电商系统和传统服务端页面开发，使用类方法提交，数组可同时承担列表和映射角色。 | `class Solution { function twoSum($nums, $target) }` |
| Swift | Apple 平台开发语言，主要用于 iOS、macOS、watchOS 和 tvOS，使用强类型数组和类方法入口。 | `class Solution { func twoSum(_ nums: [Int], _ target: Int) -> [Int] }` |
| Kotlin | 面向 JVM、Android 和服务端开发的现代强类型语言，入口简洁，具备空安全、数据类和友好的集合 API。 | `class Solution { fun twoSum(nums: IntArray, target: Int): IntArray }` |
| Dart | Flutter 主要开发语言，常用于跨平台移动端、桌面端和 Web 应用，使用类方法入口和清晰的 list/map API。 | `class Solution { List<int> twoSum(List<int> nums, int target) }` |
| Go | 面向云原生、后端服务、网络服务、命令行工具和并发系统，使用切片、map、结构体和可读性强的命令式代码。 | `func twoSum(nums []int, target int) []int` |
| Ruby | 面向脚本、Web 应用和快速业务迭代，数组、哈希、枚举和字符串处理表达力强。 | `def two_sum(nums, target)` |
| Scala | JVM 上的函数式和面向对象混合语言，常见于 Spark、Flink、Akka 和分布式大数据系统。 | `object Solution { def twoSum(nums: Array[Int], target: Int): Array[Int] }` |
| Rust | 面向系统编程、性能敏感服务、区块链、编译器、浏览器组件和安全基础设施，强调所有权、借用和内存安全。 | `impl Solution { pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> }` |
| Racket | Lisp/Scheme 家族语言，常用于函数式编程、教学、语言实验和 DSL 构建，入口保留 contract。 | `(define/contract (two-sum nums target) ...)` |
| Erlang | 面向高并发、高可用和分布式系统的函数式语言，使用 spec、模式匹配、递归、不可变数据和列表处理。 | `-spec two_sum(Nums :: [integer()], Target :: integer()) -> [integer()].` |
| Elixir | 构建在 Erlang VM 上的现代函数式语言，常用于 Phoenix Web 服务、实时系统、消息处理和高并发应用。 | `defmodule Solution do ... def two_sum(nums, target) do ... end` |
| MySQL | 常见关系型数据库方言，广泛用于 Web 应用和业务系统，题目主要考察 join、group by、聚合、过滤、窗口函数和 MySQL 语法。 | LeetCode 175: `# Write your MySQL query statement below` |
| MS SQL Server | Microsoft SQL Server 的 T-SQL 方言，常见于企业报表、数据分析和后端数据系统，需要保留 SQL Server starter comment 和方言语法。 | LeetCode 175: `/* Write your T-SQL query statement below */` |
| Oracle SQL | Oracle 数据库的 SQL / PL-SQL 环境，常见于金融、电信和大型企业数据平台，需要处理 PL-SQL 风格入口和 Oracle 方言差异。 | LeetCode 175: `/* Write your PL/SQL query statement below */` |
| PostgreSQL | 功能完整的开源关系型数据库，常用于后端系统、分析平台、地理数据和复杂查询场景，常见 CTE、窗口函数、日期处理和聚合。 | LeetCode 175: `-- Write your PostgreSQL query statement below` |
| Pandas | Python 数据分析生态中的表格数据处理库，用于 DataFrame 清洗、join、groupby、筛选、重塑和统计分析，入口是带类型标注的 DataFrame 函数。 | LeetCode 175: `def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame` |
| Bash | Unix shell 脚本语言，常用于命令行自动化、文本处理、管道组合和运维脚本，题目通常读取文件或标准输入并组合 `awk`、`sort`、`uniq`、`sed` 等工具。 | LeetCode 192: `# Read from the file words.txt and output the word frequency list to stdout.` |

## 输出目录示例

```text
Leetcode-Easy/
  0001-0100/
    0001-two-sum.md
    0009-palindrome-number.md
    0013-roman-to-integer.md
    0014-longest-common-prefix.md
    0020-valid-parentheses.md
    ...
  0101-0200/
    0101-symmetric-tree.md
    0104-maximum-depth-of-binary-tree.md
    0108-convert-sorted-array-to-binary-search-tree.md
    0110-balanced-binary-tree.md
    0111-minimum-depth-of-binary-tree.md
    ...
  0201-0300/
    0202-happy-number.md
    0203-remove-linked-list-elements.md
    0205-isomorphic-strings.md
    0206-reverse-linked-list.md
    0217-contains-duplicate.md
    ...
  ...

Leetcode-Medium/
  0001-0100/
    0002-add-two-numbers.md
    0003-longest-substring-without-repeating-characters.md
    0005-longest-palindromic-substring.md
    0006-zigzag-conversion.md
    0007-reverse-integer.md
    ...
  0101-0200/
    0102-binary-tree-level-order-traversal.md
    0103-binary-tree-zigzag-level-order-traversal.md
    0105-construct-binary-tree-from-preorder-and-inorder-traversal.md
    0106-construct-binary-tree-from-inorder-and-postorder-traversal.md
    0109-convert-sorted-list-to-binary-search-tree.md
    ...
  0201-0300/
    0200-number-of-islands.md
    0207-course-schedule.md
    0208-implement-trie-prefix-tree.md
    0209-minimum-size-subarray-sum.md
    0210-course-schedule-ii.md
    ...
  ...

Leetcode-Hard/
  0001-0100/
    0004-median-of-two-sorted-arrays.md
    0010-regular-expression-matching.md
    0023-merge-k-sorted-lists.md
    0025-reverse-nodes-in-k-group.md
    0030-substring-with-concatenation-of-all-words.md
    ...
  0101-0200/
    0123-best-time-to-buy-and-sell-stock-iii.md
    0124-binary-tree-maximum-path-sum.md
    0126-word-ladder-ii.md
    0128-longest-consecutive-sequence.md
    0132-palindrome-partitioning-ii.md
    ...
  0201-0300/
    0212-word-search-ii.md
    0214-shortest-palindrome.md
    0218-the-skyline-problem.md
    0224-basic-calculator.md
    0233-number-of-digit-one.md
    ...
  ...
```

## 当前状态

当前已完成基础工程结构和核心流程：

- 数据集读取和按难度/题号筛选
- prompt 构造，并排除 `images` 字段
- Python `ollama` 库调用封装
- Easy / Medium / Hard 对应 think 模式：`low` / `medium` / `high`
- 单次语言生成 100_000 tokens 输出限制
- 温度固定为 `0.1`
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
- `dataset/dataset.cn.md`

## 安装依赖

```bash
python -m pip install -r requirements.txt
```

依赖包括：

- `ollama`
- `tqdm`

## 运行测试

```bash
PYTHONPATH=src python -m unittest discover -s tests/unit
```

测试包含 LeetCode 1 / 2 / 4 的正式流程测试，分别覆盖 Easy、Medium、Hard，并验证第二次运行能正常跳过已生成文件。

## 验证生成题解

验证体系集中放在 `Leetcode-QC/` 下，按从轻到重分为三层：先做静态审计，再跑官方样例 Docker 验证，最后使用增强对数验证补充更多边界样例。

### 第一层：静态审计

`migrate/audit_missing_solutions.py` 和 `migrate/audit_suspicious_solutions.py` 不运行题解代码，只扫描已经生成的 Markdown。它们用来检查缺失语言、可修复顺序异常、异常长代码块、Markdown 残留和重复输出。

### 第二层：基础 Docker 验证

`Leetcode-QC/validate/` 是快速 Docker 验证层。它从 `dataset/merged_problems.json` 读取官方样例，解析已经生成的 Markdown 题解代码块，按语言编译或运行，并按难度写出 CSV 矩阵：

```text
Leetcode-QC/validate/reports/easy.csv
Leetcode-QC/validate/reports/medium.csv
Leetcode-QC/validate/reports/hard.csv
```

构建和运行：

```bash
docker compose -f Leetcode-QC/validate/compose.yaml build
docker compose -f Leetcode-QC/validate/compose.yaml run --rm validate
```

### 第三层：Validate Pro 增强对数验证

`Leetcode-QC/validate-pro/` 是增强对数验证层。这里的“对数验证”指的是：不只相信某一个生成结果，而是让 `gpt-oss:120b` 继续设计更多边界样例候选，再用本地 Python 参考解算出标准答案，只把通过校验的样例保存为 JSON，最后用更大的 Docker 验证集合检查各语言题解是否和标准答案一致。

Validate Pro 命令入口：

```bash
docker compose -f Leetcode-QC/validate-pro/compose.yaml build
docker compose -f Leetcode-QC/validate-pro/compose.yaml run --rm validate-pro
docker compose -f Leetcode-QC/validate-pro/compose.yaml run --rm generate-cases
```

Validate Pro 文档：

- `Leetcode-QC/validate-pro/specs/PRD.md`
- `Leetcode-QC/validate-pro/specs/PRD.cn.md`

`Leetcode-QC/validate-pro/` 是更深一层的验证，不替代 `Leetcode-QC/validate/`。

## 生成单题

生成 LeetCode 1：

```bash
PYTHONPATH=src python scripts/generate_solutions.py --only-frontend-id 1
```

一次生成 LeetCode 1 / 2 / 4：

```bash
PYTHONPATH=src python scripts/generate_solutions.py --frontend-ids 1 2 4
```

生成 Easy：

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

只扫描已有 Markdown，不调用模型：

```bash
PYTHONPATH=src python scripts/audit_missing_solutions.py
PYTHONPATH=src python scripts/audit_missing_solutions.py --difficulty Hard
PYTHONPATH=src python scripts/audit_missing_solutions.py --frontend-ids 4 10
```

查缺补漏脚本只打印只读报告。它不会调用 Ollama，不会写文件，也不会自己修复 Markdown。需要真正补齐时，再运行 `scripts/generate_solutions.py`，由生成器按最小补跑策略处理。

使用 tmux 后台生成全部题解：

```bash
scripts/tmux_all.sh
```

使用 tmux 后台按难度生成：

```bash
scripts/tmux_easy.sh
scripts/tmux_medium.sh
scripts/tmux_hard.sh
```

这些 tmux 脚本都会先执行 `python -m pip install -r requirements.txt`，再启动对应的 tmux session。这样依赖缺失会先在当前终端暴露，而不是让后台生成任务静默失败。

默认 session 名：

- `scripts/tmux_all.sh`: `leetcode-all`
- `scripts/tmux_easy.sh`: `leetcode-easy`
- `scripts/tmux_medium.sh`: `leetcode-medium`
- `scripts/tmux_hard.sh`: `leetcode-hard`

查看和进入后台任务：

```bash
tmux ls
tmux attach -t leetcode-all
```

取消当前生成任务：

```bash
tmux kill-session -t leetcode-all
```

取消所有 tmux session：

```bash
tmux kill-server
```

## 文档

- `specs/PRD.md`: 英文产品需求和实现约束
- `specs/PRD.cn.md`: 中文产品需求和实现约束
- `specs/PROJECT_STRUCTURE.md`: 英文项目结构、模块职责、SOLID/DRY 和测试规划
- `specs/PROJECT_STRUCTURE.cn.md`: 中文项目结构、模块职责、SOLID/DRY 和测试规划
- `dataset/dataset.md`: 英文数据集来源和字段说明
- `dataset/dataset.cn.md`: 中文数据集来源和字段说明
- `Leetcode-QC/validate-pro/specs/PRD.md`: Validate Pro 可控 AI 对数验证设计
- `Leetcode-QC/validate-pro/specs/PRD.cn.md`: Validate Pro 中文设计文档

## Prompt 复用策略

prompt 分为三层，以最大化复用和缓存命中：

- `SYSTEM_PROMPT`: 所有题目、所有语言完全相同，包含全局生成要求和输出约束。
- `problem_prompt`: 同一道题的所有语言完全相同，包含题目元信息、描述、示例、约束、提示和可用题解参考。
- `language_prompt`: 只包含目标语言和该语言的 LeetCode starter code，是每次调用中变化最小的部分。

切换语言时只改变 `language_prompt`；切换题目时 `SYSTEM_PROMPT` 仍保持不变。这个结构对 prompt cache 最友好。

`language_prompt` 中的 LeetCode starter code 和函数头必须出现在最终输出中。生成结果必须保留对应语言的提交入口，例如 `class Solution`、`impl Solution`、`func twoSum(...)` 或 `def two_sum(...)`，确保代码可以直接提交到 LeetCode。

## 设计意图

这个项目的核心不是把题目重新存一遍，而是把题目中的有效信息压缩成稳定输入，用来生成可直接提交的多语言最优解。题目正文、examples、constraints、topics、hints 和可选 editorial 都用于生成 prompt；最终 Markdown 只保存各语言代码，避免输出目录变成题目镜像。

生成流程默认按 Easy、Medium、Hard 推进。Easy 先跑可以快速验证依赖、日志、输出格式和断点续跑；Medium 再扩大覆盖；Hard 最后使用更高 think 强度，减少复杂题失败率。失败不会阻塞全局任务，而是写入 `logs/<日期时间>/failures.jsonl`，方便后续只重跑失败项。

日志分成 stdout、stderr 和 failures 三类，是为了把正常进度、模型/环境警告和结构化失败记录分开。屏幕能实时看到进度，文件日志保留完整现场，长时间 tmux 运行时也方便排查。

## 断点续跑规则

断点续跑基于每道题对应的目标 Markdown 文件进行判断。

- Easy 和 Medium 按题目粒度续跑。如果某题文件已经包含所有预期语言，就直接跳过；如果文件不完整，就补齐缺失语言，并在本次题目生成结束后写回一次文件。
- Hard 按语言粒度续跑。生成器会先读取该题 Markdown 中已有的语言代码块，跳过已经存在的语言；每生成完一个新的缺失语言，就把已有语言和新语言一起写回文件。
- 如果 Hard 在生成 Kotlin 时中断或失败，下次运行会保留这道题里已经写好的 Cpp、Java、Python 等语言，并从缺失的 Kotlin 继续，而不是从这道题的 Cpp 重新开始。
- 每次运行也会尽量修复旧版异常输出。如果某个文件只剩 Kotlin，会被视为缺失前面的语言并自动补齐；如果完整文件只是语言顺序错了，会在不调用模型的情况下按数据集语言顺序重写。

## 实现原则

生成器核心流程遵循 SOLID 和 DRY 原则。数据集读取、prompt 构造、模型调用、断点续跑判断、查缺补漏报告、日志记录和 Markdown 写入分别放在职责明确的模块里。Markdown 解析规则集中维护，确保 resume、audit 和 repair 对“一个语言是否完成”的判断完全一致。

## 项目规模

这个仓库不只是保存题解文件，而是围绕 LeetCode 多语言题解生成构建的一整套生成与质量控制系统：

- 基于 `dataset/merged_problems.json` 的数据集驱动 prompt 构造
- 多语言题解生成和稳定的 Markdown 输出规则
- 固定宽度难度分桶和自动生成的难度索引
- MkDocs 文档站和 GitHub Pages 部署链路
- 缺失语言审计和疑似异常输出审计工具
- 用于历史输出清理的迁移工具
- `Leetcode-QC/validate/` 下的 Docker 快速验证层
- `Leetcode-QC/validate-pro/` 下的可控 AI 对数验证设计

这个项目的目标是让题解文件、生成脚本、审计工具、验证工具、迁移脚本和文档系统都使用同一套路由规则和语言区块规则。只有这些规则统一，大规模生成、断点续跑、历史清理、索引生成、文档展示和后续验证才能作为一个完整工程流程稳定推进。
