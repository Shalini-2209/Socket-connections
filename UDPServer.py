import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.bind(('localhost', 9099))

while True:
    data, addr = soc.recvfrom(1024)
    print("Client says: ",data.decode())
    msg = bytes("Hello I am UDP-Server",'utf-8')
    soc.sendto(msg, addr)
    
