import socket
import datetime

def words_count(text):
    return len(text.split())

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

        server_message = 'Unknown request.'
        if client_message == 'time':
            server_message = 'Current time: ' + str(datetime.datetime.now())
        elif client_message == 'address':
            server_message = 'Your address: ' + str(address)
        
        connection.send(bytes(server_message, encoding='UTF-8'))
        connection.close()

server()