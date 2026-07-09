# 0586. Customer Placing the Largest Number of Orders

## MySQL
```sql
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT TOP (1) WITH TIES
    customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT customer_number
FROM (
    SELECT customer_number, COUNT(*) AS cnt
    FROM Orders
    GROUP BY customer_number
    ORDER BY cnt DESC
)
WHERE ROWNUM = 1;
```

## PythonData
```python
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # Count orders per customer
    cnt = orders.groupby('customer_number', as_index=False).size()
    max_cnt = cnt['size'].max()
    result = cnt[cnt['size'] == max_cnt][['customer_number']]
    return result.reset_index(drop=True)
```

## PostgreSQL
```sql
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;
```
