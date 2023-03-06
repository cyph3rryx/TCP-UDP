import socket

# create a UDP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send data to server
server_address = ('localhost', 8080)
message = b'Hello, server!'
client_socket.sendto(message, server_address)

# receive data from server
data, server_address = client_socket.recvfrom(1024)
print('received', data, 'from', server_address)

# close the connection
client_socket.close()
