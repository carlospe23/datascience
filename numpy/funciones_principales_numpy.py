import numpy as np

arr = np.random.randint(1,20,10) # => array de 10 numeros de 1 a 20 random

print(arr)

matriz = arr.reshape(2,5) # reshape para volverlo una matriz de [2 filas, 5 columnas]
print(matriz)

arr.max() #numero mayor del array
matriz.max()   #numero mayor del array, podemos enviar eje 1, para saberlo por fila 
matriz.max()   # o por el eje 0 por columna

arr.argmax() #retorna el indice donde esta el valor mas grande funciona igual en matriz
arr.min() #retorna valor mas pequeño

arr.sort() #ordena 
np.percentile(arr, 50) #obtener percentil
np.median(arr) # nos da la mediana
np.std(arr) # nos da la desviacion estandar
np.var(arr) # nos da la varianza
np.mean(arr) # media del array

a = np.array([[1,2], [3,4]])
b = np.array([5,6])


print(a.ndim)
print(b.ndim)

b = np.expand_dims(b,axis=0)

print(np.concatenate((a,b), axis=0))
print(np.concatenate((a,b.T), axis=1)) # Transpuesta de la matriz osea invierte filas i columnas



