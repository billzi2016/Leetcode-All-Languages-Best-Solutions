# Validate Pro 产品需求文档

## 1. 目标

`validate-pro/` 是一个面向生成题解的增强正确性验证系统。

核心思路是对数验证：

1. 从 `dataset/merged_problems.json` 读取原始题目。
2. 使用 `gpt-oss:120b` 的 high 推理模式，一次生成一个高质量测试样例。
3. 使用可信的 Python 参考解计算标准答案。
4. 只有能被解析、能运行、并且能通过参考解校验的样例才会保留。
5. 复用现有 `validate/` 的 Docker 多语言执行层，验证已经生成的各语言题解。
6. 按难度输出 CSV 报告，展示每道题每种语言是否通过生成样例集合。

这个模块用于比固定 examples 更强的正确性检查，重点覆盖边界情况、约束极值、重复值、特殊结构和容易让模型出错的测试点。

核心设计原则是可控 AI：模型用于有目标地发现测试样例，不负责最终判定真值。ReAct 风格推理帮助模型一次提出一个有明确目的的候选样例，而本地确定性校验负责决定该候选是否允许进入保留样例集合。

## 2. 非目标

- 不调用题解生成器。
- 不修改题解 Markdown 文件。
- 不替代 `validate/`；`validate/` 仍然作为基础样例验证层存在。
- 不保留未经过本地参考解验证的 AI 样例。
- 不使用离谱耗时的暴力解。参考解可以朴素、可以用库、可以暴力，但单个样例必须在合理时间内完成，不能出现一个样例跑很久的情况。

## 3. 输入

### 数据集

主要来源：

```text
dataset/merged_problems.json
```

每道题包含：

- `frontend_id`
- `title`
- `problem_slug`
- `difficulty`
- `description`
- `constraints`
- `examples`
- `topics`
- `hints`
- `code_snippets`

### 已生成题解

已生成的 Markdown 题解位于：

```text
Leetcode-Easy/
Leetcode-Medium/
Leetcode-Hard/
```

### 现有验证层

现有基础验证模块位于：

```text
validate/
```

`validate-pro/` 应该生成经过校验的测试样例，并复用或扩展 `validate/` 的 Docker 多语言执行结构。

## 4. 可控 AI 设计

`validate-pro/` 应把 LLM 放在一个受约束的测试设计角色中，并用确定性验证闭环约束它。

控制流程：

```text
题目上下文 -> ReAct 样例提案 -> JSON 解析 -> schema 检查
-> constraints 检查 -> Python 参考解 -> 输出规范化
-> 保留样例库 -> Docker 多语言 runner -> CSV 报告
```

LLM 可以：

- 识别尚未覆盖的边界条件；
- 提出一个候选输入；
- 在结构化字段中说明测试目的；
- 给出一个 expected 输出建议。

LLM 不可以：

- 直接决定样例正确；
- 未经本地验证就写入保留样例库；
- 绕过 constraints 检查；
- 绕过参考解比较；
- 修改已经生成的题解 Markdown。

这使系统是 AI 辅助的，但最终由本地逻辑控制。保留下来的测试集不是原始模型输出，而是模型探索和确定性参考执行共同产生的验证产物。

## 5. 输出

### 生成样例文件

经过本地参考解确认的样例应写入：

```text
Leetcode-QC/validate-pro/cases/
```

建议结构：

```text
Leetcode-QC/validate-pro/cases/
  0001-two-sum.json
  0002-add-two-numbers.json
  0020-valid-parentheses.json
```

单题样例文件建议格式：

```json
{
  "frontend_id": "1",
  "title": "Two Sum",
  "problem_slug": "two-sum",
  "difficulty": "Easy",
  "method": "twoSum",
  "cases": [
    {
      "input": {
        "nums": [2, 7, 11, 15],
        "target": 9
      },
      "expected": [0, 1],
      "source": "gpt-oss:120b",
      "purpose": "basic example with one valid pair"
    }
  ]
}
```

### CSV 报告

最终报告格式延续当前 `validate/` 风格：

```text
Leetcode-QC/validate-pro/reports/easy.csv
Leetcode-QC/validate-pro/reports/medium.csv
Leetcode-QC/validate-pro/reports/hard.csv
```

CSV 每一行是一道题。每个语言列只使用：

```text
1 = 通过全部保留样例
0 = 未通过全部保留样例
```

## 6. 高层流程

### Step 1：读取题目

对每道被选中的题：

1. 读取完整 dataset 记录。
2. 提取题面、examples、constraints、topics、hints 和 starter signatures。
3. 从 `code_snippets` 推断方法名、参数结构和返回类型。

