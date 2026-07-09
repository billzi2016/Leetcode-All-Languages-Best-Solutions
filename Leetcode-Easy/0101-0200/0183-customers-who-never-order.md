# 0183. Customers Who Never Order

## MySQL
```sql
SELECT c.name AS Customers
FROM Customers c
LEFT JOIN Orders o ON c.id = o.customerId
WHERE o.customerId IS NULL;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT c.name AS Customers
FROM Customers c
LEFT JOIN Orders o ON c.id = o.customerId
WHERE o.customerId IS NULL;
```

## OracleSQL
```sql
SELECT name AS Customers
FROM Customers c
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders o
    WHERE o.customerId = c.id
);
```

## PythonData
```python
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    ordered_ids = set(orders["customerId"])
    result = customers[~customers["id"].isin(ordered_ids)][["name"]].copy()
    result.rename(columns={"name": "Customers"}, inplace=True)
    return result
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT c.name AS Customers
FROM Customers c
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders o
    WHERE o.customerId = c.id
);
```
