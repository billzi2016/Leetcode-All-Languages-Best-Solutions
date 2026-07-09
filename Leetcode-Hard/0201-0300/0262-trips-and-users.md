# 0262. Trips and Users

## MySQL
```sql
SELECT
    t.request_at AS Day,
    ROUND(SUM(CASE WHEN t.status <> 'completed' THEN 1 ELSE 0 END) / COUNT(*), 2) AS `Cancellation Rate`
FROM Trips t
JOIN Users uc ON t.client_id = uc.users_id AND uc.banned = 'No'
JOIN Users ud ON t.driver_id = ud.users_id AND ud.banned = 'No'
WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.request_at
ORDER BY t.request_at;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT
    t.request_at AS Day,
    ROUND(SUM(CASE WHEN t.status <> 'completed' THEN 1 ELSE 0 END) * 1.0 / COUNT(*), 2) AS [Cancellation Rate]
FROM Trips t
JOIN Users c ON t.client_id = c.users_id AND c.banned = 'No'
JOIN Users d ON t.driver_id = d.users_id AND d.banned = 'No'
WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.request_at
ORDER BY t.request_at;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT
    t.request_at AS Day,
    ROUND(
        SUM(CASE WHEN t.status <> 'completed' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS "Cancellation Rate"
FROM Trips t
JOIN Users c ON t.client_id = c.users_id AND c.banned = 'No'
JOIN Users d ON t.driver_id = d.users_id AND d.banned = 'No'
WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.request_at
ORDER BY t.request_at;
```

## PythonData
```python
import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    if trips.empty or users.empty:
        return pd.DataFrame(columns=["Day", "Cancellation Rate"])
    
    banned_ids = set(users.loc[users["banned"] == "Yes", "users_id"])
    
    mask = (
        ~trips["client_id"].isin(banned_ids)
        & ~trips["driver_id"].isin(banned_ids)
        & (trips["request_at"] >= "2013-10-01")
        & (trips["request_at"] <= "2013-10-03")
    )
    
    filtered = trips[mask]
    if filtered.empty:
        return pd.DataFrame(columns=["Day", "Cancellation Rate"])
    
    rates = (
        filtered.groupby("request_at")["status"]
        .apply(lambda s: round(((s != "completed").sum()) / len(s), 2))
        .reset_index()
    )
    rates.columns = ["Day", "Cancellation Rate"]
    return rates
```

## PostgreSQL
```sql
SELECT
    t.request_at AS Day,
    ROUND(
        SUM(CASE WHEN t.status <> 'completed' THEN 1 ELSE 0 END)::DECIMAL / COUNT(*),
        2
    ) AS "Cancellation Rate"
FROM Trips t
JOIN Users cu ON t.client_id = cu.users_id AND cu.banned = 'No'
JOIN Users du ON t.driver_id = du.users_id AND du.banned = 'No'
WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.request_at
ORDER BY t.request_at;
```
