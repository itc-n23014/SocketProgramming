import socket

def send_msg(s, msg):
    total = 0
    while total < len(msg):
        sent = s.send(msg[total:])
        if sent == 0:
            raise RuntimeError('socket connection broken')
        total += sent

def recv_msg(s, chunk_len=1024):
    while True:
        received_chunk = s.recv(chunk_len)
        if len(received_chunk) == 0:
            break
        yield received_chunk

def main(HOST, PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, int(PORT)))
        while True:
            httprequest = f'GET / HTTP/1.1\r\nHost: {HOST}\r\n\r\n'
            req_decoded = httprequest.encode('utf-8')
            send_msg(s, req_decoded)
            received = b''.join(recv_msg(s))
            received_txt = received.decode('utf-8')
            print(received_txt)

if __name__ == '__main__':
    host_port_input = input("Enter HOST:PORT: ")
    HOST, PORT = host_port_input.split(':')
    main(HOST, PORT)

