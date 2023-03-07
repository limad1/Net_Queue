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

def print_menu():
    print(40*'*')
    print('\t1 - Atedimento convencional')
    print('\t2 - Atedimento preferencial')
    print('\t3 - Sair')
    print(40*'*')


def main():
    op = ''
    p = 0
    n = 0
    while op != '3':
        print_menu()
        op = input('\tSelecione opção: ')
        print(op)
        if op == '1':
            n += 1
            msg = "[N{}] ".format(n) + input('\tNome: ').strip().upper()
            response = send_msg(msg)
            if response:
                print('\t{}'.format(response))
        elif op == '2':
            p += 1
            msg = "[P{}] ".format(p) + input('\tNome: ').strip().upper()
            response = send_msg(msg)
            if response:
                print('\t{}'.format(response))

if __name__ == '__main__':
    main()
