# LeetCode All Languages Best Solutions

本项目用于生成和整理 LeetCode 所有支持语言的准确最优解，并按难度、题号区间和题目 slug 输出为 Markdown 文件。

文档站点：

- https://billzi2016.github.io/Leetcode-All-Languages-Best-Solutions/

## 支持语言

本项目覆盖 LeetCode 数据集中提供 starter code 的全部语言。下面的代码头示例来自 LeetCode 1 `Two Sum`。

| 语言 | 简介 | LeetCode 代码头示例 |
| --- | --- | --- |
| C | 适合底层数组和指针操作。 | `int* twoSum(int* nums, int numsSize, int target, int* returnSize)` |
| C++ | 适合使用 STL 容器和算法。 | `class Solution { public: vector<int> twoSum(vector<int>& nums, int target) }` |
| Java | 适合强类型面向对象实现。 | `class Solution { public int[] twoSum(int[] nums, int target) }` |
| Python | 适合简洁表达算法逻辑。 | `class Solution(object): def twoSum(self, nums, target)` |
| Python3 | 适合类型标注和现代 Python 写法。 | `class Solution: def twoSum(self, nums: List[int], target: int) -> List[int]` |
| C# | 适合 .NET 风格强类型实现。 | `public class Solution { public int[] TwoSum(int[] nums, int target) }` |
| JavaScript | 适合动态类型函数提交。 | `var twoSum = function(nums, target)` |
| TypeScript | 适合带类型约束的 JavaScript 写法。 | `function twoSum(nums: number[], target: number): number[]` |
| PHP | 适合类方法形式提交。 | `class Solution { function twoSum($nums, $target) }` |
| Swift | 适合 Apple 生态强类型实现。 | `class Solution { func twoSum(_ nums: [Int], _ target: Int) -> [Int] }` |
| Kotlin | 适合 JVM 上的现代强类型写法。 | `class Solution { fun twoSum(nums: IntArray, target: Int): IntArray }` |
| Dart | 适合 Dart 生态语法。 | `class Solution { List<int> twoSum(List<int> nums, int target) }` |
| Go | 适合简洁函数式提交。 | `func twoSum(nums []int, target int) []int` |
| Ruby | 适合脚本风格表达。 | `def two_sum(nums, target)` |
| Scala | 适合 JVM 上的函数式和面向对象混合写法。 | `object Solution { def twoSum(nums: Array[Int], target: Int): Array[Int] }` |
| Rust | 适合强安全约束和高性能实现。 | `impl Solution { pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> }` |
| Racket | 适合函数式表达和 contract 定义。 | `(define/contract (two-sum nums target) ...)` |
| Erlang | 适合函数式并发语言风格。 | `-spec two_sum(Nums :: [integer()], Target :: integer()) -> [integer()].` |
| Elixir | 适合函数式管道和模式匹配风格。 | `defmodule Solution do ... def two_sum(nums, target) do ... end` |

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
PYTHONPATH=src python -m unittest discover -s tests
```

测试包含 LeetCode 1 / 2 / 4 的正式流程测试，分别覆盖 Easy、Medium、Hard，并验证第二次运行能正常跳过已生成文件。

## 验证生成题解

`validate/` 提供容器化题解验证环境。它从 `dataset/merged_problems.json` 读取 LeetCode 样例，解析已经生成的 Markdown 题解代码块，按语言编译或运行，并按难度写出 CSV 矩阵：

```text
validate/reports/easy.csv
validate/reports/medium.csv
validate/reports/hard.csv
```

构建和运行：

```bash
docker build -f validate/Dockerfile -t leetcode-solutions-validate .
docker run --rm -v "$PWD":/workspace leetcode-solutions-validate
```

验证工具分为三层：

- `migrate/audit_missing_solutions.py` 和 `migrate/audit_suspicious_solutions.py` 用来扫描已经生成的 Markdown，找缺失语言、可修复顺序异常、异常长代码块、Markdown 残留和重复输出。
- `validate/` 是快速 Docker 验证层。它运行 dataset examples，并写出紧凑的 CSV 矩阵。
- `validate-pro/` 是增强对数验证设计。它使用 `gpt-oss:120b` 额外生成边界样例候选，再用 Python 参考解校验这些样例，把保留下来的样例保存为 JSON，最后运行更大的 Docker 验证集合。它是更深一层的验证，不替代 `validate/`。

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

- `docs/PRD.md`: 英文产品需求和实现约束
- `docs/PRD.cn.md`: 中文产品需求和实现约束
- `docs/PROJECT_STRUCTURE.md`: 英文项目结构、模块职责、SOLID/DRY 和测试规划
- `docs/PROJECT_STRUCTURE.cn.md`: 中文项目结构、模块职责、SOLID/DRY 和测试规划
- `dataset/dataset.md`: 英文数据集来源和字段说明
- `dataset/dataset.cn.md`: 中文数据集来源和字段说明

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
