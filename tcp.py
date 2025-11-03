server.py
import socket

s = socket.socket()
s.bind(('localhost', 9999))
s.listen(1)
print("Server waiting for connection...")

conn, addr = s.accept()
print("Connected with:", addr)

while True:
    data = conn.recv(1024).decode()
    if not data or data.lower() == 'bye':
        print("Connection closed.")
        break
    print("Client:", data)
    conn.send(data.encode())  # Echo back

conn.close()
s.close()


client.py

import socket

s = socket.socket()
s.connect(('localhost', 9999))

while True:
    msg = input("You: ")
    s.send(msg.encode())
    if msg.lower() == 'bye':
        break
    data = s.recv(1024).decode()
    print("Server:", data)

s.close()
