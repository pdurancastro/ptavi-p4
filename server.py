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
    list_client=[]
    
    def handle(self):                            
        client= self.rfile.read().decode('utf-8').split()                  
        if client[0] == "REGISTER":
            list_client=[self.client_address[0],client[4]]
            self.dict[client[1]] = list_client
            print( "(Cliente,Puerto)" + ":" + str(self.client_address)) #Imprime el cliente con su puerto
            self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
        
            if client[3] == "Expires:":
                if list_client[1] == '0':
                    del self.dict[client[1]]
                    
            print(self.dict) #Imprimo el diccionario para ver si se borro la gente
                
if __name__ == "__main__":
    PUERTO = int(sys.argv[1])
    serv = socketserver.UDPServer(('', PUERTO),SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
