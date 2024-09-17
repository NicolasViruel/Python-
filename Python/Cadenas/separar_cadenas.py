# Separar cadenas metodo SPLIT

datos = 'Hola mundo'
lista = datos.split() # Por default si no le asignamos un valor separa cada elemento por espacios en blanco
print(lista) # Devuelve un ['Hola','mundo']

datos = 'Juan,30,Mexico'
lista2 = datos.split(',')
print(lista2) # Devuelve ['Juan', '30', 'Mexico']

