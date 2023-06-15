import socket

def server():
    port = 54321

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))

    server_socket.listen(10)
    print('Server started')

    while True:
        connection, address = server_socket.accept()
        print('    connection: ', address)

        client_message = str(connection.recv(1024), encoding='UTF-8')
        if client_message == 'close':
            connection.close()
            break

        server_message = input('Enter message: ')
        connection.send(bytes(server_message, encoding='UTF-8'))
        connection.close()

server()