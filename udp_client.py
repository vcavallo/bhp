#!/usr/bin/env python

import socket

target_host = "127.0.0.1"
target_port = 80

# create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send something
client.sendto("AAABBBCCC",(target_host,target_port))

print "before receiving"

# receive something
data, addr = client.recvfrom(4096)

print data

print "after data print"

