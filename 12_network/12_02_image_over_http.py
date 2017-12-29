"""
program to retrieve an image across using HTTP. Instead of copying the data to the screen as the program runs,
we accumulate the data in a string, trim off the headers, and then save the image data to a file
"""

import socket
import time

HOST = 'data.pr4e.org'
PORT = 80

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect((HOST, PORT))

count = 0
picture = b""

my_socket.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')

while True:
    data = my_socket.recv(5120)
    if len(data) < 1:
        break
    time.sleep(0.25)
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

my_socket.close()

# Look for the end of header (2 CRLF)
pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())

picture = picture[pos+4:]
f_hand = open('stuff.jpg', 'wb')
f_hand.write(picture)
f_hand.close()

