# 0602. Friend Requests II: Who Has the Most Friends

## MySQL
```sql
# Write your MySQL query statement below
WITH all_ids AS (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
)
SELECT 
    id,
    COUNT(*) AS num
FROM all_ids
GROUP BY id
ORDER BY num DESC
LIMIT 1;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
WITH all_ids AS (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
)
SELECT TOP 1
    id,
    COUNT(*) AS num
FROM all_ids
GROUP BY id
ORDER BY COUNT(*) DESC;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
WITH all_ids AS (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
)
SELECT id, num
FROM (
    SELECT id,
           COUNT(*) AS num,
           DENSE_RANK() OVER (ORDER BY COUNT(*) DESC) AS rnk
    FROM all_ids
    GROUP BY id
)
WHERE rnk = 1;
```

## PythonData
```python
import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    if request_accepted.empty:
        return pd.DataFrame(columns=["id", "num"])
    
    # Count appearances of each user id in both requester and accepter columns
    counts = (
        pd.concat([request_accepted["requester_id"], request_accepted["accepter_id"]])
        .value_counts()
        .reset_index()
        .rename(columns={"index": "id", 0: "num"})
    )
    
    max_num = counts["num"].max()
    result = counts[counts["num"] == max_num].reset_index(drop=True)
    return result
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
WITH all_ids AS (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
),
cnt AS (
    SELECT id, COUNT(*) AS num
    FROM all_ids
    GROUP BY id
)
SELECT id, num
FROM cnt
WHERE num = (SELECT MAX(num) FROM cnt);
```
