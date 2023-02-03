import socket
import random

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

print("Start Server")

# get the hostname
HOST = socket.gethostname()
PORT = 5000  # initiate port no above 1024

server_socket = socket.socket()  # get instance
# look closely. The bind() function takes tuple as argument
server_socket.bind((HOST, PORT))  # bind host address and port together

# configure how many client the server can listen simultaneously
server_socket.listen(2)
conn, address = server_socket.accept()  # accept new connection
print("Connection from: " + str(address))
while True:
    # receive data stream. it won't accept data packet greater than 1024 bytes
    data = conn.recv(1024).decode().lower()
    if not data:
        # if data is not received break
        break
    print("from connected user: " + str(data))
    print()
    y = data.split(";")
    split_string = []
    for i in y:
        split_string += i.split(":")
    print(split_string)
    print(y)
    i = 0
    max=None
    min=1
    while i < len(split_string):
        print(split_string[i])
        if split_string[i] == "max":
            max = int(split_string[i+1])
        if split_string[i] == "min":
            min = int(split_string[i+1])
        i += 2

    print(max)
    print(min)

    data = str(random.randrange(min, max))
    print(data)

    conn.send(data.encode())  # send data to the client

conn.close()  # close the connection