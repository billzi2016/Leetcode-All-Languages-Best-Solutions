# 0176. Second Highest Salary

## MySQL
```sql
# Write your MySQL query statement below
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;
```

## MSSQL
```sql
/* Write your T‑SQL query statement below */
SELECT
    (SELECT DISTINCT Salary
     FROM Employee
     ORDER BY Salary DESC
     OFFSET 1 ROW FETCH NEXT 1 ROW ONLY) AS SecondHighestSalary;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT 
    (SELECT MAX(salary) 
     FROM Employee 
     WHERE salary < (SELECT MAX(salary) FROM Employee)
    ) AS SecondHighestSalary
FROM dual;
```

## PythonData
```python
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Get distinct salaries
    distinct_salaries = employee["salary"].drop_duplicates()
    # Sort descending
    sorted_salaries = distinct_salaries.sort_values(ascending=False).reset_index(drop=True)
    # Determine second highest if exists
    second_highest = sorted_salaries.iloc[1] if len(sorted_salaries) >= 2 else None
    return pd.DataFrame({"SecondHighestSalary": [second_highest]})
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    OFFSET 1 LIMIT 1
) AS SecondHighestSalary;
```
