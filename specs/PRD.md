# PRD: LeetCode All Languages Best Solutions

## Goal

This project uses the LeetCode problem data in `dataset/merged_problems.json` to generate optimal solutions for every available programming language, then organizes the generated Markdown files by difficulty, problem-id range, and problem slug.

The final artifact is a solution set, not a problem statement dataset. Each problem Markdown file stores only the best solution code for each language and does not repeat the full problem text.

## Model and Think Strength

Generation uses Ollama with `gpt-oss:120b`.

Think strength is selected by problem difficulty:

- Easy: `low`
- Medium: `medium`
- Hard: `high`

Generation order is fixed:

1. Easy
2. Medium
3. Hard

This allows the project to validate the flow on easier problems before moving to more complex ones.

## Data Source

Input data comes from:

- `dataset/merged_problems.json`

The top-level field is `questions`, and each item is one problem. Generation should use the information that improves solution correctness:

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

If `solutions` exists, it can be used as editorial reference material to improve correctness. If it is missing, skip it.

Some fields may be missing, including `solutions`, `images`, and `follow_ups`. Missing fields must be treated as optional and must not stop generation.

The `images` field is kept only as a dataset field and must not be sent into model prompts. `gpt-oss:120b` is not a multimodal model and cannot directly understand image URLs or image content.

## Prompt Design

Prompts are split into three layers:

1. Fixed system prompt
2. Cacheable shared problem prompt
3. Language-specific user prompt

### System Prompt

The system prompt contains stable requirements so every language does not rebuild different rules.

Input prompts may use Markdown or structured text to help the model understand the problem. Output must be strictly limited to raw code.

Core requirements:

- You are a senior algorithm engineer and LeetCode solution generator.
- Generate only the optimal solution for the target language.
- Prefer the best time and space complexity accepted by LeetCode.
- Strictly match the LeetCode function signature and starter-code style.
- Do not output the problem statement.
- Do not output Markdown prose.
- Do not output complexity analysis unless explicitly required later.
- Do not output tests, `main` functions, or extra I/O.
- The final output must contain raw code only.
- Do not wrap output in Markdown code fences. Do not output ``` or ```language.
- The final answer must include the LeetCode submission entry point from the starter code, such as the `Solution` class, `impl` block, function signature, module, or contract header.
- The final answer must be directly pasteable into the LeetCode editor for the target language.
- Think concisely, directly, and forcefully.
- If official editorial or solution content is provided, use it only as reference and still output clean submit-ready code.

Output quality requirements:

- Code must be complete.
- Code must directly replace the LeetCode editor starter code.
- Code must not depend on unsupported libraries or non-default LeetCode environment features.
- Code must not omit key logic.
- Code must not be pseudocode.

### Cacheable Shared Problem Prompt

The shared problem prompt is built from useful problem fields. It is identical for every language of the same problem, so it can be cached and reused.

Cache strategy:

- `SYSTEM_PROMPT` is globally stable and should be reused across problems and languages.
- The shared problem prompt contains useful problem fields except `images`; all languages for the same problem reuse it.
- The language user prompt contains only the target language and that language's starter code.
- Even when the problem changes, the system prompt stays unchanged, maximizing prompt-cache hits.
- Missing fields are skipped and do not affect the cache structure or generation flow.

Recommended content:

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

Skip missing fields instead of writing empty placeholders.

If an example contains `images`, skip that field when building prompts and use only textual `example_text`.

### Language User Prompt

The language user prompt contains only language-specific content:

- Target language name
- The corresponding `code_snippets` starter code

Example structure:

````text
Target Language: python3

Use this LeetCode starter code signature and style:

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pass
```

Generate the optimal accepted solution for this language.
Return raw code only. Do not wrap the answer in Markdown code fences.
````

This keeps the system prompt and shared problem prompt stable. Only the language layer changes, which improves cache reuse, resume behavior, and debugging.

## Output Structure

Generated results are split into three difficulty directories:

```text
Leetcode-Easy/
Leetcode-Medium/
Leetcode-Hard/
```

Inside each difficulty directory, files are bucketed by `frontend_id` in groups of 100. Directory names use fixed-width ranges so lexical sorting stays stable:

```text
Leetcode-Easy/
  0001-0100/
    0001-two-sum.md
  0101-0200/
    0101-symmetric-tree.md

Leetcode-Medium/
  0001-0100/
  0101-0200/

Leetcode-Hard/
  0001-0100/
  0101-0200/
