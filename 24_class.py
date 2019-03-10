# -*- coding: utf-8 -*-

# Diccionarios

# Los diccionarios se conocen con muchos nombres a lo largo
#   de la programacion , hastmatch, mapas, objetos,
#   En python se conocen como diccionarios y es una
#       asociación entre llaves y valores .
#       para acceder a lista debe ser un casi cualquier objeto
#       que nos podamos imaginar normalmente se ven con strings
#   Los diccionarios funcionan con cualquier tipo de llave
#   Es una asociación entre llaves y valores
#   Esto es una estructura de datos
#   para acceder a un diccionario tenemos dos asociaciones


# Un diccionario es similar a una lista en el sentido de que
#   se puede acceder a través de índices
#   (en el diccionario se llaman llaves)
#   ○ En la lista los índices tienen que ser enteros
#   ○ En el diccionario pueden ser casi cualquier tipo

# Un diccionario es una asociación entre llaves (keys)
#   y valores (values)

# Los diccionarios se inicializan con {} o con la función dict
#   ○ Ej.
productos = {}  # empiezan en basio
productos['leche'] = 23.50  # Diccionarios

# Los diccionarios tienen diferentes metodos
#       la funcion dir nos muestra las diferentes funciones de diccionario

# Existen varias formas de ciclar a lo largo de un diccionario
#   ○ Ej.
for key in my_dict.keys():
    pass
for value in my_dict.values():
    pass
for key, value in my_dict.items():
    pass

rae = {}
rae['pizza'] = 'La comiLa comida mas deliciosa del mundo'
rae['pasta'] = 'La comida mas sabrosa  de italia'
rae.keys()
# dict_keys(['pizza', 'pasta'])
rae.values()
# dict_values(['La comida mas deliciosa del mundo',
#       'La comida mas sabrosa  de italia'])
rae.items()
# dict_items([('pizza', 'La comida mas deliciosa del mundo'),
#        ('pasta', 'La comida mas sabrosa  de italia')])

# Estos metodos nos sirven para iterar
#       Ejemplo:

for key in rae.keys():
    print(key)

pizza
pasta


for key in rae.values():
    print(key)

La comida mas deliciosa del mundo
La comida mas sabrosa  de italia


for key, value in rae.items():
    print(key, value)

pizza La comida mas deliciosa del mundo
pasta La comida mas sabrosa  de italia


dir(rae)
['__class__', '__contains__', '__delattr__',
    '__delitem__', '__dir__', '__doc__', '__eq__',
    '__format__', '__ge__', '__getattribute__', '__getitem__',
    '__gt__', '__hash__', '__init__', '__init_subclass__',
    '__iter__', '__le__', '__len__', '__lt__', '__ne__',
    '__new__', '__reduce__', '__reduce_ex__', '__repr__',
    '__setattr__', '__setitem__', '__sizeof__', '__str__',
    '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get',
    'items', 'keys', 'pop', 'popitem', 'setdefault', 'update',
    'values']
