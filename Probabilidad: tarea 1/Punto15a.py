import scipy.misc as scm

# Punto 11 a.
# Evento B: Artículos buenos.
# P = 1-P(B1 y B2 y B3) es la probabilidad de encontrar alguno defectuoso entre 3 artículos.
P = 1 - (scm.comb(8,3)/scm.comb(15,3))
# 8C3 para todas las formas posibles en que puedo elegir 3 artículos de los 8 buenos.
# 15C3 para todas las formas posibles de elegir 3 artículos de 15 existentes
print('La probabildiad de que alguno de los 3 esté defectuoso es de',P)

# Punto 11 b.
P = (scm.comb(7,2)/scm.comb(15,2))*(scm.comb(8,2)/scm.comb(13,2))
'''El primer término es la probabilidad de sacar primero 2 defectuosos
El segundo término es la probabilidad de sacar luego 2 buenos
habiendo sacado 2 defectuosos primero.'''
print('La probabilidad de encontrar dos defectuosos primero y luego dos buenos es',P)