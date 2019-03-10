# -*- coding: utf-8 -*-

# Operaciones con listas

# Notas de david
# como interactuar con las diferentes Operaciones y metodos
#   de las listas , para realizar diferentes  tipos de computos
#   con esta estructura de datos.

#
# Operaciones con listas
# Los operadores son contextuales del tipo del que estemos
#    hablando ejemplo
#       si hablamos de enteros nos debe de dar enteros
#       si estamos hablando de floot es lo mismo
#       si estamos hablando de listas el operador suma
#              tiene un comportamiento distinto es la
#               es la concatenacion

#   ● El operador + (suma) concatena dos o más listas
#   ○ Ej.
a = [1, 2]
b = [2, 3]
a + b  # [1, 2, 2, 3]
# si sumamos las dos listas lo que hace es que contatena
#       las dos listas


# ● El operador * (multiplicación) repite la misma lista
#   ○ Ej.
a = [1, 2]
a * 2  # [1, 2, 1, 2]Operaciones con listas
# En la multiplicación lo que hace es que multiplica la listas
#   cuantas veces sea su valor a multiplicar


# Las listas tienen varios metodos que podemos utlizar
#   ordenar por letras o por numeros de mayor a menor o viceverza

# Para añadir un elemento al final de la lista,
#   uno de los mas usados podemos utilizar el método append
#   los strings son inmutables
#   En las listas nosotros podemos modificar los elementos y
#   tambien de como vamos anadiendo valores a la lista podemos
#   ir modificando su tamano
#       Internamente python tiene un algoritmo que permite
#       determinar o manejar en memoria cual es tamano de byts que
#       necesitamos para nuestra lista e internamente python
#       va generando las asignado
#       pero para nosotros como programadores de python simplemente
#       decimos append y podemos anadir un nuevo elemento
# ○ Ej.
a = [1]
a.append(2)  # [1, 2]

# Para eliminar el último elemento de la lista,
# podemos utilizar el método pop
#   pop tambien tiene una segunda variante donde recibe un
#   indice este indice lo que nos permite es definir que elemento
#   queremos eliminar de nuestra lista
#       y una caracteristica que tiene pop es que no nada mas
#       elimina el elemento si no que tambien regresa el varlor
#       de tal manera que lo podemos asignar a otra variable
#       por si queremos segir modificando esa lista
#   ejemplo Si tenemos una fila de personas que ingresan al cine
#       podemos ir modificando la lista de acuerdo a las personas
#       que ingresan osea (append) y las que salen del cine (pop)


#   ○ Este método, también regresa el valor que fue eliminado
#   ■ Ej.
a = [1, 2]
b = a.pop()
print(a)  # [1]
print(b)  # 2


# Para ordenar una lista, podemos utilizar el método sort
# Lo que hace el metodo sort lo que hace es modificar la propia lista
#   y ordenarla de mayor a menor

#   ○ Ej.
a = [3, 8, 1]
a.sort()  # [1, 3, 8]Operaciones con listas


# Para eliminar elementos, también podemos
#   Tenemos varia opciones si nosotros sabemos cual es el
#   indice de la lista podemos usar pop. o podemos usar el keyword
#   (del) osea si podemos ver la lista y sus indices podemos
#   escoger el elemento a borrar [-1] corresponde al ultimo
#   elemento
# utilizar el keyword (del)


#   ○ del también funciona con slices
#   ○ Ej.
a = [1, 2, 3]
del a[-1]

# Si sabes qué elemento quieres eliminar,
# pero no su índice, puedes utilizar el método remove

# Ahora imaginemos que no sabemos el indice usamos el
#    el metodo remove este nos permite pasarle un valor de tal
#   manera que python internamente compara los valores
#   y determina cual de esos dos valores hacen match o
#   son iguales y por lo tanto los remueve
