import scipy.misc as scm
# Punto 12a
F = scm.comb(15,2,1)*scm.comb(13,3,1)*scm.comb(10,6,1)
print('La cantidad de formas en que puedo formar 3 comités de un grupo de 15 personas es',F)

# Punto 12b
P = scm.comb(10,5)/scm.comb(15,5)
print('La probabilidad de que un grupo de 5 personas sólo este conformado por estudiantes de pregrado es',P)