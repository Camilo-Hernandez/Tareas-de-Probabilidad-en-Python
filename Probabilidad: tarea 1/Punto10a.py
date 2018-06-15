import scipy.misc as scm
i=6
while scm.comb(i,6) < 3*10**8:
    i+=1
print('El número total de balotas de la lotería estatal es',i)