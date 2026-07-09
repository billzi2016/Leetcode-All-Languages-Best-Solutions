# 1075. Project Employees I

## MySQL
```sql
SELECT 
    p.project_id,
    ROUND(AVG(e.experience_years), 2) AS average_years
FROM Project p
JOIN Employee e ON p.employee_id = e.employee_id
GROUP BY p.project_id;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT 
    p.project_id,
    ROUND(AVG(e.experience_years), 2) AS average_years
FROM Project p
JOIN Employee e ON p.employee_id = e.employee_id
GROUP BY p.project_id;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT
    p.project_id,
    ROUND(AVG(e.experience_years), 2) AS average_years
FROM Project p
JOIN Employee e ON p.employee_id = e.employee_id
GROUP BY p.project_id;
```

## PythonData
```python
import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    merged = project.merge(employee[['employee_id', 'experience_years']], on='employee_id')
    avg_df = merged.groupby('project_id', as_index=False)['experience_years'].mean()
    avg_df = avg_df.rename(columns={'experience_years': 'average_years'})
    avg_df['average_years'] = avg_df['average_years'].round(2)
    return avg_df
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT 
    p.project_id,
    ROUND(AVG(e.experience_years), 2) AS average_years
FROM Project p
JOIN Employee e ON p.employee_id = e.employee_id
GROUP BY p.project_id;
```
