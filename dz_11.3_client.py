import socket

def client():
    server_port = 54321

    message = input('Enter text: ')
    while message != '':
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', server_port))
        client_socket.send(bytes(message, encoding='UTF-8'))

        if message == 'close':
            client_socket.close()
            break

        response = str(client_socket.recv(1024), encoding='UTF-8')
        client_socket.close()
    
        print('    words count: ', response)

        message = input('Enter text: ')

client()