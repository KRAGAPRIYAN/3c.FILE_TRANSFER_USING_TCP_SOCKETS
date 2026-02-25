import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen(1)

print("Server waiting for connection...")

conn, addr = server.accept()
print("Connected to", addr)

file = open("sample.txt", "rb")
data = file.read()
conn.sendall(data)

print("File sent successfully")

file.close()
conn.close()
server.close()