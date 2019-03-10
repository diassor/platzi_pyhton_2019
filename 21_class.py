# -*- coding: utf-8 -*-

# Listas en Python

# Como en los etrings, las listas son secuencias de valores
#   ~ En las listas, los valores pueden tener cualquier tipo
# ej:
# [2,5,6]
# [‘Colombia’, ‘Mexico’, ‘Argentina’]
# [‘tacos’, 3, ‘arepas’, 6, ‘chorizo’, 9]

# Las listas son mutables, a diferencia de los strings
#   my_list = [1, 2, 3]
#   my_list[2] = 6
# Los índices de las listas, funcionan igual que los de los strings
# Las listas se inician con [] o con la función list
# Para ciclar a lo largo de los elementos de una lista,
#   normalmente usamos for loops
# ○ Ej.

for student in students:
    print(student)

# Si la lista está vacía, el cuerpo del loop nunca se ejecuta

# Notas de david python permite hacer constructors o estructuras
# de datos , esto nos permite agrupar varios valores, elementos de
# nuestro programa y poder los manejar con mayor facilidad
# Una lista puede tener a drentro otra lista .
#   ~Esto se llama una matriz y es la forma en la que
#       nosotros construimos matrices de dos dimenciones
#       o varias dimenciones adicionales en nuestros programas

# Las listas a diferencia de los strings son mutables
#       podemos modificar , borrar , adicionar
#   En python las listas son referenciales
#       No guarda en memoria directamente los objetos
#       Solo guarda referencia hacia donde viven los objetos en memoria

# Las listas se pueden inicializar de dos maneras
#   ~Una manera literal
#       Que es con los esquer brakers (corchetes[])
#   ~Una manera funcional que es con el bilding function list

# Cuando nosotros tenemos un string que es igual que otro string
#   viven en el mismo lugar de memoria
#   En las listas el objeto que contiene el string
#       Siempre es distinto el lugar DE memoria
#
weights = [12, 18, 24, 34, 50]
    id(weights)
140178779044616  lugar donde vive

ages = [12, 18, 24, 34, 50]
    id(ages)
140178779045000  lugar donde vive

# En las listas podemos crear, borrar o cambiar los
#   objetos que se encuentran dentro

# Con los strings no podemos hacer cambios solo
#   Crear all or delete all
countries = ('Colombia', 'Mexico', 'Venezuela', 'argentina')
countries[0] = 'Ecuador'
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment


# while in list we can creaded or change anythings in side
#   to list
countries = ['Colombia', 'Mexico', 'Venezuela', 'argentina']
countries[0] = 'Ecuador'
countries
['Ecuador', 'Mexico', 'Venezuela', 'argentina']


# Podemos crear alias para las lists
#   lo que hacemos es combiar un point of memory that together
#   variables esten apuntando to same lugar


countries
['Ecuador', 'Mexico', 'Venezuela', 'argentina']
global_countries = countries
global_countries
['Ecuador', 'Mexico', 'Venezuela', 'argentina']

# tienen el mismo valor
# Si se camia del origina algo esto afecta al alias
# y tambien  en sentido inverso

countries[0] = 'guatemal'
countries
['guatemal', 'Mexico', 'Venezuela', 'argentina']
global_countries
['guatemal', 'Mexico', 'Venezuela', 'argentina']

# Nota esto s una fuente de bugs muy importantes sucede
#  todo el tiempo

# como podemos evitarla: a veces si necesitamos copiar una lista
# dentro de otra lista
#   vamos a importar el modulo copy y con esto evitamos
#   que se reaccine nuevos valores al alias


import copy
global_countries = None
global_countries = copy.copy(countries)
countries[0] = 'Guatemala'
countries
['Guatemala', 'Mexico', 'Venezuela', 'argentina']
global_countries
['Russia', 'Mexico', 'Venezuela', 'argentina']



for countries in countries:
    print(countries)

Colombia
Mexico
Venezuela
argentina

# y asi podemos trabajar con un for loop dentro de una listas
