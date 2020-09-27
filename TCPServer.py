import socket
import datetime


s = socket.socket()
print("Socket created");

s.bind(('localhost', 9090))

s.listen(3)

print("waiting for connection")

t = datetime.datetime.now()
date = t.strftime('%m/%d/%Y ')
time = t.strftime(' %H:%M:%S')


while True:
    c, addr = s.accept()
    choice = c.recv(1024).decode()
    print("Connection established" , addr, choice)
    if choice == "date":
        c.send(bytes(date,'utf-8'))
    c.send(bytes(time, 'utf-8'))
    c.close()
