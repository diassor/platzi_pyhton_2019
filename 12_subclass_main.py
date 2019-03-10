# -*- coding: utf-8 -*-

clients = 'Edwin, Alejandro, '


def create_clients(clients_name):
    global clients

    if clients_name not in clients:
        clients += clients_name
        _add_comma
    else:
        print('Client already is in the client\'s list')


def list_clients():
    global clients
    print(clients)


def _add_comma():
    global clients
    clients += ','


def _print_welcome():
    print('Welcome to Platzi Ventas')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate cliente')
    print('[D]elete cliente')


if __name__ == '__main__':
    _print_welcome()

    command = input()

    if command == 'C':
        clients_name = input('What is the client name?')
        create_clients(clients_name)
        list_clients()
    elif command == 'D':
        pass
    else:
        print('Invalid command')
