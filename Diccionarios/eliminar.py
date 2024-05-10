# eliminar elementos de un diccionario
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(len(diccionario)) #imprimir la longitud del diccionario

del diccionario['a'] # eliminar el elemento con llave a

# segunda forma -> elimina el elemento con llave b
valor = diccionario.pop('b') # 2

# eliminar todos los elementos de un diccionario
diccionario.clear()

print(valor)

print(diccionario)
print(len(diccionario))