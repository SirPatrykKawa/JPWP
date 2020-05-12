import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 50000

s.bind((host, port))

s.listen(1)
conn, addr = s.accept()

while True:
    data = conn.recv(1024)
    print("Client 2:", data.decode())
    print("Wiadomosc:")
    msg = input()
    conn.sendall(str.encode(msg))