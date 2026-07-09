# 1667. Fix Names in a Table

## MySQL
```sql
SELECT 
    user_id,
    CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2))) AS name
FROM Users
ORDER BY user_id;
```

## MSSQL
```sql
SELECT
    user_id,
    CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2, LEN(name)))) AS name
FROM Users
ORDER BY user_id;
```

## OracleSQL
```sql
SELECT
    user_id,
    UPPER(SUBSTR(name, 1, 1)) || LOWER(SUBSTR(name, 2)) AS name
FROM Users
ORDER BY user_id;
```

## PythonData
```python
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    df = users.copy()
    df["name"] = df["name"].str.capitalize()
    return df.sort_values("user_id").reset_index(drop=True)
```

## PostgreSQL
```sql
SELECT
    user_id,
    UPPER(LEFT(name, 1)) || LOWER(SUBSTRING(name FROM 2)) AS name
FROM Users
ORDER BY user_id;
```
