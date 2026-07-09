# 1890. The Latest Login in 2020

## MySQL
```sql
# Write your MySQL query statement below
SELECT 
    user_id, 
    MAX(time_stamp) AS last_stamp
FROM 
    Logins
WHERE 
    YEAR(time_stamp) = 2020
GROUP BY 
    user_id;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT
    user_id,
    MAX(time_stamp) AS last_stamp
FROM
    Logins
WHERE
    YEAR(time_stamp) = 2020
GROUP BY
    user_id;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT user_id,
       MAX(time_stamp) AS last_stamp
FROM Logins
WHERE EXTRACT(YEAR FROM time_stamp) = 2020
GROUP BY user_id;
```

## PythonData
```python
import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    # Ensure the timestamp column is of datetime dtype
    if logins['time_stamp'].dtype != 'datetime64[ns]':
        logins = logins.copy()
        logins['time_stamp'] = pd.to_datetime(logins['time_stamp'])
    
    # Filter rows belonging to year 2020
    mask = logins['time_stamp'].dt.year == 2020
    filtered = logins.loc[mask]
    
    # Group by user_id and get the latest timestamp per user
    result = (
        filtered.groupby('user_id', as_index=False)['time_stamp']
                .max()
                .rename(columns={'time_stamp': 'last_stamp'})
    )
    return result
```

## PostgreSQL
```sql
SELECT
    user_id,
    MAX(time_stamp) AS last_stamp
FROM Logins
WHERE EXTRACT(YEAR FROM time_stamp) = 2020
GROUP BY user_id;
```
