# Validate Pro PRD

## 1. Goal

`validate-pro/` is an advanced correctness validation system for generated LeetCode solutions.

The core idea is differential testing:

1. Read the original problem from `dataset/merged_problems.json`.
2. Ask `gpt-oss:120b` in high reasoning mode to generate one strong test case at a time.
3. Use a trusted Python reference solver to compute the expected answer.
4. Keep only test cases that can be parsed, executed, and verified by the reference solver.
5. Reuse the existing `validate/` Docker execution layer to run generated solutions across languages.
6. Write CSV reports showing whether each language passes the generated validation set.

The module should produce higher-confidence validation than fixed examples alone, especially for boundary cases, tricky constraints, and model-generated edge cases.

The defining design principle is controlled AI: the model is used for targeted test-case discovery, not for final truth. ReAct-style reasoning helps the model propose one purposeful candidate at a time, while deterministic local validation decides whether the candidate is allowed into the retained case set.

## 2. Non-Goals

- Do not call the solution generator.
- Do not modify solution Markdown files.
- Do not replace `validate/`; reuse it as the final multi-language execution layer.
- Do not keep AI-generated test cases unless the reference solver confirms they are runnable and valid.
- Do not use extremely expensive brute force. A reference solution should finish a single generated case quickly, with the full validation for one problem staying within a practical runtime budget.

## 3. Inputs

### Dataset

Primary source:

```text
dataset/merged_problems.json
```

Each problem record provides:

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

### Existing Solutions

Generated solution Markdown files live under:

```text
Leetcode-Easy/
Leetcode-Medium/
Leetcode-Hard/
```

### Existing Validation Layer

The existing validator lives under:

```text
validate/
```

`validate-pro/` should produce validated test cases in a format that can be consumed by a Docker-based runner derived from the current `validate/` architecture.

## 4. Controlled AI Design

`validate-pro/` should present the LLM as a constrained test designer inside a deterministic verification loop.

The control loop is:

```text
Problem context -> ReAct case proposal -> JSON parser -> schema checker
-> constraint checker -> Python reference solver -> normalization
-> retained case store -> Docker multi-language runner -> CSV report
```

The LLM can:

- identify uncovered edge conditions;
- propose one candidate input;
- explain the intended testing purpose inside a structured field;
- suggest an expected output.

The LLM cannot:

- directly decide that a case is correct;
- write into the retained case store without local verification;
- bypass constraint checks;
- bypass reference-solver comparison;
- modify generated solution Markdown.

This makes the system AI-assisted but locally controlled. The retained test set is not a raw model transcript; it is a verified artifact produced by combining model exploration with deterministic reference execution.

## 5. Outputs

### Generated Test Case Store

Validated generated cases should be written under:

```text
Leetcode-QC/validate-pro/cases/
```

Suggested layout:

```text
Leetcode-QC/validate-pro/cases/
  0001-two-sum.json
  0002-add-two-numbers.json
  0020-valid-parentheses.json
```

Each case file should contain:

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

### CSV Reports

The final report format should match the current `validate/` style:

```text
Leetcode-QC/validate-pro/reports/easy.csv
Leetcode-QC/validate-pro/reports/medium.csv
Leetcode-QC/validate-pro/reports/hard.csv
```

Each CSV row is a problem. Each language column is:

```text
1 = passed all retained generated cases
0 = did not pass all retained generated cases
```

### Audit Reports

Validate Pro should also write Markdown audit reports:

```text
Leetcode-QC/validate-pro/reports/adapter_support.md
Leetcode-QC/validate-pro/reports/generation_audit.md
```

`adapter_support.md` lists every problem-shape kind discovered in the selected dataset and whether a Python reference adapter exists. `generation_audit.md` summarizes retained cases, unsupported kinds, rejected candidate reasons, and detailed failures.

## 6. High-Level Pipeline

### Step 1: Load Problem

For each selected problem:

