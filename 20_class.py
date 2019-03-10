# -*- coding: utf-8 -*-

#   Iterators and generators


# Un iterator es simplemente un objeto que cumple con los requisitos del
#   Iteration protocol (protocolo de iteracion ) y por lo tanto puerde ser
#   utilizado en ciclos  por ejemplo:


for i in range(10):
    print(i)
0
1
2
3
4
5
6
7
8
9
# En este caso la funcion range es un iterable que regresa
# con un nuevo valor en cada ciclo.

# Para crear una clase que implemente los metodos iter y next
#   iter = debe regresar el objeto sobre el cual se itera
#   next = debe regresar el siguiente valor y aventurar la
#          excepcion StopIteration cuando ya no hayan
#          elementos sobre el los cuales iterar

# por su parte , los generator son simplemente una forma
# rapida de crear iterables sin la necesidad de declarar
# una clase que implemente el protocolo de iteracion.

# Para crear un generator simplemente declaramos una funcion
# y utilizamos el keyword yield em ves de return para
# regresar el siguiente valor de Iterationself.

# Ejemplo:


def fibonacci(max):
    a, b = 0, 1
    while a < max:
         yield a
         a, b = b, a+b

# Es importante recalcar que una  vez que se ha agotado
# un generator ya no podemos utilizarlo y debemos crear
# una nueva instacia.

# Ejemplo :


fib_nums = [num for num in fibonacci(30)]
fib_nums
[0, 1, 1, 2, 3, 5, 8, 13, 21]
