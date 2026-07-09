# 1587. Bank Account Summary II

## MySQL
```sql
SELECT u.name, SUM(t.amount) AS balance
FROM Users u
JOIN Transactions t ON u.account = t.account
GROUP BY u.account, u.name
HAVING balance > 10000;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT u.name, SUM(t.amount) AS balance
FROM Users u
JOIN Transactions t ON u.account = t.account
GROUP BY u.account, u.name
HAVING SUM(t.amount) > 10000;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT u.name,
       SUM(t.amount) AS balance
FROM   Users u
JOIN   Transactions t ON u.account = t.account
GROUP BY u.name
HAVING SUM(t.amount) > 10000;
```

## PythonData
```python
import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    merged = users.merge(transactions, on="account")
    agg = (
        merged.groupby(["account", "name"], as_index=False)["amount"]
        .sum()
        .rename(columns={"amount": "balance"})
    )
    filtered = agg[agg["balance"] > 10000]
    return filtered[["name", "balance"]]
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT u.name,
       SUM(t.amount) AS balance
FROM Users u
JOIN Transactions t ON u.account = t.account
GROUP BY u.account, u.name
HAVING SUM(t.amount) > 10000;
```
