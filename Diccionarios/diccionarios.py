# diccionarios en python
# se define diccionario = {}
# o diccionario = dict()
# su estructura no se maneja con indices sino con llaves
# {llave:valor}
# ej: diccionario = {"total":55}
# para agregar nuevas llave valor
# diccionario['usuario']='Jose'
#actualizar un valor
# diccionario['usuario']='José'
#obtener el valor mediante una llave
# print(diccionario['usuario'])

#para conocer todas las llaves dentro de un diccionario usamos diccionario.keys()
#para conocer todos los valores dentro de un diccionario usamos diccionario.values()
# recorrer un diccionario -> for key, value in diccionario.items():
#print(key, value)
elementos = {'a': 1, 'b': 2, 'c':3, 'a': 4}

"""
elementos['nombre'] ='Cody' # Crea la llave con su valor
elementos[(1, 2, 3)] ='La llave es una tupla'

# Actualiza el valor de la llave
elementos['nombre'] = 'CódigoFacilito'

si una llave no existe dentro de un diccionario, la crea, si ya existe, la actualiza
"""

print(elementos)
print(len(elementos)) # para saber la longitud de un diccionario