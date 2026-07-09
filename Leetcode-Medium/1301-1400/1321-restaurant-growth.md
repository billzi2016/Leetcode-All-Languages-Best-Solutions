# 1321. Restaurant Growth

## MySQL
```sql
# Write your MySQL query statement below
WITH daily AS (
    SELECT visited_on, SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
),
ordered AS (
    SELECT 
        visited_on,
        amount,
        SUM(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS sum7,
        ROW_NUMBER() OVER (ORDER BY visited_on) AS rn
    FROM daily
)
SELECT 
    visited_on,
    amount,
    ROUND(sum7 / 7, 2) AS average_amount
FROM ordered
WHERE rn >= 7
ORDER BY visited_on;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
WITH daily AS (
    SELECT visited_on,
           SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
),
ordered AS (
    SELECT visited_on,
           amount,
           ROW_NUMBER() OVER (ORDER BY visited_on) AS rn,
           SUM(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS sum7
    FROM daily
)
SELECT visited_on,
       amount,
       CAST(ROUND(CAST(sum7 AS decimal(10,2)) / 7.0, 2) AS decimal(10,2)) AS average_amount
FROM ordered
WHERE rn >= 7
ORDER BY visited_on;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
WITH daily AS (
    SELECT visited_on,
           SUM(amount) AS daily_amount
    FROM Customer
    GROUP BY visited_on
),
windowed AS (
    SELECT visited_on,
           SUM(daily_amount) OVER (ORDER BY visited_on
                                   RANGE BETWEEN INTERVAL '6' DAY PRECEDING AND CURRENT ROW) AS amount_sum,
           COUNT(*)   OVER (ORDER BY visited_on
                                   RANGE BETWEEN INTERVAL '6' DAY PRECEDING AND CURRENT ROW) AS cnt
    FROM daily
)
SELECT visited_on,
       amount_sum AS amount,
       ROUND(amount_sum / 7, 2) AS average_amount
FROM windowed
WHERE cnt = 7
ORDER BY visited_on;
```

## PythonData
```python
import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    # Ensure date column is datetime
    customer = customer.copy()
    customer["visited_on"] = pd.to_datetime(customer["visited_on"])
    
    # Daily total amount per visited_on
    daily = (
        customer.groupby("visited_on", as_index=False)["amount"]
        .sum()
        .sort_values("visited_on")
    )
    
    # 7‑day rolling sum and average
    daily["rolling_sum"] = daily["amount"].rolling(window=7).sum()
    daily["average_amount"] = (daily["rolling_sum"] / 7).round(2)
    
    # Keep rows where a full window exists
    result = daily[daily["average_amount"].notna()][["visited_on", "amount", "average_amount"]]
    return result.reset_index(drop=True)
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
WITH daily AS (
    SELECT visited_on,
           SUM(amount) AS daily_amount
    FROM Customer
    GROUP BY visited_on
),
windowed AS (
    SELECT visited_on,
           SUM(daily_amount) OVER (
               ORDER BY visited_on
               RANGE BETWEEN INTERVAL '6 day' PRECEDING AND CURRENT ROW
           ) AS amount_sum
    FROM daily
)
SELECT visited_on,
       amount_sum AS amount,
       ROUND(amount_sum::numeric / 7, 2) AS average_amount
FROM windowed
WHERE visited_on >= (SELECT MIN(visited_on) FROM daily) + INTERVAL '6 day'
ORDER BY visited_on;
```
