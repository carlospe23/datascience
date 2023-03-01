import pandas as pd


df_books = pd.read_csv('bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv', sep=',', header=0)

mayor_a_2016 = df_books['Year'] > 2016
solo_ficcion = df_books['Genre'] == 'Fiction'


#print(df_books[mayor_a_2016 & solo_ficcion])

#print(df_books[~mayor_a_2016]) # ~ es para negar la condicion

print(df_books.info())

print(df_books.describe()) #distribucion de los datos de forma estadistica
print(df_books.memory_usage(deep=True)) #consumo de memoria

print(df_books['Author'].value_counts()) #cuenta los datos 