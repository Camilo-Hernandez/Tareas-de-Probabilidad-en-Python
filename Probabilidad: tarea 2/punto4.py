# Literal a)
# Hallar n para que se cumpla P(k>=90) >= 0.9
import scipy.stats as st
ProbabilidadTotal=0 # Acumula las probabilidades individuales
    # P(k=90) + P(k=91) + ... + P(k=100)
    # en cada iteración, hasta averiguar el n que satisfaga la probabilidad
    # P(k >= 90) >= 0.9
n=100
while ProbabilidadTotal<=0.9: # Momento de corte cuando P(k>=90) >= 0.9
    ProbabilidadTotal=0 # Probar con un n=n+1
    for k in range(90,n+1):
        Pk = st.binom.pmf(k, n, 0.9) # P(K=k)
        ProbabilidadTotal+=Pk # P(K>=k)
    n+=1
print('''El número mínimo de tiquets que la aerolínea debe ofertar
para que el avión se llene en, al menos, un 90% es:''',n,
'''Con probabilidad de''',ProbabilidadTotal)

# Literal b)
# Hallar P(k>100)
ProbabilidadTotal=0
for k in range(101,n+1): # Se presenten al vuelo más de 100 personas
    Pk = st.binom.pmf(k, n, 0.9) # P(K=k)
    ProbabilidadTotal+=Pk # P(K>=k)
print("La probabilidad de que se presenten al vuelo mas de 100 personas es:",ProbabilidadTotal)