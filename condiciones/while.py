# ciclo while
# se ejecuta mientras una condicion se cumpla
# se usa cuando no se sepa la cantidad de iteraciones que se necesitan

# contador = 1
# while contador <= 10:
    # print(contador)
    # contador = contador + 1


numero = 123456789
contador_digitos = 0

while numero >= 1:
    # contador_digitos = contador_digitos + 1
    contador_digitos += 1

    numero = numero / 10
#else: si la condicion no se cumple
    # print('fin del ciclo')
    print(contador_digitos)