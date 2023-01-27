import socket

HOST = socket.gethostname()  # as both code is running on same pc
PORT = 5000  # socket server port number

print("Start Client")

client_socket = socket.socket()  # instantiate
client_socket.connect((HOST, PORT))  # connect to the server

message = input(" -> ")  # take input

while message.lower().strip() != 'bye':
    client_socket.send(message.encode())  # send message

    message = input(" -> ")  # again take input

client_socket.close()  # close the connection

