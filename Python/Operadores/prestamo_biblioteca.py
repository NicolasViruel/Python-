print('*** Prestamo de libros en la biblioteca ***') # Operador OR

KM_distancia = 3
eres_estudiante = input(f'Eres estudiante en la universidad? (Si/No)')
distancia = int(input(f'A cuantos Km vives de la universidad= '))

resultado = distancia <= KM_distancia or eres_estudiante.lower().split() == 'si'

print(f'El resultado es: {resultado}')