# 题目清单

生成出来的题目清单位于仓库根目录的难度目录中。文档站点通过 symlink 把它们暴露为 MkDocs 页面，所以不会把很长的表格复制到 `docs-site/`。

| 难度 | 英文清单 | 中文清单 |
| --- | --- | --- |
| Easy | [Easy index](../en/solution-indexes/easy/index.md) | [Easy 中文清单](solution-indexes/easy/index.md) |
| Medium | [Medium index](../en/solution-indexes/medium/index.md) | [Medium 中文清单](solution-indexes/medium/index.md) |
| Hard | [Hard index](../en/solution-indexes/hard/index.md) | [Hard 中文清单](solution-indexes/hard/index.md) |

重新生成这些文件：

```bash
PYTHONPATH=src python scripts/generate_difficulty_readmes.py
```

这些清单复用题解生成器的输出路径规则，包括 `0001-0100` 这种固定宽度分桶目录。
