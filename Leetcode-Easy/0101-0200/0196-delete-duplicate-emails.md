# 0196. Delete Duplicate Emails

## MySQL
```sql
# Write your MySQL query statement below
DELETE p1 
FROM Person p1
JOIN Person p2 
  ON p1.email = p2.email 
 AND p1.id > p2.id;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
;WITH CTE AS (
    SELECT id,
           ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rn
    FROM Person
)
DELETE p
FROM Person p
JOIN CTE ON p.id = CTE.id
WHERE CTE.rn > 1;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
DELETE FROM Person p
WHERE EXISTS (
    SELECT 1 FROM Person q
    WHERE q.email = p.email
      AND q.id < p.id
);
```

## PythonData
```python
import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values('id', inplace=True)
    person.drop_duplicates(subset=['email'], keep='first', inplace=True)
```

## PostgreSQL
```sql
DELETE FROM Person
WHERE id NOT IN (
    SELECT MIN(id)
    FROM Person
    GROUP BY email
);
```
