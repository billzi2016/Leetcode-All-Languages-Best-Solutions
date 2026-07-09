# 3465. Find Products with Valid Serial Numbers

## MySQL
```sql
# Write your MySQL query statement below
SELECT product_id, product_name, description
FROM products
WHERE description REGEXP 'SN[0-9]{4}-[0-9]{4}'
ORDER BY product_id;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT
    product_id,
    product_name,
    description
FROM products
WHERE description LIKE '%SN[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]%'
  AND description NOT LIKE '%SN[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][0-9]%'
ORDER BY product_id;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT product_id,
       product_name,
       description
FROM   products
WHERE  REGEXP_LIKE(description, 'SN[0-9]{4}-[0-9]{4}')
ORDER BY product_id;
```

## PythonData
```python
import pandas as pd

def find_valid_serial_products(products: pd.DataFrame) -> pd.DataFrame:
    mask = products["description"].str.contains(r"SN\d{4}-\d{4}", na=False)
    return products.loc[mask].sort_values("product_id").reset_index(drop=True)
```

## PostgreSQL
```sql
SELECT product_id, product_name, description
FROM products
WHERE description ~ 'SN[0-9]{4}-[0-9]{4}'
ORDER BY product_id;
```
