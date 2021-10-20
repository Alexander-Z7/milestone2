#coding=utf-8
import socket
import datetime

# Create a TCP/IP socket
sock_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address_1 = ('localhost', 1111)
server_address_2 = ('localhost', 2222)
server_address_3 = ('localhost', 3333)
print("Connecting to {} port {}".format(server_address_1[0], server_address_1[1]))
sock_1.connect(server_address_1)
sock_2.connect(server_address_2)
sock_3.connect(server_address_3)

# send the client name C1 to server
client_name = "C2"
sock_1.send(client_name.encode())
sock_2.send(client_name.encode())
sock_3.send(client_name.encode())

# receive the successful connection message from server
success_message_1 = sock_1.recv(1024).decode()
print(success_message_1)

success_message_2 = sock_2.recv(1024).decode()
print(success_message_2)

success_message_3 = sock_3.recv(1024).decode()
print(success_message_3)

while True:
    # Send request to server
    request_message = input("\nPlease enter the message you want to send to Sever: ")
    sock_1.send(request_message.encode())
    sock_2.send(request_message.encode())
    sock_3.send(request_message.encode())

    # Print request message on client console
    current_time = datetime.datetime.now()
    print("[{}] Sent <{}, S1，S2, S3 {}, request>".format(str(current_time), client_name, request_message))

    # disconnect from server using 'exit'
    if request_message == "exit":
        print("Disconnect from S1，S2, S3!")
        break

    # Get reply from server
    reply_message_1 = sock_1.recv(1024).decode()
    reply_message_2 = sock_2.recv(1024).decode()
    reply_message_3 = sock_3.recv(1024).decode()

    # Print reply message on client console
    current_time = datetime.datetime.now()
    print("[{}] Received <{}, S1, {}, reply>".format(str(current_time), client_name, reply_message_1))
    print("[{}] Received <{}, S2, {}, reply>".format(str(current_time), client_name, reply_message_2))
    print("[{}] Received <{}, S3, {}, reply>".format(str(current_time), client_name, reply_message_3))

# close the socket
sock_1.close()
sock_2.close()
sock_3.close()
