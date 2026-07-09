# 0585. Investments in 2016

## MySQL
```sql
SELECT 
    ROUND(COALESCE(SUM(tiv_2016), 0), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
        SELECT tiv_2015
        FROM Insurance
        GROUP BY tiv_2015
        HAVING COUNT(*) > 1
    )
  AND (lat, lon) NOT IN (
        SELECT lat, lon
        FROM Insurance
        GROUP BY lat, lon
        HAVING COUNT(*) > 1
    );
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
WITH CTE AS (
    SELECT 
        tiv_2016,
        COUNT(*) OVER (PARTITION BY tiv_2015) AS cnt_tiv,
        COUNT(*) OVER (PARTITION BY lat, lon) AS cnt_loc
    FROM Insurance
)
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM CTE
WHERE cnt_tiv > 1 AND cnt_loc = 1;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM (
    SELECT i.*,
           COUNT(*) OVER (PARTITION BY tiv_2015) AS cnt_tiv,
           COUNT(*) OVER (PARTITION BY lat, lon) AS cnt_loc
    FROM Insurance i
)
WHERE cnt_tiv > 1
  AND cnt_loc = 1;
```

## PythonData
```python
import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    cnt_tiv = insurance.groupby('tiv_2015')['pid'].transform('size')
    cnt_loc = insurance.groupby(['lat', 'lon'])['pid'].transform('size')
    filtered = insurance[(cnt_tiv > 1) & (cnt_loc == 1)]
    total = round(filtered['tiv_2016'].sum(), 2)
    return pd.DataFrame({'tiv_2016': [total]})
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT 
    CAST(ROUND(SUM(tiv_2016), 2) AS DECIMAL(10,2)) AS tiv_2016
FROM (
    SELECT 
        tiv_2016,
        COUNT(*) OVER (PARTITION BY tiv_2015) AS cnt_tiv,
        COUNT(*) OVER (PARTITION BY lat, lon) AS cnt_loc
    FROM Insurance
) AS sub
WHERE cnt_tiv > 1
  AND cnt_loc = 1;
```
