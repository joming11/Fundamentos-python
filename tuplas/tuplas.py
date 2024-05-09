# tuplas en python
# se usan para guardar y listar elementos
# una ve definidas no se pueden modificar
# estructura de una tupla -> tupla = ()
# se pueden almacenar distintos tipos de datos
# tupla = ('string', '10', '11.7', False, [1,2,3])
# tambien se pueden almacenar otras tuplas

# indices de tuplas
cursos = ('Python', 'Flask', 'Django', 'Rails', 'MongoDB')
#           0           1       2          3        4

primer_curso = cursos[0]
print(primer_curso)

ultimo_curso = cursos[-1]
print(ultimo_curso)

# sub_tupla = cursos[0:3]
# sub_tupla = cursos[:3]
sub_tupla = cursos[:]
print(sub_tupla)