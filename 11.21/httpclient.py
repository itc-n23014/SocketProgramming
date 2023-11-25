import socket

def sending(sock,msg):
    total = 0
    msg_len = len(msg)
    while total < msg_len:
        sent_len = sock.send(msg[total:])
        if sent_len == 0:
            raise RuntimeError('socket sonnection broken')
        total += sent_len

def receiving(sock):
    while True:
        received = sock.recv(1024)
        if len(received) == 0:
            break
        yield received

def main(host,port):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect((host,port))
        request = "GET / HTTP/1.1\r\n"
        + f'Host: {host}:{port}\r\n'
        + 'User-Agent: curl/7.68.0\r\n'
        + 'Accept: */*\r\n\r\n'
        request_byte = request.encode('utf-8')
        sending(s,request_byte)
        received = b''.join(receiving(s))
        received_txt = received.decode('utf-8')
        print(received_txt)

if __name__ == '__main__':
    host,port = input().split(':')
    main(host,int(port))
