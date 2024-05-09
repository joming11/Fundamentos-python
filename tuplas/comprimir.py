# comprimir elementos para generar tuplas
# lista = [1, 2, 3, 4, 5]
# tupla = (10, 20, 30, 40, 50)
# resultado = zip(lista, tupla) -> esto genera un objeto zip que combina ambos elementos
# si se quiere una tuplas de ese zip
#resultado = tuple(resultado) -> genera una tupla con subtuplas
# print(resultado)

#si uno de los elementos tiene un mayor numero de elementos, estos se ignoraran, en este caso, 6 y 7 no tomaran en cuenta en los emparejamientos
lista = [1, 2, 3, 4, 5, 6, 7]

tupla = (10, 20, 30, 40, 50)

lista_2 = [100, 200, 300, 400, 500, 600, 700]

tupla_2 = (1000, 2000, 3000, 4000, 5000)

resultado = zip(lista, tupla, lista_2, tupla_2) # -> zip
# resultado = list(resultado)
resultado = tuple(resultado)

print(resultado)