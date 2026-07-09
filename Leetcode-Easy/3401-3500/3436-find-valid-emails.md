# 3436. Find Valid Emails

## MySQL
```sql
SELECT user_id, email
FROM Users
WHERE email LIKE '%_@_%.__%' 
  AND email NOT LIKE '%@%@%'
ORDER BY user_id;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT user_id, email
FROM Users
WHERE email LIKE '%_@_%._%' 
  AND email NOT LIKE '%@%@%'
ORDER BY user_id;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT user_id,
       email
FROM   Users
WHERE  REGEXP_LIKE(email, '^[^@]+@[^@]+\.[^@]+$')
ORDER BY user_id;
```

## PythonData
```python
import pandas as pd

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    valid = users[users['email'].str.contains(pattern, na=False)]
    return valid.sort_values('user_id').reset_index(drop=True)
```

## PostgreSQL
```sql
SELECT
    user_id,
    email
FROM
    Users
WHERE
    email ~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
ORDER BY
    user_id;
```
