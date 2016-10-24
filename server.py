#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    dict={}
    def handle(self):                            
        client= self.rfile.read().decode('utf-8').split()                  
        if client[0] == "REGISTER":
            self.dict[client[1]] = self.client_address[0]
            print( "(Cliente,Puerto)" + ":" + str(self.client_address))
            self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
            print(self.dict)
                
if __name__ == "__main__":
    PUERTO = int(sys.argv[1])
    serv = socketserver.UDPServer(('', PUERTO),SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
