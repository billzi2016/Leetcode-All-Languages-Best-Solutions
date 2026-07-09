# 1164. Product Price at a Given Date

## MySQL
```sql
# Write your MySQL query statement below
SELECT 
    p.product_id,
    COALESCE(
        (SELECT new_price 
         FROM Products 
         WHERE product_id = p.product_id AND change_date <= '2019-08-16'
         ORDER BY change_date DESC LIMIT 1),
        10) AS price
FROM (SELECT DISTINCT product_id FROM Products) p;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT p.product_id,
       ISNULL(pc.new_price, 10) AS price
FROM (SELECT DISTINCT product_id FROM Products) p
LEFT JOIN (
    SELECT pr.product_id, pr.new_price
    FROM Products pr
    INNER JOIN (
        SELECT product_id, MAX(change_date) AS max_change
        FROM Products
        WHERE change_date <= '2019-08-16'
        GROUP BY product_id
    ) mx ON pr.product_id = mx.product_id AND pr.change_date = mx.max_change
) pc ON p.product_id = pc.product_id;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT p.product_id,
       COALESCE(l.new_price, 10) AS price
FROM (SELECT DISTINCT product_id FROM Products) p
LEFT JOIN (
    SELECT product_id, new_price
    FROM (
        SELECT product_id,
               new_price,
               ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY change_date DESC) rn
        FROM Products
        WHERE change_date <= DATE '2019-08-16'
    )
    WHERE rn = 1
) l ON p.product_id = l.product_id;
```

## PythonData
```python
import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    target = pd.Timestamp('2019-08-16')
    # Ensure proper datetime type
    if products['change_date'].dtype != 'datetime64[ns]':
        products = products.copy()
        products['change_date'] = pd.to_datetime(products['change_date'])
    
    # Latest price change on or before target date per product
    filtered = products[products['change_date'] <= target]
    latest = (
        filtered.sort_values(['product_id', 'change_date'], ascending=[True, False])
               .drop_duplicates('product_id')[['product_id', 'new_price']]
    )
    
    # All distinct products (including those without any change before target)
    all_products = pd.DataFrame({'product_id': products['product_id'].unique()})
    
    result = all_products.merge(latest, on='product_id', how='left')
    result['price'] = result['new_price'].fillna(10).astype(int)
    return result[['product_id', 'price']]
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
WITH last_change AS (
    SELECT product_id, new_price
    FROM Products
    WHERE (product_id, change_date) IN (
        SELECT product_id, MAX(change_date) AS max_date
        FROM Products
        WHERE change_date <= DATE '2019-08-16'
        GROUP BY product_id
    )
)
SELECT p.product_id,
       COALESCE(lc.new_price, 10) AS price
FROM (SELECT DISTINCT product_id FROM Products) p
LEFT JOIN last_change lc USING (product_id);
```
