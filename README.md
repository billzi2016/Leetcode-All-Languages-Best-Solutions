# LeetCode All Languages Best Solutions

This project generates and organizes accurate optimal LeetCode solutions for every supported language, then writes them as Markdown files grouped by difficulty, problem range, and problem slug.

Documentation site:

- https://billzi2016.github.io/Leetcode-All-Languages-Bset-Solutions/

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
easy/
  1-100/
    0001-two-sum.md
    0009-palindrome-number.md
    0013-roman-to-integer.md
    0014-longest-common-prefix.md
    0020-valid-parentheses.md
    ...

medium/
  1-100/
    0002-add-two-numbers.md
    0003-longest-substring-without-repeating-characters.md
    0005-longest-palindromic-substring.md
    0006-zigzag-conversion.md
    0007-reverse-integer.md
    ...

hard/
  1-100/
    0004-median-of-two-sorted-arrays.md
    0010-regular-expression-matching.md
    0023-merge-k-sorted-lists.md
    0025-reverse-nodes-in-k-group.md
    0030-substring-with-concatenation-of-all-words.md
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
PYTHONPATH=src python -m unittest discover -s tests
```

The tests include formal-flow coverage for LeetCode 1 / 2 / 4, covering Easy, Medium, and Hard, and verify that a second run skips already generated files.

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

- `docs/PRD.md`: Product requirements and implementation constraints
- `docs/PRD.cn.md`: Chinese version of the PRD
- `docs/PROJECT_STRUCTURE.md`: Project structure, module responsibilities, SOLID/DRY, and test plan
- `docs/PROJECT_STRUCTURE.cn.md`: Chinese version of the project structure document
- `dataset/dataset.md`: Dataset source and field documentation
- `dataset/dataset.cn.md`: Chinese version of the dataset documentation

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
