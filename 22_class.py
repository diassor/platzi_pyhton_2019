# -*- coding: utf-8 -*-

# Operaciones con listas

# Operaciones con listas
#   ● El operador + (suma) concatena dos o más listas
#   ○ Ej.
a = [1, 2]
b = [2, 3]
a + b  # [1, 2, 2, 3]
# ● El operador * (multiplicación) repite la misma lista
#   ○ Ej.
a = [1, 2]
a * 2  # [1, 2, 1, 2]Operaciones con listas

# Para añadir un elemento al final de la lista,
# podemos utilizar el método append
# ○ Ej.
a = [1]
a.append(2)  # [1, 2]

# Para eliminar el último elemento de la lista,
# podemos utilizar el método pop
#   ○ Este método, también regresa el valor que fue eliminado
#   ■ Ej.
a = [1, 2]
b = a.pop()
print(a)  # [1]
print(b)  # 2

# Para ordenar una lista, podemos utilizar el método sort
#   ○ Ej.
a = [3, 8, 1]
a.sort()  # [1, 3, 8]Operaciones con listas

# Para eliminar elementos, también podemos
# utilizar el keyword del
#   ○ del también funciona con slices
#   ○ Ej.
a = [1, 2, 3]
del a[-1]

# Si sabes qué elemento quieres eliminar,
# pero no su índice, puedes utilizar el método remove
