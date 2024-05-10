# obtener elementos de un diccionario
# obtener el valor de una llave, siempre y cuando exista
# valor = diccionario['d']
# print(valor)
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# print('a' in diccionario) -> para saber si la llave a eiste dentro del diccionario
print('z' in diccionario)

"""
valor = diccionario['z']
print(valor)
"""

# get -> para obtener el valor de una llave de forma segura
# setdefault -> obtener el valor de una llave, si esta no eiste, la crea con su respectivo valor

# valor = diccionario.get('d') -> devuelve el valor
# valor = diccionario.get('y') -> devuelve el valor none ya que es una llave que no existe dentro del diccionario
# valor = diccionario.get('y', 'la llave no existe') -> se define un segundo parametro que indica que la llave no existe dentro del diccionario

#ej de .setdefault
valor = diccionario.setdefault('e', 5)

print(valor)
print(diccionario)