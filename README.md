# LeetCode All Languages Best Solutions

This project generates and organizes accurate optimal LeetCode solutions for every supported language, then writes them as Markdown files grouped by difficulty, problem range, and problem slug.

Documentation site:

- https://billzi2016.github.io/Leetcode-All-Languages-Best-Solutions/

## Supported Languages

The project covers every language that appears in the LeetCode dataset with starter code. The signature examples below come from LeetCode 1, `Two Sum`.

| Language | Short Description | LeetCode Signature Example |
| --- | --- | --- |
| C | Good for low-level array and pointer work. | `int* twoSum(int* nums, int numsSize, int target, int* returnSize)` |
| C++ | Good for STL containers and algorithmic implementations. | `class Solution { public: vector<int> twoSum(vector<int>& nums, int target) }` |
| Java | Good for strongly typed object-oriented solutions. | `class Solution { public int[] twoSum(int[] nums, int target) }` |
| Python | Good for concise algorithm expression. | `class Solution(object): def twoSum(self, nums, target)` |
| Python3 | Good for modern Python with type annotations. | `class Solution: def twoSum(self, nums: List[int], target: int) -> List[int]` |
| C# | Good for .NET-style strongly typed solutions. | `public class Solution { public int[] TwoSum(int[] nums, int target) }` |
| JavaScript | Good for dynamic function submissions. | `var twoSum = function(nums, target)` |
| TypeScript | Good for JavaScript-style solutions with type constraints. | `function twoSum(nums: number[], target: number): number[]` |
| PHP | Good for class-method submissions. | `class Solution { function twoSum($nums, $target) }` |
| Swift | Good for strongly typed Apple ecosystem code. | `class Solution { func twoSum(_ nums: [Int], _ target: Int) -> [Int] }` |
| Kotlin | Good for modern strongly typed JVM code. | `class Solution { fun twoSum(nums: IntArray, target: Int): IntArray }` |
| Dart | Good for Dart ecosystem syntax. | `class Solution { List<int> twoSum(List<int> nums, int target) }` |
| Go | Good for concise function submissions. | `func twoSum(nums []int, target int) []int` |
| Ruby | Good for script-style expression. | `def two_sum(nums, target)` |
| Scala | Good for mixed functional and object-oriented JVM code. | `object Solution { def twoSum(nums: Array[Int], target: Int): Array[Int] }` |
| Rust | Good for memory-safe and high-performance implementations. | `impl Solution { pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> }` |
| Racket | Good for functional solutions with contracts. | `(define/contract (two-sum nums target) ...)` |
| Erlang | Good for functional concurrent-language style. | `-spec two_sum(Nums :: [integer()], Target :: integer()) -> [integer()].` |
| Elixir | Good for functional pipeline and pattern-matching style. | `defmodule Solution do ... def two_sum(nums, target) do ... end` |

## Output Layout Example

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

## Current Status

The foundational project structure and core flow are implemented:

- Dataset loading and filtering by difficulty/problem id
- Prompt construction with `images` excluded
- Python `ollama` library client wrapper
- Easy / Medium / Hard think modes: `low` / `medium` / `high`
- 100_000-token output limit per language generation
- Temperature fixed at `0.1`
- Markdown output paths and file format
- Resume support and completed-problem skipping
- stdout / stderr / failures log separation
- `unittest` coverage

## Dataset

This repository does not commit `dataset/merged_problems.json`. Download it locally before running generation:

```bash
curl -L -o dataset/merged_problems.json https://raw.githubusercontent.com/neenza/leetcode-problems/master/merged_problems.json
```

Dataset field documentation:

- `dataset/dataset.md`
- `dataset/dataset.cn.md`

## Install Dependencies

```bash
python -m pip install -r requirements.txt
```

Dependencies:

- `ollama`
- `tqdm`

## Run Tests

```bash
PYTHONPATH=src python -m unittest discover -s tests/unit
```

