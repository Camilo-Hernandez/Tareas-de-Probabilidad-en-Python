# Probabilidad de los sensores
import scipy.stats as st
lam = 50000/40000
PTotal=0
for x in range(1,5):
    Px = st.poisson.pmf(x,lam)
    PTotal+=Px
print('La probabilidad de que la zona examinada tenga entre 1 y 4 sensores es',PTotal)

# Costo promedio
Esperanza = lam*(20*20) # u = lambda*t en Poisson 
Promedio = st.poisson(Esperanza).mean()
CostoPromedio = Promedio*100
print('El costo promedio de los sensores en un área de 400 metros cuadrados es',CostoPromedio)
print('Se puede notar que son iguales:', Promedio,'=', Esperanza)