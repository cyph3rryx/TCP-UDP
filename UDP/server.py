import socket

# create a UDP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind the socket to a specific address and port
server_address = ('localhost', 8080)
server_socket.bind(server_address)

while True:
    # receive data and client address
    data, client_address = server_socket.recvfrom(1024)
    print('received', data, 'from', client_address)

    # send data back to client
    server_socket.sendto(data, client_address)
