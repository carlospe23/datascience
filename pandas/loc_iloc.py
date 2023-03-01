import pandas as pd

df_books = pd.read_csv('bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv', sep=',', header=0)


print(df_books[0:4])

print('\n\n')

print('*'*50+'Filtrado por nombre de columna'+'*'*50)

print(df_books[['Name', 'Author', 'Year']])

print('*'*50+'Filtrado por loc'+'*'*50)

print(df_books.loc[0:4]) #incluye la ultima posicion a diferencia del slicing pasado

print(df_books.loc[0:4, ['Name', 'Author']]) #podemos filtrar la cantidad de filas y que columnas mostrar

print(df_books.loc[:,['Reviews']] * - 1) #de esta forma solo afectamos los resultados del loc

print(df_books.iloc[:,0:3]) #todas las rows pero solo con las columnas 0 a 3, se maneja por indice no por label
