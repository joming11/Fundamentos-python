#metodos para trabajar con string
#split -> genera una lista a partir de un string
#join -> genera un string a partir de una lista
"""
si el listado estuviese unido con guiones se tomaria como un solo elemento
lenguajes = 'Python-Ruby-Java-Rust-C++-C'

teniendo espacio si se tomara cada elemento
lenguajes = 'Python Ruby Java Rust C++ C'

separa por default con espacios
listado_lenguajes = lenguajes.split('', numero de coincidencias que quiero) # espacios 

print(listado_lenguajes)
"""

lenguajes = ['Python', 'Ruby', 'Java', 'Rust']
# ' '.join(lenguajes) -> se indica primero como se quiere separar las palabras dentro del string
# ' - '.join(lenguajes)
# ' / '.join(lenguajes)

string_lenguajes = '-'.join(lenguajes)

print(string_lenguajes)
print(type(string_lenguajes))