```

Filename format:

```text
{zero-padded four-digit frontend_id}-{problem_slug}.md
```

Examples:

```text
0001-two-sum.md
0011-container-with-most-water.md
```

If `frontend_id` is not numeric, record it as an exceptional problem and skip or handle it separately.

## Per-Problem Markdown Format

Each `.md` file contains only language solutions, not the problem statement.

Recommended format:

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

The title keeps only the problem id and problem title for identification. Do not include the problem description, examples, constraints, hints, or editorial content.

## Language Scope

The language list comes from each problem's `code_snippets` field.

Generation should iterate over every language key in that object, such as:

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

Available languages may vary by problem. Use the actual `code_snippets` present for that problem.

## Progress Bars

Use `tqdm` for progress and process difficulties sequentially:

1. Run Easy until the Easy problem progress reaches 100%.
2. Run Medium until the Medium problem progress reaches 100%.
3. Run Hard until the Hard problem progress reaches 100%.

Each difficulty stage uses one outer `tqdm` for the number of completed problems. Each problem uses an inner `tqdm` for completed languages.

Pseudo-code:

```python
for difficulty in ["Easy", "Medium", "Hard"]:
    problems = get_problems_by_difficulty(difficulty)
    for problem in tqdm(problems, desc=difficulty):
        languages = get_languages(problem)
        for language in tqdm(languages, desc=problem["problem_slug"], leave=False):
            generate_solution(problem, language)
```

Keep the implementation simple. Do not hand-roll text progress bars or display Easy, Medium, and Hard progress bars simultaneously.

Progress is primarily tracked by problem Markdown files:

- Outer `tqdm` represents completed `.md` files for the current difficulty.
- Inner `tqdm` represents language generation progress for the current problem only.
- Easy and Medium increment the outer progress after all languages for a problem are generated and written once.
- Hard updates the problem `.md` after each generated language, but the outer progress still increments only after all languages for that problem are complete.

## Resume Behavior

Generation may run for a long time and must support resume.

Recommended strategy:

- If the target `.md` already exists and contains all target language headings, skip the problem.
- If the file exists but is missing languages, generate only the missing languages.
- Easy and Medium: collect all language results for the problem in memory, then write the target `.md` once after all languages succeed. This reduces SSD writes.
- Hard: update the target `.md` after each completed language to reduce loss from interruption.
- Use a temporary file and replace the target file to avoid corrupting files during interruption.

## Logging Requirements

Logs must support both debugging and real-time observation:

- Output has two paths: one to the screen and one to the current run's log directory.
- stdout messages print to screen stdout and write to `stdout.log`.
- stderr messages print to screen stderr and write to `stderr.log`.
- The log root is `logs/`, which is not committed to Git.
- Each run creates a dedicated timestamped log directory.
- stdout writes to `stdout.log` in the current run directory.
- stderr writes to `stderr.log` in the current run directory.
- Failure records write to `failures.jsonl` in the current run directory.
- Every log line must include a timestamp.
- stdout, stderr, and failure records must be separated and must not be mixed into one file.
- Model failures, retries, timeouts, invalid return formats, and skipped missing fields must be logged.

Log directory example:

```text
logs/
  2026-07-03_03-30-00/
    stdout.log
    stderr.log
    failures.jsonl
