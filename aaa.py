import socket

def main():
    client_socket = socket.create_connection(('127.0.0.1', 80))
    client_socket.sendall('GET / HTTP/1.0\r\n\r\n'.encode('ASCII'))
    response = client_socket.recv(4096).decode('ASCII')
    print(response)
    client_socket.close()

if __name__ == '__main__':
    main()
