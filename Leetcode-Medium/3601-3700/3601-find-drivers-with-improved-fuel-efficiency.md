# 3601. Find Drivers with Improved Fuel Efficiency

## MySQL
```sql
SELECT 
    d.driver_id,
    d.driver_name,
    ROUND(f.avg_eff, 2) AS first_half_avg,
    ROUND(s.avg_eff, 2) AS second_half_avg,
    ROUND(s.avg_eff - f.avg_eff, 2) AS efficiency_improvement
FROM drivers d
JOIN (
    SELECT driver_id, AVG(distance_km / fuel_consumed) AS avg_eff
    FROM trips
    WHERE MONTH(trip_date) BETWEEN 1 AND 6
    GROUP BY driver_id
) f ON d.driver_id = f.driver_id
JOIN (
    SELECT driver_id, AVG(distance_km / fuel_consumed) AS avg_eff
    FROM trips
    WHERE MONTH(trip_date) BETWEEN 7 AND 12
    GROUP BY driver_id
) s ON d.driver_id = s.driver_id
WHERE s.avg_eff > f.avg_eff
ORDER BY efficiency_improvement DESC, driver_name ASC;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
WITH driver_eff AS (
    SELECT d.driver_id,
           d.driver_name,
           AVG(CASE WHEN MONTH(t.trip_date) BETWEEN 1 AND 6
                    THEN t.distance_km / NULLIF(t.fuel_consumed,0) END) AS first_half_avg,
           AVG(CASE WHEN MONTH(t.trip_date) BETWEEN 7 AND 12
                    THEN t.distance_km / NULLIF(t.fuel_consumed,0) END) AS second_half_avg
    FROM drivers d
    LEFT JOIN trips t ON d.driver_id = t.driver_id
    GROUP BY d.driver_id, d.driver_name
)
SELECT driver_id,
       driver_name,
       ROUND(first_half_avg, 2)      AS first_half_avg,
       ROUND(second_half_avg, 2)     AS second_half_avg,
       ROUND(second_half_avg - first_half_avg, 2) AS efficiency_improvement
FROM driver_eff
WHERE first_half_avg IS NOT NULL
  AND second_half_avg IS NOT NULL
  AND second_half_avg > first_half_avg
ORDER BY efficiency_improvement DESC,
         driver_name ASC;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT driver_id,
       driver_name,
       ROUND(first_half_avg, 2) AS first_half_avg,
       ROUND(second_half_avg, 2) AS second_half_avg,
       ROUND(improvement, 2)   AS efficiency_improvement
FROM (
    SELECT d.driver_id,
           d.driver_name,
           AVG(CASE WHEN EXTRACT(MONTH FROM t.trip_date) BETWEEN 1 AND 6 
                    THEN t.distance_km / t.fuel_consumed END) AS first_half_avg,
           AVG(CASE WHEN EXTRACT(MONTH FROM t.trip_date) BETWEEN 7 AND 12 
                    THEN t.distance_km / t.fuel_consumed END) AS second_half_avg,
           AVG(CASE WHEN EXTRACT(MONTH FROM t.trip_date) BETWEEN 7 AND 12 
                    THEN t.distance_km / t.fuel_consumed END) -
           AVG(CASE WHEN EXTRACT(MONTH FROM t.trip_date) BETWEEN 1 AND 6 
                    THEN t.distance_km / t.fuel_consumed END) AS improvement
    FROM drivers d
    JOIN trips t ON d.driver_id = t.driver_id
    GROUP BY d.driver_id, d.driver_name
)
WHERE improvement > 0
ORDER BY improvement DESC, driver_name ASC;
```

## PythonData
```python
import pandas as pd

def find_improved_efficiency_drivers(drivers: pd.DataFrame, trips: pd.DataFrame) -> pd.DataFrame:
    trips = trips.copy()
    trips["trip_date"] = pd.to_datetime(trips["trip_date"])
    trips["month"] = trips["trip_date"].dt.month
    trips["efficiency"] = trips["distance_km"] / trips["fuel_consumed"]
    trips["half"] = trips["month"].apply(lambda m: "first" if m <= 6 else "second")
    
    agg = (
        trips.groupby(["driver_id", "half"])["efficiency"]
        .mean()
        .reset_index()
    )
    pivot = agg.pivot(index="driver_id", columns="half", values="efficiency").reset_index()
    pivot = pivot.rename(columns={"first": "first_half_avg", "second": "second_half_avg"})
    
    result = pd.merge(pivot, drivers[["driver_id", "driver_name"]], on="driver_id")
    result = result.dropna(subset=["first_half_avg", "second_half_avg"])
    result["efficiency_improvement"] = result["second_half_avg"] - result["first_half_avg"]
    result = result[result["efficiency_improvement"] > 0]
    
    cols_to_round = ["first_half_avg", "second_half_avg", "efficiency_improvement"]
    result[cols_to_round] = result[cols_to_round].round(2)
    
    result = result[
        ["driver_id", "driver_name", "first_half_avg", "second_half_avg", "efficiency_improvement"]
    ]
    result = result.sort_values(
        by=["efficiency_improvement", "driver_name"], ascending=[False, True]
    ).reset_index(drop=True)
    
    return result
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
WITH driver_eff AS (
    SELECT
        d.driver_id,
        d.driver_name,
        SUM(CASE WHEN EXTRACT(MONTH FROM t.trip_date) BETWEEN 1 AND 6 THEN t.distance_km END) AS dist_first,
        SUM(CASE WHEN EXTRACT(MONTH FROM t.trip_date) BETWEEN 1 AND 6 THEN t.fuel_consumed END) AS fuel_first,
        SUM(CASE WHEN EXTRACT(MONTH FROM t.trip_date) BETWEEN 7 AND 12 THEN t.distance_km END) AS dist_second,
        SUM(CASE WHEN EXTRACT(MONTH FROM t.trip_date) BETWEEN 7 AND 12 THEN t.fuel_consumed END) AS fuel_second
    FROM drivers d
    JOIN trips t ON d.driver_id = t.driver_id
    GROUP BY d.driver_id, d.driver_name
)
SELECT
    driver_id,
    driver_name,
    ROUND(dist_first::numeric / NULLIF(fuel_first, 0), 2)      AS first_half_avg,
    ROUND(dist_second::numeric / NULLIF(fuel_second, 0), 2)    AS second_half_avg,
    ROUND(
        (dist_second::numeric / NULLIF(fuel_second, 0)) -
        (dist_first::numeric  / NULLIF(fuel_first,  0)),
        2
    )                                                          AS efficiency_improvement
FROM driver_eff
WHERE dist_first IS NOT NULL AND fuel_first IS NOT NULL
  AND dist_second IS NOT NULL AND fuel_second IS NOT NULL
  AND (dist_second::numeric / NULLIF(fuel_second, 0)) >
      (dist_first::numeric  / NULLIF(fuel_first,  0))
ORDER BY efficiency_improvement DESC, driver_name ASC;
```
