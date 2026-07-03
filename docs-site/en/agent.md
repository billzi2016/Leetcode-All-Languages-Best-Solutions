# Agent Generation Flow

This page explains how the project generator agent calls Ollama, organizes prompts, uses prompt reuse, and continues after failures.

## Generator Call Chain

```mermaid
sequenceDiagram
    participant Script as generate_solutions.py
    participant Dataset as merged_problems.json
    participant Prompt as Prompt Builder
    participant Client as Python ollama
    participant Server as Ollama Server
    participant File as Markdown Output
    participant Logs as Logs

    Script->>Dataset: Load questions
    Script->>Prompt: Build system / problem / language prompts
    Prompt-->>Script: Return messages
    Script->>Client: chat(model, messages, options)
    Client->>Server: Call local Ollama API
    Server-->>Client: Return target-language code
    Client-->>Script: Return response text
    Script->>File: Write by difficulty and problem range
    Script->>Logs: Record stdout / stderr / failures
```

The generator uses the Python `ollama` package instead of hand-written `requests` calls. The client library already handles Ollama API data structures and response wrapping, so project code can focus on problems, languages, output, and recovery.

## Prompt Boundary

The model receives textual problem data and the target language starter code. It does not receive images. If `solutions` exists, it is included as an editorial-style reference in the shared problem prompt; if missing, it is skipped. The final response must be submit-ready code only: no Markdown fences, no problem restatement, no complexity explanation, and no test harness.

```mermaid
flowchart LR
    A[Problem metadata] --> D[problem_prompt]
    B[description / examples / constraints] --> D
    C[hints / solutions if present] --> D
    E[Target language starter code] --> F[language_prompt]
    D --> G[Ollama messages]
    F --> G
    H[SYSTEM_PROMPT output rules] --> G
    G --> I[Raw code response]
```

## Prompt Layers

```mermaid
flowchart LR
    S[SYSTEM_PROMPT] --> M[Ollama Messages]
    P[problem_prompt] --> M
    L[language_prompt] --> M
    M --> O[Raw LeetCode Code]
```

- `SYSTEM_PROMPT`: global requirements shared by all problems and all languages.
- `problem_prompt`: problem metadata, statement, examples, constraints, hints, and optional editorial reference.
- `language_prompt`: target language plus that language's starter code.

This structure maximizes prompt reuse because only the final language prompt changes when generating another language for the same problem.

## Prompt Examples

The generator sends three Ollama messages in a fixed order:

```python
[
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": problem_prompt},
    {"role": "user", "content": language_prompt},
]
```

`SYSTEM_PROMPT` stores global rules and is identical for every problem and language. It constrains the model to submit-ready code only:

```text
You are a senior algorithm engineer and LeetCode solution generator.
Generate only the optimal accepted solution for the requested target language.
Use the provided LeetCode starter code signature and style exactly.
Return raw code only. Do not wrap the answer in Markdown code fences.
Do not include the problem statement, explanations, complexity analysis, tests,
main functions, extra I/O, pseudocode, or unsupported dependencies.
```

`problem_prompt` stores context shared by every language for the same problem. For LeetCode 1, the shape is roughly:

```text
# Problem Context

## Problem Metadata
- title: Two Sum
- problem_id: 1
- frontend_id: 1
- difficulty: Easy
- problem_slug: two-sum
- topics: Array, Hash Table

## Problem Statement
Given an array of integers nums and an integer target...

## Examples
- example_num: 1
- example_text: Input: nums = [2,7,11,15], target = 9 ...

## Constraints
- 2 <= nums.length <= 10^4

## Editorial / Solution Reference
Hash map based one-pass lookup...
```

`language_prompt` contains only the target language and starter code. For Python3:

```text
Target Language: python3

Use this LeetCode starter code signature and style:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pass

Generate the optimal accepted solution for this language.
Return raw code only. Do not wrap the answer in Markdown code fences.
```

The output must preserve the LeetCode submission entry point, such as `class Solution` and `def twoSum(...)`. For Rust, Elixir, and Racket, the same rule applies to `impl Solution`, `defmodule Solution do`, and `define/contract`.

## Prompt Cache and Reuse

The cache idea here is not a hand-written key-value cache in the repository. It is about making the model server's input prefix as stable as possible. During LLM inference, stable long prefixes are easier for the serving layer to reuse. This project has two stable prefixes:

1. `SYSTEM_PROMPT`: identical across every problem and language.
2. `problem_prompt`: identical across every language for the same problem.

When generating many languages for one problem, requests look like this:

```text
Language 1: SYSTEM_PROMPT + problem_prompt(0001) + language_prompt(python3)
Language 2: SYSTEM_PROMPT + problem_prompt(0001) + language_prompt(cpp)
Language 3: SYSTEM_PROMPT + problem_prompt(0001) + language_prompt(java)
```

The first two layers stay unchanged; only the final language layer changes. This is more cache-friendly than mixing rules, problem data, and language requirements into a newly formatted prompt every time. It also makes debugging easier: if only one language fails for a problem, the likely issue is that language's starter code or output, not the shared problem prompt.

When the problem changes, `problem_prompt` changes, but `SYSTEM_PROMPT` remains stable:

```text
Problem 1: SYSTEM_PROMPT + problem_prompt(0001) + language_prompt(...)
Problem 2: SYSTEM_PROMPT + problem_prompt(0002) + language_prompt(...)
Problem 4: SYSTEM_PROMPT + problem_prompt(0004) + language_prompt(...)
```

This is why global rules belong in the system prompt, problem data belongs in the shared problem prompt, and language-specific differences should stay compressed in the language prompt.

## Failure Behavior

Each language can retry up to three times. After the retry limit, the failure is logged and generation continues with the next unit of work.

Non-blocking failure handling is intentional. A full run can take a long time, and one language, one problem, or one model timeout should not stop the entire batch. Failed units record the frontend id, slug, language, retry count, and error message so later runs can target only the missing work.

