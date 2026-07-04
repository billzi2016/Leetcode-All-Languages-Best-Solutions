# 0586. Customer Placing the Largest Number of Orders

## Mysql

```mysql
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;
```

## Mssql

```mssql
/* Write your T-SQL query statement below */
SELECT TOP (1) WITH TIES
    customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC;
```

## Oraclesql

```oraclesql
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

## Pythondata

```pythondata
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # Count orders per customer
    cnt = orders.groupby('customer_number', as_index=False).size()
    max_cnt = cnt['size'].max()
    result = cnt[cnt['size'] == max_cnt][['customer_number']]
    return result.reset_index(drop=True)
```

## Postgresql

```postgresql
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;
```
