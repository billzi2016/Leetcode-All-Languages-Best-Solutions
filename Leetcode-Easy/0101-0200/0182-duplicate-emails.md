# 0182. Duplicate Emails

## MySQL
```sql
SELECT
    email AS Email
FROM
    Person
GROUP BY
    email
HAVING
    COUNT(*) > 1;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;
```

## PythonData
```python
import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    duplicated = person['email'][person['email'].duplicated(keep=False)].unique()
    return pd.DataFrame({'Email': duplicated})
```

## PostgreSQL
```sql
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;
```
