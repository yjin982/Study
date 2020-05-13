#echo server - client의 요청을 1회만 수행
from socket import *

#server 구축
serversock = socket(AF_INET, SOCK_STREAM) #소켓의 종류와 유형
serversock.bind(('127.0.0.1', 9999))  #bind 할때는 튜플로
serversock.listen(1) #1 ~ 5 : 동시 접속수

print('server start...')
conn, addr = serversock.accept() #연결 대기
print('client addr :', addr)
print('client message :', conn.recv(1024).decode())

conn.close()
serversock.close()
