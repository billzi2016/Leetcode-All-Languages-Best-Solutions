# 3617. Find Students with Study Spiral Pattern

## MySQL
```sql
# Write your MySQL query statement below
WITH ordered AS (
    SELECT ss.*,
           ROW_NUMBER() OVER (PARTITION BY student_id ORDER BY session_date, session_id) AS rn
    FROM study_sessions ss
),
first_occurrence AS (
    SELECT student_id,
           subject,
           MIN(rn) AS first_rn
    FROM ordered
    GROUP BY student_id, subject
),
subject_order AS (
    SELECT student_id,
           subject,
           DENSE_RANK() OVER (PARTITION BY student_id ORDER BY first_rn) AS seq_order,
           COUNT(*) OVER (PARTITION BY student_id) AS distinct_cnt
    FROM first_occurrence
),
joined AS (
    SELECT o.student_id,
           o.rn,
           o.subject,
           o.hours_studied,
           so.seq_order,
           so.distinct_cnt
    FROM ordered o
    JOIN subject_order so
      ON o.student_id = so.student_id AND o.subject = so.subject
),
valid_students AS (
    SELECT student_id,
           MAX(distinct_cnt) AS cycle_length,
           SUM(hours_studied) AS total_study_hours,
           SUM(CASE WHEN seq_order = ((rn - 1) % distinct_cnt) + 1 THEN 0 ELSE 1 END) AS mismatches
    FROM joined
    GROUP BY student_id
    HAVING mismatches = 0 AND cycle_length >= 3
)
SELECT v.student_id,
       s.student_name,
       s.major,
       v.cycle_length,
       v.total_study_hours
FROM valid_students v
JOIN students s ON v.student_id = s.student_id
ORDER BY v.cycle_length DESC, v.total_study_hours DESC;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
WITH ordered AS (
    SELECT ss.*,
           ROW_NUMBER() OVER (PARTITION BY student_id ORDER BY session_date, session_id) AS rn
    FROM study_sessions ss
),
first_subj AS (
    SELECT student_id, subject AS first_subject
    FROM ordered
    WHERE rn = 1
),
candidate_len AS (
    SELECT o.student_id,
           MIN(o.rn - 1) AS cycle_length
    FROM ordered o
    JOIN first_subj f ON o.student_id = f.student_id
    WHERE o.rn > 1 AND o.subject = f.first_subject
    GROUP BY o.student_id
),
cnts AS (
    SELECT student_id, COUNT(*) AS total_sessions
    FROM ordered
    GROUP BY student_id
),
valid_students AS (
    SELECT c.student_id,
           c.cycle_length
    FROM candidate_len c
    JOIN cnts ct ON c.student_id = ct.student_id
    WHERE c.cycle_length > 2
      AND ct.total_sessions >= 2 * c.cycle_length
      AND NOT EXISTS (
          SELECT 1
          FROM ordered a
          JOIN ordered b
            ON a.student_id = b.student_id
           AND a.rn = b.rn + c.cycle_length
          WHERE a.student_id = c.student_id
            AND a.subject <> b.subject
      )
)
SELECT v.student_id,
       s.student_name,
       s.major,
       v.cycle_length,
       SUM(ss.hours_studied) AS total_study_hours
FROM valid_students v
JOIN students s ON v.student_id = s.student_id
JOIN study_sessions ss ON ss.student_id = v.student_id
GROUP BY v.student_id, s.student_name, s.major, v.cycle_length
ORDER BY v.cycle_length DESC, total_study_hours DESC;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
WITH ordered AS (
  SELECT s.student_id,
         s.student_name,
         s.major,
         ss.session_id,
         ss.subject,
         ss.hours_studied,
         ROW_NUMBER() OVER (PARTITION BY s.student_id ORDER BY ss.session_date, ss.session_id) rn,
         COUNT(*) OVER (PARTITION BY s.student_id) total_sessions,
         SUM(ss.hours_studied) OVER (PARTITION BY s.student_id) total_hours,
         COUNT(DISTINCT ss.subject) OVER (PARTITION BY s.student_id) distinct_cnt
  FROM students s
  JOIN study_sessions ss ON s.student_id = ss.student_id
),
cycle_subjects AS (
  SELECT student_id, rn, subject
  FROM ordered
  WHERE rn <= distinct_cnt
),
check_match AS (
  SELECT o.student_id,
         o.distinct_cnt   AS cycle_length,
         o.total_hours    AS total_study_hours,
         o.total_sessions,
         MIN(CASE WHEN o.subject = cs.subject THEN 1 ELSE 0 END) AS all_match
  FROM ordered o
  JOIN cycle_subjects cs
    ON o.student_id = cs.student_id
   AND MOD(o.rn - 1, o.distinct_cnt) + 1 = cs.rn
  GROUP BY o.student_id, o.distinct_cnt, o.total_hours, o.total_sessions
)
SELECT s.student_id,
       s.student_name,
       s.major,
       c.cycle_length,
       c.total_study_hours
FROM check_match c
JOIN students s ON s.student_id = c.student_id
WHERE c.all_match = 1
  AND MOD(c.total_sessions, c.cycle_length) = 0
  AND c.cycle_length >= 3
ORDER BY c.cycle_length DESC,
         c.total_study_hours DESC;
```

