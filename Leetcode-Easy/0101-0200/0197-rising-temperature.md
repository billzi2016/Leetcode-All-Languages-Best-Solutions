# 0197. Rising Temperature

## MySQL
```sql
SELECT w1.id
FROM Weather w1
JOIN Weather w2
  ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT
    w_cur.id
FROM
    Weather AS w_cur
JOIN
    Weather AS w_prev
    ON DATEDIFF(day, w_prev.recordDate, w_cur.recordDate) = 1
WHERE
    w_cur.temperature > w_prev.temperature;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT w1.id
FROM Weather w1
JOIN Weather w2 ON w1.recordDate = w2.recordDate + 1
WHERE w1.temperature > w2.temperature;
```

## PythonData
```python
import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    df = weather.copy()
    df['recordDate'] = pd.to_datetime(df['recordDate'])
    df = df.sort_values('recordDate')
    df['prev_temp'] = df['temperature'].shift(1)
    df['prev_date'] = df['recordDate'].shift(1)
    mask = (df['temperature'] > df['prev_temp']) & (df['recordDate'] - df['prev_date'] == pd.Timedelta(days=1))
    return df.loc[mask, ['id']]
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT w2.id
FROM Weather w1
JOIN Weather w2
  ON w2.recordDate = w1.recordDate + INTERVAL '1 day'
WHERE w2.temperature > w1.temperature;
```
