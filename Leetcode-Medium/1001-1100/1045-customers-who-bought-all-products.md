# 1045. Customers Who Bought All Products

## MySQL
```sql
# Write your MySQL query statement below
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product);
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT c.customer_id
FROM Customer c
GROUP BY c.customer_id
HAVING COUNT(DISTINCT c.product_key) = (SELECT COUNT(*) FROM Product);
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product);
```

## PythonData
```python
import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    if product.empty or customer.empty:
        return pd.DataFrame(columns=["customer_id"])
    
    # Keep only purchases of existing products
    merged = pd.merge(customer, product, on="product_key", how="inner")
    
    # Number of distinct products each customer bought
    cust_counts = (
        merged.groupby("customer_id")["product_key"]
        .nunique()
        .reset_index(name="cnt")
    )
    
    total_products = product["product_key"].nunique()
    
    result = cust_counts[cust_counts["cnt"] == total_products][["customer_id"]]
    return result.reset_index(drop=True)
```

## PostgreSQL
```sql
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product);
```
