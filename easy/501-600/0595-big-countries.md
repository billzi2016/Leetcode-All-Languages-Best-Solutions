# 0595. Big Countries

## Mysql

```mysql
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

## Mssql

```mssql
/* Write your T-SQL query statement below */
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;
```

## Oraclesql

```oraclesql
/* Write your PL/SQL query statement below */
SELECT name,
       population,
       area
FROM   world
WHERE  area >= 3000000
    OR population >= 25000000;
```

## Pythondata

```pythondata
import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    result = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return result[['name', 'population', 'area']]
```

## Postgresql

```postgresql
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
