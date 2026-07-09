# 0596. Classes With at Least 5 Students

## MySQL
```sql
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(*) >= 5;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(*) >= 5;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(*) >= 5;
```

## PythonData
```python
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # Count number of students per class
    class_counts = courses.groupby('class', as_index=False)['student'].count()
    # Keep classes with at least 5 students and return only the class column
    result = class_counts[class_counts['student'] >= 5][['class']]
    return result.reset_index(drop=True)
```

## PostgreSQL
```sql
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(*) >= 5;
```
