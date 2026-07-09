# 0178. Rank Scores

## MySQL
```sql
SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores
ORDER BY score DESC;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS rank
FROM Scores
ORDER BY score DESC;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS rank
FROM Scores
ORDER BY score DESC;
```

## PythonData
```python
import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    df = scores.copy()
    df["rank"] = df["score"].rank(method="dense", ascending=False).astype(int)
    result = df.sort_values(by="score", ascending=False)[["score", "rank"]]
    return result.reset_index(drop=True)
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS rank
FROM Scores
ORDER BY score DESC;
```