The tests include formal-flow coverage for LeetCode 1 / 2 / 4, covering Easy, Medium, and Hard, and verify that a second run skips already generated files.

## Validate Generated Solutions

The validation system is organized under `Leetcode-QC/`. It has three layers, from lightweight static checks to deeper generated-case differential validation.

### Layer 1: Static Audits

`migrate/audit_missing_solutions.py` and `migrate/audit_suspicious_solutions.py` scan generated Markdown without running solution code. They check for missing language sections, repairable ordering issues, suspiciously long code blocks, Markdown leftovers, and repeated output.

### Layer 2: Baseline Docker Validation

`Leetcode-QC/validate/` is the fast Docker validation layer. It reads official examples from `dataset/merged_problems.json`, extracts generated solution code blocks, compiles or runs supported language sections, and writes CSV matrices by difficulty:

```text
Leetcode-QC/validate/reports/easy.csv
Leetcode-QC/validate/reports/medium.csv
Leetcode-QC/validate/reports/hard.csv
```

Build and run:

```bash
docker compose -f Leetcode-QC/validate/compose.yaml build
docker compose -f Leetcode-QC/validate/compose.yaml run --rm validate
```

### Layer 3: Validate Pro Differential Validation

`Leetcode-QC/validate-pro/` is the extended differential validation layer. Differential validation means the project does not only trust one generated solution: it asks `gpt-oss:120b` to design more edge-case candidates, uses local Python reference solvers to calculate the expected answers, stores only verified cases as JSON, and then runs a larger Docker validation set against the generated solutions.

Validate Pro entry points:

```bash
docker compose -f Leetcode-QC/validate-pro/compose.yaml build
docker compose -f Leetcode-QC/validate-pro/compose.yaml run --rm validate-pro
docker compose -f Leetcode-QC/validate-pro/compose.yaml run --rm generate-cases
```

Validate Pro documentation:

- `Leetcode-QC/validate-pro/specs/PRD.md`
- `Leetcode-QC/validate-pro/specs/PRD.cn.md`

`Leetcode-QC/validate-pro/` is a deeper validation layer, not a replacement for `Leetcode-QC/validate/`.

## Generate Problems

Generate LeetCode 1:

```bash
PYTHONPATH=src python scripts/generate_solutions.py --only-frontend-id 1
```

Generate LeetCode 1 / 2 / 4 in one run:

```bash
PYTHONPATH=src python scripts/generate_solutions.py --frontend-ids 1 2 4
```

Generate Easy:

```bash
PYTHONPATH=src python scripts/generate_solutions.py --difficulty Easy
```

Generate Medium:

```bash
PYTHONPATH=src python scripts/generate_solutions.py --difficulty Medium
```

Generate Hard:

```bash
PYTHONPATH=src python scripts/generate_solutions.py --difficulty Hard
```

Generate all difficulties:

```bash
PYTHONPATH=src python scripts/generate_solutions.py
```

Audit generated Markdown without calling the model:

```bash
PYTHONPATH=src python scripts/audit_missing_solutions.py
PYTHONPATH=src python scripts/audit_missing_solutions.py --difficulty Hard
PYTHONPATH=src python scripts/audit_missing_solutions.py --frontend-ids 4 10
```

The audit script prints a read-only report. It does not call Ollama, does not write files, and does not repair Markdown by itself. Run `scripts/generate_solutions.py` after the audit when you want the generator to perform the minimal backfill.

Generate all solutions in a background tmux session:

```bash
scripts/tmux_all.sh
```

Generate one difficulty in a background tmux session:

```bash
scripts/tmux_easy.sh
scripts/tmux_medium.sh
scripts/tmux_hard.sh
```

These tmux scripts run `python -m pip install -r requirements.txt` before starting their tmux sessions. Missing dependencies therefore fail in the foreground instead of causing a silent background generation failure.

Default session names:

