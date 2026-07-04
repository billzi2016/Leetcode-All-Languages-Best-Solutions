# 0627. Swap Salary

## Mysql

```mysql
UPDATE Salary
SET sex = CASE sex
            WHEN 'm' THEN 'f'
            WHEN 'f' THEN 'm'
          END;
```

## Mssql

```mssql
/* Write your T-SQL query statement below */
UPDATE Salary
SET sex = CASE sex 
            WHEN 'f' THEN 'm'
            WHEN 'm' THEN 'f'
          END;
```

## Oraclesql

```oraclesql
UPDATE Salary
SET sex = CASE sex WHEN 'm' THEN 'f' ELSE 'm' END;
```

## Pythondata

```pythondata
import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary = salary.copy()
    salary['sex'] = salary['sex'].map({'f': 'm', 'm': 'f'})
    return salary
```

## Postgresql

```postgresql
-- Write your PostgreSQL query statement below
UPDATE Salary
SET sex = CASE 
            WHEN sex = 'm' THEN 'f'
            WHEN sex = 'f' THEN 'm'
          END;
```
