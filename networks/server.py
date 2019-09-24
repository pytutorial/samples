import socket

HOST = '127.0.0.1'
PORT = 8080

s = socket.socket()
s.bind((HOST, PORT))
s.listen()

print(f'Listen at {HOST}:{PORT}')

while True:
  conn, addr = s.accept()
  print('Connected from ', addr)
  data = conn.recv(4096)
  msg = data.decode()
  print(msg)
  response = 'I got your message : ' + msg 
  conn.send(response.encode())
  conn.close()

