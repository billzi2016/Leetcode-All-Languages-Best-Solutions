# 1141. User Activity for the Past 30 Days I

## MySQL
```sql
# Write your MySQL query statement below
SELECT 
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND '2019-07-27'
GROUP BY activity_date;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT 
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM 
    Activity
WHERE 
    activity_date BETWEEN DATEADD(day, -29, CAST('2019-07-27' AS date)) AND CAST('2019-07-27' AS date)
GROUP BY 
    activity_date;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN DATE '2019-06-28' AND DATE '2019-07-27'
GROUP BY activity_date;
```

## PythonData
```python
import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.copy()
    if not pd.api.types.is_datetime64_any_dtype(df["activity_date"]):
        df["activity_date"] = pd.to_datetime(df["activity_date"])
    mask = (df["activity_date"] >= "2019-06-28") & (df["activity_date"] <= "2019-07-27")
    filtered = df.loc[mask]
    result = (
        filtered.groupby("activity_date")["user_id"]
        .nunique()
        .reset_index()
        .rename(columns={"activity_date": "day", "user_id": "active_users"})
    )
    return result
```

## PostgreSQL
```sql
SELECT
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN DATE '2019-06-28' AND DATE '2019-07-27'
GROUP BY activity_date;
```
