# 3626. Find Stores with Inventory Imbalance

## MySQL
```sql
# Write your MySQL query statement below
WITH ranked AS (
    SELECT 
        i.*,
        ROW_NUMBER() OVER (PARTITION BY store_id ORDER BY price DESC, inventory_id) AS rn_max,
        ROW_NUMBER() OVER (PARTITION BY store_id ORDER BY price ASC, inventory_id)  AS rn_min
    FROM inventory i
)
SELECT 
    s.store_id,
    s.store_name,
    s.location,
    max_i.product_name   AS most_exp_product,
    min_i.product_name   AS cheapest_product,
    ROUND(min_i.quantity / max_i.quantity, 2) AS imbalance_ratio
FROM stores s
JOIN ranked max_i ON s.store_id = max_i.store_id AND max_i.rn_max = 1
JOIN ranked min_i ON s.store_id = min_i.store_id AND min_i.rn_min = 1
WHERE max_i.quantity < min_i.quantity
ORDER BY imbalance_ratio DESC, s.store_name ASC;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
WITH MaxPrice AS (
    SELECT i.*,
           ROW_NUMBER() OVER (PARTITION BY store_id ORDER BY price DESC, inventory_id) AS rn
    FROM inventory i
),
MinPrice AS (
    SELECT i.*,
           ROW_NUMBER() OVER (PARTITION BY store_id ORDER BY price ASC, inventory_id) AS rn
    FROM inventory i
)
SELECT s.store_id,
       s.store_name,
       s.location,
       mp.product_name   AS most_exp_product,
       np.product_name   AS cheapest_product,
       CAST(np.quantity * 1.0 / mp.quantity AS decimal(10,2)) AS imbalance_ratio
FROM stores s
JOIN MaxPrice mp ON s.store_id = mp.store_id AND mp.rn = 1
JOIN MinPrice np ON s.store_id = np.store_id AND np.rn = 1
WHERE mp.quantity < np.quantity
ORDER BY imbalance_ratio DESC,
         s.store_name ASC;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
WITH max_prod AS (
    SELECT store_id,
           product_name AS most_exp_product,
           quantity     AS max_qty
    FROM (
        SELECT i.*,
               ROW_NUMBER() OVER (PARTITION BY store_id ORDER BY price DESC, inventory_id) rn
        FROM inventory i
    )
    WHERE rn = 1
),
min_prod AS (
    SELECT store_id,
           product_name AS cheapest_product,
           quantity     AS min_qty
    FROM (
        SELECT i.*,
               ROW_NUMBER() OVER (PARTITION BY store_id ORDER BY price ASC, inventory_id) rn
        FROM inventory i
    )
    WHERE rn = 1
)
SELECT s.store_id,
       s.store_name,
       s.location,
       mp.most_exp_product,
       cp.cheapest_product,
       ROUND(cp.min_qty / mp.max_qty, 2) AS imbalance_ratio
FROM stores s
JOIN max_prod mp ON s.store_id = mp.store_id
JOIN min_prod cp ON s.store_id = cp.store_id
WHERE mp.max_qty < cp.min_qty
ORDER BY imbalance_ratio DESC, s.store_name ASC;
```

## PythonData
```python
import pandas as pd

def find_inventory_imbalance(stores: pd.DataFrame, inventory: pd.DataFrame) -> pd.DataFrame:
    # Most expensive product per store
    max_idx = inventory.groupby('store_id')['price'].idxmax()
    most = inventory.loc[max_idx, ['store_id', 'product_name', 'quantity']].rename(
        columns={'product_name': 'most_exp_product', 'quantity': 'most_quantity'}
    )
    
    # Cheapest product per store
    min_idx = inventory.groupby('store_id')['price'].idxmin()
    cheap = inventory.loc[min_idx, ['store_id', 'product_name', 'quantity']].rename(
        columns={'product_name': 'cheapest_product', 'quantity': 'cheap_quantity'}
    )
    
    # Combine most and cheapest info
    combined = pd.merge(most, cheap, on='store_id')
    combined = pd.merge(combined, stores, on='store_id')
    
    # Filter stores where most expensive quantity is less than cheapest quantity
    filtered = combined[combined['most_quantity'] < combined['cheap_quantity']].copy()
    if filtered.empty:
        return pd.DataFrame(
            columns=[
                'store_id',
                'store_name',
                'location',
                'most_exp_product',
                'cheapest_product',
                'imbalance_ratio'
            ]
        )
    
    # Compute imbalance ratio
    filtered['imbalance_ratio'] = (filtered['cheap_quantity'] / filtered['most_quantity']).round(2)
    
    # Select required columns and sort
    result = filtered[
        [
            'store_id',
            'store_name',
            'location',
            'most_exp_product',
            'cheapest_product',
            'imbalance_ratio'
        ]
    ]
    result = result.sort_values(
        by=['imbalance_ratio', 'store_name'],
        ascending=[False, True]
    ).reset_index(drop=True)
    
    return result
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
WITH store_prices AS (
    SELECT 
        s.store_id,
        s.store_name,
        s.location,
        MAX(i.price) AS max_price,
        MIN(i.price) AS min_price
    FROM stores s
    JOIN inventory i ON s.store_id = i.store_id
    GROUP BY s.store_id, s.store_name, s.location
)
SELECT 
    s.store_id,
    s.store_name,
    s.location,
    me.product_name      AS most_exp_product,
    ce.product_name      AS cheapest_product,
    ROUND(ce.quantity::decimal / me.quantity, 2) AS imbalance_ratio
FROM store_prices sp
JOIN stores s ON s.store_id = sp.store_id
JOIN LATERAL (
    SELECT i.product_name, i.quantity
    FROM inventory i
    WHERE i.store_id = s.store_id AND i.price = sp.max_price
    LIMIT 1
) me ON true
JOIN LATERAL (
    SELECT i.product_name, i.quantity
    FROM inventory i
    WHERE i.store_id = s.store_id AND i.price = sp.min_price
    LIMIT 1
) ce ON true
WHERE me.quantity < ce.quantity
ORDER BY imbalance_ratio DESC, s.store_name ASC;
```
