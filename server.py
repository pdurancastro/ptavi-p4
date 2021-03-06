#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import time
import json


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    dict = {}
    list_client = []

    def handle(self):
        client = self.rfile.read().decode('utf-8').split()
#       print(client)

        if client[0] == "REGISTER":
            list_client = [self.client_address[0], client[4]]
            self.dict[client[1]] = list_client
#            Imprime el cliente con su puerto
            print("(Cliente,Puerto)" + ":" + str(self.client_address))
            self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")

            if client[3] == "Expires:":
                t = int(list_client[1])
                tempo_cad = int(time.time() + t)

                list_client[1] = tempo_cad

                print(list_client[1])

                lista = []
                for cliente in self.dict:
                    tiempo_actual = int(time.time())
                    tiempo_exp = self.dict[cliente][1]
                    if tiempo_exp < tiempo_actual:
                        lista.append(cliente)
                for usuario in lista:
                    del self.dict[usuario]

#                for client in self.dict:
#                    t = self.dict[client][1]
#                    client = time.strftime('%Y-%m-%d %H:%M:%S',
#                                           time.gmtime(t))
#                    list_client[1]= client
#                    Errata si itero con el mismo cliente

#           Imprimo el diccionario para ver si se borro la gente
            print(self.dict)
            self.register2json()
            self.registered()

    def register2json(self):
        json.dump(self.dict, open('registered.json', 'w'))

    def registered(self):
        try:
            with open('registered.json') as datafile:
                self.dict = json.load(datafile)
        except:
            print('No hay registro')


if __name__ == "__main__":
    PUERTO = int(sys.argv[1])
    serv = socketserver.UDPServer(('', PUERTO), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