1. Load its full dataset record.
2. Extract description, examples, constraints, topics, hints, and starter signatures.
3. Infer the callable method name and argument structure from `code_snippets`.

### Step 2: Build Reference Solver

For each supported problem shape, provide a trusted Python reference solver.

Reference solvers may use:

- simple brute force,
- Python standard library,
- direct simulation,
- exhaustive enumeration for small generated inputs,
- straightforward dynamic programming,
- known mathematically correct formulas.

Reference solvers must not use unrealistic runtime. A single generated case should be fast enough for repeated validation. As a practical rule, avoid any reference method that can run for minutes on one case.

Examples:

- `Two Sum`: brute force all pairs.
- `Valid Parentheses`: stack simulation.
- `Merge Two Sorted Lists`: convert lists to arrays, merge arrays, rebuild list.
- `Best Time to Buy and Sell Stock`: brute force all buy/sell pairs for small arrays or linear scan.
- SQL/Shell/Pandas problems: separate reference strategy, not mixed with algorithm runners.

### Step 3: Generate One Candidate Case

Call `gpt-oss:120b` with high reasoning mode and ask for exactly one candidate test case.

The prompt should include:

- full original problem statement,
- constraints,
- examples,
- topics,
- starter signatures,
- existing accepted example format,
- target JSON schema,
- request for a specific testing purpose.

The generator should use a ReAct-style planning format internally:

1. identify one untested behavior,
2. propose input,
3. reason why it is valid,
4. output strict JSON only in the final answer.

The stored final output must be machine-readable JSON. Any explanatory text outside the JSON should make the candidate invalid.

### Step 4: Validate Candidate Case

For each candidate:

1. Parse JSON.
2. Check required keys.
3. Check input types match the inferred function signature.
4. Check constraints.
5. Run the Python reference solver.
6. Compare the reference result with the candidate expected value if the model supplied one.
7. Normalize output where needed, such as unordered index pairs or equivalent answer sets.

Only retain cases that pass all checks.

If the AI generates an invalid, ambiguous, too-large, or non-runnable case, discard it and request another candidate.

### Step 5: Build Case Set

For each problem, retain a balanced set of cases.

The set should include:

- original dataset examples,
- minimum-size inputs,
- maximum small safe inputs,
- duplicate values,
- negative values where allowed,
- empty inputs where allowed,
- single-element inputs,
- all-equal inputs,
- sorted inputs,
- reverse-sorted inputs,
- cases with multiple valid answers when the problem allows them,
- cases targeting each major topic or constraint.

Coverage should be explicit, not accidental. Each retained case should have a `purpose` string that maps to a coverage category such as:

| Category | Examples |
| --- | --- |
| Minimum size | Empty list when allowed, single node, one-character string, one-row matrix |
| Small exhaustive | Array length small enough for brute force, short strings covering all character classes |
| Boundary values | Minimum and maximum numeric values allowed by constraints |
| Duplicates | All equal values, repeated keys, repeated characters, repeated rows |
| Sign handling | Negative-only, positive-only, mixed sign, zero-heavy inputs |
| Ordering | Already sorted, reverse sorted, nearly sorted, cyclic order |
| Shape | Skewed tree, balanced tree, disconnected graph, single-cell grid |
| Ambiguity | Multiple valid answers, answer order does not matter, set-like outputs |
| Failure path | No match, impossible target, empty result, false boolean answer |
| Stress within budget | Largest input that still keeps the reference solver comfortably fast |

Suggested defaults:

```text
min_cases_per_problem = 10
max_cases_per_problem = 50
max_generation_attempts_per_case = 5
```

### Step 6: Run Multi-Language Validation

After cases are retained, run generated solution Markdown through a Docker-based validation layer.

The execution layer should reuse the design from `validate/`:

- parse Markdown language sections,
- generate language-specific harness code,
- compile or run code,
- compare output against retained expected answers,
- write per-difficulty CSV matrices.

## 7. GPT-OSS Prompt Requirements

