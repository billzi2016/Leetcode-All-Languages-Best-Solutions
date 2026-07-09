# 0607. Sales Person

## MySQL
```sql
# Write your MySQL query statement below
SELECT sp.name
FROM SalesPerson AS sp
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders o
    JOIN Company c ON o.com_id = c.com_id
    WHERE o.sales_id = sp.sales_id
      AND c.name = 'RED'
);
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT s.name
FROM SalesPerson AS s
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders o
    JOIN Company c ON o.com_id = c.com_id
    WHERE o.sales_id = s.sales_id
      AND c.name = 'RED'
);
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT s.name
FROM SalesPerson s
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders o
    JOIN Company c ON o.com_id = c.com_id
    WHERE o.sales_id = s.sales_id
      AND c.name = 'RED'
);
```

## PythonData
```python
import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red_com_ids = company.loc[company['name'] == 'RED', 'com_id']
    red_sales_ids = orders.loc[orders['com_id'].isin(red_com_ids), 'sales_id'].unique()
    result = sales_person.loc[~sales_person['sales_id'].isin(red_sales_ids), ['name']]
    return result.reset_index(drop=True)
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT s.name
FROM SalesPerson s
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders o
    JOIN Company c ON o.com_id = c.com_id
    WHERE o.sales_id = s.sales_id AND c.name = 'RED'
);
```
