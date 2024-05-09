#Concatenacion en python
# los strings en python son inmutables
# para modificarlos hay que concatenar 
nombre = 'Miguel Angel'
apellido = 'Navas'

# nombre_completo = nombre + apellido -> los valores quedan pegados
# nombre_completo = nombre + ' ' + apellido -> se concatena tambien un espacio

# nombre_completo = 'Mr.' +  nombre + ' ' + apellido + '.'

#segunda forma de conatenar
# cada %s corresponde a una valor que se va a agregar, valor definido dentro de los parentesis
# nombre_completo = 'Mr. %s %s.' %(nombre, apellido)
#ejemplo 2
# nombre_completo = 'Mr. %s %s %s.' %(nombre, apellido, 'Pérez')

#otras formas de concatenar
#string base.format()
# nombre_completo = 'Mr. {} {}.'.format()
# nombre_completo = 'Mr. {} {}.'.format(nombre, apellido)
"""
nombre_completo = 'Mr. {nombre} {primer_apellido} {segundo_apellido}.'.format(
    nombre=nombre,
    primer_apellido=apellido,
    segundo_apellido='Pérez'
)
"""
# fstrigns generan un nuevo string usando interpolacion
nombre_completo = f'Mr. {nombre} {apellido} {"Manzanilla"}'

print(nombre_completo)