print('*** Generacion de numero aleatorio ***')

# Necesitamos importar primero el modulo randoint
from random import randint

numero_aleatorio = randint(1, 10)
print(f'El numero aleatorio es: {numero_aleatorio}')



print('*** --------Lanzar el dado ---------- ***')


dado = randint(1, 6)
print(f'El numero del dado es: {dado}')