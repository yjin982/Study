#client side
from socket import *

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('127.0.0.1', 8888)) #server와 연결
clientsock.sendall('hello world'.encode(encoding='utf_8'))  #송신

re_msg = clientsock.recv(1024).decode()
print('수신 자료  - ' + re_msg)

clientsock.close()
