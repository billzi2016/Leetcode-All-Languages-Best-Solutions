# 3586. Find COVID Recovery Patients

## MySQL
```sql
# Write your MySQL query statement below
WITH first_pos AS (
    SELECT patient_id, MIN(test_date) AS pos_date
    FROM covid_tests
    WHERE result = 'Positive'
    GROUP BY patient_id
),
first_neg_after AS (
    SELECT ct.patient_id, MIN(ct.test_date) AS neg_date
    FROM covid_tests ct
    JOIN first_pos fp ON ct.patient_id = fp.patient_id
    WHERE ct.result = 'Negative' AND ct.test_date > fp.pos_date
    GROUP BY ct.patient_id
)
SELECT p.patient_id,
       p.patient_name,
       p.age,
       DATEDIFF(fn.neg_date, fp.pos_date) AS recovery_time
FROM patients p
JOIN first_pos fp ON p.patient_id = fp.patient_id
JOIN first_neg_after fn ON p.patient_id = fn.patient_id
ORDER BY recovery_time ASC, patient_name ASC;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
WITH first_positive AS (
    SELECT
        patient_id,
        MIN(test_date) AS pos_date
    FROM covid_tests
    WHERE result = 'Positive'
    GROUP BY patient_id
),
first_negative_after_pos AS (
    SELECT
        ct.patient_id,
        MIN(ct.test_date) AS neg_date
    FROM covid_tests ct
    JOIN first_positive fp ON ct.patient_id = fp.patient_id
    WHERE ct.result = 'Negative' AND ct.test_date > fp.pos_date
    GROUP BY ct.patient_id
)
SELECT
    p.patient_id,
    pt.patient_name,
    pt.age,
    DATEDIFF(day, p.pos_date, n.neg_date) AS recovery_time
FROM first_positive p
JOIN first_negative_after_pos n ON p.patient_id = n.patient_id
JOIN patients pt ON pt.patient_id = p.patient_id
ORDER BY recovery_time ASC, patient_name ASC;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
WITH first_positive AS (
    SELECT patient_id, MIN(test_date) AS pos_date
    FROM covid_tests
    WHERE result = 'Positive'
    GROUP BY patient_id
),
first_negative_after_pos AS (
    SELECT ct.patient_id, MIN(ct.test_date) AS neg_date
    FROM covid_tests ct
    JOIN first_positive fp ON ct.patient_id = fp.patient_id
    WHERE ct.result = 'Negative' AND ct.test_date > fp.pos_date
    GROUP BY ct.patient_id
)
SELECT p.patient_id,
       p.patient_name,
       p.age,
       (fn.neg_date - fp.pos_date) AS recovery_time
FROM patients p
JOIN first_positive fp ON p.patient_id = fp.patient_id
JOIN first_negative_after_pos fn ON p.patient_id = fn.patient_id
ORDER BY recovery_time ASC, p.patient_name ASC;
```

## PythonData
```python
import pandas as pd

def find_covid_recovery_patients(patients: pd.DataFrame, covid_tests: pd.DataFrame) -> pd.DataFrame:
    tests = covid_tests.copy()
    tests['test_date'] = pd.to_datetime(tests['test_date'])
    
    # earliest positive per patient
    pos = (
        tests[tests['result'] == 'Positive']
        .groupby('patient_id', as_index=False)['test_date']
        .min()
        .rename(columns={'test_date': 'pos_date'})
    )
    
    # all negatives
    neg = tests[tests['result'] == 'Negative'][['patient_id', 'test_date']]
    
    # join and keep negatives after the earliest positive
    merged = pd.merge(pos, neg, on='patient_id')
    filtered = merged[merged['test_date'] > merged['pos_date']]
    
    # earliest qualifying negative per patient
    first_neg = (
        filtered.groupby('patient_id', as_index=False)['test_date']
        .min()
        .rename(columns={'test_date': 'neg_date'})
    )
    
    # combine positive and corresponding negative dates
    rec = pd.merge(pos, first_neg, on='patient_id')
    rec['recovery_time'] = (rec['neg_date'] - rec['pos_date']).dt.days
    
    # attach patient details
    result = pd.merge(rec, patients, on='patient_id')
    result = result[['patient_id', 'patient_name', 'age', 'recovery_time']]
    
    # order as required
    result = result.sort_values(['recovery_time', 'patient_name']).reset_index(drop=True)
    return result
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
WITH pos AS (
    SELECT p.patient_id,
           p.patient_name,
           p.age,
           ct.test_date AS pos_date
    FROM patients p
    JOIN covid_tests ct
      ON p.patient_id = ct.patient_id
    WHERE ct.result = 'Positive'
),
first_neg AS (
    SELECT p.patient_id,
           p.patient_name,
           p.age,
           p.pos_date,
           n.neg_date,
           ROW_NUMBER() OVER (PARTITION BY p.patient_id ORDER BY p.pos_date) AS rn
    FROM pos p
    JOIN LATERAL (
        SELECT ct2.test_date AS neg_date
        FROM covid_tests ct2
        WHERE ct2.patient_id = p.patient_id
          AND ct2.result = 'Negative'
          AND ct2.test_date > p.pos_date
        ORDER BY ct2.test_date
        LIMIT 1
    ) n ON true
)
SELECT patient_id,
       patient_name,
       age,
       (neg_date - pos_date) AS recovery_time
FROM first_neg
WHERE rn = 1
ORDER BY recovery_time, patient_name;
```
