print(f'*** Sistema de Descuento VIP ***') # Operador AND

numero_productos = 10
condicion1 = int(input(f'Cuantos productos compro en la tienda? '))
condicion2 = input(f'Esta usted registrado? Si/No ')

resultado = condicion1 >= numero_productos and condicion2.strip().lower() == 'si'

print(f'El resultado es: {resultado}')