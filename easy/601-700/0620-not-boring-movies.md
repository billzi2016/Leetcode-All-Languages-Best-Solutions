# 0620. Not Boring Movies

## Mysql

```mysql
SELECT *
FROM Cinema
WHERE id % 2 = 1
  AND description <> 'boring'
ORDER BY rating DESC;
```

## Mssql

```mssql
/* Write your T-SQL query statement below */
SELECT *
FROM Cinema
WHERE id % 2 = 1
  AND description <> 'boring'
ORDER BY rating DESC;
```

## Oraclesql

```oraclesql
/* Write your PL/SQL query statement below */
SELECT *
FROM Cinema
WHERE MOD(id, 2) = 1
  AND description <> 'boring'
ORDER BY rating DESC;
```

## Pythondata

```pythondata
import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    filtered = cinema[(cinema['id'] % 2 == 1) & (cinema['description'] != 'boring')]
    return filtered.sort_values(by='rating', ascending=False)
```

## Postgresql

```postgresql
SELECT *
FROM Cinema
WHERE id % 2 = 1
  AND description <> 'boring'
ORDER BY rating DESC;
```
