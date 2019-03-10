# -*- coding: utf-8 -*-
# Operaciones con strings


# Los strings tienen varios métodos que nos sirven para manipularlas
# Algunos son:
#   ○ upper
#   ○ lower
#   ○ find
#   ○ startswith
#   ○ endswith
#   ○ capitalize


# Operadores de pertenencia
#   ○ in
#   ○ not in
# Comparaciones entre strings
#   ○ Las comparaciones son lexicográficas
#   ○ Tener cuidado:
#       ■ En Python ‘a’ y ‘A’ son diferentes
"""
Nos permite  saber si un substring  se encuentra dentro
de una secuencia mayor

# funcion dir
dir(platzi)
['__add__', '__class__', '__contains__',
'__delattr__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__',
'__getitem__', '__getnewargs__', '__gt__',
'__hash__', '__init__', '__init_subclass__',
'__iter__', '__le__', '__len__', '__lt__',
'__mod__', '__mul__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__',
'__rmod__', '__rmul__', '__setattr__', '__sizeof__',
'__str__', '__subclasshook__', 'capitalize',
'casefold', 'center', 'count', 'encode', 'endswith',
'expandtabs', 'find', 'format', 'format_map',
'index', 'isalnum', 'isalpha', 'isdecimal',
'isdigit', 'isidentifier', 'islower', 'isnumeric',
'isprintable', 'isspace', 'istitle', 'isupper',
'join', 'ljust', 'lower', 'lstrip', 'maketrans',
'partition', 'replace', 'rfind', 'rindex', 'rjust',
'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
'startswith', 'strip', 'swapcase', 'title', 'translate',
'upper', 'zfill']
"""

# lo que permiten hacer es configurar como Python
# se ejecuta

# estos son todos los metodos que podemos usar sobre la
# variante platzi
# los metodos que tienen doble guion bajop al inicio y al final
# son llamados metodos magicos

# Un doble guión bajo Antes y Después de un nombre
# (por ejemplo __spam__)
# Esta convención se utiliza para nombrar métodos
# especiales utilizado por Python
# (también llamados como "métodos mágicos"
# como por ejemplo: __init__, __len__, etc.).
# Estos métodos proporcionan características sintácticas
# especiales o hacen cosas especiales al usarlos,
# por ejemplo __file__ le indica la ubicación de un
# archivo a Python.

# Esto es sólo una convención, una forma para que Python
# utilice nombres que no van a entrar en conflicto con
# los nombres definidos por el usuario.
# Uno puede sobrescribir estos métodos y definir el
# comportamiento deseado para cuando Python los llama.
# Por ejemplo, es usual sobrescribir el método
# `` __init__`` al escribir una clase.

# Estos metodos nos importa por el momento
"""
'casefold', 'center', 'count', 'encode', 'endswith',
'expandtabs', 'find', 'format', 'format_map',
'index', 'isalnum', 'isalpha', 'isdecimal',
'isdigit', 'isidentifier', 'islower', 'isnumeric',
'isprintable', 'isspace', 'istitle', 'isupper',
'join', 'ljust', 'lower', 'lstrip', 'maketrans',
'partition', 'replace', 'rfind', 'rindex', 'rjust',
'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
'startswith', 'strip', 'swapcase', 'title', 'translate',
'upper', 'zfill'
"""
# Estos metodos son lo que generalmente usamos para
# trabajar con los strings


def my_fuction():
    """ este es un texto de ayuda de como utilizar esta funcion"""
    pass


# dentro de la shell
'''


help(my_fuction)
Help on function my_fuction in module __main__:

my_fuction()
    este es un texto de ayuda de como utilizar esta funcion
(END)
'''
