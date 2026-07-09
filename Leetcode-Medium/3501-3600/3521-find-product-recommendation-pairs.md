# 3521. Find Product Recommendation Pairs

## MySQL
```sql
SELECT
    p1.product_id AS product1_id,
    p2.product_id AS product2_id,
    i1.category   AS product1_category,
    i2.category   AS product2_category,
    COUNT(DISTINCT p1.user_id) AS customer_count
FROM ProductPurchases p1
JOIN ProductPurchases p2
  ON p1.user_id = p2.user_id
 AND p1.product_id < p2.product_id
JOIN ProductInfo i1 ON p1.product_id = i1.product_id
JOIN ProductInfo i2 ON p2.product_id = i2.product_id
GROUP BY p1.product_id, p2.product_id, i1.category, i2.category
HAVING COUNT(DISTINCT p1.user_id) >= 3
ORDER BY customer_count DESC, product1_id ASC, product2_id ASC;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT 
    a.product_id AS product1_id,
    b.product_id AS product2_id,
    i1.category   AS product1_category,
    i2.category   AS product2_category,
    COUNT(DISTINCT a.user_id) AS customer_count
FROM ProductPurchases a
JOIN ProductPurchases b
      ON a.user_id = b.user_id
     AND a.product_id < b.product_id
JOIN ProductInfo i1 ON a.product_id = i1.product_id
JOIN ProductInfo i2 ON b.product_id = i2.product_id
GROUP BY 
    a.product_id,
    b.product_id,
    i1.category,
    i2.category
HAVING COUNT(DISTINCT a.user_id) >= 3
ORDER BY 
    customer_count DESC,
    product1_id ASC,
    product2_id ASC;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT
    pp1.product_id   AS product1_id,
    pp2.product_id   AS product2_id,
    pi1.category     AS product1_category,
    pi2.category     AS product2_category,
    COUNT(DISTINCT pp1.user_id) AS customer_count
FROM ProductPurchases pp1
JOIN ProductPurchases pp2
      ON pp1.user_id = pp2.user_id
     AND pp1.product_id < pp2.product_id
JOIN ProductInfo pi1 ON pi1.product_id = pp1.product_id
JOIN ProductInfo pi2 ON pi2.product_id = pp2.product_id
GROUP BY
    pp1.product_id,
    pp2.product_id,
    pi1.category,
    pi2.category
HAVING COUNT(DISTINCT pp1.user_id) >= 3
ORDER BY
    customer_count DESC,
    product1_id ASC,
    product2_id ASC;
```

## PythonData
```python
import pandas as pd
from itertools import combinations

def find_product_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    # Keep distinct user-product pairs
    df = product_purchases[['user_id', 'product_id']].drop_duplicates()
    
    # Self join on user to generate product pairs per user
    merged = df.merge(df, on='user_id')
    # Keep only ordered pairs to avoid duplicates (product1 < product2)
    pairs = merged[merged['product_id_x'] < merged['product_id_y']][['product_id_x', 'product_id_y']]
    pairs = pairs.rename(columns={'product_id_x': 'product1_id', 'product_id_y': 'product2_id'})
    
    # Count distinct users for each pair
    counts = (
        df.merge(pairs, left_on='product_id', right_on='product1_id')
          .merge(df, left_on='user_id', right_on='user_id')
          .query('product_id_y == product2_id')
          .groupby(['product1_id', 'product2_id'])
          .size()
          .reset_index(name='customer_count')
    )
    
    # Filter pairs with at least 3 customers
    filtered = counts[counts['customer_count'] >= 3]
    
    if filtered.empty:
        return pd.DataFrame(columns=[
            'product1_id', 'product2_id',
            'product1_category', 'product2_category',
            'customer_count'
        ])
    
    # Add category information
    result = filtered.merge(
        product_info[['product_id', 'category']],
        left_on='product1_id',
        right_on='product_id',
        how='left'
    ).rename(columns={'category': 'product1_category'}).drop(columns=['product_id'])
    
    result = result.merge(
        product_info[['product_id', 'category']],
        left_on='product2_id',
        right_on='product_id',
        how='left'
    ).rename(columns={'category': 'product2_category'}).drop(columns=['product_id'])
    
    # Order the final output
    result = result[
        ['product1_id', 'product2_id', 'product1_category', 'product2_category', 'customer_count']
    ].sort_values(
        by=['customer_count', 'product1_id', 'product2_id'],
        ascending=[False, True, True]
    ).reset_index(drop=True)
    
    return result
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT
    pp1.product_id AS product1_id,
    pp2.product_id AS product2_id,
    pi1.category   AS product1_category,
    pi2.category   AS product2_category,
    COUNT(DISTINCT pp1.user_id) AS customer_count
FROM ProductPurchases pp1
JOIN ProductPurchases pp2
  ON pp1.user_id = pp2.user_id
 AND pp1.product_id < pp2.product_id
JOIN ProductInfo pi1 ON pi1.product_id = pp1.product_id
JOIN ProductInfo pi2 ON pi2.product_id = pp2.product_id
GROUP BY pp1.product_id, pp2.product_id, pi1.category, pi2.category
HAVING COUNT(DISTINCT pp1.user_id) >= 3
ORDER BY customer_count DESC,
         product1_id ASC,
         product2_id ASC;
```
