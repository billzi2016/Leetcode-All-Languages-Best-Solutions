# 1757. Recyclable and Low Fat Products

## MySQL
```sql
SELECT
    product_id
FROM
    Products
WHERE
    low_fats = 'Y' AND recyclable = 'Y';
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';
```

## PythonData
```python
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[(products["low_fats"] == "Y") & (products["recyclable"] == "Y")][["product_id"]]
```

## PostgreSQL
```sql
SELECT
    product_id
FROM
    Products
WHERE
    low_fats = 'Y' AND recyclable = 'Y';
```
