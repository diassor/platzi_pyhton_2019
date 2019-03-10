# -*- coding: utf-8 -*-
# Estructuras condicionales
# entender como funcionan las Estructuras booleanas
# una expresion booleana siempre se evalua como verdadero o
# como falso

# Entender como funcionan  los operadores de comparacion
# como se relacionan dos valores
"""
x = 2
y = 3

    X == Y      si es igual a Y
    x != y      si es diferente de Y
    x > y       si es mayor que x
    x < y       si es menor que x
    x >= y      si es menor o igual
    x <= y      si es mayor o igual

"""

# vamos al interactive shell dentro nuestro entorno virtual
"""
>>> x = 2
>>> y = 3
>>> x == y
False
>>> y = 2
>>> x == y
True
"""

# nota si  dejo un espacion antes de escribir la variante sale un error
""">>>  x != y
  File "<stdin>", line 1
    x != y
    ^
IndentationError: unexpected indent
>>> x == y
True
>>> x != y
False """

"""
Tablas de verdad

        AND
    A   B   salida
    F   F      F
    F   T      F
    T   T      F
    T   T      T


        OR
    A   B   salida
    F   F      F
    F   T      T
    T   T      T
    T   T      T


            NOT
        A      salida
        F         T
        T         F


>>> (x < y ) and (a > b)
False
>>> (x <= y ) or (a < b)
True
>>> (x <= y ) and  (a < b)
True
"""

# usando una condicional como if

"""
>>> if x < y :
...     print('x es menor que y')
... else:
...     print('x es mayot que y')
...
x es menor que y
"""
