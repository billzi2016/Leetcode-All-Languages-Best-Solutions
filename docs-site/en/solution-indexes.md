# Solution Indexes

The generated problem indexes live in the repository difficulty directories. The documentation site exposes them as MkDocs pages through symlinks, so the long tables are not copied into `docs-site/`.

| Difficulty | English index | Chinese index |
| --- | --- | --- |
| Easy | [Easy index](solution-indexes/easy/index.md) | [Easy 中文清单](../cn/solution-indexes/easy/index.md) |
| Medium | [Medium index](solution-indexes/medium/index.md) | [Medium 中文清单](../cn/solution-indexes/medium/index.md) |
| Hard | [Hard index](solution-indexes/hard/index.md) | [Hard 中文清单](../cn/solution-indexes/hard/index.md) |

Regenerate these files with:

```bash
PYTHONPATH=src python scripts/generate_difficulty_readmes.py
```

The generated rows use the same output path rules as the solution generator, including fixed-width bucket directories such as `0001-0100`.
