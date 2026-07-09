# 0595. Big Countries

## MySQL
```sql
# Write your MySQL query statement below
SELECT
    name,
    population,
    area
FROM
    World
WHERE
    area >= 3000000 OR population >= 25000000;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT name,
       population,
       area
FROM   world
WHERE  area >= 3000000
    OR population >= 25000000;
```

## PythonData
```python
import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    result = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return result[['name', 'population', 'area']]
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT
    name,
    population,
    area
FROM
    World
WHERE
    area >= 3000000 OR population >= 25000000;
```
