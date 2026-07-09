# 1341. Movie Rating

## MySQL
```sql
# Write your MySQL query statement below
WITH user_cnt AS (
    SELECT user_id, COUNT(*) AS cnt
    FROM MovieRating
    GROUP BY user_id
), max_user AS (
    SELECT MAX(cnt) AS mx FROM user_cnt
), best_user AS (
    SELECT u.name
    FROM Users u
    JOIN user_cnt uc ON u.user_id = uc.user_id
    CROSS JOIN max_user mu
    WHERE uc.cnt = mu.mx
    ORDER BY u.name
    LIMIT 1
),
movie_feb_avg AS (
    SELECT movie_id, AVG(rating) AS avg_rating
    FROM MovieRating
    WHERE MONTH(created_at) = 2
    GROUP BY movie_id
), max_movie AS (
    SELECT MAX(avg_rating) AS mx FROM movie_feb_avg
), best_movie AS (
    SELECT m.title
    FROM Movies m
    JOIN movie_feb_avg ma ON m.movie_id = ma.movie_id
    CROSS JOIN max_movie mm
    WHERE ma.avg_rating = mm.mx
    ORDER BY m.title
    LIMIT 1
)
SELECT name AS results FROM best_user
UNION ALL
SELECT title AS results FROM best_movie;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
WITH UserCounts AS (
    SELECT u.name, COUNT(*) AS cnt
    FROM Users u
    JOIN MovieRating mr ON u.user_id = mr.user_id
    GROUP BY u.name
),
TopUser AS (
    SELECT TOP (1) name
    FROM UserCounts
    ORDER BY cnt DESC, name ASC
),
MovieAvg AS (
    SELECT m.title, AVG(CAST(r.rating AS FLOAT)) AS avg_rating
    FROM Movies m
    JOIN MovieRating r ON m.movie_id = r.movie_id
    WHERE MONTH(r.created_at) = 2
    GROUP BY m.title
),
TopMovie AS (
    SELECT TOP (1) title
    FROM MovieAvg
    ORDER BY avg_rating DESC, title ASC
)
SELECT name AS results FROM TopUser
UNION ALL
SELECT title FROM TopMovie;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
WITH user_counts AS (
    SELECT u.name,
           COUNT(DISTINCT mr.movie_id) AS cnt
    FROM Users u
    JOIN MovieRating mr ON u.user_id = mr.user_id
    GROUP BY u.name
),
max_user_cnt AS (
    SELECT MAX(cnt) AS maxcnt FROM user_counts
),
top_user AS (
    SELECT name
    FROM (
        SELECT uc.name,
               ROW_NUMBER() OVER (ORDER BY uc.name) rn
        FROM user_counts uc, max_user_cnt muc
        WHERE uc.cnt = muc.maxcnt
    )
    WHERE rn = 1
),
movie_avg AS (
    SELECT m.title,
           AVG(mr.rating) AS avg_rating
    FROM Movies m
    JOIN MovieRating mr ON m.movie_id = mr.movie_id
    WHERE EXTRACT(MONTH FROM mr.created_at) = 2
    GROUP BY m.title
),
max_movie_avg AS (
    SELECT MAX(avg_rating) AS maxavg FROM movie_avg
),
top_movie AS (
    SELECT title
    FROM (
        SELECT ma.title,
               ROW_NUMBER() OVER (ORDER BY ma.title) rn
        FROM movie_avg ma, max_movie_avg mma
        WHERE ma.avg_rating = mma.maxavg
    )
    WHERE rn = 1
)
SELECT name AS results FROM top_user
UNION ALL
SELECT title FROM top_movie;
```

## PythonData
```python
import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    # User with most ratings (lexicographically smallest name on tie)
    user_counts = movie_rating.groupby('user_id').size().reset_index(name='cnt')
    max_cnt = user_counts['cnt'].max()
    top_users = user_counts[user_counts['cnt'] == max_cnt]['user_id']
    candidate_names = users[users['user_id'].isin(top_users)]['name']
    best_user = candidate_names.min()

    # Movie with highest average rating in February (lexicographically smallest title on tie)
    mr = movie_rating.copy()
    mr['created_at'] = pd.to_datetime(mr['created_at'])
    feb_ratings = mr[mr['created_at'].dt.month == 2]
    avg_rating = feb_ratings.groupby('movie_id')['rating'].mean().reset_index()
    max_avg = avg_rating['rating'].max()
    top_movies = avg_rating[avg_rating['rating'] == max_avg]['movie_id']
    candidate_titles = movies[movies['movie_id'].isin(top_movies)]['title']
    best_movie = candidate_titles.min()

    return pd.DataFrame({'results': [best_user, best_movie]})
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
WITH user_counts AS (
    SELECT mr.user_id, COUNT(DISTINCT mr.movie_id) AS cnt
    FROM MovieRating mr
    GROUP BY mr.user_id
),
top_user AS (
    SELECT u.name
    FROM user_counts uc
    JOIN Users u ON u.user_id = uc.user_id
    ORDER BY uc.cnt DESC, u.name ASC
    LIMIT 1
),
movie_avg_feb AS (
    SELECT mr.movie_id, AVG(mr.rating) AS avg_rating
    FROM MovieRating mr
    WHERE EXTRACT(MONTH FROM mr.created_at) = 2
    GROUP BY mr.movie_id
),
top_movie AS (
    SELECT m.title
    FROM movie_avg_feb maf
    JOIN Movies m ON m.movie_id = maf.movie_id
    ORDER BY maf.avg_rating DESC, m.title ASC
    LIMIT 1
)
SELECT name AS results FROM top_user
UNION ALL
SELECT title AS results FROM top_movie;
```
