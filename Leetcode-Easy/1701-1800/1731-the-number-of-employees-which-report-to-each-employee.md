# 1731. The Number of Employees Which Report to Each Employee

## MySQL
```sql
SELECT 
    mgr.employee_id,
    mgr.name,
    COUNT(emp.employee_id) AS reports_count,
    ROUND(AVG(emp.age)) AS average_age
FROM Employees emp
JOIN Employees mgr ON emp.reports_to = mgr.employee_id
GROUP BY mgr.employee_id, mgr.name
ORDER BY mgr.employee_id;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT
    mgr.employee_id,
    mgr.name,
    COUNT(emp.employee_id) AS reports_count,
    ROUND(AVG(CAST(emp.age AS FLOAT)), 0) AS average_age
FROM Employees emp
JOIN Employees mgr ON emp.reports_to = mgr.employee_id
GROUP BY
    mgr.employee_id,
    mgr.name
ORDER BY
    mgr.employee_id;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT
    mgr.employee_id,
    mgr.name,
    COUNT(emp.employee_id) AS reports_count,
    ROUND(AVG(emp.age)) AS average_age
FROM employees emp
JOIN employees mgr ON emp.reports_to = mgr.employee_id
GROUP BY
    mgr.employee_id,
    mgr.name
ORDER BY
    mgr.employee_id;
```

## PythonData
```python
import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    # Aggregate direct reports per manager
    agg = (
        employees.groupby("reports_to", as_index=False)
        .agg(reports_count=("employee_id", "size"), average_age=("age", "mean"))
    )
    # Exclude rows where manager id is null (no manager) and keep only actual managers
    agg = agg[agg["reports_to"].notna()].copy()
    # Round average age to nearest integer, rounding .5 up
    agg["average_age"] = (agg["average_age"] + 1e-12).round().astype(int)
    # Merge with employees to get manager names
    merged = agg.merge(
        employees[["employee_id", "name"]],
        left_on="reports_to",
        right_on="employee_id",
        how="left",
    )
    # Prepare final output
    result = merged[["employee_id_y", "name", "reports_count", "average_age"]].rename(
        columns={"employee_id_y": "employee_id"}
    )
    result = result.sort_values("employee_id").reset_index(drop=True)
    return result
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT
    mgr.employee_id,
    mgr.name,
    COUNT(emp.employee_id) AS reports_count,
    ROUND(AVG(emp.age))::int AS average_age
FROM employees emp
JOIN employees mgr ON emp.reports_to = mgr.employee_id
GROUP BY mgr.employee_id, mgr.name
ORDER BY mgr.employee_id;
```
