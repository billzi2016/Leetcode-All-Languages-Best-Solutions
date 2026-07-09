# 0570. Managers with at Least 5 Direct Reports

## MySQL
```sql
# Write your MySQL query statement below
SELECT e.name
FROM Employee e
JOIN (
    SELECT managerId
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
    HAVING COUNT(*) >= 5
) AS m ON e.id = m.managerId;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT e.name
FROM Employee e
JOIN (
    SELECT managerId
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
    HAVING COUNT(*) >= 5
) AS m ON e.id = m.managerId;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT e.name
FROM Employee e
JOIN (
    SELECT managerId
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
    HAVING COUNT(*) >= 5
) m ON e.id = m.managerId;
```

## PythonData
```python
import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # Count direct reports for each manager (ignore null managerId)
    report_counts = employee['managerId'].value_counts()
    # Managers with at least 5 direct reports
    eligible_ids = report_counts[report_counts >= 5].index
    # Retrieve their names
    result = employee[employee['id'].isin(eligible_ids)][['name']]
    return result.reset_index(drop=True)
```

## PostgreSQL
```sql
SELECT e.name
FROM Employee e
JOIN (
    SELECT managerId
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
    HAVING COUNT(*) >= 5
) m ON e.id = m.managerId;
```