```

stdout example:

```text
2026-07-03 03:15:20 [INFO] Starting Easy generation
2026-07-03 03:16:10 [INFO] Finished 0001-two-sum
```

stderr example:

```text
2026-07-03 03:15:24 [WARN] ollama warning: ...
2026-07-03 03:16:02 [ERROR] 0001-two-sum python3 retry=2 timeout
```

`failures.jsonl` stores only structured failure records, not normal stdout/stderr text.

## Error Handling

Handle these cases:

- Missing `code_snippets`: log and skip the problem.
- Missing starter code for one language: skip that language.
- Model returns non-code output: record failure and retry.
- Model call timeout: retry; after 3 attempts, record failure.
- Missing JSON field: skip the field and continue.
- `frontend_id` cannot be parsed as a number: record as exceptional.

Each language can retry at most 3 times. After 3 failures, do not block the main flow. The system must:

1. Write to the current run's `stderr.log`.
2. Write to the current run's `failures.jsonl`.
3. Continue with the next problem or next processable unit.

Failure log path:

```text
logs/{run_datetime}/failures.jsonl
```

Each record contains:

- `frontend_id`
- `problem_slug`
- `difficulty`
- `language`
- `error`
- `retry_count`

## Code Quality Requirements

Implementation must remain maintainable:

- Every code file must start with an intent comment explaining what the file owns and does not own.
- Every public or core function must have a comment/docstring describing inputs, outputs, and side effects.
- Long logic, complex conditions, retry policy, resume behavior, file replacement, and log tee behavior must have focused comments.
- Comments should explain intent and edge cases, not restate every line.
- Module design must follow SOLID.
- Repeated logic must be extracted into functions or modules, following DRY.
- Prompt construction, Ollama calls, Markdown writing, progress display, logging, and dataset reading should be split into separate modules.
- A single module should have a clear responsibility; avoid putting the entire flow into one large script.

## Testing Requirements

All unit tests live in `tests/unit/` and use Python's standard `unittest` library.

Use `python` for Python commands. Do not write `python3` in docs or script instructions.

Tests must cover:

- Dataset loading, missing fields, difficulty filtering, and problem-id sorting.
- Prompt construction, especially `images` exclusion, optional `solutions`, and language starter-code insertion.
- Markdown output path, 100-problem buckets, filename format, and language section format.
- Easy/Medium write-once-per-problem behavior and Hard write-once-per-language behavior.
- Resume detection for complete problems and missing languages.
- stdout/stderr/failures log separation.
- Filtering for known requests dependency warnings in the current environment.
- Retry-3 failure behavior that records logs and continues with the next problem.
- Ollama client uses the Python `ollama` package, not `requests`.
- Ollama smoke test: use `hello` to verify `low`, `medium`, and `high` think modes are accepted locally.
- Ollama option tests: verify the 100_000 token output limit and temperature `0.1`.
- CLI argument tests: support multiple problem ids, such as `--frontend-ids 1 2 4`.
- Formal-flow tests for LeetCode 1 / 2 / 4, covering Easy, Medium, and Hard:
  - LeetCode 1 `Two Sum` -> `Leetcode-Easy/0001-0100/0001-two-sum.md`
  - LeetCode 2 `Add Two Numbers` -> `Leetcode-Medium/0001-0100/0002-add-two-numbers.md`
  - LeetCode 4 `Median of Two Sorted Arrays` -> `Leetcode-Hard/0001-0100/0004-median-of-two-sorted-arrays.md`
- After LeetCode 1 / 2 / 4 are generated, running again must detect complete `.md` files and skip model calls.

## Git Commit Requirements

Commit messages must be clear, detailed, and intention-revealing. Do not write vague messages such as `update`, `fix`, or `change`.

Recommended commit message structure:

```text
Implement the base LeetCode multi-language solution generator flow

Why this commit is needed:
- Use dataset/merged_problems.json as the problem input
- Generate in Easy, Medium, Hard order to reduce full-run validation risk
- Split prompt construction, model calls, file writes, and logging for maintainability

What changed:
- Add Ollama gpt-oss:120b client wrapper
- Add difficulty and problem-id bucketed Markdown output
- Add tqdm problem progress and language sub-progress
- Add logs/failures.jsonl failure records

Impact:
- Generated artifact directories are Leetcode-Easy/, Leetcode-Medium/, and Leetcode-Hard/
- dataset/merged_problems.json is still downloaded by users and is not committed
```

Commit messages should let future maintainers understand the purpose, design tradeoffs, and impact of the change.

## Ollama Call Requirements

Model calls must support:

- Model name: `gpt-oss:120b`
- Python `ollama` package; do not call HTTP directly with `requests`.
- Think strength based on difficulty: `low`, `medium`, `high`.
- Think strength smoke tests to verify local Ollama accepts `low`, `medium`, and `high`.
- System prompt.
- Shared problem prompt.
- Language user prompt.
- Maximum output limit of 100_000 tokens per problem/language generation.
- Temperature `0.1`.
- Timeout control.
- Retry control, with at most 3 retries per language.

If the actual Ollama API uses a different field name for think mode, implementation should follow the local Ollama version.

## Acceptance Criteria

Phase 1:

- Can read `dataset/merged_problems.json`.
- Can process in Easy -> Medium -> Hard order.
- Can select think strength by problem difficulty.
- Can generate one `.md` file containing all `code_snippets` languages for a problem.
- Can write files under paths such as `Leetcode-Easy/0001-0100/0001-two-sum.md`.
- Can show difficulty progress and language sub-progress.
- Easy and Medium write each problem `.md` once after all languages are complete.
- Hard updates the `.md` after each generated language.
- stdout/stderr are written both to screen and the current run's log directory.
- failures are written as structured records to `failures.jsonl`.
- Core modules have `unittest` coverage under `tests/unit/`.
- Ollama client tests cover the `ollama` package call, three think modes, 100_000 token output limit, and temperature `0.1`.
- LeetCode 1 / 2 / 4 can pass the formal flow and skip correctly on the second run.
- Missing fields are skipped.
- Resume is supported.

Phase 2:

- Full Easy generation is complete.
- Randomly sampled solutions can be pasted directly into LeetCode for their target languages.
- Failure logs can be replayed.

Phase 3:

- Full Medium generation is complete.
- Full Hard generation is complete.
- All generated file structures are stable and can be indexed, searched, or published by later scripts.
