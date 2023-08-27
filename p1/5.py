import numpy as np
n= int(input("Ingrese el valor de n para la matriz: "))
matriz=np.random.rand(n,n)
traza=np.trace(matriz)

sumatoriatotal=np.sum(matriz[:-1,:-1])

metrica= traza/sumatoriatotal
print("la metrica es: ",metrica)