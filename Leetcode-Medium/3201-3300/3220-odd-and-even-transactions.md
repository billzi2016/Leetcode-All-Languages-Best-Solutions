# 3220. Odd and Even Transactions

## MySQL
```sql
SELECT
    transaction_date,
    COALESCE(SUM(CASE WHEN MOD(amount, 2) = 1 THEN amount END), 0) AS odd_sum,
    COALESCE(SUM(CASE WHEN MOD(amount, 2) = 0 THEN amount END), 0) AS even_sum
FROM transactions
GROUP BY transaction_date
ORDER BY transaction_date;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT
    transaction_date,
    SUM(CASE WHEN amount % 2 = 1 THEN amount ELSE 0 END) AS odd_sum,
    SUM(CASE WHEN amount % 2 = 0 THEN amount ELSE 0 END) AS even_sum
FROM transactions
GROUP BY transaction_date
ORDER BY transaction_date;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT transaction_date,
       SUM(CASE WHEN MOD(amount, 2) = 1 THEN amount ELSE 0 END) AS odd_sum,
       SUM(CASE WHEN MOD(amount, 2) = 0 THEN amount ELSE 0 END) AS even_sum
FROM transactions
GROUP BY transaction_date
ORDER BY transaction_date;
```

## PythonData
```python
import pandas as pd

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    odd = transactions[transactions["amount"] % 2 != 0].groupby("transaction_date")["amount"].sum()
    even = transactions[transactions["amount"] % 2 == 0].groupby("transaction_date")["amount"].sum()
    result = pd.concat([odd, even], axis=1).fillna(0)
    result.columns = ["odd_sum", "even_sum"]
    result = result.reset_index().sort_values("transaction_date")
    result["odd_sum"] = result["odd_sum"].astype(int)
    result["even_sum"] = result["even_sum"].astype(int)
    return result
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT
    transaction_date,
    SUM(CASE WHEN amount % 2 = 1 THEN amount ELSE 0 END) AS odd_sum,
    SUM(CASE WHEN amount % 2 = 0 THEN amount ELSE 0 END) AS even_sum
FROM transactions
GROUP BY transaction_date
ORDER BY transaction_date;
```
