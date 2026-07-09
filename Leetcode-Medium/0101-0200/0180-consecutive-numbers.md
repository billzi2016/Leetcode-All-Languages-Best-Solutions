# 0180. Consecutive Numbers

## MySQL
```sql
# Write your MySQL query statement below
SELECT DISTINCT
    l1.num AS ConsecutiveNums
FROM
    Logs l1,
    Logs l2,
    Logs l3
WHERE
    l1.id = l2.id - 1
    AND l2.id = l3.id - 1
    AND l1.num = l2.num
    AND l2.num = l3.num;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT DISTINCT l1.Num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2 ON l2.Id = l1.Id + 1
JOIN Logs l3 ON l3.Id = l2.Id + 1
WHERE l1.Num = l2.Num
  AND l2.Num = l3.Num;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2 ON l2.id = l1.id + 1
JOIN Logs l3 ON l3.id = l2.id + 1
WHERE l1.num = l2.num
  AND l2.num = l3.num;
```

## PythonData
```python
import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    df = logs.sort_values('id')
    mask = (df['num'] == df['num'].shift(1)) & (df['num'] == df['num'].shift(2))
    result = df.loc[mask, ['num']].drop_duplicates().rename(columns={'num': 'ConsecutiveNums'})
    return result
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT DISTINCT
    l1.num AS ConsecutiveNums
FROM
    Logs l1
JOIN Logs l2 ON l2.id = l1.id + 1
JOIN Logs l3 ON l3.id = l2.id + 1
WHERE
    l1.num = l2.num
    AND l2.num = l3.num;
```
