import socket

HOST = socket.gethostname()  # as both code is running on same pc
PORT = 5000  # socket server port number

#---------------------------------------------------------------------------

#Erste Aufgabe variablen
minimum = 1
data_string= ""
#---------------------------------------------------------------------------

print("Start Client")

client_socket = socket.socket()  # instantiate
client_socket.connect((HOST, PORT))  # connect to the server

message = input(" -> ")  # take input

while message.lower().strip() != 'bye':

    if message == "number":
        maximum = int(input("Maximum -> "))
        minimum = int(input("Minimum -> "))
        data_string = ""

        data_string += "Max:" + str(maximum) + ";"
        data_string += "Min:" + str(minimum) + ";"

        print(data_string)

        client_socket.send(data_string.encode())  # send message

    else:
        client_socket.send(message.encode())  # send message

    num = client_socket.recv(1024).decode()  # receive response
    print('Received number from server: ' + num)  # show in terminal

    message = input(" -> ")  # again take input

client_socket.close()  # close the connection

