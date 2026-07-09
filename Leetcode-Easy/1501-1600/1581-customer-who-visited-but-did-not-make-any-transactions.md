# 1581. Customer Who Visited but Did Not Make Any Transactions

## MySQL
```sql
SELECT
    v.customer_id,
    COUNT(*) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t ON v.visit_id = t.visit_id
WHERE t.visit_id IS NULL
GROUP BY v.customer_id;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT 
    v.customer_id,
    COUNT(*) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t ON v.visit_id = t.visit_id
WHERE t.visit_id IS NULL
GROUP BY v.customer_id;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT
    v.customer_id,
    COUNT(*) AS count_no_trans
FROM
    Visits v
LEFT JOIN
    Transactions t ON v.visit_id = t.visit_id
WHERE
    t.visit_id IS NULL
GROUP BY
    v.customer_id;
```

## PythonData
```python
import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    # Identify visits without any associated transaction
    no_trans_visits = visits[~visits["visit_id"].isin(transactions["visit_id"])]
    
    # Count such visits per customer
    result = (
        no_trans_visits.groupby("customer_id", as_index=False)["visit_id"]
        .count()
        .rename(columns={"visit_id": "count_no_trans"})
    )
    return result
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT
    v.customer_id,
    COUNT(*) AS count_no_trans
FROM
    Visits v
LEFT JOIN
    Transactions t ON v.visit_id = t.visit_id
WHERE
    t.visit_id IS NULL
GROUP BY
    v.customer_id;
```
