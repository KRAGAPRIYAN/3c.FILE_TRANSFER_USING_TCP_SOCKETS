import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))

file = open("received.txt", "wb")

while True:
    data = client.recv(1024)
    if not data:
        break
    file.write(data)

file.close()
print("File received successfully")

file = open("received.txt", "r")
content = file.read()
print("File Content:")
print(content)

file.close()
client.close()