#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

f_priori = []
f_normal = []


def print_menu():
    print(40*'*')
    print('\t1 - Iniciar o servidor')
    print('\t2 - Sair')
    print(40*'*')


def fila_prioridade(message):
        cliente = dict(nome=message)
        f_priori.append(cliente)
        return str("Adicionado a fila de espera.\n")

            
def fila_convencional(message):
        cliente = dict(nome=message)
        f_normal.append(cliente)
        return str("Adicionado a fila de espera.\n")

def em_espera(message):
        message = str("\n\t{} em espera.\n\t[P] - Prioridade: {}\n\t[N] - Normal: {}".format((len(f_priori) + len(f_normal)), len(f_priori),len(f_normal)))
        return message  


def proximo_p(message):
    if len(f_priori) > 0:
        for cliente in f_priori:
            message = str("{}".format(cliente["nome"]))
            f_priori.pop(0)
            return message
    else:
        return str("Prioridade {} em espera.".format(len(f_priori)))


def proximo_n(message):
    if len(f_normal) > 0:
        for cliente in f_normal:
            message = str("{}".format(cliente["nome"]))
            f_normal.pop(0)
            return message
    else:
        return str("Normal {} em espera.".format(len(f_normal)))

def start_server():
    localIP = "0.0.0.0"
    localPort = 2022
    bufferSize = 1024
    continue_loop = True
    try:
        # Create a datagram socket
        UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        # Bind to address and ip
        UDPServerSocket.bind((localIP, localPort))
        print("Server waiting for data... (CTRL+C to Stop)")
    except Exception as ex:
        print("Startup error: {}".format(ex))
        continue_loop = False

    while (continue_loop):
        try:
            # Listen for incoming datagrams
            bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
            message = bytesAddressPair[0].decode('utf-8')
            address = bytesAddressPair[1]
            return_msg = str(message).upper().encode()
            print('Message from {}: {}'.format(address, message))

            if message[1] == "P":
                return_msg = fila_prioridade(message)
            
            elif message[1] == "N":
                return_msg = fila_convencional(message)
             
            elif message.upper() == "CFP":
                return_msg = proximo_p(message)
                UDPServerSocket.sendto(str(return_msg).upper().encode(), ("192.168.1.67",2040))

            elif message.upper() == "CFN":
                return_msg = proximo_n(message)
                UDPServerSocket.sendto(str(return_msg).upper().encode(), ("192.168.1.67",2040))

            elif message.upper() == "CFE":
                return_msg = em_espera(message)

            # Sending a reply to client
            UDPServerSocket.sendto(str(return_msg).upper().encode(), address)
        except KeyboardInterrupt as ex:
            print('Execução cancelada')
            continue_loop = False
        except Exception as ex:
            print('Erro de execução: {}'.format(str(ex)))

    # Release socket
    try:
        UDPServerSocket.close()
    except:
        print('.')


def main():
    op = ''
    while op != '2':
        print_menu()
        op = input('\tSelecione opção: ')
        print(op)
        if op == '1':
            start_server()


if __name__ == '__main__':
    main()