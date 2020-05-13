#echo server - client의 요청을 계속 처리
from socket import *
import sys

host = ''
port = 8888

#server 구축
serversock = socket(AF_INET, SOCK_STREAM)

try:
    serversock.bind((host, port))
    print('server service start ... ')
    serversock.listen(5)
    
    while True:
        conn, addr = serversock.accept()
        print('client info :', addr[0], addr[1]) #ip, port num
        print(conn.recv(1024).decode())       #client message 수신 후 출력
        
        #client에게 송신
        conn.send(('from server : ' + str(addr[1]) + ' have a nice day').encode('utf_8'))

except socket.error as e:
    print('error : ', e)
    sys.exit()
finally:
    serversock.close()
    conn.close()