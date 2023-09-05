import numpy as np 
import matplotlib.pyplot as plt

edad= int(25)
senal= np.empty((0,))
matriz=np.empty((0,100))
for i in range(edad):
  ventana=np.random.rand()*np.random.randn(100)+np.random.rand()
  senal=np.hstack((senal,ventana))
  matriz=np.vstack((matriz,ventana))


plt.figure(figsize=(10, 6))
plt.plot(senal, label='Señal')
plt.title('Gráfica de la Señal Generada')
plt.xlabel('')
plt.ylabel('amplitud')
plt.legend()
plt.grid()
plt.show() #mirar como se puede solucionar desde este entorno para graficar. 


for fila in matriz:
    media = np.mean(fila)
    desviacion_estandar = np.std(fila)
    print(f"Media: {media:.2f}, Desviación Estándar: {desviacion_estandar:.2f}")


