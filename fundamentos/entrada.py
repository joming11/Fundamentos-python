# Recibir y leer valores ingresados por un usuario

#input() se usa para leer valores ingresados por un usuario
#se puede agregar un mensaje opcional para indicar al usuario que informacion debe suministrar

nombre_completo = input('Ingresa tu nombre completo: ') # str
#print(nombre_completo)
#input siempre va a retornar un string

# para generar un entero a partir del string
# edad = input('ingresa tu edad')
# edad = int(edad)
# print(edad)
# print(type(edad))
# o
edad = int(input('Ingresa tu edad: '))

# para generar un float a partir del sting
# altura = input('ingresa tu altura')
# altura = float(altura)
altura = float(input('Ingresa tu altura: '))

# para generar un bool a partir del string
# autorizacion = input('¿Autorizas el programa? (si/no)')
# autorizacion = autorizacion == 'si'
autorizacion = input('¿Autorizas el programa? (si/no)') == 'si'

print(nombre_completo)
print(edad)
print(altura)
print(autorizacion)