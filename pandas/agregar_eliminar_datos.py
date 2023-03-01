import pandas as pd
import numpy as np

df_books = pd.read_csv('bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv')

df_books.head(2)

# DROP COLUMNS

df_books.drop('Genre', axis=1).head(2) #0 filas 1 columnas #borra solo ed la salida de datos

df_books.drop('Genre', axis=1, inplace=True) #esta si borra del data frame

df_books = df_books.drop('Year', axis=1) #re asinando es como si si borrara sin el inplace

del df_books['Price']

print(df_books.head(2))

#agregar columna
df_books['Nueva_Columna'] = np.nan

print(df_books)

#add rows

df_books.append(df_books)