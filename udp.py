server.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 9999))
print("UDP Server is running...")

while True:
    data, addr = s.recvfrom(1024)
    msg = data.decode()
    if msg.lower() == 'bye':
        print("Client disconnected.")
        break
    print("Client:", msg)
    s.sendto(data, addr)  # Echo back the same data

s.close()

client.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = ('localhost', 9999)

while True:
    msg = input("You: ")
    s.sendto(msg.encode(), server)
    if msg.lower() == 'bye':
        break
    data, _ = s.recvfrom(1024)
    print("Server:", data.decode())

s.close()
