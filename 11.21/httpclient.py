import socket

HOST = input('IPアドレスかドメイン名を入力してください: ')
PORT = int(input('ポート番号を指定してください: '))
print(f"{HOST}へ{PORT}番ポートで接続します...")
HOST = socket.gethostbyname(HOST)

def sending(s, msg):
    total = 0
    while total < len(msg):
        sent = s.send(msg[total:])
        if sent == 0:
            raise RuntimeError('socket connection broken')
        total += sent

def receiving(s):
    while True:
        received = s.recv(1024)
        if not received:
            break
        yield received

def main(HOST, PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        request = ('GET / HTTP/1.1\r\n'
                   + f'Host: {HOST}\r\n\r\n')
        sending(s, request.encode('utf-8'))
        received_bytes = b''.join(receiving(s))
        received_txt = received_bytes.decode('utf-8')
        print(received_txt)

if __name__ == '__main__':
    main(HOST, PORT)

