# 0577. Employee Bonus

## MySQL
```sql
SELECT e.name, b.bonus
FROM Employee AS e
LEFT JOIN Bonus AS b ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;
```

## MSSQL
```sql
SELECT e.name, b.bonus
FROM Employee AS e
LEFT JOIN Bonus AS b ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;
```

## PythonData
```python
import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employee[['empId', 'name']], bonus, on='empId', how='left')
    filtered = merged[(merged['bonus'].isna()) | (merged['bonus'] < 1000)]
    return filtered[['name', 'bonus']]
```

## PostgreSQL
```sql
SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;
```
