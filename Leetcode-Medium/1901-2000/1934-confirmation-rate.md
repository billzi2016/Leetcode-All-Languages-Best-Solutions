# 1934. Confirmation Rate

## MySQL
```sql
# Write your MySQL query statement below
SELECT 
    s.user_id,
    ROUND(IFNULL(c.confirmed_cnt / NULLIF(c.total_cnt, 0), 0), 2) AS confirmation_rate
FROM Signups s
LEFT JOIN (
    SELECT 
        user_id,
        SUM(action = 'confirmed') AS confirmed_cnt,
        COUNT(*) AS total_cnt
    FROM Confirmations
    GROUP BY user_id
) c ON s.user_id = c.user_id;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT s.user_id,
       CAST(COALESCE(ROUND(CAST(c.confirmed AS float) / c.total, 2), 0) AS DECIMAL(10,2)) AS confirmation_rate
FROM Signups s
LEFT JOIN (
    SELECT user_id,
           SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END) AS confirmed,
           COUNT(*) AS total
    FROM Confirmations
    GROUP BY user_id
) c ON s.user_id = c.user_id;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT s.user_id,
       CASE 
           WHEN c.cnt IS NULL THEN 0
           ELSE ROUND(c.confirmed_cnt * 1.0 / c.cnt, 2)
       END AS confirmation_rate
FROM Signups s
LEFT JOIN (
    SELECT user_id,
           SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END) AS confirmed_cnt,
           COUNT(*) AS cnt
    FROM Confirmations
    GROUP BY user_id
) c ON s.user_id = c.user_id;
```

## PythonData
```python
import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    # Aggregate confirmation counts per user
    agg = (
        confirmations.groupby("user_id")
        .agg(
            total=("action", "size"),
            confirmed=("action", lambda x: (x == "confirmed").sum()),
        )
        .reset_index()
    )

    # Ensure every signup user appears in the result
    users = signups[["user_id"]].drop_duplicates()
    df = pd.merge(users, agg, on="user_id", how="left")

    df["total"] = df["total"].fillna(0)
    df["confirmed"] = df["confirmed"].fillna(0)

    # Compute rate with proper handling of zero total
    df["confirmation_rate"] = df.apply(
        lambda r: round(r["confirmed"] / r["total"], 2) if r["total"] > 0 else 0.00, axis=1
    )

    return df[["user_id", "confirmation_rate"]]
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT 
    s.user_id,
    COALESCE(ROUND(c.confirmed::numeric / NULLIF(c.total, 0), 2), 0)::numeric(10,2) AS confirmation_rate
FROM Signups s
LEFT JOIN (
    SELECT 
        user_id,
        COUNT(*) AS total,
        SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END) AS confirmed
    FROM Confirmations
    GROUP BY user_id
) c ON s.user_id = c.user_id;
```
