print('**** Operadores de asignacion ****')

numero = 5
print(f'Valor de numero: {numero}')
numero = 10
print(f'Valor de numero: {numero}')

cadena = "Saludos desde Python"
print(f'Valor de la cadena: {cadena}')

# Asignacion Multiple

x, y ,z = 5, "hola", -9.15
print(f'\n Valor de X: {x}, valor de Y: {y}, valor de Z: {z}')

# Asignacion Encadenada

a = b = c = 10
print(f'\n Valor a = {a}, valor de b = {b}, valor de c = {c}')

# Intercambio de valores de una variable, sin utilizar variables temporales
x, y = 5 , 10
print(f'\n Valor de X: {x}, valor de Y: {y}')
# Aplicando el concepto de asignacion multiple, intercambio valores
x, y = y, x
print(f'\n Invertimos los valores, valor de X: {x}, valor de Y: {y}')


print('**** Recibir multiples valores de entrada del usuario ****')

nombre, apellido = input('Ingresa tu nombre y apellido separados por coma: ').split(",") #Con los metodos split, separo por coma y strip elimino los espacios
print(f'Su nombre es {nombre.strip()} y su apellido es {apellido.strip()}') 
