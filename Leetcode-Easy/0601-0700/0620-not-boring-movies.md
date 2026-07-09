# 0620. Not Boring Movies

## MySQL
```sql
SELECT *
FROM Cinema
WHERE id % 2 = 1
  AND description <> 'boring'
ORDER BY rating DESC;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT *
FROM Cinema
WHERE id % 2 = 1
  AND description <> 'boring'
ORDER BY rating DESC;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT *
FROM Cinema
WHERE MOD(id, 2) = 1
  AND description <> 'boring'
ORDER BY rating DESC;
```

## PythonData
```python
import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    filtered = cinema[(cinema['id'] % 2 == 1) & (cinema['description'] != 'boring')]
    return filtered.sort_values(by='rating', ascending=False)
```

## PostgreSQL
```sql
SELECT *
FROM Cinema
WHERE id % 2 = 1
  AND description <> 'boring'
ORDER BY rating DESC;
```
