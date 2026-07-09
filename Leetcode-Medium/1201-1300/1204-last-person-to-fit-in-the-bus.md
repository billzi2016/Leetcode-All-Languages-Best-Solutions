# 1204. Last Person to Fit in the Bus

## MySQL
```sql
SELECT person_name
FROM (
    SELECT person_name, turn,
           SUM(weight) OVER (ORDER BY turn) AS cum_weight
    FROM Queue
) q
WHERE cum_weight <= 1000
ORDER BY turn DESC
LIMIT 1;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT TOP 1 person_name
FROM (
    SELECT person_name,
           turn,
           SUM(weight) OVER (ORDER BY turn ROWS UNBOUNDED PRECEDING) AS cum_weight
    FROM Queue
) q
WHERE cum_weight <= 1000
ORDER BY turn DESC;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT person_name
FROM (
    SELECT person_name,
           turn,
           SUM(weight) OVER (ORDER BY turn) AS cum_weight
    FROM Queue
)
WHERE cum_weight <= 1000
ORDER BY turn DESC
FETCH FIRST 1 ROW ONLY;
```

## PythonData
```python
import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    df = queue.sort_values('turn').reset_index(drop=True)
    df['cum_weight'] = df['weight'].cumsum()
    fitting = df[df['cum_weight'] <= 1000]
    if fitting.empty:
        return pd.DataFrame(columns=['person_name'])
    last_name = fitting.iloc[-1]['person_name']
    return pd.DataFrame({'person_name': [last_name]})
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT person_name
FROM (
    SELECT person_name,
           SUM(weight) OVER (ORDER BY turn) AS cum_weight,
           turn
    FROM Queue
) q
WHERE cum_weight <= 1000
ORDER BY turn DESC
LIMIT 1;
```
