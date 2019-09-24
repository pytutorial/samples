import socket

HOST = '127.0.0.1'
PORT = 8080


while True:
    s = socket.socket()
    s.connect((HOST, PORT))

    text = input('Enter message: ')
    s.send(text.encode())
    data = s.recv(4096)
    print(data.decode())
    
    s.close()  