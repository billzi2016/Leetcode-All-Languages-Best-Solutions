# 1978. Employees Whose Manager Left the Company

## MySQL
```sql
SELECT e.employee_id
FROM Employees e
LEFT JOIN Employees m ON e.manager_id = m.employee_id
WHERE e.salary < 30000
  AND e.manager_id IS NOT NULL
  AND m.employee_id IS NULL
ORDER BY e.employee_id;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT e.employee_id
FROM Employees AS e
LEFT JOIN Employees AS m ON e.manager_id = m.employee_id
WHERE e.salary < 30000
  AND e.manager_id IS NOT NULL
  AND m.employee_id IS NULL
ORDER BY e.employee_id;
```

## OracleSQL
```sql
SELECT employee_id
FROM Employees e
WHERE salary < 30000
  AND NOT EXISTS (
        SELECT 1
        FROM Employees m
        WHERE m.employee_id = e.manager_id
    )
ORDER BY employee_id;
```

## PythonData
```python
import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    mask = (
        (employees["salary"] < 30000)
        & employees["manager_id"].notna()
        & ~employees["manager_id"].isin(employees["employee_id"])
    )
    return (
        employees.loc[mask, ["employee_id"]]
        .sort_values("employee_id")
        .reset_index(drop=True)
    )
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT e.employee_id
FROM Employees e
LEFT JOIN Employees m ON e.manager_id = m.employee_id
WHERE e.salary < 30000
  AND e.manager_id IS NOT NULL
  AND m.employee_id IS NULL
ORDER BY e.employee_id;
```
