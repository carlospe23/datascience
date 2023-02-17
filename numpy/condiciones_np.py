import numpy as np

arr = np.linspace(1,10,10, dtype='int8')

print(arr)

indices_cond = arr > 5
print(arr[indices_cond])


print(arr[(arr > 5) & (arr < 9)])

print(arr[arr % 2 == 0 ])
print(arr[arr % 2 != 0 ])

arr[(arr > 5)] = 99
print(arr)
