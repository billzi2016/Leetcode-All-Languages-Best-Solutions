# 0584. Find Customer Referee

## Mysql

```mysql
# Write your MySQL query statement below
SELECT name
FROM Customer
WHERE referee_id <> 2 OR referee_id IS NULL;
```

## Mssql

```mssql
/* Write your T-SQL query statement below */
SELECT name
FROM Customer
WHERE referee_id <> 2 OR referee_id IS NULL;
```

## Oraclesql

```oraclesql
/* Write your PL/SQL query statement below */
SELECT name
FROM Customer
WHERE referee_id <> 2 OR referee_id IS NULL;
```

## Pythondata

```pythondata
import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    mask = (customer["referee_id"] != 2) | customer["referee_id"].isna()
    return customer.loc[mask, ["name"]]
```

## Postgresql

```postgresql
-- Write your PostgreSQL query statement below
SELECT name
FROM Customer
WHERE referee_id <> 2 OR referee_id IS NULL;
```
