# LeetCode All Languages Best Solutions

Accurate best solutions for LeetCode problems across all supported programming languages.

This documentation site is available in English and Chinese.

GitHub repository:

- [billzi2016/Leetcode-All-Languages-Best-Solutions](https://github.com/billzi2016/Leetcode-All-Languages-Best-Solutions)

## Solution Indexes

The generated problem indexes live in the repository difficulty directories. The documentation site exposes them as MkDocs pages through symlinks, so the long tables are not copied into `docs-site/`.

| Difficulty | English index | Chinese index |
| --- | --- | --- |
| Easy | [Easy index](en/solution-indexes/easy/index.md) | [Easy 中文清单](cn/solution-indexes/easy/index.md) |
| Medium | [Medium index](en/solution-indexes/medium/index.md) | [Medium 中文清单](cn/solution-indexes/medium/index.md) |
| Hard | [Hard index](en/solution-indexes/hard/index.md) | [Hard 中文清单](cn/solution-indexes/hard/index.md) |

Regenerate these files with:

```bash
PYTHONPATH=src python scripts/generate_difficulty_readmes.py
```

The generated rows use the same output path rules as the solution generator, including fixed-width bucket directories such as `0001-0100`.

For dataset and generation details, see [LeetCode](en/leetcode.md).

数据集和生成流程说明见 [LeetCode](cn/leetcode.md)。

## Language

- [English](en/index.md)
- [中文](cn/index.md)
