# 3c.CREATION FOR FILE TRANSFER USING TCP SOCKETS
## AIM
To write a python program for creating File Transfer using TCP Sockets Links

## Date: 25/02/2026
## Roll.No: 212225040323

## ALGORITHM:
1. Import the necessary python modules.
2. Create a socket connection using socket module.
3. Send the message to write into the file to the client file.
4. Open the file and then send it to the client in byte format.
5. In the client side receive the file from server and then write the content into it.
## PROGRAM

server.py

```
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
```

client.py

```
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
```

## OUPUT

Server-Side

![alt text](<Screenshot 2026-02-25 110518.png>)

Client-Side

![alt text](<Screenshot 2026-02-25 110542.png>)

Execution

![alt text](<Screenshot 2026-02-25 110558.png>)

## RESULT
Thus, the python program for creating File Transfer using TCP Sockets Links was 
successfully created and executed.
