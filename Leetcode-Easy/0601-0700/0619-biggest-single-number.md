# 0619. Biggest Single Number

## MySQL
```sql
SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) AS single_numbers;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) AS t;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
);
```

## PythonData
```python
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

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) AS single_numbers;
```
