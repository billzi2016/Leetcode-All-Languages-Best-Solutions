# 1633. Percentage of Users Attended a Contest

## MySQL
```sql
# Write your MySQL query statement below
SELECT 
    r.contest_id,
    ROUND(COUNT(DISTINCT r.user_id) * 100.0 / u.total_users, 2) AS percentage
FROM Register r
CROSS JOIN (SELECT COUNT(*) AS total_users FROM Users) u
GROUP BY r.contest_id
ORDER BY percentage DESC, contest_id ASC;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT
    contest_id,
    ROUND(COUNT(DISTINCT user_id) * 100.0 / (SELECT COUNT(*) FROM Users), 2) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT
    r.contest_id,
    ROUND(COUNT(DISTINCT r.user_id) * 100.0 / (SELECT COUNT(*) FROM Users), 2) AS percentage
FROM Register r
GROUP BY r.contest_id
ORDER BY percentage DESC, contest_id ASC;
```

## PythonData
```python
import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    total_users = users["user_id"].nunique()
    cnt = (
        register.groupby("contest_id")["user_id"]
        .nunique()
        .reset_index(name="count")
    )
    cnt["percentage"] = (cnt["count"] / total_users * 100).round(2)
    result = cnt[["contest_id", "percentage"]].sort_values(
        by=["percentage", "contest_id"], ascending=[False, True]
    ).reset_index(drop=True)
    return result
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT
    r.contest_id,
    ROUND(COUNT(DISTINCT r.user_id) * 100.0 / u.total_cnt, 2) AS percentage
FROM Register r
CROSS JOIN (SELECT COUNT(*) AS total_cnt FROM Users) u
GROUP BY r.contest_id, u.total_cnt
ORDER BY percentage DESC, contest_id ASC;
```
