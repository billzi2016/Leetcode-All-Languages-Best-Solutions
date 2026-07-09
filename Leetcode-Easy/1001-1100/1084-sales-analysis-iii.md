# 1084. Sales Analysis III

## MySQL
```sql
SELECT p.product_id, p.product_name
FROM Product p
JOIN Sales s ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name
HAVING MIN(s.sale_date) >= '2019-01-01' AND MAX(s.sale_date) <= '2019-03-31';
```

## MSSQL
```sql
SELECT p.product_id, p.product_name
FROM Sales s
JOIN Product p ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name
HAVING MIN(s.sale_date) >= '2019-01-01' 
   AND MAX(s.sale_date) <= '2019-03-31';
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT p.product_id,
       p.product_name
FROM   Product p
JOIN   Sales s ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name
HAVING MIN(s.sale_date) >= DATE '2019-01-01'
   AND MAX(s.sale_date) <= DATE '2019-03-31';
```

## PythonData
```python
import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    # Ensure sale_date is datetime
    sales = sales.copy()
    sales["sale_date"] = pd.to_datetime(sales["sale_date"])
    
    # Aggregate min and max sale dates per product
    agg = (
        sales.groupby("product_id")
        .agg(min_date=("sale_date", "min"), max_date=("sale_date", "max"))
        .reset_index()
    )
    
    # Keep products whose sales are only within Q1 2019
    mask = (agg["min_date"] >= pd.Timestamp("2019-01-01")) & (
        agg["max_date"] <= pd.Timestamp("2019-03-31")
    )
    filtered = agg[mask]
    
    # Join with product table to get product_name
    result = filtered.merge(
        product[["product_id", "product_name"]],
        on="product_id",
        how="inner"
    )
    
    return result[["product_id", "product_name"]]
```

## PostgreSQL
```sql
SELECT p.product_id, p.product_name
FROM Product p
JOIN (
    SELECT product_id
    FROM Sales
    GROUP BY product_id
    HAVING MIN(sale_date) >= DATE '2019-01-01'
       AND MAX(sale_date) <= DATE '2019-03-31'
) s ON p.product_id = s.product_id;
```
