# 1789. Primary Department for Each Employee

## MySQL
```sql
# Write your MySQL query statement below
SELECT employee_id, department_id
FROM (
    SELECT *, COUNT(*) OVER (PARTITION BY employee_id) AS cnt
    FROM Employee
) e
WHERE cnt = 1 OR primary_flag = 'Y';
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT employee_id, department_id
FROM (
    SELECT *, COUNT(*) OVER (PARTITION BY employee_id) AS emp_cnt
    FROM Employee
) AS e
WHERE emp_cnt = 1 OR primary_flag = 'Y';
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT employee_id,
       department_id
FROM (
    SELECT e.*,
           COUNT(*) OVER (PARTITION BY employee_id) AS emp_cnt
    FROM Employee e
)
WHERE emp_cnt = 1 OR primary_flag = 'Y';
```

## PythonData
```python
import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    employee_counts = employee.groupby('employee_id')['employee_id'].transform('size')
    return employee[(employee_counts == 1) | (employee['primary_flag'] == 'Y')][['employee_id', 'department_id']]
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT employee_id,
       department_id
FROM (
    SELECT *,
           COUNT(*) OVER (PARTITION BY employee_id) AS emp_cnt
    FROM Employee
) AS sub
WHERE emp_cnt = 1 OR primary_flag = 'Y';
```
