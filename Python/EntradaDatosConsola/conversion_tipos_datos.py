# Conversion de tipos de datos

# Convertir de cadena a un numero
numero_cadena = '10'
numero_entero = int(numero_cadena)
print(f'Valor de Numero en cadena: {numero_cadena}')
print(f'Numero cadena a entero: {numero_entero}')

# Convertir a Flotante
numero_cadena= '3.14'
numero_flotante= float(numero_cadena)
print(f'Valor de Numero en flotante:  {numero_flotante}')

# Convertir de numero a cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print(f'Numero a cadena: {numero_cadena}')

# Convertir a tipo Boolean
# Tipo bool es Falso en los siguientes casos
# Si el valor es 0, cadena vacia, o None, entonces regresa False
# Regresa Tru, si el valor es distinto de 0, si es dintinto a cadena vacia
# y tambien si es distinto de None

numero_entero = 0
booleano = bool(numero_entero)
print(f'Numero a Booleano: {booleano}') # False