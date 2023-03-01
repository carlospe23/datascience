import pandas as pd

df1 = pd.DataFrame({'A':['A0', 'A1', 'A2', 'A3'], 
 'B':['B0', 'B1', 'B2', 'B3'],
 'C':['C0', 'C1', 'C2', 'C3'],
 'D':['D0', 'D1', 'D2', 'D3']})


df2 = pd.DataFrame({'A':['A4', 'A5', 'A6', 'A7'], 
 'B':['B4', 'B5', 'B6', 'B7'],
 'C':['C4', 'C5', 'C6', 'C7'],
 'D':['D4', 'D5', 'D6', 'D7']})


print(pd.concat([df1,df2], ignore_index=True)) #por defecto usa axis 0 lo normal
print(pd.concat([df1,df2], ignore_index=True, axis=1))


izq = pd.DataFrame({'Key':['k0', 'k1', 'k2', 'k3'], 
 'A':['A0', 'A1', 'A2', 'A3'],
 'B':['B0', 'B1', 'B2', 'B3']})


der = pd.DataFrame({'Key_2':['k0', 'k1', 'k2', 'k3'], 
 'C':['C0', 'C1', 'C2', 'C3'],
 'D':['D0', 'D1', 'D2', 'D3']})

print(izq.merge(der, left_on='Key', right_on='Key_2'))