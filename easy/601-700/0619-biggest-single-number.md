# 0619. Biggest Single Number

## Mysql

```mysql
SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) AS single_numbers;
```

## Mssql

```mssql
/* Write your T-SQL query statement below */
SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) AS t;
```

## Oraclesql

```oraclesql
/* Write your PL/SQL query statement below */
SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
);
```

## Pythondata

```pythondata
import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    if my_numbers.empty:
        return pd.DataFrame({"num": [None]})
    counts = my_numbers["num"].value_counts()
    singles = counts[counts == 1].index
    if len(singles) == 0:
        return pd.DataFrame({"num": [None]})
    max_single = singles.max()
    return pd.DataFrame({"num": [max_single]})
```

## Postgresql

```postgresql
-- Write your PostgreSQL query statement below
SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) AS single_numbers;
```
