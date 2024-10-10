print('*** Generacion de email ***')

# Solicitamos los datos
nombre = input('Introduzca su nombre: ')
apellido = input('Introduzca su apellido: ')
empresa = input('Introduzca el nombre de su empresa: ')
dominio = input('Cual es el dominio en su pais? ejmplo (.com.ar)')


nombre2 = nombre.strip().replace(" ", ".").lower()
apellido2 = apellido.strip().replace(" ", ".").lower()
empresa2 = empresa.strip().replace(" ", "").lower()
dominio2 = dominio.strip()

print(f'su email es: {nombre2}.{apellido2}@{empresa2}{dominio2}')