# 3580. Find Consistently Improving Employees

## MySQL
```sql
# Write your MySQL query statement below
WITH ranked AS (
    SELECT 
        pr.employee_id,
        pr.rating,
        ROW_NUMBER() OVER (PARTITION BY pr.employee_id ORDER BY pr.review_date DESC) AS rn
    FROM performance_reviews pr
),
last_three AS (
    SELECT 
        employee_id,
        MAX(CASE WHEN rn = 1 THEN rating END) AS r_latest,
        MAX(CASE WHEN rn = 2 THEN rating END) AS r_mid,
        MAX(CASE WHEN rn = 3 THEN rating END) AS r_earliest,
        COUNT(*) AS cnt
    FROM ranked
    WHERE rn <= 3
    GROUP BY employee_id
    HAVING COUNT(*) = 3
)
SELECT 
    e.employee_id,
    e.name,
    (l.r_latest - l.r_earliest) AS improvement_score
FROM last_three l
JOIN employees e ON e.employee_id = l.employee_id
WHERE l.r_earliest < l.r_mid AND l.r_mid < l.r_latest
ORDER BY improvement_score DESC, e.name ASC;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
WITH ranked AS (
    SELECT
        pr.employee_id,
        e.name,
        pr.rating,
        ROW_NUMBER() OVER (PARTITION BY pr.employee_id ORDER BY pr.review_date DESC) AS rn
    FROM performance_reviews pr
    JOIN employees e ON pr.employee_id = e.employee_id
)
SELECT
    r.employee_id,
    r.name,
    MAX(CASE WHEN rn = 1 THEN rating END) - MAX(CASE WHEN rn = 3 THEN rating END) AS improvement_score
FROM ranked r
WHERE rn <= 3
GROUP BY r.employee_id, r.name
HAVING COUNT(*) = 3
   AND MAX(CASE WHEN rn = 1 THEN rating END) > MAX(CASE WHEN rn = 2 THEN rating END)
   AND MAX(CASE WHEN rn = 2 THEN rating END) > MAX(CASE WHEN rn = 3 THEN rating END)
ORDER BY improvement_score DESC, name ASC;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
WITH ranked AS (
    SELECT e.employee_id,
           e.name,
           r.rating,
           ROW_NUMBER() OVER (PARTITION BY e.employee_id ORDER BY r.review_date DESC) AS rn
    FROM employees e
    JOIN performance_reviews r ON e.employee_id = r.employee_id
),
agg AS (
    SELECT employee_id,
           name,
           MAX(CASE WHEN rn = 1 THEN rating END) AS latest_rating,
           MAX(CASE WHEN rn = 2 THEN rating END) AS mid_rating,
           MAX(CASE WHEN rn = 3 THEN rating END) AS earliest_rating,
           COUNT(*) AS cnt
    FROM ranked
    WHERE rn <= 3
    GROUP BY employee_id, name
)
SELECT employee_id,
       name,
       latest_rating - earliest_rating AS improvement_score
FROM agg
WHERE cnt = 3
  AND latest_rating > mid_rating
  AND mid_rating > earliest_rating
ORDER BY improvement_score DESC, name ASC;
```

## PythonData
```python
import pandas as pd

def find_consistently_improving_employees(employees: pd.DataFrame, performance_reviews: pd.DataFrame) -> pd.DataFrame:
    # Ensure dates are datetime
    reviews = performance_reviews.copy()
    if reviews['review_date'].dtype != 'datetime64[ns]':
        reviews['review_date'] = pd.to_datetime(reviews['review_date'])
    
    # Sort by employee and date (ascending)
    reviews = reviews.sort_values(['employee_id', 'review_date'])
    
    def evaluate(group: pd.DataFrame):
        if len(group) < 3:
            return None
        last_three = group.tail(3)
        ratings = last_three['rating'].values
        if ratings[0] < ratings[1] < ratings[2]:
            improvement = int(ratings[2] - ratings[0])
            return pd.Series({
                'employee_id': group['employee_id'].iloc[0],
                'improvement_score': improvement
            })
        return None
    
    result = reviews.groupby('employee_id', as_index=False).apply(evaluate).dropna()
    
    if result.empty:
        return pd.DataFrame(columns=['employee_id', 'name', 'improvement_score'])
    
    # Merge with employee names
    result = result.merge(employees[['employee_id', 'name']], on='employee_id')
    result = result[['employee_id', 'name', 'improvement_score']]
    
    # Sort as required
    result = result.sort_values(['improvement_score', 'name'], ascending=[False, True]).reset_index(drop=True)
    return result
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
WITH ranked AS (
    SELECT e.employee_id,
           e.name,
           r.rating,
           r.review_date,
           ROW_NUMBER() OVER (PARTITION BY e.employee_id ORDER BY r.review_date DESC) AS rn
    FROM employees e
    JOIN performance_reviews r ON e.employee_id = r.employee_id
),
last_three AS (
    SELECT employee_id, name, rating, review_date
    FROM ranked
    WHERE rn <= 3
)
SELECT employee_id,
       name,
       ratings[3] - ratings[1] AS improvement_score
FROM (
    SELECT employee_id,
           name,
           ARRAY_AGG(rating ORDER BY review_date ASC) AS ratings
    FROM last_three
    GROUP BY employee_id, name
) t
WHERE array_length(ratings, 1) = 3
  AND ratings[2] > ratings[1]
  AND ratings[3] > ratings[2]
ORDER BY improvement_score DESC, name ASC;
```
