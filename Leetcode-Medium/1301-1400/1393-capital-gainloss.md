# 1393. Capital Gain/Loss

## MySQL
```sql
# Write your MySQL query statement below
SELECT 
    stock_name,
    SUM(CASE 
            WHEN operation = 'Buy'  THEN -price
            WHEN operation = 'Sell' THEN price
        END) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name;
```

## MSSQL
```sql
SELECT 
    stock_name,
    SUM(CASE 
            WHEN operation = 'Buy' THEN -price
            ELSE price
        END) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT
    stock_name,
    SUM(CASE WHEN operation = 'Buy' THEN -price ELSE price END) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name;
```

## PythonData
```python
import pandas as pd
import numpy as np

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    # Convert operation to lowercase for safety and compute signed price
    signed_price = np.where(
        stocks["operation"].str.lower() == "buy",
        -stocks["price"],
        stocks["price"]
    )
    result = (
        pd.DataFrame({"stock_name": stocks["stock_name"], "signed_price": signed_price})
        .groupby("stock_name")["signed_price"]
        .sum()
        .reset_index(name="capital_gain_loss")
    )
    return result
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT
    stock_name,
    SUM(CASE WHEN operation = 'Buy' THEN -price ELSE price END) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name;
```
