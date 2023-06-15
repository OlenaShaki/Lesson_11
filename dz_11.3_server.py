import socket

def is_punktiantian(znak):
    return znak == "," or znak == "." or znak == ";" or znak == ":" or znak == "!" or znak == "?" or znak == '-' or znak == '='

def get_clean_string(text):
    s = ""
    for i in text:
        if is_punktiantian(i) == False:
            s += i
    return s

def words_count(text):
    return len(get_clean_string(text).split())


def server():
    port = 54321

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))

    server_socket.listen(10)
    print('Server started')

    while True:
        connection, address = server_socket.accept()
        print('    connection: ', address)

        message = str(connection.recv(1024), encoding='UTF-8')
        if message == 'close':
            connection.close()
            break

        response = str(words_count(message))
        connection.send(bytes(response, encoding='UTF-8'))
        connection.close()

server()