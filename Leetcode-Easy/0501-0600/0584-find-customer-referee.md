# 0584. Find Customer Referee

## MySQL
```sql
# Write your MySQL query statement below
SELECT name
FROM Customer
WHERE referee_id <> 2 OR referee_id IS NULL;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT name
FROM Customer
WHERE referee_id <> 2 OR referee_id IS NULL;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT name
FROM Customer
WHERE referee_id <> 2 OR referee_id IS NULL;
```

## PythonData
```python
import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    mask = (customer["referee_id"] != 2) | customer["referee_id"].isna()
    return customer.loc[mask, ["name"]]
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT name
FROM Customer
WHERE referee_id <> 2 OR referee_id IS NULL;
```
