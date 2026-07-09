# 2890. Reshape Data: Melt

## PythonData
```python
import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(report, id_vars=["product"], var_name="quarter", value_name="sales")
```
