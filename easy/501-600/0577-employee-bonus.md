# 0577. Employee Bonus

## Mysql

```mysql
SELECT e.name, b.bonus
FROM Employee AS e
LEFT JOIN Bonus AS b ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;
```

## Mssql

```mssql
SELECT e.name, b.bonus
FROM Employee AS e
LEFT JOIN Bonus AS b ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;
```

## Oraclesql

```oraclesql
/* Write your PL/SQL query statement below */
SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;
```

## Pythondata

```pythondata
import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employee[['empId', 'name']], bonus, on='empId', how='left')
    filtered = merged[(merged['bonus'].isna()) | (merged['bonus'] < 1000)]
    return filtered[['name', 'bonus']]
```

## Postgresql

```postgresql
SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;
```
