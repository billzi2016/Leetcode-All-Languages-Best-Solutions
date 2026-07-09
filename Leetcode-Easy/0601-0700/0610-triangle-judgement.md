# 0610. Triangle Judgement

## MySQL
```sql
SELECT
    x,
    y,
    z,
    CASE
        WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT
    x,
    y,
    z,
    CASE 
        WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle;
```

## OracleSQL
```sql
SELECT
    x,
    y,
    z,
    CASE
        WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle;
```

## PythonData
```python
import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    cond = (
        (triangle['x'] + triangle['y'] > triangle['z']) &
        (triangle['x'] + triangle['z'] > triangle['y']) &
        (triangle['y'] + triangle['z'] > triangle['x'])
    )
    result = triangle.copy()
    result['triangle'] = cond.map({True: 'Yes', False: 'No'})
    return result
```

## PostgreSQL
```sql
SELECT
    x,
    y,
    z,
    CASE
        WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle;
```
