import socket

def client():
    port = 54321

    message = input('Enter message: ')
    while message != '':
        client_socket = socket.socket()
        client_socket.connect(('localhost', port))
        client_socket.send(bytes(message, encoding='UTF-8'))

        if message == 'close':
            client_socket.close()
            break

        response = str(client_socket.recv(1024), encoding='UTF-8')
        client_socket.close()

        print('    ', response)

        message = input('Enter message: ')

client()