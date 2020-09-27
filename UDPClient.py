import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto("Hello".encode('utf-8'), ("127.0.0.1", 9099))
data, addr = sock.recvfrom(1024)
print("Server says: ")
print(data.decode())
