# -*- coding: utf-8 -*-

# For loops
"""
~ los for loops permiten ciclar a lo largo de una secuencia
~ se usan cuando se requiere ejecutar un conjunto de instrucciones
    varias veces
        * Esto tambien se llama iteration
~ Se puede utilizar el keyword continue para saltarse
    los statements restantes y pasar a la siguiente
    iteration
    ~ ej;
        for i in range(1000):
            print(i)

~ como funciona la funcion range nos da un objeto rango
    range(10) esto es igual a (0, 10)
    la i es una variable y es por convencion que se usa la i
    primero trae el 0 y luego de uno en uno hasta 10


>>> for i in range(10):
...     print(i)
...
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

"""
# Comentarios de David
# python tiene varias formas de iterar pero las usadas
# son for loop y while loop
# los while loops nos permiten iterar hasta que
# una secuencia sea falsa


# vamos a incorporar esta funcion en platzi_ventas
# vamos a usar un for loop para buscar a un cliente
# dentro de nuestra lista de clients

clients = 'Edwin, Alejandro, '


def create_clients(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client already is in the client\'s list')


def list_clients():
    global clients
    print(clients)


def update_client(client_name, updated_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', updated_name + ',')
    else:
        print('Client is not in client\'s list')


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        print('Client is not in clients list')


def _add_comma():
    global clients
    clients += ','


def _print_welcome():
    print('Welcome to Platzi Ventas')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate cliente')
    print('[U]pdate client')
    print('[D]elete cliente')


def _get_client_name():
    return input('What is the client name? ')


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_clients(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name = input('What is the updated client name ')
        update_client(client_name, update_client_name)
        list_clients()

    else:
        print('Invalid command')
