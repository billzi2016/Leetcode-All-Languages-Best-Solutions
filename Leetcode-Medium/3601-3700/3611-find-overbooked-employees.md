# 3611. Find Overbooked Employees

## MySQL
```sql
# Write your MySQL query statement below
SELECT 
    e.employee_id,
    e.employee_name,
    e.department,
    COUNT(*) AS meeting_heavy_weeks
FROM (
    SELECT 
        employee_id,
        YEARWEEK(meeting_date, 1) AS wk
    FROM meetings
    GROUP BY employee_id, YEARWEEK(meeting_date, 1)
    HAVING SUM(duration_hours) > 20
) mh
JOIN employees e ON e.employee_id = mh.employee_id
GROUP BY e.employee_id, e.employee_name, e.department
ORDER BY meeting_heavy_weeks DESC, e.employee_name ASC;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
WITH weekly_meetings AS (
    SELECT 
        m.employee_id,
        DATEPART(year, m.meeting_date) AS yr,
        DATEPART(week, m.meeting_date) AS wk,
        SUM(m.duration_hours) AS total_hours
    FROM meetings m
    GROUP BY 
        m.employee_id,
        DATEPART(year, m.meeting_date),
        DATEPART(week, m.meeting_date)
    HAVING SUM(m.duration_hours) > 20   -- more than 50% of a standard 40‑hour week
)
SELECT 
    e.employee_id,
    e.employee_name,
    e.department,
    COUNT(*) AS meeting_heavy_weeks
FROM weekly_meetings wm
JOIN employees e ON e.employee_id = wm.employee_id
GROUP BY 
    e.employee_id,
    e.employee_name,
    e.department
ORDER BY 
    meeting_heavy_weeks DESC,
    e.employee_name ASC;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
WITH weekly_meetings AS (
    SELECT
        e.employee_id,
        TRUNC(m.meeting_date, 'IW') AS week_start,
        SUM(m.duration_hours) AS total_hours
    FROM employees e
    JOIN meetings m ON e.employee_id = m.employee_id
    GROUP BY e.employee_id, TRUNC(m.meeting_date, 'IW')
),
heavy_weeks AS (
    SELECT
        employee_id,
        COUNT(*) AS meeting_heavy_weeks
    FROM weekly_meetings
    WHERE total_hours > 20   -- more than 50% of a standard 40‑hour work week
    GROUP BY employee_id
)
SELECT
    e.employee_id,
    e.employee_name,
    e.department,
    h.meeting_heavy_weeks
FROM heavy_weeks h
JOIN employees e ON e.employee_id = h.employee_id
ORDER BY h.meeting_heavy_weeks DESC, e.employee_name ASC;
```

## PythonData
```python
import pandas as pd

def find_overbooked_employees(employees: pd.DataFrame, meetings: pd.DataFrame) -> pd.DataFrame:
    # Ensure meeting_date is datetime
    if meetings.empty:
        return pd.DataFrame(columns=["employee_id", "employee_name", "department", "meeting_heavy_weeks"])
    meetings = meetings.copy()
    meetings["meeting_date"] = pd.to_datetime(meetings["meeting_date"])

    # Define week identifier (ISO year and week)
    iso = meetings["meeting_date"].dt.isocalendar()
    meetings["year_week"] = iso["year"] * 100 + iso["week"]

    # Sum meeting durations per employee per week
    weekly_sum = (
        meetings.groupby(["employee_id", "year_week"], as_index=False)["duration_hours"]
        .sum()
    )

    # Threshold: more than 50% of a standard 40‑hour work week => >20 hours
    heavy_weeks = weekly_sum[weekly_sum["duration_hours"] > 20]

    # Count heavy weeks per employee
    heavy_counts = (
        heavy_weeks.groupby("employee_id", as_index=False)
        .size()
        .rename(columns={"size": "meeting_heavy_weeks"})
    )

    # Join with employees info
    result = pd.merge(
        heavy_counts,
        employees[["employee_id", "employee_name", "department"]],
        on="employee_id",
        how="inner",
    )

    # Sort by meeting_heavy_weeks desc, then employee_name asc
    result = result.sort_values(
        by=["meeting_heavy_weeks", "employee_name"], ascending=[False, True]
    ).reset_index(drop=True)

    # Reorder columns
    return result[["employee_id", "employee_name", "department", "meeting_heavy_weeks"]]
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
WITH weekly_meetings AS (
    SELECT
        e.employee_id,
        DATE_TRUNC('week', m.meeting_date)::date AS week_start,
        SUM(m.duration_hours) AS total_hours
    FROM employees e
    JOIN meetings m ON e.employee_id = m.employee_id
    GROUP BY e.employee_id, week_start
),
overbooked_weeks AS (
    SELECT
        employee_id,
        COUNT(*) AS meeting_heavy_weeks
    FROM weekly_meetings
    WHERE total_hours > 20
    GROUP BY employee_id
)
SELECT
    e.employee_id,
    e.employee_name,
    e.department,
    o.meeting_heavy_weeks
FROM overbooked_weeks o
JOIN employees e ON e.employee_id = o.employee_id
WHERE o.meeting_heavy_weeks >= 2
ORDER BY o.meeting_heavy_weeks DESC, e.employee_name ASC;
```
