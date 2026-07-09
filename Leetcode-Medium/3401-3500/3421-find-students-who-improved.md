# 3421. Find Students Who Improved

## MySQL
```sql
# Write your MySQL query statement below
WITH first AS (
    SELECT student_id,
           subject,
           score AS first_score,
           ROW_NUMBER() OVER (PARTITION BY student_id, subject ORDER BY exam_date) AS rn
    FROM Scores
),
last AS (
    SELECT student_id,
           subject,
           score AS latest_score,
           ROW_NUMBER() OVER (PARTITION BY student_id, subject ORDER BY exam_date DESC) AS rn
    FROM Scores
)
SELECT f.student_id,
       f.subject,
       f.first_score,
       l.latest_score
FROM first f
JOIN last l
  ON f.student_id = l.student_id AND f.subject = l.subject
WHERE f.rn = 1
  AND l.rn = 1
  AND f.first_score < l.latest_score
ORDER BY f.student_id, f.subject;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
WITH FirstLast AS (
    SELECT
        student_id,
        subject,
        MIN(CONVERT(date, exam_date)) AS first_date,
        MAX(CONVERT(date, exam_date)) AS latest_date
    FROM Scores
    GROUP BY student_id, subject
)
SELECT
    s_first.student_id,
    s_first.subject,
    s_first.score AS first_score,
    s_last.score AS latest_score
FROM FirstLast fl
JOIN Scores s_first
  ON s_first.student_id = fl.student_id
 AND s_first.subject = fl.subject
 AND CONVERT(date, s_first.exam_date) = fl.first_date
JOIN Scores s_last
  ON s_last.student_id = fl.student_id
 AND s_last.subject = fl.subject
 AND CONVERT(date, s_last.exam_date) = fl.latest_date
WHERE s_last.score > s_first.score
ORDER BY s_first.student_id, s_first.subject;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT
    student_id,
    subject,
    MIN(score) KEEP (DENSE_RANK FIRST ORDER BY exam_date) AS first_score,
    MAX(score) KEEP (DENSE_RANK LAST  ORDER BY exam_date) AS latest_score
FROM Scores
GROUP BY
    student_id,
    subject
HAVING
    MAX(score) KEEP (DENSE_RANK LAST ORDER BY exam_date) >
    MIN(score) KEEP (DENSE_RANK FIRST ORDER BY exam_date)
ORDER BY
    student_id,
    subject;
```

## PythonData
```python
import pandas as pd

def find_students_who_improved(scores: pd.DataFrame) -> pd.DataFrame:
    # Ensure exam_date is datetime for proper ordering
    df = scores.copy()
    df["exam_date"] = pd.to_datetime(df["exam_date"])
    
    # Sort to get chronological first and last records per student & subject
    df_sorted = df.sort_values(["student_id", "subject", "exam_date"])
    
    # Group and extract first and latest scores
    grouped = df_sorted.groupby(["student_id", "subject"], as_index=False)
    first_scores = grouped.first()[["student_id", "subject", "score"]].rename(columns={"score": "first_score"})
    last_scores = grouped.last()[["student_id", "subject", "score"]].rename(columns={"score": "latest_score"})
    
    # Merge first and latest scores
    merged = pd.merge(first_scores, last_scores, on=["student_id", "subject"])
    
    # Keep only rows where the student improved
    improved = merged[merged["latest_score"] > merged["first_score"]]
    
    # Order by student_id then subject
    improved = improved.sort_values(["student_id", "subject"]).reset_index(drop=True)
    
    return improved[['student_id', 'subject', 'first_score', 'latest_score']]
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
WITH date_bounds AS (
    SELECT
        student_id,
        subject,
        MIN(exam_date) AS first_date,
        MAX(exam_date) AS last_date
    FROM Scores
    GROUP BY student_id, subject
),
score_pairs AS (
    SELECT
        s.student_id,
        s.subject,
        MAX(CASE WHEN s.exam_date = db.first_date THEN s.score END) AS first_score,
        MAX(CASE WHEN s.exam_date = db.last_date  THEN s.score END) AS latest_score
    FROM Scores s
    JOIN date_bounds db
      ON s.student_id = db.student_id AND s.subject = db.subject
    GROUP BY s.student_id, s.subject
)
SELECT
    student_id,
    subject,
    first_score,
    latest_score
FROM score_pairs
WHERE latest_score > first_score
ORDER BY student_id, subject;
```
