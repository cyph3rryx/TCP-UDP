import socket

# create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the socket to the server's address and port
server_address = ('localhost', 8080)
client_socket.connect(server_address)

# send data
message = b'Hello, server!'
client_socket.sendall(message)

# receive data
data = client_socket.recv(1024)
print('received:', data)

# close the connection
client_socket.close()