### Step 2：构建 Python 参考解

每种已支持题型都需要一个可信 Python 参考解。

参考解可以使用：

- 简单暴力枚举；
- Python 标准库；
- 直接模拟；
- 小规模穷举；
- 朴素动态规划；
- 明确正确的数学公式。

参考解不追求最优复杂度，但必须受控。单个生成样例应快速完成，整道题的样例生成和验证应在可接受时间内完成。

示例：

- `Two Sum`：双重循环枚举所有下标对。
- `Valid Parentheses`：栈模拟。
- `Merge Two Sorted Lists`：链表转数组、合并数组、再转回链表。
- `Best Time to Buy and Sell Stock`：小规模时可枚举买卖日，也可线性扫描。
- SQL、Shell、Pandas 题：需要单独参考策略，不和普通算法 runner 混用。

### Step 3：一次生成一个候选样例

调用 `gpt-oss:120b`，使用 high 推理模式，一次只要求生成一个候选测试样例。

Prompt 必须包含：

- 完整原题；
- constraints；
- examples；
- topics；
- starter signatures；
- 已知输入输出格式；
- 目标 JSON schema；
- 本轮希望覆盖的测试目的。

样例生成可以采用 ReAct 风格的内部流程：

1. 找一个尚未覆盖的行为或边界；
2. 提议输入；
3. 解释为什么该输入合法；
4. 最终只输出严格 JSON。

最终保留的输出必须是机器可解析 JSON。如果最终答案里混入 JSON 外的解释文字，则该候选样例无效。

### Step 4：校验候选样例

每个候选样例需要经过以下检查：

1. JSON 可解析。
2. 必要字段存在。
3. 输入类型符合推断出的函数签名。
4. 输入满足题目 constraints。
5. Python 参考解可以运行。
6. 如果模型给出 expected，则 expected 必须和参考解结果一致。
7. 对允许多答案的题，先做规范化再比较。

只有通过全部检查的样例才会进入样例库。

如果 AI 生成的样例不合法、不明确、太大、跑不动，或者 expected 和参考解不一致，就丢弃并重新请求一个候选样例。

### Step 5：构建样例集合

每道题应保留一组覆盖面均衡的样例。

样例集合应包含：

- 原 dataset examples；
- 最小规模输入；
- 安全范围内的较大输入；
- 重复值；
- 负数；
- 空输入；
- 单元素输入；
- 全相等输入；
- 已排序输入；
- 逆序输入；
- 允许多答案时的多答案场景；
- 针对每个主要 topic 或 constraint 的专项样例。

覆盖要显式设计，而不是碰运气。每个保留样例都应该有 `purpose` 字段，并映射到某个覆盖类别：

| 类别 | 示例 |
| --- | --- |
| 最小规模 | 允许时的空列表、单节点、单字符字符串、单行矩阵 |
| 小规模穷举 | 数组长度小到可以暴力验证，短字符串覆盖所有字符类别 |
| 边界值 | constraints 允许的最小值和最大值 |
| 重复值 | 全相等值、重复 key、重复字符、重复行 |
| 符号处理 | 全负数、全正数、正负混合、大量 0 |
| 顺序 | 已排序、逆序、几乎有序、环状顺序 |
| 形状 | 偏斜树、平衡树、非连通图、单格 grid |
| 歧义 | 多个正确答案、答案顺序无关、集合式输出 |
| 失败路径 | 无匹配、不可能 target、空结果、布尔 false |
| 预算内压力 | 在参考解可以稳定快速处理范围内的较大输入 |

建议默认值：

```text
min_cases_per_problem = 10
max_cases_per_problem = 50
max_generation_attempts_per_case = 5
```

### Step 6：多语言验证

样例集合确认后，使用 Docker 多语言验证层运行已生成的 Markdown 题解。

执行层复用 `validate/` 的设计：

- 解析 Markdown 语言 section；
- 生成语言专用 harness；
- 编译或运行代码；
- 对比 retained cases 的 expected；
- 按难度写出 CSV 矩阵。

## 7. GPT-OSS Prompt 要求

测试样例生成 prompt 必须给足上下文，让模型表现为谨慎的测试设计者。

必须包含以下内容：

```text
Problem ID
Title
Difficulty
Topics
Original Description
Constraints
Examples
Starter Signatures
Known Input Schema
Known Output Schema
Reference Case Purposes Already Covered
Requested New Case Purpose
Strict JSON Schema
```

Prompt 应明确要求模型：

