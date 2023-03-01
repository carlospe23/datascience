import pandas as pd
import numpy as np

diccionario ={'col1': [1,2,3,np.nan],
  'col2': [4,np.nan,6,7],
  'col3': ['a', 'b', 'c', None]
  }


df = pd.DataFrame(diccionario)

print(df)

print(df.isnull()*1)

print(df.fillna('Missing'))

print(df.fillna(df.mean()))
print(df.dropna())