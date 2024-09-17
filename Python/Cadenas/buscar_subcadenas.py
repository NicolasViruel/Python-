# Buscar subcadenas

cadena = 'Hola, Mundo!'

indice = cadena.find('Mundo')
print(f'Subcadena de mundo: {indice}')

# Obtener el indice de la subcadena de hola (Recordar que python es un lenguaje sencible y distingue entre May y Min)
indice = cadena.find('Hola') # Si no encuentra el valor devuelve -1
print(f'Subcadena de hola: {indice}' )