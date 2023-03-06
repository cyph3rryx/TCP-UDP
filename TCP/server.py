import socket

# create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific address and port
server_address = ('localhost', 8080)
server_socket.bind(server_address)

# listen for incoming connections
server_socket.listen(1)

while True:
    # wait for a connection
    print('waiting for a connection...')
    client_socket, client_address = server_socket.accept()
    print('connection from', client_address)

    # receive and send data
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.sendall(data)

    # close the connection
    client_socket.close()
