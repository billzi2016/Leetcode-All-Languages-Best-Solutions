# 0181. Employees Earning More Than Their Managers

## MySQL
```sql
# Write your MySQL query statement below
SELECT e.name AS Employee
FROM Employee e
JOIN Employee m ON e.managerId = m.id
WHERE e.salary > m.salary;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT
    e.name AS Employee
FROM
    Employee e
JOIN
    Employee m ON e.managerId = m.id
WHERE
    e.salary > m.salary;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT e.name AS Employee
FROM Employee e
JOIN Employee m ON e.managerId = m.id
WHERE e.salary > m.salary;
```

## PythonData
```python
import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    mgr = employee.rename(columns={"id": "manager_id", "salary": "manager_salary"})
    merged = pd.merge(
        employee,
        mgr[["manager_id", "manager_salary"]],
        left_on="managerId",
        right_on="manager_id",
        how="inner",
    )
    res = merged[merged["salary"] > merged["manager_salary"]][["name"]]
    return res.rename(columns={"name": "Employee"})
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT e.name AS Employee
FROM Employee e
JOIN Employee m ON e.managerId = m.id
WHERE e.salary > m.salary;
```