The test case generation prompt must contain enough context to make the model behave like a careful test designer.

Required prompt sections:

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

The prompt should instruct the model:

- generate exactly one case;
- keep the input within constraints;
- prefer a case that tests a specific edge condition;
- avoid huge inputs;
- avoid random noise without purpose;
- output strict JSON only;
- include a short `purpose` field inside the JSON.

Example final JSON shape:

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

## 8. Example Case Generation Strategies

This module should include concrete generation strategies by problem shape. The model prompt should request one of these strategies at a time, and the reference adapter should verify the candidate before storing it.

### Array Search

Example problem shapes:

- `Two Sum`
- `Contains Duplicate`
- `Search Insert Position`

Candidate purposes:

- pair at both ends of the array;
- pair using negative and positive values;
- duplicate values that are not part of the answer;
- smallest valid array;
- multiple possible pairs when the problem permits any valid answer;
- target absent for problems that return insertion position or boolean false.

### String and Stack

Example problem shapes:

- `Valid Parentheses`
- `Longest Common Prefix`
- `Valid Palindrome`

Candidate purposes:

- empty string when allowed;
- one-character string;
- nested structures;
- adjacent structures;
- early mismatch;
- late mismatch;
- non-letter characters when the original problem allows them;
- case-insensitive comparisons where required.

### Linked List

Example problem shapes:

- `Add Two Numbers`
- `Merge Two Sorted Lists`
- `Remove Duplicates from Sorted List`

Candidate purposes:

- empty list;
- one empty list and one non-empty list;
- carry propagation across all digits;
- duplicate runs of different lengths;
- all nodes from one list before the other;
- alternating merge order.

### Tree

Example problem shapes:

- `Maximum Depth of Binary Tree`
- `Same Tree`
- `Symmetric Tree`

Candidate purposes:

- empty tree;
- single node;
- fully skewed tree;
- balanced tree;
- same values but different structure;
- mirror structure with one deep mismatch.

### Graph and Grid

Example problem shapes:

- `Number of Islands`
- `Flood Fill`
- `Course Schedule`

Candidate purposes:

- single-cell grid;
- all water or all land;
- diagonal adjacency that should not count;
- disconnected components;
- cycle in dependency graph;
- long chain without cycle.

### Dynamic Programming

Example problem shapes:

- `Climbing Stairs`
- `House Robber`
- `Maximum Subarray`

Candidate purposes:

- minimum `n`;
- repeated equal values;
- all negative values when allowed;
- local optimum differs from global optimum;
- alternating high and low values;
- input size near safe reference-solver limit.

### SQL, Shell, and Pandas

These should use separate adapters instead of ordinary algorithm adapters.

Candidate purposes:

- empty table;
- duplicate rows;
- null values;
- ties in ranking;
- missing join partner;
- single-line file;
- file with trailing newline;
- mixed whitespace.

The expected answer for these problems should be computed by a controlled local evaluator such as SQLite, pandas, or a temporary shell fixture, depending on the problem type.

## 9. Candidate Rejection Rules

Reject a generated case when:

- JSON cannot be parsed.
- Required input keys are missing.
- Input types do not match the function signature.
- It violates problem constraints.
- It is too large for the reference solver budget.
- It is too expensive for the Docker language runner budget.
- It is ambiguous and the problem does not allow multiple outputs.
- Expected output disagrees with the reference solver after normalization.
- It relies on hidden assumptions not present in the original problem.
- It is only a duplicate of an already retained case.
- It covers the same purpose as an existing retained case without adding new behavior.
- It cannot be serialized into the retained JSON format.

## 10. Reference Solver Requirements

Each reference solver should expose:

```python
def solve(case_input: dict) -> object:
    ...
```

Each problem adapter should also expose:

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

This separation matters because some LeetCode problems allow multiple valid outputs.

Example:

- `Two Sum` can accept either `[0, 1]` or `[1, 0]` depending on normalization.
- Problems returning sets or paths may need sorted normalization.
- Floating-point problems need tolerance.

