#채팅 유저
import threading, socket, sys

def Handle(socket):
    while True:
        data = socket.recv(1024)
        if not data: continue #데이터가 없는 경우
        print(data.decode('utf-8'))
        
sys.stdout.flush() #버퍼 비우기

name = input('채팅 아이디 입력 :')
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect(('127.0.0.1', 7777))
cs.send(name.encode('utf-8')) #대화명 전송

th = threading.Thread(target=Handle, args=(cs, ))
th.start()

while True:
    msg = input('>>')
    sys.stdout.flush()
    
    if not msg: continue
    cs.send(msg.encode('utf-8')) #대화 메세지 전송
    
cs.close()
    
