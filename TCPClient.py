import socket

c = socket.socket()

c.connect(('localhost', 9090))

name = input('Enter your choice: date/time')
c.send(bytes(name, 'utf-8'))

print(c.recv(1024).decode())
