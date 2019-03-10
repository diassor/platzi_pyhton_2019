# -*- coding: utf-8 -*-

# String en Python

# lo mas importante del curso es praticar y experimentar todo lo
# relacionado a este tema de Python

# Nota buscar las propias respuestas
# Las cadenas (strings) es un tipo con comportamiento diferente
# a los int, float y bool
#   ○ Las cadenas son secuencias
#   ○ Las secuencias se pueden acceder a través de un índice
#       ■ apple = ‘apple’
#         apple[1]
# Las cadenas (al igual que otras secuencias) tienen
#  una longitud
#   ○ Para saber la longitud de una secuencia, se puede usar la función len
#       ■ len(apple)
# En Python, los caracteres que componen un string
# se reutilizan a lo largo del programa
#   ○ Esto ayuda a reducir la cantidad de memoria
#       que necesita el programa
#   ○ También significa que las strings deben ser inmutables
#       ■ x = ‘a’
#       y = ‘b’
#       id(x) == id(y)

# El conteo de un string siempre es de 0 (cero)

country = 'Colombia'
country[1]
'o'
country[-1]
'a'
country[2]
'l'
country[-2]
'i'
len(country)
8
second_letter = country[1]
print(second_letter)
'o'

# aqui es donde vive esta letra dentro de nuestro
# sistema o sea en la parte de la memoria del disco
# El alfabeto tienen un espacio en el directorio
# mis experimentos la 'o' siempre se dirije a la misma ruta

id(second_letter)
140204090190680

# otro ejercicio by myself


a = 'CCCCCCCC'
d = a[-1]
b = 'CCCCCCC'
a[-1]
'C'
v = b[-2]
id(d)
140204090128232
id(v)
140204090128232


# los strings son inmutables
# si modificamos un string un objeto esta cambia de lugar
# inmediatamente

# Por que no se pueden cambiar las strings
# por que python reutiliza todad las letras u caracteres
#  ejemplo

country = 'Mexico'
id(country)
140204089914456
country += 's'
country
'Mexicos'
id(country)
140204089914344
