print('*** Generador de email ***')

nombre = ' Nicolas Viruel Vallejo '
# Quitamos los espacios en blanco
nombre_corregido =  nombre.strip().lower() # Pasamos todo a minusculas 

# Pasamos a reemplazar los espacios por un .
nombre_corregido = nombre_corregido.replace(' ', '.')
print(nombre_corregido)

print('\n* Segunda parte *')

nombre_empresa = 'Phinx Lab'
# Quitamos espacios y pasamos a minusculas
empresa_actualizado = nombre_empresa.replace(' ', '').lower()
extension = '.com.ar'
print(f'{empresa_actualizado}{extension}')

print('\n** Ultimo paso **')

print(f'{nombre_corregido}@{empresa_actualizado}{extension}')







