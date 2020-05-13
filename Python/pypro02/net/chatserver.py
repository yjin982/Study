#멀티 채팅 서버 - thread, socket
import threading, socket

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('192.168.0.61', 7777))
ss.listen(5)
print('chat server service ... ')

users = []

def ChatUser(conn):
    name = conn.recv(1024)
    data = 'ㅇㅅㅇ ' + name.decode('utf-8') + '님 입장 ㅇㅁㅇ'
    print(data)
    
    try:
        for p in users:
            p.send(data.encode('utf-8'))
            
        while True:
            msg = conn.recv(1024)
            data = name.decode('utf-8') + ' --> ' + msg.decode('utf-8')
            print('server : ', data)
            
            for p in users:
                p.send(data.encode('utf-8'))
            
    except:
        users.remove(conn) #유저가 종료한 경우 
        data = '__' + name.decode('utf-8') + '님 퇴장__'
        print('server도 볼끄야 : ', data)
        if users:
            for p in users:
                p.send(data.encode('utf-8'))
        else:
            print('서버 종료')
    

while True:
    conn, addr = ss.accept()
    users.append(conn)
    th = threading.Thread(target=ChatUser, args=(conn, ))
    th.start()
    #클라이언트가 들어올때마다 users에 담기고 유저마다 chatuser 스레드를 스타드        