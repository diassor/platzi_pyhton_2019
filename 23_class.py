# -*- coding: utf-8 -*-
import sys
# Agregando listas a nuestro proyecto

# Vamos a modificar le codigo de main para hacer uso de
#   estos datos

clients = ['Edwin', 'Alejandro']


def create_clients(client_name):
    global clients

    if client_name not in clients:
        clients.append(client_name)
    else:
        print('Client already is in the client\'s list')

# truco para asignar indice cuando estamos iterando
#   la funcion idx indice
#   la funcion enumerate que es para enumerar a nuestros clientes
#   las llaves solo son place hoder, osea espacios para guardar {}:


def list_clients():
    for idx, client in enumerate(clients):
        print('{}: {}'.format(idx, client))


# vamos a usar los indices dentro  de nuestra lista
#  usamos la funcion de index para allar la ubicacion
#   del nombre del cliente que queremos modificar


def update_client(client_name, updated_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_name
    else:
        print('Client is not in client\'s list')


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        print('Client is not in clients list')


def search_client(client_name):
    for client in clients_list:
        if client != client_name:
            continue
        else:
            return True


def _print_welcome():
    print('Welcome to Platzi Ventas')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[R]ead client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


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
    elif command == 'R':
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name = input('What is the updated client name ')
        update_client(client_name, update_client_name)
        list_clients()

    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()

    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        print('Invalid command')
