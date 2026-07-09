# 1527. Patients With a Condition

## MySQL
```sql
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%';
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT patient_id,
       patient_name,
       conditions
FROM   Patients
WHERE  conditions LIKE 'DIAB1%'      -- starts with DIAB1
    OR conditions LIKE '% DIAB1%';   -- contains DIAB1 after a space
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT patient_id,
       patient_name,
       conditions
FROM   Patients
WHERE  conditions LIKE 'DIAB1%' 
    OR conditions LIKE '% DIAB1%';
```

## PythonData
```python
import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    mask = (
        patients["conditions"]
        .fillna("")
        .str.split()
        .apply(lambda codes: any(code.startswith("DIAB1") for code in codes))
    )
    return patients[mask]
```

## PostgreSQL
```sql
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%' 
   OR conditions LIKE '% DIAB1%';
```
