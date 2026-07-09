# 0601. Human Traffic of Stadium

## MySQL
```sql
# Write your MySQL query statement below
WITH filtered AS (
    SELECT id, visit_date, people,
           ROW_NUMBER() OVER (ORDER BY id) AS rn
    FROM Stadium
    WHERE people >= 100
),
grp AS (
    SELECT id, visit_date, people,
           (id - rn) AS island
    FROM filtered
)
SELECT id, visit_date, people
FROM grp
WHERE island IN (
    SELECT island FROM grp GROUP BY island HAVING COUNT(*) >= 3
)
ORDER BY visit_date;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
WITH filtered AS (
    SELECT id, visit_date, people,
           ROW_NUMBER() OVER (ORDER BY id) AS rn
    FROM Stadium
    WHERE people >= 100
),
grouped AS (
    SELECT *,
           id - rn AS grp
    FROM filtered
)
SELECT id, visit_date, people
FROM grouped
WHERE grp IN (
    SELECT grp
    FROM grouped
    GROUP BY grp
    HAVING COUNT(*) >= 3
)
ORDER BY visit_date;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
WITH filtered AS (
    SELECT id,
           visit_date,
           people,
           ROW_NUMBER() OVER (ORDER BY id) rn
    FROM Stadium
    WHERE people >= 100
),
islands AS (
    SELECT id,
           visit_date,
           people,
           (id - rn) AS island
    FROM filtered
)
SELECT id,
       visit_date,
       people
FROM islands
WHERE island IN (
    SELECT island
    FROM islands
    GROUP BY island
    HAVING COUNT(*) >= 3
)
ORDER BY visit_date;
```

## PythonData
```python
import pandas as pd
import numpy as np

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    # keep only rows with people >= 100
    df = stadium[stadium['people'] >= 100].copy()
    if df.empty:
        return df.sort_values('visit_date')
    
    # ensure ordering by id to detect consecutive ids
    df = df.sort_values('id').reset_index(drop=True)
    
    # group key: difference between id and its position gives same value for consecutive sequences
    df['_group'] = df['id'] - np.arange(len(df))
    
    # mark groups with size >= 3
    mask = df.groupby('_group')['id'].transform('size') >= 3
    
    result = df.loc[mask, ['id', 'visit_date', 'people']]
    return result.sort_values('visit_date').reset_index(drop=True)
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
WITH qualified AS (
    SELECT *, ROW_NUMBER() OVER (ORDER BY id) AS rn
    FROM Stadium
    WHERE people >= 100
), islands AS (
    SELECT *, (id - rn) AS grp
    FROM qualified
)
SELECT id, visit_date, people
FROM islands
WHERE grp IN (
    SELECT grp
    FROM islands
    GROUP BY grp
    HAVING COUNT(*) >= 3
)
ORDER BY visit_date;
```
