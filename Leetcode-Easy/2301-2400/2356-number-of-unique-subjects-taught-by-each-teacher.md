# 2356. Number of Unique Subjects Taught by Each Teacher

## MySQL
```sql
SELECT
    teacher_id,
    COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT
    teacher_id,
    COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id;
```

## OracleSQL
```sql
SELECT teacher_id,
       COUNT(DISTINCT subject_id) AS cnt
FROM   Teacher
GROUP  BY teacher_id;
```

## PythonData
```python
import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return (
        teacher.groupby("teacher_id")["subject_id"]
        .nunique()
        .reset_index(name="cnt")
    )
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT
    teacher_id,
    COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id;
```
