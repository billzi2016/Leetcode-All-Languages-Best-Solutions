# 1158. Market Analysis I

## MySQL
```sql
SELECT 
    u.user_id AS buyer_id,
    u.join_date,
    COUNT(o.order_id) AS orders_in_2019
FROM Users u
LEFT JOIN Orders o
    ON u.user_id = o.buyer_id
    AND YEAR(o.order_date) = 2019
GROUP BY u.user_id, u.join_date;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT 
    u.user_id AS buyer_id,
    u.join_date,
    COUNT(o.order_id) AS orders_in_2019
FROM Users u
LEFT JOIN Orders o
    ON u.user_id = o.buyer_id AND YEAR(o.order_date) = 2019
GROUP BY u.user_id, u.join_date;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT 
    u.user_id AS buyer_id,
    u.join_date,
    COUNT(o.order_id) AS orders_in_2019
FROM Users u
LEFT JOIN Orders o
    ON u.user_id = o.buyer_id
   AND EXTRACT(YEAR FROM o.order_date) = 2019
GROUP BY 
    u.user_id,
    u.join_date
ORDER BY 
    u.user_id;
```

## PythonData
```python
import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    # Ensure order_date is datetime
    if not pd.api.types.is_datetime64_any_dtype(orders["order_date"]):
        orders = orders.copy()
        orders["order_date"] = pd.to_datetime(orders["order_date"])
    
    # Filter orders from year 2019
    orders_2019 = orders[orders["order_date"].dt.year == 2019]
    
    # Count orders per buyer
    cnt = (
        orders_2019.groupby("buyer_id")
        .size()
        .reset_index(name="orders_in_2019")
    )
    
    # Merge with users to include all users
    merged = pd.merge(
        users[["user_id", "join_date"]],
        cnt,
        left_on="user_id",
        right_on="buyer_id",
        how="left",
    )
    
    merged["orders_in_2019"] = merged["orders_in_2019"].fillna(0).astype(int)
    merged = merged.rename(columns={"user_id": "buyer_id"})
    
    # Select required columns
    result = merged[["buyer_id", "join_date", "orders_in_2019"]]
    return result
```

## PostgreSQL
```sql
SELECT 
    u.user_id AS buyer_id,
    u.join_date,
    COUNT(o.order_id) AS orders_in_2019
FROM Users u
LEFT JOIN Orders o
    ON u.user_id = o.buyer_id
   AND EXTRACT(YEAR FROM o.order_date) = 2019
GROUP BY 
    u.user_id,
    u.join_date
ORDER BY 
    u.user_id;
```
