# 1050. Actors and Directors Who Cooperated At Least Three Times

## MySQL
```sql
SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(*) >= 3;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT
    actor_id,
    director_id
FROM
    ActorDirector
GROUP BY
    actor_id,
    director_id
HAVING
    COUNT(*) >= 3;
```

## OracleSQL
```sql
SELECT actor_id,
       director_id
FROM   ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(*) >= 3;
```

## PythonData
```python
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    cnt = (
        actor_director
        .groupby(['actor_id', 'director_id'])
        .size()
        .reset_index(name='cnt')
    )
    result = cnt[cnt['cnt'] >= 3][['actor_id', 'director_id']]
    return result.reset_index(drop=True)
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT
    actor_id,
    director_id
FROM
    ActorDirector
GROUP BY
    actor_id,
    director_id
HAVING
    COUNT(*) >= 3;
```
