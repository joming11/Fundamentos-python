# desempaquetado
# * -> lista
# _ -> Omitir valor

#declaramos multiples variables
# uno, dos, tres, cuatro = 1, 2, 3, 4
# podemos simplificar con una tupla
# numeros = (1, 2, 3, 4)
# uno, dos, tres, cuatro = numeros

# el desempaquetado corresponde a que los valores de una tuplas pueden ser asigandos dinamicamente a variables
# si el numero de elementos dentro de la tupla es mayor a la cantidad de variables declaradas, dará un error
# se puede definir que la ultima variable se quede con el resto de valores obteniendo una lista de valores como valor
# se define antecediendo con *
# si no se quieren usar el resto de valores, se coloca *_ para omitirlos
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# en este caso, se omite el segundo valor, y tambien se omiten el 5,6,7 y 8.
uno, _, tres, cuatro, *_, nueve, diez = numeros

print(uno)

print(tres)
print(cuatro)

print(nueve)
print(diez)

# print(resto_numeros)
