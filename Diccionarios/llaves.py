# conocer las llaves, valores e items dentro de un diccionario
# keys
# values
# items
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# keys
# llaves = diccionario.keys()
llaves = tuple(diccionario.keys())
print(llaves)

# valores
# valores.values()
valores = tuple(diccionario.values())
print(valores)

# elementos -> llave:valor
# elementos = diccionario.items
elementos = tuple(diccionario.items())
print(elementos)