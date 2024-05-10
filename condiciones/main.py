#asignar valores mediante operadores logicos
# para or uno de los valores debe ser true
# asignara el primer valor True
variable = 'Cody' or 'CodigoFacilito'
variable = ' ' or 0 or [] or True
print(variable)

#ej
listado = []
nombre = 'Cody'

# evaluamos
'''
if listado:
    variable = listado
else:
    variable = nombre

print(variable)
'''
# esa condicion es lo mismo que hacer
variable = listado or nombre