# 3564. Seasonal Sales Analysis

## MySQL
```sql
# Write your MySQL query statement below
WITH sales_by_season AS (
    SELECT 
        CASE 
            WHEN MONTH(s.sale_date) IN (3,4,5) THEN 'Spring'
            WHEN MONTH(s.sale_date) IN (6,7,8) THEN 'Summer'
            WHEN MONTH(s.sale_date) IN (9,10,11) THEN 'Fall'
            ELSE 'Winter'
        END AS season,
        p.category,
        SUM(s.quantity) AS total_quantity,
        SUM(s.quantity * s.price) AS total_revenue
    FROM sales s
    JOIN products p ON s.product_id = p.product_id
    GROUP BY season, p.category
),
ranked_season AS (
    SELECT 
        season,
        category,
        total_quantity,
        total_revenue,
        ROW_NUMBER() OVER (PARTITION BY season ORDER BY total_quantity DESC, total_revenue DESC) AS rn
    FROM sales_by_season
)
SELECT 
    season,
    category,
    total_quantity,
    total_revenue
FROM ranked_season
WHERE rn = 1
ORDER BY season;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
WITH sales_agg AS (
    SELECT 
        CASE 
            WHEN MONTH(s.sale_date) IN (12,1,2) THEN 'Winter'
            WHEN MONTH(s.sale_date) IN (3,4,5)  THEN 'Spring'
            WHEN MONTH(s.sale_date) IN (6,7,8)  THEN 'Summer'
            ELSE 'Fall' 
        END AS season,
        p.category,
        SUM(s.quantity) AS total_quantity,
        SUM(s.quantity * s.price) AS total_revenue
    FROM sales s
    JOIN products p ON s.product_id = p.product_id
    GROUP BY 
        CASE 
            WHEN MONTH(s.sale_date) IN (12,1,2) THEN 'Winter'
            WHEN MONTH(s.sale_date) IN (3,4,5)  THEN 'Spring'
            WHEN MONTH(s.sale_date) IN (6,7,8)  THEN 'Summer'
            ELSE 'Fall' 
        END,
        p.category
),
ranked AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY season 
                              ORDER BY total_quantity DESC, total_revenue DESC) AS rn
    FROM sales_agg
)
SELECT 
    season,
    category,
    total_quantity,
    CAST(total_revenue AS decimal(10,2)) AS total_revenue
FROM ranked
WHERE rn = 1
ORDER BY CASE season
            WHEN 'Winter' THEN 1
            WHEN 'Spring' THEN 2
            WHEN 'Summer' THEN 3
            WHEN 'Fall'   THEN 4
         END;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
WITH sales_with_season AS (
    SELECT s.*,
        CASE 
            WHEN EXTRACT(MONTH FROM s.sale_date) IN (12, 1, 2) THEN 'Winter'
            WHEN EXTRACT(MONTH FROM s.sale_date) IN (3, 4, 5)  THEN 'Spring'
            WHEN EXTRACT(MONTH FROM s.sale_date) IN (6, 7, 8)  THEN 'Summer'
            ELSE 'Fall'
        END AS season
    FROM sales s
)
SELECT season,
       category,
       total_quantity,
       total_revenue
FROM (
    SELECT sws.season,
           p.category,
           SUM(sws.quantity)                         AS total_quantity,
           SUM(sws.quantity * sws.price)             AS total_revenue,
           ROW_NUMBER() OVER (PARTITION BY sws.season
                              ORDER BY SUM(sws.quantity) DESC,
                                       SUM(sws.quantity * sws.price) DESC) AS rn
    FROM sales_with_season sws
    JOIN products p ON sws.product_id = p.product_id
    GROUP BY sws.season, p.category
)
WHERE rn = 1
ORDER BY season;
```

## PythonData
```python
import pandas as pd

def seasonal_sales_analysis(products: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(products[['product_id', 'category']], on='product_id', how='inner')
    df['sale_date'] = pd.to_datetime(df['sale_date'])
    month = df['sale_date'].dt.month

    def get_season(m):
        if m in (12, 1, 2):
            return 'Winter'
        if m in (3, 4, 5):
            return 'Spring'
        if m in (6, 7, 8):
            return 'Summer'
        return 'Fall'

    df['season'] = month.apply(get_season)
    df['revenue'] = df['quantity'] * df['price']

    agg = (
        df.groupby(['season', 'category'], as_index=False)
          .agg(total_quantity=('quantity', 'sum'), total_revenue=('revenue', 'sum'))
    )

    agg_sorted = agg.sort_values(
        ['season', 'total_quantity', 'total_revenue'],
        ascending=[True, False, False]
    )
    result = agg_sorted.groupby('season', as_index=False).first()
    result = result[['season', 'category', 'total_quantity', 'total_revenue']]
    result = result.sort_values('season')
    return result
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
WITH sales_category AS (
    SELECT 
        CASE 
            WHEN EXTRACT(MONTH FROM s.sale_date) IN (12,1,2) THEN 'Winter'
            WHEN EXTRACT(MONTH FROM s.sale_date) IN (3,4,5)  THEN 'Spring'
            WHEN EXTRACT(MONTH FROM s.sale_date) IN (6,7,8)  THEN 'Summer'
            ELSE 'Fall'
        END AS season,
        p.category,
        SUM(s.quantity) AS total_quantity,
        SUM(s.quantity * s.price) AS total_revenue
    FROM sales s
    JOIN products p ON s.product_id = p.product_id
    GROUP BY season, p.category
),
ranked AS (
    SELECT 
        season,
        category,
        total_quantity,
        total_revenue,
        ROW_NUMBER() OVER (PARTITION BY season 
                           ORDER BY total_quantity DESC, total_revenue DESC) AS rn
    FROM sales_category
)
SELECT 
    season,
    category,
    total_quantity,
    ROUND(total_revenue::numeric, 2) AS total_revenue
FROM ranked
WHERE rn = 1
ORDER BY season;
```
