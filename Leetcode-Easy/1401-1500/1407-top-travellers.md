# 1407. Top Travellers

## MySQL
```sql
SELECT 
    u.name,
    COALESCE(SUM(r.distance), 0) AS travelled_distance
FROM Users u
LEFT JOIN Rides r ON u.id = r.user_id
GROUP BY u.id, u.name
ORDER BY travelled_distance DESC, u.name ASC;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT 
    u.name,
    ISNULL(SUM(r.distance), 0) AS travelled_distance
FROM Users u
LEFT JOIN Rides r ON u.id = r.user_id
GROUP BY u.id, u.name
ORDER BY travelled_distance DESC, u.name ASC;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT
    u.name,
    NVL(SUM(r.distance), 0) AS travelled_distance
FROM
    Users u
LEFT JOIN
    Rides r ON u.id = r.user_id
GROUP BY
    u.id, u.name
ORDER BY
    travelled_distance DESC,
    u.name ASC;
```

## PythonData
```python
import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    # Sum distances per user
    distance_sum = rides.groupby('user_id', as_index=False)['distance'].sum()
    
    # Left join with users to include those without rides
    merged = pd.merge(users, distance_sum, left_on='id', right_on='user_id', how='left')
    
    # Replace NaN distances with 0 and ensure integer type
    merged['travelled_distance'] = merged['distance'].fillna(0).astype(int)
    
    # Select required columns
    result = merged[['name', 'travelled_distance']]
    
    # Sort by travelled distance descending, then name ascending
    result = result.sort_values(by=['travelled_distance', 'name'], ascending=[False, True])
    
    return result.reset_index(drop=True)
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT 
    u.name,
    COALESCE(SUM(r.distance), 0) AS travelled_distance
FROM Users u
LEFT JOIN Rides r ON u.id = r.user_id
GROUP BY u.id, u.name
ORDER BY travelled_distance DESC, u.name ASC;
```
