# 0177. Nth Highest Salary

## MySQL
```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
    SELECT 
      (SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT N-1,1)
  );
END
```

## MSSQL
```sql
CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        SELECT Salary
        FROM (SELECT DISTINCT Salary FROM Employee) AS t
        ORDER BY Salary DESC
        OFFSET (@N - 1) ROWS FETCH NEXT 1 ROWS ONLY
    );
END
```

## OracleSQL
```sql
CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
  result NUMBER;
BEGIN
  SELECT salary INTO result
  FROM (
    SELECT salary,
           DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM (SELECT DISTINCT salary FROM Employee)
  )
  WHERE rnk = N;

  RETURN result;
EXCEPTION
  WHEN NO_DATA_FOUND THEN
    RETURN NULL;
END;
/
```

## PythonData
```python
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salaries = employee["salary"].drop_duplicates()
    sorted_salaries = salaries.sort_values(ascending=False).reset_index(drop=True)
    if len(sorted_salaries) >= N:
        val = sorted_salaries.iloc[N - 1]
    else:
        val = None
    return pd.DataFrame({f"getNthHighestSalary({N})": [val]})
```

## PostgreSQL
```sql
CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY
  SELECT (
      SELECT DISTINCT salary 
      FROM Employee 
      ORDER BY salary DESC 
      OFFSET N-1 LIMIT 1
  ) AS Salary;
END;
$$ LANGUAGE plpgsql;
```
