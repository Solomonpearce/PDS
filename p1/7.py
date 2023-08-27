import numpy as np 
import matplotlib.pyplot as plt


def senal_matriz(edad):
    senal = np.empty((0,))
    matriz = np.empty((0, 100))

    for i in range(edad):
        ventana = np.random.rand() * np.random.randn(100) + np.random.rand()
        senal = np.hstack((senal, ventana))
        matriz = np.vstack((matriz, ventana))

    return senal, matriz

def graficar_senal_y_calcular_estadisticas(senal, matriz):
    medias_desviaciones = []

    plt.figure(figsize=(10, 6))
    plt.plot(senal, label='Señal')
    plt.title('Gráfica de la Señal Generada')
    plt.xlabel('Muestras')
    plt.ylabel('Valor')
    plt.legend()
    plt.grid()
    plt.show()

    for fila in matriz:
        media = np.mean(fila)
        desviacion_estandar = np.std(fila)
        medias_desviaciones.append((media, desviacion_estandar))

    return medias_desviaciones

edad = int(input("Ingresa tu edad (número de iteraciones del ciclo): "))
senal_generada, matriz_ventanas = senal_matriz(edad)
resultados = graficar_senal_y_calcular_estadisticas(senal_generada, matriz_ventanas)

print("Medias y Desviaciones Estándar:")
for i, (media, desviacion) in enumerate(resultados, start=1):
    print(f"Ventana {i}: Media={media:.2f}, Desviación Estándar={desviacion:.2f}")