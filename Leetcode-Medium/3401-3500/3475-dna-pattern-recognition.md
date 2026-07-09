# 3475. DNA Pattern Recognition

## MySQL
```sql
SELECT
    sample_id,
    dna_sequence,
    species,
    CASE WHEN dna_sequence LIKE 'ATG%' THEN 1 ELSE 0 END AS has_start,
    CASE WHEN dna_sequence LIKE '%TAA' OR dna_sequence LIKE '%TAG' OR dna_sequence LIKE '%TGA' THEN 1 ELSE 0 END AS has_stop,
    CASE WHEN dna_sequence LIKE '%ATAT%' THEN 1 ELSE 0 END AS has_atat,
    CASE WHEN dna_sequence LIKE '%GGG%' THEN 1 ELSE 0 END AS has_ggg
FROM Samples
ORDER BY sample_id;
```

## MSSQL
```sql
/* Write your T-SQL query statement below */
SELECT
    sample_id,
    dna_sequence,
    species,
    CASE WHEN LEFT(dna_sequence, 3) = 'ATG' THEN 1 ELSE 0 END AS has_start,
    CASE WHEN RIGHT(dna_sequence, 3) IN ('TAA', 'TAG', 'TGA') THEN 1 ELSE 0 END AS has_stop,
    CASE WHEN dna_sequence LIKE '%ATAT%' THEN 1 ELSE 0 END AS has_atat,
    CASE WHEN dna_sequence LIKE '%GGG%' THEN 1 ELSE 0 END AS has_ggg
FROM Samples
ORDER BY sample_id;
```

## OracleSQL
```sql
/* Write your PL/SQL query statement below */
SELECT
    sample_id,
    dna_sequence,
    species,
    CASE WHEN SUBSTR(dna_sequence, 1, 3) = 'ATG' THEN 1 ELSE 0 END AS has_start,
    CASE WHEN INSTR(dna_sequence, 'TAA') > 0 
          OR INSTR(dna_sequence, 'TAG') > 0 
          OR INSTR(dna_sequence, 'TGA') > 0
         THEN 1 ELSE 0 END AS has_stop,
    CASE WHEN INSTR(dna_sequence, 'ATAT') > 0 THEN 1 ELSE 0 END AS has_atat,
    CASE WHEN INSTR(dna_sequence, 'GGG') > 0 THEN 1 ELSE 0 END AS has_ggg
FROM Samples
ORDER BY sample_id;
```

## PythonData
```python
import pandas as pd

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    df = samples.copy()
    df['has_start'] = df['dna_sequence'].str.startswith('ATG').astype(int)
    stop_codons = ('TAA', 'TAG', 'TGA')
    df['has_stop'] = df['dna_sequence'].apply(lambda x: int(any(x.endswith(c) for c in stop_codons)))
    df['has_atat'] = df['dna_sequence'].str.contains('ATAT').astype(int)
    df['has_ggg'] = df['dna_sequence'].str.contains('GGG').astype(int)
    return df.sort_values('sample_id').reset_index(drop=True)
```

## PostgreSQL
```sql
-- Write your PostgreSQL query statement below
SELECT
    sample_id,
    CASE WHEN dna_sequence LIKE 'ATG%' THEN 1 ELSE 0 END AS has_start,
    CASE 
        WHEN dna_sequence LIKE '%TAA' OR dna_sequence LIKE '%TAG' OR dna_sequence LIKE '%TGA'
        THEN 1 ELSE 0 END AS has_stop,
    CASE WHEN dna_sequence LIKE '%ATAT%' THEN 1 ELSE 0 END AS has_atat,
    CASE WHEN dna_sequence LIKE '%GGG%' THEN 1 ELSE 0 END AS has_ggg
FROM Samples
ORDER BY sample_id;
```