- `scripts/tmux_all.sh`: `leetcode-all`
- `scripts/tmux_easy.sh`: `leetcode-easy`
- `scripts/tmux_medium.sh`: `leetcode-medium`
- `scripts/tmux_hard.sh`: `leetcode-hard`

Inspect and attach to the background task:

```bash
tmux ls
tmux attach -t leetcode-all
```

Cancel the current generation task:

```bash
tmux kill-session -t leetcode-all
```

Cancel all tmux sessions:

```bash
tmux kill-server
```

## Documentation

- `specs/PRD.md`: Product requirements and implementation constraints
- `specs/PRD.cn.md`: Chinese version of the PRD
- `specs/PROJECT_STRUCTURE.md`: Project structure, module responsibilities, SOLID/DRY, and test plan
- `specs/PROJECT_STRUCTURE.cn.md`: Chinese version of the project structure document
- `dataset/dataset.md`: Dataset source and field documentation
- `dataset/dataset.cn.md`: Chinese version of the dataset documentation
- `Leetcode-QC/validate-pro/specs/PRD.md`: Validate Pro controlled-AI differential validation design
- `Leetcode-QC/validate-pro/specs/PRD.cn.md`: Chinese version of the Validate Pro design

## Prompt Reuse Strategy

Prompts are split into three layers to maximize reuse and cache hits:

- `SYSTEM_PROMPT`: identical for every problem and every language; contains global generation requirements and output constraints.
- `problem_prompt`: identical for all languages of the same problem; contains problem metadata, description, examples, constraints, hints, and optional solution reference.
- `language_prompt`: contains only the target language and that language's LeetCode starter code; this is the smallest changing part of each call.

Changing the target language only changes `language_prompt`; changing the problem still keeps `SYSTEM_PROMPT` unchanged. This structure is the most cache-friendly.

The LeetCode starter code and function header in `language_prompt` must appear in the final output. The generated code must preserve the submission entry point for the target language, such as `class Solution`, `impl Solution`, `func twoSum(...)`, or `def two_sum(...)`, so it can be pasted directly into LeetCode.

## Design Intent

The project is not meant to mirror LeetCode problem statements. It turns the useful problem data into stable generation input, then stores only submit-ready multilingual solution code. Problem statements, examples, constraints, topics, hints, and optional editorials are used in prompts; the final Markdown files stay focused on code.

Generation proceeds in Easy, Medium, then Hard order. Easy validates dependencies, logging, output layout, and resume behavior quickly. Medium expands coverage. Hard runs last with the highest think mode to reduce failures on complex problems. A failed language does not block the full run; it is written to `logs/<datetime>/failures.jsonl` for later targeted reruns.

stdout, stderr, and failures are intentionally separated. Progress remains visible on screen, file logs preserve the run context, and long tmux jobs can be debugged without mixing normal progress with warnings or structured failure data.

## Resume Rules

Resume detection is based on the target Markdown file for each problem.

- Easy and Medium use problem-level resume. If a problem file already contains all expected language sections, the problem is skipped. If it is incomplete, the generator fills the missing languages and writes the problem file once after the run has collected the available results.
- Hard uses language-level resume. The generator reads the existing language sections from the problem Markdown, skips languages that are already present, and writes the file after each newly generated language.
- If a Hard run stops or fails while generating Kotlin, the next run keeps the earlier sections such as Cpp, Java, and Python, then resumes from the missing Kotlin section instead of restarting the problem from Cpp.
- Each run also repairs old malformed output when possible. A file that only contains Kotlin is treated as missing the earlier languages and will be backfilled; a complete file with languages in the wrong order is rewritten into the dataset language order without calling the model.

## Implementation Principles

The generator follows SOLID and DRY principles in the core workflow. Dataset loading, prompt construction, model calls, resume detection, audit reporting, logging, and Markdown writing live in separate modules with narrow responsibilities. Markdown parsing rules are centralized so resume, audit, and repair behavior use the same definition of a completed language section.
