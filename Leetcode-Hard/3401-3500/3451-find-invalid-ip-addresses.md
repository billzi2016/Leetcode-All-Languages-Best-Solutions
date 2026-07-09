# 3451. Find Invalid IP Addresses

## MySQL
```sql
SELECT
    ip,
    COUNT(*) AS invalid_count
FROM logs
WHERE ip NOT REGEXP '^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$'
GROUP BY ip
ORDER BY invalid_count DESC, ip DESC;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
WITH ip_parts AS (
    SELECT
        ip,
        PARSENAME(ip, 4) AS p1,
        PARSENAME(ip, 3) AS p2,
        PARSENAME(ip, 2) AS p3,
        PARSENAME(ip, 1) AS p4
    FROM logs
)
SELECT
    ip,
    COUNT(*) AS invalid_count
FROM ip_parts
WHERE
    p1 IS NULL OR p2 IS NULL OR p3 IS NULL OR p4 IS NULL
    OR TRY_CAST(p1 AS int) IS NULL OR TRY_CAST(p2 AS int) IS NULL
       OR TRY_CAST(p3 AS int) IS NULL OR TRY_CAST(p4 AS int) IS NULL
    OR CAST(p1 AS int) NOT BETWEEN 0 AND 255
    OR CAST(p2 AS int) NOT BETWEEN 0 AND 255
    OR CAST(p3 AS int) NOT BETWEEN 0 AND 255
    OR CAST(p4 AS int) NOT BETWEEN 0 AND 255
    OR (LEN(p1) > 1 AND LEFT(p1, 1) = '0')
    OR (LEN(p2) > 1 AND LEFT(p2, 1) = '0')
    OR (LEN(p3) > 1 AND LEFT(p3, 1) = '0')
    OR (LEN(p4) > 1 AND LEFT(p4, 1) = '0')
GROUP BY ip
ORDER BY invalid_count DESC, ip DESC;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT
    ip,
    COUNT(*) AS invalid_count
FROM logs
WHERE NOT REGEXP_LIKE(
        ip,
        '^((25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)$'
      )
GROUP BY ip
ORDER BY invalid_count DESC, ip DESC;
```

## PythonData
```python
import pandas as pd

def find_invalid_ips(logs: pd.DataFrame) -> pd.DataFrame:
    def is_invalid(ip):
        if not isinstance(ip, str):
            return True
        parts = ip.split('.')
        if len(parts) != 4:
            return True
        for p in parts:
            if not p.isdigit():
                return True
            # leading zeroes are not allowed unless the part is exactly "0"
            if len(p) > 1 and p[0] == '0':
                return True
            val = int(p)
            if val < 0 or val > 255:
                return True
        return False

    invalid_series = logs.loc[logs['ip'].apply(is_invalid), 'ip']
    if invalid_series.empty:
        return pd.DataFrame(columns=['ip', 'invalid_count'])
    
    result = (
        invalid_series.value_counts()
        .reset_index()
        .rename(columns={'index': 'ip', 'ip': 'invalid_count'})
    )
    result = result.sort_values(by=['invalid_count', 'ip'], ascending=[False, False])
    return result.reset_index(drop=True)
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT
    ip,
    COUNT(*) AS invalid_count
FROM logs
WHERE ip NOT ~ '^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$'
GROUP BY ip
ORDER BY invalid_count DESC, ip DESC;
```
