# listas en python
# utilizando la funcion list list()
# o []
# lista = ['string', 10, 11.7, True]
# idealmente hay que crear listas que almacenen un solo tipo de valor

# obtener los valores dentro de una lista segun su posicion
# lista_cursos = ['php', 'css', 'js', 'python']
# primer_curso = lista [0]
# print(primer_curso)
# los valores se obtienen de su indice, el cual se puede leer de izquierda a derecha desde el cero, o con numeros negativos de derecha a izquierda desde el -1

# actualizar elemntos dentro de una lista
# se define la posicion y se asigna un nuevo valor
# lista_cursos = ['php', 'css', 'js', 'python']
# lista_cursos[3] = 'html'

#Sublista
# lista_cursos = ['php', 'css', 'js', 'python']
# definimos una sublista indicando las posiciones que queremos en la sublista
# sub_lista = lista_cursos[0:3]
# el elemento en el indice 3 no se incluira

# si se coloca un numero de indice superior al numeros de elementos dentro de la lista, python dara todos los elementos posibles, no arrojara error
# lista_cursos[0:100]

# si no definimos el valor final, python devolvera todos los valores en adelante

# lista_cursos[2:] dara todos los valores desde el indice 2 en adelante

# tambien podemos omitir el indice inicial de la lista, y dara los valores hasta el indice final indicado

# se pueden tomar valores segun un salto de posiciones especificado

#sub_lista = lista_curso[1:4:2] tomara los valores del indice 1 al 4 pero de 2 en 2

#modificar listas
#añadir un nuevo elemento al final de la lista
# lista_cursos = ['php', 'css', 'js', 'python']
#lista cursos.append('react')

#añadir un nuevo elemento en un indice definido
# lista_cursos = ['php', 'css', 'js', 'python']
#list_cursos.insert(indice, nuevo elemento)
#list_cursos.insert(2, 'Angular')

#extender una lista de otra - sumar los valores de una una lista a otra lista
# lista_cursos = ['php', 'css', 'js', 'python']
#lista_cursos_2 = ['java', 'c', 'C++']
#lista_cursos.extend(lista_cursos_2)
#agrega al final los nuevos valores y no afecta en nada a listas_cursos_2

#eliminar elementos dentro de una lista
# lista_cursos.remove('html')
# utilizando indice
# se usa la palabra reservada del
# del lista_cursos[1]

# eliminar todos los elementos almacenados dentro de una lista
# lista_cursos.clear()

# metodos para listas
# para listas con un solo tipo de valor
# lista = [8, 5, 90, 1, 5, 44, 132, 600, 3, 4, 5]
# lista.sort() ordena los valores de menor a mayor
# lista.sort(reverse=True) ordena los valores de mayor a menor

# para obtener el valor minimo y maximo, se usa sort y se imprimen los indices[0] y [-1]
# o
# se puede usar min y max
# print(min(lista))
# print(max(lista))

# para saber si un elemento se encuentra dentro de la lista
# ej: print(11 in lista -> esto devolvera un booleano
#para confirmar que un numero no esta dentro de la lista
# print (11 not in lista)

# una vez confirmada la existencia de un elemento dentro de la lista, para saber su posicion usamos lista.index
# si hay mas de un elemento con el mismo valor .index retornara la primera posicion 
lista = [8, 5, 90, 1, 5, 44, 132, 600, 3, 4, 5]

print(5 in lista)

index = lista.index(5)
print(index)