print('*** Generacion de ID unico ***')

# Necesitamos importar primero el modulo randoint
from random import randint

nombre= input('Introduzca su nombre: ')
apellido= input('Introduzca su apellido: ')
nacimiento= input('Introduzca su fecha de nacimiento (YYYY): ')


nombre_2 = nombre.strip().upper()[0:2]
apellido_2 = apellido.strip().upper()[0:2]
anio_nacimiento = nacimiento.strip()[2:] #puede ir vacio el segundo campo tambien podria ser [2:4]

aleatorio = randint(1000,9999)
# Generamos el valor de id unico
id_unico = f'{nombre_2}{apellido_2}{anio_nacimiento}{aleatorio}'
print(f'\n Hola {nombre} tu codigo ID generado es {id_unico} Felicidades!')


