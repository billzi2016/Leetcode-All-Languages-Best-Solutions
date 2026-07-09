# 1683. Invalid Tweets

## MySQL
```sql
SELECT tweet_id
FROM Tweets
WHERE CHAR_LENGTH(content) > 15;
```

## MSSQL
```sql
SELECT tweet_id
FROM Tweets
WHERE LEN(content) > 15;
```

## OracleSQL
```sql
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;
```

## PythonData
```python
import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    mask = tweets["content"].astype(str).str.len() > 15
    return tweets.loc[mask, ["tweet_id"]].reset_index(drop=True)
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;
```
