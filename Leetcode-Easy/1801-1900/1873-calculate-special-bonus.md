# 1873. Calculate Special Bonus

## MySQL
```sql
SELECT 
    employee_id,
    CASE 
        WHEN MOD(employee_id, 2) = 1 AND LEFT(name, 1) <> 'M' THEN salary 
        ELSE 0 
    END AS bonus
FROM Employees
ORDER BY employee_id;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT
    employee_id,
    CASE
        WHEN employee_id % 2 = 1 AND LEFT(name, 1) <> 'M' THEN salary
        ELSE 0
    END AS bonus
FROM Employees
ORDER BY employee_id;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT
    employee_id,
    CASE WHEN MOD(employee_id, 2) = 1 AND SUBSTR(name, 1, 1) != 'M'
         THEN salary ELSE 0 END AS bonus
FROM Employees
ORDER BY employee_id;
```

## PythonData
```python
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    mask = (employees["employee_id"] % 2 == 1) & (~employees["name"].str.startswith("M"))
    bonus = employees["salary"].where(mask, 0).astype(int)
    result = (
        pd.concat([employees["employee_id"], bonus.rename("bonus")], axis=1)
        .sort_values("employee_id")
        .reset_index(drop=True)
    )
    return result
```

## PostgreSQL
```sql
SELECT 
    employee_id,
    CASE 
        WHEN (employee_id % 2 = 1) AND name NOT LIKE 'M%' THEN salary 
        ELSE 0 
    END AS bonus
FROM Employees
ORDER BY employee_id;
```
