import numpy as np


lista = [1, 2, 3, 4, 5]

arr = np.array(lista)

print(type(arr))

matriz = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

matriz = np.array(matriz)
print(matriz)


print(arr[0])
#el primer dato son filas y el segundo las columnas
print(matriz[0,2])

#el primer dato son las filas y el segundo las columbas
#es decir 1 puede tener : e ir por ejemplo del 0:1
#luego de la coma pasamos la condicion de las columnas
#en este caso esta tomando de la columna 0 hasta la 2 
print(matriz[1:,0:2])

#---------------------------------------------------------------
#                          Dimensiones
#---------------------------------------------------------------

"""
scalar: dim = 0 Un solo dato o valor

vector: dim = 1 Listas de Python

matriz: dim = 2 Hoja de cálculo

tensor: dim > 3 Series de tiempo o Imágenes

Declarando un escalar.

"""

scalar = np.array(42)
print(scalar)
print(scalar.ndim )


vector = np.array([1, 2, 3])
print(vector) 
print(vector.ndim )


matriz = np.array(
    [
        [1, 2, 3], 
        [4, 5, 6]
    ]
)
print(matriz)
print(matriz.ndim)



tensor = np.array(
    [
        [
            [1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 9], 
            [10, 11, 12]
        ], 
        [
            [13, 13, 15], 
            [16, 17, 18], 
            [19, 20, 21], 
            [22, 23, 24]
        ]
    ]
)

print(tensor)
print(tensor.ndim)

#---------------------------------------------------------------

#AGREGAR O QUITAR DIMENSIONES

#---------------------------------------------------------------


vector = np.array([1, 2, 3], ndmin = 10)
print(vector) 
print(vector.ndim )


expand = np.expand_dims(np.array([1, 2, 3]), axis = 0) #0 FILAS 1 COLUMNAS
print(expand)
print(expand.ndim)

#---------------------------------------------------------------

# Ajustar a las dimensiones correctas

#---------------------------------------------------------------

print(vector, vector.ndim)
vector_2 = np.squeeze(vector)
print(vector_2, vector_2.ndim)


#---------------------------------------------------------------

#Creado arrays

#---------------------------------------------------------------

np.arange(0, 10) # datos de 0 a 10 
np.arange(0, 20, 2) # datos de 0 a 20 con pasos de 2

np.zeros((10,10)) # => array matriz 10 x 10 (primero filas, segundo columnas) solo ceros

np.ones((10,10)) # => array matriz 10 x 10 (primero filas, segundo columnas) solo unos

np.linspace(0, 10, 100) # 100 datos de 0 a 10

np.eye(4) # matriz con diagonal en uno

np.random.rand(4,4) # => matriz de 4 x 4 con datos aleatorios

np.random.randint(1,15)

np.random.randint(1,100,(10,10)) # valores random de 0 a 100 en una matriz 10 x 10



#---------------------------------------------------------------
#       SHAPE Y RESHAPE
#---------------------------------------------------------------

arr = np.random.randint(1,10,(3,2))

print(arr.shape)