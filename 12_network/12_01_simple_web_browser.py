"""
    program makes a connection to port 80 on the server www.py4e.com. Since our program is playing the role of the
    "web browser", the HTTP protocol says we must send the GET command followed by a blank line.
"""

import socket

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
my_sock.send(cmd)

while True:
    data = my_sock.recv(20)
    if len(data) < 1:
        break
    print(data.decode(),end='')

my_sock.close()