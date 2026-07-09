# 1280. Students and Examinations

## MySQL
```sql
# Write your MySQL query statement below
SELECT 
    s.student_id,
    s.student_name,
    sub.subject_name,
    COALESCE(e.attended_exams, 0) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN (
    SELECT student_id, subject_name, COUNT(*) AS attended_exams
    FROM Examinations
    GROUP BY student_id, subject_name
) e ON s.student_id = e.student_id AND sub.subject_name = e.subject_name
ORDER BY s.student_id, sub.subject_name;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT 
    s.student_id,
    s.student_name,
    sub.subject_name,
    COALESCE(e.attended_exams, 0) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN (
    SELECT 
        student_id,
        subject_name,
        COUNT(*) AS attended_exams
    FROM Examinations
    GROUP BY student_id, subject_name
) e
ON s.student_id = e.student_id AND sub.subject_name = e.subject_name
ORDER BY s.student_id, sub.subject_name;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT s.student_id,
       s.student_name,
       sub.subject_name,
       COUNT(e.subject_name) AS attended_exams
FROM   Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e
       ON e.student_id = s.student_id
      AND e.subject_name = sub.subject_name
GROUP BY s.student_id, s.student_name, sub.subject_name
ORDER BY s.student_id, sub.subject_name;
```

## PythonData
```python
import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    # All possible student‑subject pairs
    all_pairs = pd.merge(students, subjects, how='cross')
    
    # Count actual exam attendances
    attendance = (
        examinations.groupby(['student_id', 'subject_name'])
        .size()
        .reset_index(name='attended_exams')
    )
    
    # Merge counts onto the full set of pairs
    result = pd.merge(all_pairs, attendance, on=['student_id', 'subject_name'], how='left')
    result['attended_exams'] = result['attended_exams'].fillna(0).astype(int)
    
    # Order as required and select columns
    result = result.sort_values(['student_id', 'subject_name']).reset_index(drop=True)
    return result[['student_id', 'student_name', 'subject_name', 'attended_exams']]
```

## PostgreSQL
```sql
SELECT 
    s.student_id,
    s.student_name,
    sub.subject_name,
    COALESCE(e.cnt, 0) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN (
    SELECT student_id, subject_name, COUNT(*) AS cnt
    FROM Examinations
    GROUP BY student_id, subject_name
) e ON s.student_id = e.student_id AND sub.subject_name = e.subject_name
ORDER BY s.student_id, sub.subject_name;
```