- 只生成一个 case；
- 输入必须满足 constraints；
- 优先覆盖某个明确边界或特殊行为；
- 避免巨大输入；
- 避免没有目的的随机数据；
- 最终只输出严格 JSON；
- JSON 内部包含简短 `purpose` 字段。

示例输出：

```json
{
  "input": {
    "nums": [-3, 4, 3, 90],
    "target": 0
  },
  "expected": [0, 2],
  "purpose": "negative and positive values form the only valid pair"
}
```

## 8. 样例生成策略示例

模块应按题型设计具体的样例生成策略。Prompt 每次只请求其中一种策略，adapter 再用参考解验证候选样例后才保存。

### 数组搜索

典型题型：

- `Two Sum`
- `Contains Duplicate`
- `Search Insert Position`

候选目的：

- 答案下标位于数组两端；
- 正负数共同组成答案；
- 存在重复值，但重复值不是答案；
- 最小合法数组；
- 题目允许时存在多个可行答案；
- 对返回插入位置或 boolean false 的题，构造目标不存在的情况。

### 字符串和栈

典型题型：

- `Valid Parentheses`
- `Longest Common Prefix`
- `Valid Palindrome`

候选目的：

- 允许时的空字符串；
- 单字符字符串；
- 嵌套结构；
- 相邻结构；
- 早期不匹配；
- 末尾才不匹配；
- 原题允许时包含非字母字符；
- 需要忽略大小写的场景。

### 链表

典型题型：

- `Add Two Numbers`
- `Merge Two Sorted Lists`
- `Remove Duplicates from Sorted List`

候选目的：

- 空链表；
- 一个空链表和一个非空链表；
- 进位贯穿所有位；
- 不同长度的重复段；
- 一个链表所有节点都小于另一个链表；
- 合并时两个链表交替出节点。

### 树

典型题型：

- `Maximum Depth of Binary Tree`
- `Same Tree`
- `Symmetric Tree`

候选目的：

- 空树；
- 单节点；
- 完全偏斜树；
- 平衡树；
- 值相同但结构不同；
- 镜像结构中某个深层节点不匹配。

### 图和 Grid

典型题型：

- `Number of Islands`
- `Flood Fill`
- `Course Schedule`

候选目的：

- 单格 grid；
- 全水或全陆地；
- 只对角相邻但不应连通；
- 多个非连通分量；
- 依赖图中存在环；
- 长链依赖但没有环。

### 动态规划

典型题型：

- `Climbing Stairs`
- `House Robber`
- `Maximum Subarray`

候选目的：

- 最小 `n`；
- 重复相等值；
- 允许时全负数；
- 局部最优不等于全局最优；
- 高低值交替；
- 输入规模接近参考解安全上限。

### SQL、Shell 和 Pandas

这些题应使用独立 adapter，不和普通算法 adapter 混用。

候选目的：

- 空表；
- 重复行；
- null 值；
- 排名并列；
- join 目标缺失；
- 单行文件；
- 文件末尾换行；
- 混合空白字符。

这些题的 expected 应由受控本地执行器计算，例如 SQLite、pandas 或临时 shell fixture，具体取决于题型。

## 9. 候选样例拒绝规则

以下情况必须拒绝：

- JSON 无法解析。
- 缺少必要输入字段。
- 输入类型和函数签名不匹配。
- 违反题目 constraints。
- 对参考解来说输入过大。
- 对 Docker 多语言 runner 来说执行成本过高。
- 题目不允许多答案，但样例存在歧义。
- expected 经过规范化后仍和参考解不一致。
- 依赖原题没有说明的隐藏假设。
- 和已保留样例重复。
- 和已有样例覆盖同一个 purpose，且没有新增行为。
- 无法序列化为保留样例 JSON 格式。

## 10. 参考解要求

每个参考解应暴露：

```python
def solve(case_input: dict) -> object:
    ...
```

每个题型 adapter 还应暴露：

```python
def validate_input(case_input: dict) -> None:
    ...

def normalize_expected(value: object) -> object:
    ...

def normalize_actual(value: object) -> object:
    ...

def equivalent(expected: object, actual: object) -> bool:
    ...
```

这样拆分是因为部分 LeetCode 题允许多种正确输出。

示例：

- `Two Sum` 可以把 `[0, 1]` 和 `[1, 0]` 规范化后视为相同答案。
- 返回集合、路径、组合的题需要排序或集合化。
- 浮点数题需要误差容忍。

参考解还应暴露安全输入预算，例如：

```python
MAX_N = 30
MAX_GRID_CELLS = 400
MAX_TREE_NODES = 200
```

