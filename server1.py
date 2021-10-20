import socket
import datetime
from _thread import *

server_name = 'S1'
server_ip = 'localhost'
server_port = 1111

def init_socket(server_ip, server_port):
    # Create a TCP/IP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = (server_ip, server_port)
    print("Starting up on {} port {}".format(server_address[0], server_address[1]))
    server.bind(server_address)

    # Listen for incoming connections
    server.listen(5)
    print("Waiting for connection!")
    return server

def threaded_client(connection, server_name):

    # initiate a state in server
    my_state = ""

    # receive client name: C1 / C2 / C3 from clients
    client_name = connection.recv(1024).decode()

    # send success message to notify client/LFD of successful connection
    success_message = ("Successful connection between {} and {}!".format(server_name, client_name))
    connection.send(success_message.encode())
    
    # print success message to server console
    print(success_message)


    while True:
        # receive and print message from client / LFD
        current_time = datetime.datetime.now()
        request_message = connection.recv(1024).decode()
        print("[{}] Received <{}, {}, {}, request>".format(str(current_time), client_name, server_name, request_message))

        # Change state only for clients
        if (client_name == 'C1' or client_name == 'C2' or client_name == 'C3'):
            # server state before change
            current_time = datetime.datetime.now()
            print("[{}] my_state_S = {}  before processing <{}, {}, {}, request>".format(str(current_time), my_state, client_name, server_name, request_message))

            # server state after change
            my_state = request_message
            current_time = datetime.datetime.now()
            print("[{}] my_state_S = {}  after processing <{}, {}, {}, request>".format(str(current_time), my_state, client_name, server_name, request_message))

        # disconnect to client/LFD using 'exit'
        if request_message == "exit":
            break

        # send and print receipt message to client/LFD 
        current_time = datetime.datetime.now()
        connection.send(request_message.encode())
        print("[{}] Sending: <{}, {}, {}, reply>".format(str(current_time), client_name, server_name, request_message))

    # close the connection and print on server console
    print("Connection to {} closed!\n".format(client_name))
    connection.close()


# Main method

# Initialize a socket
server = init_socket(server_ip, server_port)

# Run multithreaded socket
while True:
    connection,address = server.accept()
    start_new_thread(threaded_client, (connection, server_name))


