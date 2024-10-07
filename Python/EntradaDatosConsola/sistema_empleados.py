print(' *** Sistema de empleados ***')

nombre_empleado = input('Nombre del empleado: ')
edad_empleado = int(input('Edad del empleado: '))
sueldo_empleado = float(input('Sueldo del empleado: '))
es_jefe_departamento = input('Es jede de departamento (Si/No)?')

# converitmos la variable es_jefe_departamento a un valor booleano
es_jefe_departamento = es_jefe_departamento.lower() == 'si'

#Imprimimos los resultados

print('\nDatos del empleado')
print(f'Nombre del empleado: {nombre_empleado}')
print(f'Edad del empleado: {edad_empleado:.2f}') #indicamos cuantos decimales queremos que se imprima despues del punto
print(f'Es jede de departamento?: {es_jefe_departamento}')