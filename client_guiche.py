#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

def send_msg(msg):
    serverAddressPort = ("127.0.0.1", 2022)
    bufferSize = 1024
    bytesToSend = str.encode(msg)
    msgFromServer = None
    try:
        # Create a UDP socket at client side
        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        # Send to server using created UDP socket
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        msgFromServer = str(msgFromServer[0].decode('utf-8'))
    except Exception as ex:
        print("Sending msg error: {}".format(ex))

    # Release socket
    try:
        UDPClientSocket.close()
    except:
        pass

    return msgFromServer

def print_menu_a():
    print(40*'*')
    print('\t1 - Guichê')
    print('\t2 - Sair')
    print(40*'*')

def print_menu_b():
    print(40*'*')
    print('\t1 - Chamar preferencial')
    print('\t2 - Chamar convencional')
    print('\t3 - Em espera')
    print('\t4 - Sair')
    print(40*'*')

def main():
    op = ''
    op_a = ''
    while op != '2':
        print_menu_a()
        op = input('\tSelecione opção: ')
        print(op)
        if op == '1':
            while op_a != "4":
                print_menu_b()
                op_a = input('\tSelecione opção: ')
                if op_a == "1":
                    msg = "CFP"
                    response = send_msg(msg)
                    if response:
                        print('\t{}'.format(response)) 
 
                elif op_a == "2":
                    msg = "CFN"
                    response = send_msg(msg)
                    if response:
                        print('\t{}'.format(response))

                elif op_a == "3":
                    msg = "CFE"
                    response = send_msg(msg)
                    if response:
                        print('\t{}'.format(response))


if __name__ == '__main__':
    main()
