#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

# Constantes. Dirección IP del servidor y contenido a enviar

Lista = [sys.argv[1],sys.argv[2],sys.argv[3:]]
SERVIDOR = Lista[0]
PUERTO = int(Lista[1])

if len(Lista[2]) > 0:
	LINEA = ' '.join(Lista[2])
else:
	sys.exit( 'No estas mandando texto al servidor')
 

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVIDOR, PUERTO))
    print("Enviando:", LINEA)
    my_socket.send(bytes(LINEA, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")
