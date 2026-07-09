# 1251. Average Selling Price

## MySQL
```sql
# Write your MySQL query statement below
SELECT p.product_id,
       IFNULL(ROUND(s.total_rev / s.total_units, 2), 0) AS average_price
FROM (SELECT DISTINCT product_id FROM Prices) p
LEFT JOIN (
    SELECT us.product_id,
           SUM(us.units * pr.price) AS total_rev,
           SUM(us.units) AS total_units
    FROM UnitsSold us
    JOIN Prices pr
      ON us.product_id = pr.product_id
     AND us.purchase_date BETWEEN pr.start_date AND pr.end_date
    GROUP BY us.product_id
) s ON p.product_id = s.product_id;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
WITH SalesAgg AS (
    SELECT 
        p.product_id,
        SUM(u.units * p.price) AS total_revenue,
        SUM(u.units) AS total_units
    FROM Prices p
    JOIN UnitsSold u
      ON p.product_id = u.product_id
     AND u.purchase_date BETWEEN p.start_date AND p.end_date
    GROUP BY p.product_id
)
SELECT 
    p.product_id,
    CASE 
        WHEN sa.total_units IS NULL OR sa.total_units = 0 THEN 0
        ELSE ROUND(sa.total_revenue * 1.0 / sa.total_units, 2)
    END AS average_price
FROM (SELECT DISTINCT product_id FROM Prices) p
LEFT JOIN SalesAgg sa ON p.product_id = sa.product_id;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
WITH sales AS (
    SELECT u.product_id,
           SUM(u.units * p.price) AS total_revenue,
           SUM(u.units)          AS total_units
    FROM UnitsSold u
    JOIN Prices p
      ON u.product_id = p.product_id
     AND u.purchase_date BETWEEN p.start_date AND p.end_date
    GROUP BY u.product_id
),
all_products AS (
    SELECT product_id FROM Prices
    UNION
    SELECT product_id FROM UnitsSold
)
SELECT ap.product_id,
       ROUND(COALESCE(s.total_revenue / NULLIF(s.total_units, 0), 0), 2) AS average_price
FROM all_products ap
LEFT JOIN sales s ON ap.product_id = s.product_id;
```

## PythonData
```python
import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    # Ensure date columns are datetime
    if 'start_date' in prices.columns:
        prices['start_date'] = pd.to_datetime(prices['start_date'])
    if 'end_date' in prices.columns:
        prices['end_date'] = pd.to_datetime(prices['end_date'])
    if 'purchase_date' in units_sold.columns:
        units_sold['purchase_date'] = pd.to_datetime(units_sold['purchase_date'])

    # Join on product_id and filter by date range
    merged = units_sold.merge(prices, on='product_id', how='left')
    mask = (merged['purchase_date'] >= merged['start_date']) & (merged['purchase_date'] <= merged['end_date'])
    valid = merged[mask].copy()

    # Compute total price and total units per product
    if not valid.empty:
        valid['total_price'] = valid['price'] * valid['units']
        agg = (
            valid.groupby('product_id')
                .agg({'total_price': 'sum', 'units': 'sum'})
                .reset_index()
        )
        agg['average_price'] = (agg['total_price'] / agg['units']).round(2)
    else:
        agg = pd.DataFrame(columns=['product_id', 'average_price'])

    # Include all products, fill missing averages with 0
    all_products = pd.DataFrame(
        {'product_id': pd.concat([prices['product_id'], units_sold['product_id']]).unique()}
    )
    result = all_products.merge(agg[['product_id', 'average_price']], on='product_id', how='left')
    result['average_price'] = result['average_price'].fillna(0)

    return result[['product_id', 'average_price']]
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
WITH revenue AS (
    SELECT us.product_id,
           SUM(p.price * us.units) AS total_rev,
           SUM(us.units) AS total_units
    FROM UnitsSold us
    JOIN Prices p
      ON us.product_id = p.product_id
     AND us.purchase_date BETWEEN p.start_date AND p.end_date
    GROUP BY us.product_id
),
all_products AS (
    SELECT product_id FROM Prices
    UNION
    SELECT product_id FROM UnitsSold
)
SELECT ap.product_id,
       COALESCE(ROUND(r.total_rev::numeric / NULLIF(r.total_units, 0), 2), 0) AS average_price
FROM all_products ap
LEFT JOIN revenue r ON ap.product_id = r.product_id;
```