预算应由 adapter 自己决定。暴力参考解可以设置更小上限，线性参考解可以设置更大上限。这样可以保证生成样例有价值，同时避免单个样例占用过多运行时间。

## 11. 目录设计

建议结构：

```text
Leetcode-QC/
  validate-pro/
    specs/
      PRD.md
      PRD.cn.md
    README.md
    README.cn.md
    Dockerfile
    requirements.txt
    generate_cases.py
    run_validation.py
    cases/
  reports/
  src/
    adapters/
      two_sum.py
      valid_parentheses.py
    llm_case_generator.py
    dataset.py
    markdown.py
    reference.py
    report.py
  tests/
    unit/
      test_dataset.py
      test_markdown.py
      test_prompt_builder.py
      test_reference_adapters.py
      test_case_generation.py
      test_case_retention.py
      test_report.py
      test_cli.py
    integration/
    smoke/
```

`cases/`、`reports/` 和 `work/` 应加入 Git 忽略，因为它们是生成产物。

`tests/unit/` 用于放置该模块的全部 unittest。validate-pro 的测试应覆盖 dataset 解析、prompt 构造、候选 JSON 解析、参考解 adapter、候选样例拒绝规则、保留样例持久化、CSV 报告生成和 CLI 参数解析。

## 12. CLI 设计

为单题生成样例：

```bash
python Leetcode-QC/validate-pro/generate_cases.py --frontend-id 1
```

为多题生成样例：

```bash
python Leetcode-QC/validate-pro/generate_cases.py --frontend-ids 1 2 20 121
```

按难度生成样例：

```bash
python Leetcode-QC/validate-pro/generate_cases.py --difficulty Easy
```

使用已保留样例运行验证：

```bash
python Leetcode-QC/validate-pro/run_validation.py
```

Docker 入口：

```bash
docker compose -f Leetcode-QC/validate-pro/compose.yaml build
docker compose -f Leetcode-QC/validate-pro/compose.yaml run --rm validate-pro
```

## 13. 运行控制

建议参数：

```text
--min-cases
--max-cases
--max-attempts-per-case
--max-reference-seconds
--difficulty
--frontend-ids
--languages
--reports-dir
--cases-dir
--coverage-profile
--token-budget
```

样例生成需要支持断点续跑：

- 如果某题已经有 retained case 文件，先读取已有文件。
- 只生成缺少的样例。
- 除非显式指定，否则不要覆盖已经保留的样例。
- 记录已经尝试过的 purpose，避免反复请求同一类样例。
- 达到配置的 token 预算或 case 数量预算后停止生成。

## 14. 安全性和可靠性

系统应把 LLM 当作不可信的测试样例提议者。

Python 参考解才是判定权威。一个样例只有经过本地确定性验证后，才能进入验证集合。

ReAct trace 对探索有用，但它不是可信输出。只有 final answer 中的严格 JSON 可以进入解析器，而且只有经过参考解验证的 JSON 才能进入 `Leetcode-QC/validate-pro/cases/`。

Docker runner 应该：

- 使用超时；
- 把临时 harness 文件隔离到 work 目录；
- 编译失败或运行失败时在 CSV 中写 `0`；
- 不修改题解 Markdown；
- 把生成报告放到被 Git 忽略的目录。

## 15. 和现有工具的关系

现有工具：

```text
migrate/audit_missing_solutions.py
migrate/audit_suspicious_solutions.py
validate/run_validation.py
```

建议工作流：

1. 用缺失审计找不完整 Markdown。
2. 用疑似异常审计找异常代码块。
3. 用 `validate/` 做 dataset examples 基础验证。
4. 用 `validate-pro/` 做生成边界样例验证。
5. 对失败题解按情况处理：重新生成、机械迁移，或直接修改具体 Markdown 代码块。

## 16. 成功标准

第一个可用版本应满足：

- 从 `dataset/merged_problems.json` 读取题目；
- 支持若干常见算法题型；
- 使用 `gpt-oss:120b` high 推理模式生成候选样例；
- 使用可控 AI 闭环：ReAct 提出候选，本地确定性检查决定是否保留；
- 自动拒绝非法 AI 样例；
- 只保留参考解验证过的样例；
- 按边界、重复、顺序、歧义、预算内压力等类别保留带 purpose 的样例；
- 在 Docker 中运行已生成 Markdown 题解；
- 写出 `easy.csv`、`medium.csv`、`hard.csv`；
- 所有生成样例和报告产物都不进入 Git；
- 包含 `validate-pro/tests/unit/` unittest 测试套件，覆盖解析器、adapter、样例生成、样例保留、报告和 CLI 行为；
- 保留当前 `validate/` 作为基础验证模块。
