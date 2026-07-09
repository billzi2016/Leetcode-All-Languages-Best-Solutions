# 0511. Game Play Analysis I

## MySQL
```sql
SELECT
    player_id,
    MIN(event_date) AS first_login
FROM
    Activity
GROUP BY
    player_id;
```

## MSSQL
```sql
/* Write your T‑SQL query statement below */
SELECT
    player_id,
    MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT
    player_id,
    MIN(event_date) AS first_login
FROM
    Activity
GROUP BY
    player_id;
```

## PythonData
```python
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    result = activity.groupby('player_id', as_index=False)['event_date'].min()
    result.rename(columns={'event_date': 'first_login'}, inplace=True)
    return result
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT
    player_id,
    MIN(event_date) AS first_login
FROM
    Activity
GROUP BY
    player_id;
```
