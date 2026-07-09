# 1965. Employees With Missing Information

## MySQL
```sql
# Write your MySQL query statement below
SELECT employee_id
FROM Employees
WHERE employee_id NOT IN (SELECT employee_id FROM Salaries)
UNION
SELECT employee_id
FROM Salaries
WHERE employee_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY employee_id;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT e.employee_id
FROM Employees e
LEFT JOIN Salaries s ON e.employee_id = s.employee_id
WHERE s.salary IS NULL

UNION

SELECT s.employee_id
FROM Salaries s
LEFT JOIN Employees e ON s.employee_id = e.employee_id
WHERE e.name IS NULL
ORDER BY employee_id;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT employee_id
FROM Employees e
FULL OUTER JOIN Salaries s USING (employee_id)
WHERE e.name IS NULL OR s.salary IS NULL
ORDER BY employee_id;
```

## PythonData
```python
import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    emp_ids = set(employees["employee_id"])
    sal_ids = set(salaries["employee_id"])
    missing = sorted(emp_ids ^ sal_ids)
    return pd.DataFrame({"employee_id": missing})
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT 
    COALESCE(e.employee_id, s.employee_id) AS employee_id
FROM 
    Employees e
FULL OUTER JOIN 
    Salaries s USING (employee_id)
WHERE 
    e.name IS NULL OR s.salary IS NULL
ORDER BY 
    employee_id;
```
