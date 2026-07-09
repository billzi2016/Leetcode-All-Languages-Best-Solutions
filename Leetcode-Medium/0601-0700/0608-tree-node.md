# 0608. Tree Node

## MySQL
```sql
SELECT 
    t.id,
    CASE
        WHEN t.p_id IS NULL THEN 'Root'
        WHEN COUNT(c.id) > 0 THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree t
LEFT JOIN Tree c ON c.p_id = t.id
GROUP BY t.id, t.p_id;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT
    t.id,
    CASE 
        WHEN t.p_id IS NULL THEN 'Root'
        WHEN c.cnt > 0      THEN 'Inner'
        ELSE                'Leaf'
    END AS type
FROM Tree t
LEFT JOIN (
    SELECT p_id, COUNT(*) AS cnt
    FROM Tree
    GROUP BY p_id
) c ON t.id = c.p_id;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT t.id,
       CASE
         WHEN t.p_id IS NULL THEN 'Root'
         WHEN EXISTS (SELECT 1 FROM Tree c WHERE c.p_id = t.id) THEN 'Inner'
         ELSE 'Leaf'
       END AS type
FROM   Tree t;
```

## PythonData
```python
import pandas as pd
import numpy as np

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    # Identify root nodes (no parent)
    is_root = tree['p_id'].isnull()
    # Identify nodes that have at least one child
    has_child = tree['id'].isin(tree['p_id'])
    
    node_type = np.where(
        is_root,
        'Root',
        np.where(~has_child, 'Leaf', 'Inner')
    )
    
    result = pd.DataFrame({
        'id': tree['id'],
        'type': node_type
    })
    return result[['id', 'type']]
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT 
    t.id,
    CASE
        WHEN t.p_id IS NULL THEN 'Root'
        WHEN EXISTS (SELECT 1 FROM Tree WHERE p_id = t.id) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree t;
```
