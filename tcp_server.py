#!/usr/bin/env python

import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))

server.listen(5)

print "[*] listening on %s:%d" % (bind_ip, bind_port)

# client-handling thread
def handle_client(client_socket):
    # print what the client sends
    request = client_socket.recv(1024)

    print "[*] received: %s" % request

    # send back a packet
    client_socket.send("Yo!")
    
    client_socket.close()


while True:
    clientsocket, addr = server.accept()

    print "[*] accepted connection from: %s:%d" % (addr[0],addr[1])

    # spin up client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client,args=(clientsocket,))
    client_handler.start()
    

