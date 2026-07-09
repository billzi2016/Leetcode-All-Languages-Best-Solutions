# 3554. Find Category Recommendation Pairs

## MySQL
```sql
# Write your MySQL query statement below
WITH user_categories AS (
    SELECT DISTINCT pu.user_id, pi.category
    FROM ProductPurchases pu
    JOIN ProductInfo pi ON pu.product_id = pi.product_id
)
SELECT 
    uc1.category AS category1,
    uc2.category AS category2,
    COUNT(*) AS customer_count
FROM user_categories uc1
JOIN user_categories uc2
  ON uc1.user_id = uc2.user_id
 AND uc1.category < uc2.category
GROUP BY uc1.category, uc2.category
HAVING COUNT(*) >= 3
ORDER BY customer_count DESC, category1 ASC, category2 ASC;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
WITH UserCategories AS (
    SELECT DISTINCT pp.user_id, pi.category
    FROM ProductPurchases pp
    JOIN ProductInfo pi ON pp.product_id = pi.product_id
)
SELECT 
    uc1.category AS category1,
    uc2.category AS category2,
    COUNT(DISTINCT uc1.user_id) AS customer_count
FROM UserCategories uc1
JOIN UserCategories uc2
    ON uc1.user_id = uc2.user_id
   AND uc1.category < uc2.category
GROUP BY 
    uc1.category,
    uc2.category
HAVING 
    COUNT(DISTINCT uc1.user_id) >= 3
ORDER BY 
    customer_count DESC,
    category1 ASC,
    category2 ASC;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
WITH user_categories AS (
    SELECT DISTINCT pp.user_id, pi.category
    FROM ProductPurchases pp
    JOIN ProductInfo pi ON pp.product_id = pi.product_id
)
SELECT uc1.category AS category1,
       uc2.category AS category2,
       COUNT(*)   AS customer_count
FROM   user_categories uc1
JOIN   user_categories uc2
       ON uc1.user_id = uc2.user_id
      AND uc1.category < uc2.category
GROUP BY uc1.category, uc2.category
HAVING COUNT(*) >= 3
ORDER BY customer_count DESC,
         category1 ASC,
         category2 ASC;
```

## PythonData
```python
import pandas as pd
import itertools

def find_category_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    # Join purchases with categories
    df = product_purchases.merge(product_info[['product_id', 'category']], on='product_id')
    
    # Get distinct categories per user
    user_cats = (
        df.groupby('user_id')['category']
        .apply(lambda x: set(x))
        .reset_index()
    )
    
    # Build (user, cat1, cat2) rows for each unordered category pair a user bought
    records = []
    for _, row in user_cats.iterrows():
        uid = row['user_id']
        cats = sorted(row['category'])
        if len(cats) < 2:
            continue
        for c1, c2 in itertools.combinations(cats, 2):
            records.append((uid, c1, c2))
    
    if not records:
        return pd.DataFrame(columns=['category1', 'category2', 'customer_count'])
    
    pair_df = pd.DataFrame(records, columns=['user_id', 'category1', 'category2'])
    
    # Count distinct users per category pair
    result = (
        pair_df.groupby(['category1', 'category2'])['user_id']
        .nunique()
        .reset_index(name='customer_count')
    )
    
    # Keep only pairs with at least 3 customers
    result = result[result['customer_count'] >= 3]
    
    # Sort as required
    result = result.sort_values(
        by=['customer_count', 'category1', 'category2'],
        ascending=[False, True, True]
    ).reset_index(drop=True)
    
    return result
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
WITH user_categories AS (
    SELECT DISTINCT pp.user_id, pi.category
    FROM ProductPurchases pp
    JOIN ProductInfo pi ON pp.product_id = pi.product_id
)
SELECT uc1.category AS category1,
       uc2.category AS category2,
       COUNT(*) AS customer_count
FROM user_categories uc1
JOIN user_categories uc2
  ON uc1.user_id = uc2.user_id
 AND uc1.category < uc2.category
GROUP BY uc1.category, uc2.category
HAVING COUNT(*) >= 3
ORDER BY customer_count DESC,
         category1 ASC,
         category2 ASC;
```
