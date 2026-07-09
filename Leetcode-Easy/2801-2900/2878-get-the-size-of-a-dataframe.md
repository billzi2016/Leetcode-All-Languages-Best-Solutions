# 2878. Get the Size of a DataFrame

## PythonData
```python
import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0], players.shape[1]]
```
