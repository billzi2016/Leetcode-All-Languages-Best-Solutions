# 0175. Combine Two Tables

## MySQL
```sql
SELECT p.FirstName, p.LastName, a.City, a.State
FROM Person AS p
LEFT JOIN Address AS a ON p.PersonId = a.PersonId;
```

## MSSQL
```sql
SELECT p.FirstName,
       p.LastName,
       a.City,
       a.State
FROM Person AS p
LEFT JOIN Address AS a
    ON p.PersonId = a.PersonId;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT p.FirstName,
       p.LastName,
       a.City,
       a.State
FROM   Person p
LEFT JOIN Address a
ON     p.PersonId = a.PersonId;
```

## PythonData
```python
import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(person, address, on="personId", how="left")
    return merged[["firstName", "lastName", "city", "state"]]
```

## PostgreSQL
```sql
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person AS p
LEFT JOIN Address AS a ON p.personId = a.personId;
```
