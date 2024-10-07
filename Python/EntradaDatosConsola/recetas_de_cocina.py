print('*** Receta de cocina ***')

nombre_receta= input('Introduzca el nombre de la receta: ')
ingredientes_receta = input('Ingrese los ingredientes para su preparacion: ')
tiempo_preparacion = int(input('Tiempo de preparacion en (min): '))
dificultad = input('Ingrese la dificultad de la receta: (Facil/Medio/Dificil)')


# Cambiamos el resultado de la variable dificultad


# Imprimimos los datos solicitados

print('\nDatos de la receta')
print(f'El nombre de la receta es: {nombre_receta}')
print(f'Ingredientes de la receta: {ingredientes_receta}')
print(f'El tiempo de preparacion: {tiempo_preparacion}')
print(f'La dificultad es: {dificultad}')