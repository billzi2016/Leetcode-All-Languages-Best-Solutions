# 1907. Count Salary Categories

## MySQL
```sql
# Write your MySQL query statement below
SELECT 'Low Salary' AS category, COUNT(*) AS accounts_count
FROM Accounts
WHERE income < 30000
UNION ALL
SELECT 'Average Salary', COUNT(*)
FROM Accounts
WHERE income BETWEEN 30000 AND 70000
UNION ALL
SELECT 'High Salary', COUNT(*)
FROM Accounts
WHERE income > 70000;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT cat.category,
       COALESCE(cnt.accounts_count, 0) AS accounts_count
FROM (SELECT 'Low Salary' AS category UNION ALL
      SELECT 'Average Salary' UNION ALL
      SELECT 'High Salary') AS cat
LEFT JOIN (
    SELECT CASE
               WHEN income < 30000 THEN 'Low Salary'
               WHEN income >= 30000 AND income < 80000 THEN 'Average Salary'
               ELSE 'High Salary'
           END AS category,
           COUNT(*) AS accounts_count
    FROM Accounts
    GROUP BY CASE
                 WHEN income < 30000 THEN 'Low Salary'
                 WHEN income >= 30000 AND income < 80000 THEN 'Average Salary'
                 ELSE 'High Salary'
             END
) AS cnt
ON cat.category = cnt.category;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT 'Low Salary' AS category,
       COUNT(*) AS accounts_count
FROM   Accounts
WHERE  income < 30000

UNION ALL

SELECT 'Average Salary',
       COUNT(*)
FROM   Accounts
WHERE  income BETWEEN 30000 AND 70000

UNION ALL

SELECT 'High Salary',
       COUNT(*)
FROM   Accounts
WHERE  income > 70000;
```

## PythonData
```python
import pandas as pd
import numpy as np

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    categories = ["Low Salary", "Average Salary", "High Salary"]
    # Ensure we always return all three categories even if input is empty
    if accounts.empty:
        return pd.DataFrame({"category": categories, "accounts_count": [0, 0, 0]})
    
    conds = [
        accounts["income"] < 30000,
        (accounts["income"] >= 30000) & (accounts["income"] <= 70000),
        accounts["income"] > 70000
    ]
    df = accounts.copy()
    df["category"] = np.select(conds, categories)
    
    result = (
        df.groupby("category")
          .size()
          .reindex(categories, fill_value=0)
          .reset_index()
    )
    result.columns = ["category", "accounts_count"]
    return result
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
WITH categorized AS (
    SELECT CASE
               WHEN income < 30000 THEN 'Low Salary'
               WHEN income <= 70000 THEN 'Average Salary'
               ELSE 'High Salary'
           END AS category
    FROM Accounts
),
cnt AS (
    SELECT category, COUNT(*) AS accounts_count
    FROM categorized
    GROUP BY category
)
SELECT cat.category,
       COALESCE(cnt.accounts_count, 0) AS accounts_count
FROM (VALUES ('Low Salary'), ('Average Salary'), ('High Salary')) AS cat(category)
LEFT JOIN cnt ON cat.category = cnt.category;
```
