# -*- coding: utf-8 -*-


"""
Las funciones

Las funciones es lo mas importante en la programacion

En el contexto de la programación, una función es una secuencia
enunciados (statements) con un nombre que realizan un cómputo
Una función tiene un nombre, parámetros (opcional) y valor de regreso
(return value)(opcional)
Python incluye varias built-in functions en su librería estándar

En el contexto de la programacion las funciones son una agrupacion
    de statements de enunciados que tienen un nombre

Por que agrupamos nuestras funciones ?

    El nombre de las funciones deben ser descriptivos
        es muy importante

    Deben terner parametros (opcional) Que es lo que recive
    y puede regresar un valor


Python() es uno de los lenguajes que se conocen como Battery include
    con baterias includas tiene muchas librerias para ser usadas




Las funciones (Built-in functions)

    es una lista de constructores de funciones
    (https://docs.python.org/3/library/functions.html)
        aqui dejo el link de la informacion de
        las funciones de los constructores

Para declarar otras funciones debemos declarar (un modulo)


Otras funciones se pueden encontrar en módulos
    ○ Para utilizarlas es necesario importar el módulo
        ■ Ej. import math

Para declarar una función, utilizamos el keyword def
    ○ Ej. def my_fuction(first_arg, second_arg=None)

Las funciones se pueden componer.
    ○ Ej.
        def sum_two_numbers(x, y):
            return x + y

            other_function(sum_two_numbers(3, 4))


Ejemplo el metodo math que es para ecuaciones matematicas

    las funciones se pueden componer  osea hacer una funcion y pasar
    este valor a otra funcion


El orden las funciones es de arriba to down
    and left to right
Los argumentos pueden ser posicionales(positional arguments)
    o con nombre (named arguments)
        *Los parametros y variables son locales a la funcion
            ~ global keyword



fin del comunicado


# ejecutando desde la shell

>>> type(1)
        <class 'int'>
>>> un_entero = int('5')  comillas simples es un str
>>> print(un_entero)      pero la funcion int lo combierte
        5                 en un entero
>>> type(5)
        <class 'int'>
>>>


>>> a = bool('a')       Booleano
>>> print(a)
True
>>> a = float(3)        Flotante
>>> print(a)
3.0
>>> type(a)
<class 'float'>

>>> def suma_de_dos_numeros(x, y):  funcion
...     return x + y
...
>>> suma_de_dos_numeros(10, 15)
25
>>> type(suma_de_dos_numeros)
<class 'function'>


>>> suma_total = suma_de_dos_numeros(10, 15)   tipo entero
>>> print(suma_total)
25
>>> type(suma_total)
<class 'int'>




"""
