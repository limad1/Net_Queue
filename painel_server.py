#!/usr/bin/env python
# -*- coding: utf-8 -*-


from datetime import datetime
import socket

def hora():
    data_e_hora_em_texto = datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')
    return data_e_hora_em_texto



def print_menu():
    print(40*'*')
    print('\t1 - Iniciar o servidor')
    print('\t2 - Sair')
    print(40*'*')


def start_server():
    localIP = "192.168.1.67"
    localPort = 2040
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
            #print('Message from {}: {}'.format(address, message))
            if message[1] == "P":
                hora_atual = hora()
                nome = message
            if message[1] == "P":
                hora_atual = hora()
                nome = message
            else:
                hora_atual = hora()
                nome = message

            print("""
#################################################
                   ATEDIMENTO
=================================================
                    CHAMANDO:
    {}
=================================================
    [P] - Prioridade  | [N] - Normal    
-------------------------------------------------
    {}
#################################################
""".format(nome,hora_atual))

            # Sending a reply to client
            #UDPServerSocket.sendto(str(message).upper().encode(), address)
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
        op = input('Digite a opção: ')
        print(op)
        if op == '1':
            start_server()

if __name__ == '__main__':
    main()