import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 50000


s.connect((host, port))

while True:
    print("Wiadomosc:")
    msg = input()
    data = s.sendall(str.encode(msg))
    resp = s.recv(1024)
    print("Client 1:", resp.decode())