Reference solvers should also expose a safe input budget, for example:

```python
MAX_N = 30
MAX_GRID_CELLS = 400
MAX_TREE_NODES = 200
```

The budget should be adapter-specific. A brute-force reference may choose a smaller maximum than a linear reference. This keeps generated cases useful without allowing a single case to dominate runtime.

## 11. Directory Design

Suggested structure:

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

`cases/`, `reports/`, and `work/` should be ignored by Git because they are generated artifacts.

`tests/unit/` should contain all unit tests for this module. The validate-pro test suite should cover dataset parsing, prompt construction, candidate JSON parsing, reference solver adapters, candidate rejection rules, retained-case persistence, CSV report generation, audit report generation, and CLI argument parsing.

`tests/integration/` should cover a tiny fixture dataset and verify that no-LLM generation can retain dataset examples and write audit reports.

`tests/smoke/` should cover command-line parser defaults and cheap startup behavior.

## 12. CLI Design

Generate cases for one problem:

```bash
python Leetcode-QC/validate-pro/generate_cases.py --frontend-id 1
```

Generate cases for selected problems:

```bash
python Leetcode-QC/validate-pro/generate_cases.py --frontend-ids 1 2 20 121
```

Generate cases for one difficulty:

```bash
python Leetcode-QC/validate-pro/generate_cases.py --difficulty Easy
```

Run validation using retained cases:

```bash
python Leetcode-QC/validate-pro/run_validation.py
```

Docker entry:

```bash
docker compose -f Leetcode-QC/validate-pro/compose.yaml build
docker compose -f Leetcode-QC/validate-pro/compose.yaml run --rm validate-pro
```

## 13. Runtime Controls

Recommended controls:

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

Generation should be resumable:

- If a retained case file already exists, read it first.
- Generate only missing cases.
- Never overwrite retained cases unless explicitly requested.
- Track attempted purposes to avoid repeatedly asking for the same style of case.
- Stop generation when the configured token budget or case budget is reached.

## 14. Safety and Reliability

The system should treat the LLM as an untrusted test-case proposer.

The Python reference solver is the authority. A case only becomes part of the validation set after deterministic local verification.

The ReAct trace is useful for exploration, but it is not trusted output. Only strict JSON from the final answer should enter the parser, and only reference-verified JSON should enter `Leetcode-QC/validate-pro/cases/`.

The Docker runner should:

- use timeouts,
- isolate generated harness files in a work directory,
- return `0` in CSV for compile/runtime failures,
- avoid modifying solution Markdown,
- keep generated reports under ignored directories.

## 15. Relationship With Existing Tools

Existing tools:

```text
migrate/audit_missing_solutions.py
migrate/audit_suspicious_solutions.py
validate/run_validation.py
```

Suggested workflow:

1. Use missing audit to find incomplete Markdown.
2. Use suspicious audit to find abnormal generated code.
3. Use `validate/` for dataset example validation.
4. Use `validate-pro/` for generated edge-case validation.
5. Repair failed solutions by rerunning generation, applying mechanical migrations, or editing specific Markdown code blocks.

## 16. Success Criteria

The first usable version should:

- read problems from `dataset/merged_problems.json`;
- support at least several common algorithm shapes;
- generate candidate cases with `gpt-oss:120b` high reasoning mode;
- use a controlled AI loop where ReAct proposes candidates and local deterministic checks decide retention;
- reject invalid AI cases automatically;
- retain only reference-verified cases;
- retain purpose-labeled cases across boundary, duplicate, ordering, ambiguity, and stress-within-budget categories;
- run generated Markdown solutions in Docker;
- write `easy.csv`, `medium.csv`, and `hard.csv`;
- keep all generated case and report artifacts out of Git;
- include a `validate-pro/tests/unit/` unittest suite for the module's parser, adapter, generation, retention, report, and CLI behavior;
- preserve the current `validate/` module as the simpler baseline validator.
