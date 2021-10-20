import socket
from sys import _clear_type_cache
import time
import datetime

# Initialize hearbeat frequency to be every 10 second
hearbeat_freq = 10
user_input = input("The default heartbeat frequency is set to be every 10 second. Do you want to change the heartbeat frequency? (y/n):")

# User manually change hearbeat frequency
if (user_input == "y"):
    hearbeat_freq = int(input("Enter the heartbeat frequency in second: "))
    print("Set heartbeat frequency to be every {} second.".format(hearbeat_freq))
# Use default hearbeat frequency
else:
    print("Use default heartbeat frequency: every 10 second.")


while True:
    try:
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #sock.settimeout(1000)

        # Connect the socket to the port where the server is listening
        server_address = ('localhost', 6666)
        sock.connect(server_address)

        # send the LFD name to server
        LFD_name = ("LFD")
        sock.send(LFD_name.encode())

        # receive the successful connection message from server
        success_message = sock.recv(1024).decode()
        print(success_message)

        # Send heartbeat message to server
        heartbeat_message = ("Are you alive?")
        sock.send(heartbeat_message.encode())

        # Print heartbeat message to LFD console
        current_time = datetime.datetime.now()
        print("[{}] Sent: <LFD, S, {}, request>".format(str(current_time), heartbeat_message))

        # Get reply from server
        reply_message = sock.recv(1024).decode()

        # Print reply message to LFD console
        current_time = datetime.datetime.now()
        print("[{}] Received: <LFD, S, {}, reply>".format(str(current_time), reply_message))

        # prevent error
        time.sleep(1) 

        # send disconnection message to server
        exit_message = ("exit")
        sock.send(exit_message.encode())
        print("Disconnect from S!\n")

        # close LFD
        sock.close()

        # set heart beaat frequency
        time.sleep(hearbeat_freq-1)

    except:
        #Fault detected
        print("Heart beat fail! Error detected from Server S!")
        break




