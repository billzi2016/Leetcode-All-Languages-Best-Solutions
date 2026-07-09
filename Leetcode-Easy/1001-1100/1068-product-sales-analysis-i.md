# 1068. Product Sales Analysis I

## MySQL
```sql
SELECT p.product_name, s.year, s.price
FROM Sales s
JOIN Product p ON s.product_id = p.product_id;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT
    p.product_name,
    s.year,
    s.price
FROM
    Sales AS s
JOIN
    Product AS p
ON
    s.product_id = p.product_id;
```

## OracleSQL
```sql
SELECT p.product_name,
       s.year,
       s.price
FROM   Sales s
JOIN   Product p
ON     s.product_id = p.product_id;
```

## PythonData
```python
import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    merged = sales.merge(product, on="product_id", how="inner")
    return merged[["product_name", "year", "price"]]
```

## PostgreSQL
```sql
SELECT p.product_name, s.year, s.price
FROM Sales s
JOIN Product p ON s.product_id = p.product_id;
```
