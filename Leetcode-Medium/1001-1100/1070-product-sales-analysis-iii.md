# 1070. Product Sales Analysis III

## MySQL
```sql
# Write your MySQL query statement below
SELECT 
    s.product_id,
    s.year AS first_year,
    s.quantity,
    s.price
FROM Sales s
WHERE (s.product_id, s.year) IN (
    SELECT product_id, MIN(year)
    FROM Sales
    GROUP BY product_id
);
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT 
    s.product_id,
    s.year AS first_year,
    s.quantity,
    s.price
FROM 
    Sales s
WHERE 
    s.year = (
        SELECT MIN(year)
        FROM Sales
        WHERE product_id = s.product_id
    );
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT
    s.product_id,
    s.year AS first_year,
    s.quantity,
    s.price
FROM Sales s
JOIN (
    SELECT product_id, MIN(year) AS min_year
    FROM Sales
    GROUP BY product_id
) t
ON s.product_id = t.product_id AND s.year = t.min_year;
```

## PythonData
```python
import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    # Find the first year each product was sold
    first_year = sales.groupby('product_id', as_index=False)['year'].min()
    # Merge to bring the first year alongside original rows
    merged = sales.merge(first_year, on='product_id')
    # Keep only rows where the sale year matches the first year
    filtered = merged[merged['year_x'] == merged['year_y']]
    # Rename and select required columns
    result = (
        filtered.rename(columns={'year_x': 'first_year'})
               .loc[:, ['product_id', 'first_year', 'quantity', 'price']]
    )
    return result
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT s.product_id,
       s.year AS first_year,
       s.quantity,
       s.price
FROM Sales s
WHERE (s.product_id, s.year) IN (
    SELECT product_id, MIN(year)
    FROM Sales
    GROUP BY product_id
);
```
