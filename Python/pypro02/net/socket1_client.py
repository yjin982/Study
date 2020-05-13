#client side
from socket import *

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('127.0.0.1', 9999)) #server와 연결
clientsock.sendall('hello world'.encode(encoding='utf_8', errors='strict'))
clientsock.close()
