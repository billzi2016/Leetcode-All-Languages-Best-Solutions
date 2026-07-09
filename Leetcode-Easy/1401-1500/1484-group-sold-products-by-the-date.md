# 1484. Group Sold Products By The Date

## MySQL
```sql
SELECT
    sell_date,
    COUNT(DISTINCT product) AS num_sold,
    GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',') AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT
    sell_date,
    COUNT(DISTINCT product) AS num_sold,
    STRING_AGG(product, ',') WITHIN GROUP (ORDER BY product) AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;
```

## OracleSQL
```sql
SELECT
    sell_date,
    COUNT(*) AS num_sold,
    LISTAGG(product, ',') WITHIN GROUP (ORDER BY product) AS products
FROM (
    SELECT DISTINCT sell_date, product
    FROM Activities
)
GROUP BY sell_date
ORDER BY sell_date;
```

## PythonData
```python
import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    # Aggregate distinct products per date, sort them lexicographically
    agg = activities.groupby('sell_date').agg(
        prod_list=('product', lambda x: sorted(set(x)))
    ).reset_index()
    
    # Number of distinct products
    agg['num_sold'] = agg['prod_list'].apply(len)
    # Comma‑separated string of product names
    agg['products'] = agg['prod_list'].apply(','.join)
    
    # Select required columns and order by date
    result = agg[['sell_date', 'num_sold', 'products']].sort_values('sell_date')
    return result
```

## PostgreSQL
```sql
SELECT
    sell_date,
    COUNT(DISTINCT product) AS num_sold,
    STRING_AGG(DISTINCT product, ',' ORDER BY product) AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;
```
