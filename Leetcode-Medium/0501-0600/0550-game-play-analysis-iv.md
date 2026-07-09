# 0550. Game Play Analysis IV

## MySQL
```sql
# Write your MySQL query statement below
SELECT ROUND(
    COUNT(a1.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity),
    2
) AS fraction
FROM Activity a1
WHERE (a1.player_id, DATE_SUB(a1.event_date, INTERVAL 1 DAY)) IN (
    SELECT player_id, MIN(event_date)
    FROM Activity
    GROUP BY player_id
);
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
WITH first_logins AS (
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
),
consecutive_players AS (
    SELECT DISTINCT a.player_id
    FROM Activity a
    JOIN first_logins f
      ON a.player_id = f.player_id
     AND a.event_date = DATEADD(day, 1, f.first_login)
)
SELECT ROUND(CAST(COUNT(cp.player_id) AS float) / (SELECT COUNT(*) FROM first_logins), 2) AS fraction
FROM consecutive_players cp;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT ROUND(
    (SELECT COUNT(DISTINCT a.player_id)
     FROM Activity a
     JOIN (SELECT player_id, MIN(event_date) AS first_login
           FROM Activity
           GROUP BY player_id) f
       ON a.player_id = f.player_id
      AND a.event_date = f.first_login + INTERVAL '1' DAY
    ) / 
    (SELECT COUNT(DISTINCT player_id) FROM Activity),
 2) AS fraction
FROM dual;
```

## PythonData
```python
import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # first login date per player
    first_login = activity.groupby('player_id', as_index=False)['event_date'].min()
    # merge to have each record with its player's first login
    merged = activity.merge(first_login, on='player_id')
    # check if the record is exactly one day after the first login
    cond = merged['event_date'] == merged['event_date_y'] + pd.Timedelta(days=1)
    consecutive_players = merged.loc[cond, 'player_id'].nunique()
    total_players = activity['player_id'].nunique()
    fraction = round(consecutive_players / total_players if total_players else 0, 2)
    return pd.DataFrame({'fraction': [fraction]})
```

## PostgreSQL
```sql
WITH first_logins AS (
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
), consecutive_players AS (
    SELECT COUNT(DISTINCT a.player_id) AS cnt
    FROM Activity a
    JOIN first_logins f
      ON a.player_id = f.player_id
     AND a.event_date = f.first_login + INTERVAL '1 day'
)
SELECT ROUND(cp.cnt::numeric / tp.total, 2) AS fraction
FROM consecutive_players cp,
     (SELECT COUNT(DISTINCT player_id)::numeric AS total FROM Activity) tp;
```
