# 0185. Department Top Three Salaries

## MySQL
```sql
# Write your MySQL query statement below
WITH employee_department AS (
    SELECT 
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        DENSE_RANK() OVER (PARTITION BY d.id ORDER BY e.salary DESC) AS rnk
    FROM Employee e
    JOIN Department d ON e.departmentId = d.id
)
SELECT Department, Employee, Salary
FROM employee_department
WHERE rnk <= 3;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
WITH RankedEmployees AS (
    SELECT 
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS rnk
    FROM Employee e
    JOIN Department d ON e.departmentId = d.id
)
SELECT Department, Employee, Salary
FROM RankedEmployees
WHERE rnk <= 3;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT d.name   AS Department,
       e.name   AS Employee,
       e.salary AS Salary
FROM (
    SELECT e.*,
           DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS rnk
    FROM Employee e
) e
JOIN Department d ON e.departmentId = d.id
WHERE e.rnk <= 3;
```

## PythonData
```python
import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    emp = employee.copy()
    emp['rnk'] = emp.groupby('departmentId')['salary'].rank(method='dense', ascending=False)
    top_emp = emp[emp['rnk'] <= 3]
    merged = top_emp.merge(department, left_on='departmentId', right_on='id')
    result = merged[['name_y', 'name_x', 'salary']].copy()
    result.columns = ['Department', 'Employee', 'Salary']
    return result
```

## PostgreSQL
```sql
SELECT d.name AS Department,
       e.name AS Employee,
       e.salary AS Salary
FROM (
    SELECT *, DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rnk
    FROM Employee
) e
JOIN Department d ON e.departmentId = d.id
WHERE e.rnk <= 3;
```
