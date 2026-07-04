# 0596. Classes With at Least 5 Students

## Mysql

```mysql
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(*) >= 5;
```

## Mssql

```mssql
/* Write your T-SQL query statement below */
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(*) >= 5;
```

## Oraclesql

```oraclesql
/* Write your PL/SQL query statement below */
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(*) >= 5;
```

## Pythondata

```pythondata
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # Count number of students per class
    class_counts = courses.groupby('class', as_index=False)['student'].count()
    # Keep classes with at least 5 students and return only the class column
    result = class_counts[class_counts['student'] >= 5][['class']]
    return result.reset_index(drop=True)
```

## Postgresql

```postgresql
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(*) >= 5;
```
