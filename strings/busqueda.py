#extraer y encontrar strings dentro de otros
# para saber si un stirng existe dentro de otro se usa .count
titulo_curso = 'Curso profesional de Python, donde aprenderemos Python'
# titulo_curso.count('Python') -> indicara las veces que aparece python dentro del string
# se pueden evaluar strings, frases o letras
# tambien podemos usar
# print('Python' in titulo_curso)
# print('python' in titulo_curso) dara false
# para python hay diferencia entre mayusculas y minusculas
#se puede poner todo el string en minuscula para que no de false
# print('python' in titulo_curso.lower())
# print('php' not in titulo_curso.lower()) -> para confirmar que un texto no esta dentro del string

"""
contador = titulo_curso.count('a')

print(contador)
"""

# startswith -> para saber si un string comienza con la palabra que pasemos como parametro
# endswith -> para saber si un string termina con la palabra que pasemos como parametro

print(titulo_curso.endswith('Python'))