# 0626. Exchange Seats

## MySQL
```sql
# Write your MySQL query statement below
SELECT 
    id,
    CASE 
        WHEN MOD(id, 2) = 1 THEN COALESCE(LEAD(student) OVER (ORDER BY id), student)
        ELSE LAG(student) OVER (ORDER BY id)
    END AS student
FROM Seat
ORDER BY id;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
WITH MaxIdCTE AS (
    SELECT MAX(id) AS max_id FROM Seat
)
SELECT 
    CASE 
        WHEN s.id % 2 = 1 AND s.id < m.max_id THEN s.id + 1
        WHEN s.id % 2 = 0 THEN s.id - 1
        ELSE s.id
    END AS id,
    s.student
FROM Seat s
CROSS JOIN MaxIdCTE m
ORDER BY id;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT id,
       CASE 
         WHEN MOD(id, 2) = 1 THEN NVL(lead_student, student)
         ELSE lag_student
       END AS student
FROM (
    SELECT id,
           student,
           LEAD(student) OVER (ORDER BY id) AS lead_student,
           LAG(student) OVER (ORDER BY id) AS lag_student
    FROM Seat
)
ORDER BY id;
```

## PythonData
```python
import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    # Ensure rows are ordered by id
    df = seat.sort_values('id').reset_index(drop=True)
    students = df['student'].tolist()
    # Swap every two consecutive students
    for i in range(0, len(students) - 1, 2):
        students[i], students[i + 1] = students[i + 1], students[i]
    df['student'] = students
    return df
```

## PostgreSQL
```sql
SELECT 
    id,
    CASE 
        WHEN id % 2 = 1 THEN COALESCE(LEAD(student) OVER (ORDER BY id), student)
        ELSE LAG(student) OVER (ORDER BY id)
    END AS student
FROM Seat
ORDER BY id;
```
