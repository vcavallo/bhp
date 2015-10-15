#!/usr/bin/env python

import socket
target_host = "0.0.0.0"
target_port = 9999

# create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send something
client.send("this is a request!")

# receive something
response = client.recv(4096)

print response
