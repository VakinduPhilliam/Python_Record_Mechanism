# Python Application Logging
# This script that takes a filename and sends that file 
# to the server, properly preceded with the binary-encoded 
# length, as the new logging configuration:
 
#!/usr/bin/env python

import socket, sys, struct

with open(sys.argv[1], 'rb') as f:
    data_to_send = f.read()

HOST = 'localhost'
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('connecting...')

s.connect((HOST, PORT))

print('sending config...')

s.send(struct.pack('>L', len(data_to_send)))
s.send(data_to_send)
s.close()

print('complete')
