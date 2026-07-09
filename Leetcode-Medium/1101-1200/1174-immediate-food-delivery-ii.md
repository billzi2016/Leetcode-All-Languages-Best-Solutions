# 1174. Immediate Food Delivery II

## MySQL
```sql
SELECT ROUND(
    100 * SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) / COUNT(*),
    2
) AS immediate_percentage
FROM (
    SELECT d.*
    FROM Delivery d
    JOIN (
        SELECT customer_id, MIN(order_date) AS first_order_date
        FROM Delivery
        GROUP BY customer_id
    ) f ON d.customer_id = f.customer_id AND d.order_date = f.first_order_date
) t;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
WITH FirstOrders AS (
    SELECT
        delivery_id,
        customer_id,
        order_date,
        customer_pref_delivery_date,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS rn
    FROM Delivery
)
SELECT 
    CAST(ROUND(
        100.0 * SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) 
        / COUNT(*), 2) AS DECIMAL(5,2)) AS immediate_percentage
FROM FirstOrders
WHERE rn = 1;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT ROUND(
         SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) * 100 / COUNT(*),
         2
       ) AS immediate_percentage
FROM (
    SELECT d.*,
           ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) rn
    FROM Delivery d
) t
WHERE rn = 1;
```

## PythonData
```python
import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    # Get the first order (earliest order_date) for each customer
    first_orders = (
        delivery.sort_values("order_date")
        .drop_duplicates(subset="customer_id", keep="first")
    )
    
    # Count immediate orders where preferred delivery date equals order date
    immediate_cnt = (first_orders["order_date"] == first_orders["customer_pref_delivery_date"]).sum()
    total_customers = len(first_orders)
    
    # Calculate percentage rounded to 2 decimal places
    perc = round(immediate_cnt * 100 / total_customers, 2) if total_customers else 0.0
    
    return pd.DataFrame({"immediate_percentage": [perc]})
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT ROUND(
         (SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END)::numeric * 100) 
         / COUNT(*)
       , 2) AS immediate_percentage
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS rn
    FROM Delivery
) AS first_orders
WHERE rn = 1;
```
