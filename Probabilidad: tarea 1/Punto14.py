import matplotlib.pyplot as plt
import numpy as np
dado1 = np.random.randint(1,7,1000) #Lanzado el dado mil veces (vector de resultados aleatorios)
dado2 = np.random.randint(1,7,1000) #Lanzado el segundo dado mil veces también
suma = dado1+dado2 #suma de cada resultado del lanzamiento de ambos dados
resta = list(abs(dado1-dado2)) #Diferencia entre los resultados

# 14a

##### Creación del histograma de la suma de los dados #####
plt.hist(suma,bins=10,range=(2,12),color='yellow')
plt.title('Lanzamiento de dados')
plt.xlabel('Resultados')
plt.ylabel('Número de veces')
'''hist(datos,número de particiones, rango de resultados del experimento)
Generamos el histograma con la función hist.
Observar que los argumentos de la función hist son:
los datos, la cantidad de diferentes valores del experimento,
y el rango de dichos valores. '''

# 14b

print('La probabilidad de que la diferencia entre los dos resultados sea igual a 2 es',resta.count(2)) 
# Imprimir en pantalla el número de veces que aparece el número 2.
# Esa es la probabilidad de que la resta entre 2 resultados de lanzamiento de dados sea igual a 2.
# Primero hay que transformar el arreglo "resta" a una lista para aplicar el método .count()
