import socket

HOST = socket.gethostname()  # as both code is running on same pc
PORT = 5000  # socket server port number

#---------------------------------------------------------------------------

#Erste Aufgabe variablen
minimum = 1
message1= ""
#---------------------------------------------------------------------------

print("Start Client")

client_socket = socket.socket()  # instantiate
client_socket.connect((HOST, PORT))  # connect to the server

message = input(" -> ")  # take input
if message == "number":

    maximum = int(input("Maximum -> "))
    minimum = int(input("Minimum -> "))
    message1 = " "

    message1 += "Max:" + str(maximum) + ";"
    message1 += "Min:" + str(minimum) + ";"

    print(message1)



while message.lower().strip() != 'bye':
    client_socket.send(message.encode())  # send message
    client_socket.send(message1.encode())  # send message

    data = client_socket.recv(1024).decode()  # receive response
    num = client_socket.recv(1024).decode()  # receive response
    print('Received from server: ' + data)  # show in terminal

    message = input(" -> ")  # again take input

client_socket.close()  # close the connection

