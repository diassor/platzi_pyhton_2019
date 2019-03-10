# -*- coding: utf-8 -*-
#
# Usando funciones en nuestro proyecto

# Estamos ediatndo el main.py
"""
clients = 'Edwin, Alejandro y '

if __name__ == '__main__':
    clients += 'Juan'
    print(clients)
"""

# el codigono va a correr por que es una variable global
# y las funciones tinen un ambito de acceso a las variables que se
# conocen como scout o name spaces

#            segun el info de linder

#    F823 — local variable 'clients'
#    (defined in enclosing scope on line 9)
#    referenced before assignment

#    local variable 'clients' is assigned to but never used


# usamos otro keyword global
#    declaramos dentro nuestra funcion la variable
#    global clients   # esta linea le permite usar
#                    la variable clients para poder la usar


# claro por que esta fuera de la funcion por eso no la puede leer
# al usar el keyword global nos permite contatenar la variable que
# tiene el mismo nombre para su uso dentro de la funcion

# Adicional en la funcion crearemos una funcion privada
# para poder usar la coma que esta despues de Alejandro

# es un afuncion de ayuda
"""
def _add_comma():
   global clients
   clients += ','
"""
# otra funcion de ayuda
"""
def list_clients():
    global clients

"""
#  con esta funcion son ayuda a listar los clientes y segun
# su donde se use vamos a traer a los clientes antes
# y de

clients = 'Edwin, Alejandro y '


def create_clients(clients_name):
    global clients

    clients += clients_name
    _add_comma()


def list_clients():
    global clients
    print(clients)


def _add_comma():
    global clients
    clients += ','


if __name__ == '__main__':
    list_clients()
    create_clients('Andrea')
    list_clients()
