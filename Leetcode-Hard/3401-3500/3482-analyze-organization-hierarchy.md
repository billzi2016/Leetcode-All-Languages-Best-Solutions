# 3482. Analyze Organization Hierarchy

## MySQL
```sql
# Write your MySQL query statement below
WITH RECURSIVE hierarchy AS (
    SELECT
        employee_id,
        employee_name,
        manager_id,
        salary,
        CAST(employee_id AS CHAR(200)) AS path,
        1 AS lvl
    FROM Employees
    WHERE manager_id IS NULL
    UNION ALL
    SELECT
        e.employee_id,
        e.employee_name,
        e.manager_id,
        e.salary,
        CONCAT(h.path, ',', e.employee_id),
        h.lvl + 1
    FROM Employees e
    JOIN hierarchy h ON e.manager_id = h.employee_id
)
SELECT
    h.employee_id,
    h.employee_name,
    h.lvl AS level,
    COUNT(d.employee_id) - 1 AS team_size,
    SUM(d.salary) AS budget
FROM hierarchy h
JOIN hierarchy d ON FIND_IN_SET(h.employee_id, d.path) > 0
GROUP BY h.employee_id, h.employee_name, h.lvl
ORDER BY level ASC, budget DESC, employee_name ASC;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
WITH LevelCTE AS (
    SELECT
        employee_id,
        employee_name,
        manager_id,
        salary,
        1 AS lvl
    FROM Employees
    WHERE manager_id IS NULL

    UNION ALL

    SELECT
        e.employee_id,
        e.employee_name,
        e.manager_id,
        e.salary,
        p.lvl + 1
    FROM Employees e
    JOIN LevelCTE p ON e.manager_id = p.employee_id
),
AncDesc AS (
    SELECT
        employee_id AS anc,
        employee_id AS desc
    FROM Employees

    UNION ALL

    SELECT
        ad.anc,
        e.employee_id
    FROM AncDesc ad
    JOIN Employees e ON e.manager_id = ad.desc
)
SELECT
    a.anc AS employee_id,
    l.employee_name,
    l.lvl AS level,
    COUNT(a.desc) - 1 AS team_size,
    SUM(e2.salary) AS budget
FROM AncDesc a
JOIN LevelCTE l ON l.employee_id = a.anc
JOIN Employees e2 ON e2.employee_id = a.desc
GROUP BY a.anc, l.employee_name, l.lvl
ORDER BY level ASC, budget DESC, employee_name ASC;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT e.employee_id,
       e.employee_name,
       LEVEL AS level,
       (SELECT COUNT(*)
          FROM Employees d
         START WITH d.manager_id = e.employee_id
        CONNECT BY PRIOR d.employee_id = d.manager_id) AS team_size,
       (SELECT SUM(d.salary)
          FROM Employees d
         START WITH d.employee_id = e.employee_id
        CONNECT BY PRIOR d.employee_id = d.manager_id) AS budget
FROM Employees e
START WITH e.manager_id IS NULL
CONNECT BY PRIOR e.employee_id = e.manager_id
ORDER BY level ASC, budget DESC, employee_name ASC;
```

## PythonData
```python
import pandas as pd

def analyze_organization_hierarchy(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.copy().reset_index(drop=True)
    n = len(df)

    # map employee_id to row index
    id_to_idx = {eid: i for i, eid in enumerate(df["employee_id"])}

    # build parent and children relationships
    parent = [-1] * n
    children = [[] for _ in range(n)]
    for i, mgr in enumerate(df["manager_id"]):
        if pd.notna(mgr):
            p_idx = id_to_idx[int(mgr)]
            parent[i] = p_idx
            children[p_idx].append(i)

    # compute level (distance from root, root level = 1)
    level = [0] * n

    def get_level(idx: int) -> int:
        if level[idx]:
            return level[idx]
        if parent[idx] == -1:
            level[idx] = 1
        else:
            level[idx] = get_level(parent[idx]) + 1
        return level[idx]

    for i in range(n):
        get_level(i)

    # compute subtree size and budget via post‑order DFS
    subtree_size = [0] * n
    subtree_budget = [0] * n

    def dfs(idx: int) -> None:
        sz = 1
        bud = df.at[idx, "salary"]
        for c in children[idx]:
            dfs(c)
            sz += subtree_size[c]
            bud += subtree_budget[c]
        subtree_size[idx] = sz
        subtree_budget[idx] = bud

    for i in range(n):
        if parent[i] == -1:
            dfs(i)

    result = pd.DataFrame({
        "employee_id": df["employee_id"],
        "employee_name": df["employee_name"],
        "level": level,
        "team_size": [sz - 1 for sz in subtree_size],
        "budget": subtree_budget
    })

    result = result.sort_values(
        by=["level", "budget", "employee_name"],
        ascending=[True, False, True]
    ).reset_index(drop=True)

    return result
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
WITH RECURSIVE ancestors AS (
    SELECT employee_id AS anc,
           employee_id AS desc,
           salary
    FROM Employees
    UNION ALL
    SELECT a.anc,
           e.employee_id,
           e.salary
    FROM ancestors a
    JOIN Employees e ON e.manager_id = a.desc
),
levels AS (
    SELECT employee_id,
           1 AS level
    FROM Employees
    WHERE manager_id IS NULL
    UNION ALL
    SELECT e.employee_id,
           l.level + 1
    FROM Employees e
    JOIN levels l ON e.manager_id = l.employee_id
)
SELECT e.employee_id,
       e.employee_name,
       lv.level,
       COALESCE(ag.team_size, 0) AS team_size,
       ag.budget
FROM Employees e
JOIN levels lv ON e.employee_id = lv.employee_id
LEFT JOIN (
    SELECT anc AS employee_id,
           SUM(salary) AS budget,
           COUNT(*) - 1 AS team_size
    FROM ancestors
    GROUP BY anc
) ag ON e.employee_id = ag.employee_id
ORDER BY lv.level ASC, ag.budget DESC, e.employee_name ASC;
```
