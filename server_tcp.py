import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
file = open('output.txt', 'w')

try:
    server.bind(("0.0.0.0", 3356))
    server.listen(5)
    print('Server TCP - n0body v1.1.4.')
    print('------------------------------------------------------')
    print('Listening...')
    print('------------------------------------------------------')

    client_socket, address = server.accept()
    print('Received from: ' + address[0])
    print('------------------------------------------------------')

    data = client_socket.recv(2024).decode()
    file.write(data)
    server.close()

except Exception as error:
    print('------------------------------------------------------')
    print('---> Algo deu errado!', error)
    server.close()