## PythonData
```python
import pandas as pd

def find_study_spiral_pattern(students: pd.DataFrame, study_sessions: pd.DataFrame) -> pd.DataFrame:
    # Prepare sessions sorted by date (and session_id for deterministic order)
    sess = study_sessions.sort_values(['student_id', 'session_date', 'session_id'])
    
    def analyze(group):
        subjects = group['subject'].tolist()
        n = len(subjects)
        if n < 3:  # need at least one full cycle of length >=3
            return None
        # find minimal period L that divides n and repeats
        for L in range(1, n + 1):
            if n % L != 0:
                continue
            pattern = subjects[:L]
            ok = True
            for i in range(n):
                if subjects[i] != pattern[i % L]:
                    ok = False
                    break
            if ok:
                return L
        return None

    # Group by student and compute cycle length
    results = []
    grouped = sess.groupby('student_id')
    for student_id, group in grouped:
        L = analyze(group)
        if L is not None and L >= 3:
            total_hours = group['hours_studied'].sum()
            stu_info = students.loc[students['student_id'] == student_id].iloc[0]
            results.append({
                'student_id': student_id,
                'student_name': stu_info['student_name'],
                'major': stu_info['major'],
                'cycle_length': L,
                'total_study_hours': total_hours
            })
    if not results:
        return pd.DataFrame(columns=['student_id','student_name','major','cycle_length','total_study_hours'])
    
    res_df = pd.DataFrame(results)
    res_df = res_df.sort_values(['cycle_length', 'total_study_hours'], ascending=[False, False])
    # Ensure column order
    return res_df[['student_id', 'student_name', 'major', 'cycle_length', 'total_study_hours']]
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
WITH ordered AS (
    SELECT ss.student_id,
           ss.subject,
           ss.hours_studied,
           ROW_NUMBER() OVER (PARTITION BY ss.student_id ORDER BY ss.session_date, ss.session_id) AS rn,
           COUNT(*) OVER (PARTITION BY ss.student_id) AS cnt
    FROM study_sessions ss
),
candidates AS (
    SELECT student_id,
           cnt,
           generate_series(3, (cnt/2)::int) AS L
    FROM (SELECT DISTINCT student_id, cnt FROM ordered) o
    WHERE cnt >= 6
),
mismatches AS (
    SELECT c.student_id, c.L
    FROM candidates c
    JOIN ordered s ON s.student_id = c.student_id
    LEFT JOIN ordered ref
        ON ref.student_id = c.student_id
       AND ref.rn = ((s.rn - 1) % c.L) + 1
    WHERE s.subject <> ref.subject
),
valid_cycles AS (
    SELECT c.student_id, c.L
    FROM candidates c
    LEFT JOIN mismatches m
        ON m.student_id = c.student_id AND m.L = c.L
    WHERE m.student_id IS NULL
),
min_cycle AS (
    SELECT student_id, MIN(L) AS cycle_length
    FROM valid_cycles
    GROUP BY student_id
)
SELECT s.student_id,
       s.student_name,
       s.major,
       mc.cycle_length,
       ROUND(SUM(ss.hours_studied)::numeric, 1) AS total_study_hours
FROM min_cycle mc
JOIN students s ON s.student_id = mc.student_id
JOIN study_sessions ss ON ss.student_id = mc.student_id
GROUP BY s.student_id, s.student_name, s.major, mc.cycle_length
ORDER BY mc.cycle_length DESC, total_study_hours DESC;
```
