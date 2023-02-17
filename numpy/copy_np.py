import numpy as np

arr = np.arange(0,11)

print(arr)

arr_copy = arr.copy()

arr_copy[:] = 100
print(arr_copy)
print(arr)
