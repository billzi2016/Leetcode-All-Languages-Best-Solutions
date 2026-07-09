# 1193. Monthly Transactions I

## MySQL
```sql
SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month,
       country,
       COUNT(*) AS trans_count,
       SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,
       SUM(amount) AS trans_total_amount,
       SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY month, country;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT 
    CONVERT(varchar(7), trans_date, 120) AS month,
    country,
    COUNT(*) AS trans_count,
    SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY 
    CONVERT(varchar(7), trans_date, 120),
    country;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT TO_CHAR(trans_date, 'YYYY-MM') AS month,
       country,
       COUNT(*) AS trans_count,
       SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,
       SUM(amount) AS trans_total_amount,
       SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY TO_CHAR(trans_date, 'YYYY-MM'), country;
```

## PythonData
```python
import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    df = transactions.copy()
    if df.empty:
        return pd.DataFrame(columns=[
            "month", "country", "trans_count",
            "approved_count", "trans_total_amount",
            "approved_total_amount"
        ])
    
    # Ensure proper datetime type
    df["trans_date"] = pd.to_datetime(df["trans_date"])
    # Extract month in required format
    df["month"] = df["trans_date"].dt.strftime("%Y-%m")
    
    # Flags for approved transactions
    df["approved_flag"] = (df["state"] == "approved").astype(int)
    df["approved_amount"] = df["amount"].where(df["state"] == "approved", 0)
    
    # Aggregate per month and country
    result = (
        df.groupby(["month", "country"], as_index=False)
          .agg(
              trans_count=("id", "size"),
              trans_total_amount=("amount", "sum"),
              approved_count=("approved_flag", "sum"),
              approved_total_amount=("approved_amount", "sum")
          )
    )
    
    # Ensure column order matches expected output
    return result[
        [
            "month",
            "country",
            "trans_count",
            "approved_count",
            "trans_total_amount",
            "approved_total_amount"
        ]
    ]
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT TO_CHAR(trans_date, 'YYYY-MM') AS month,
       country,
       COUNT(*) AS trans_count,
       COUNT(*) FILTER (WHERE state = 'approved') AS approved_count,
       SUM(amount) AS trans_total_amount,
       SUM(amount) FILTER (WHERE state = 'approved') AS approved_total_amount
FROM Transactions
GROUP BY TO_CHAR(trans_date, 'YYYY-MM'), country;
```
