'''
Process
실행 중인 응용프로그램으로 자신만의 메모리를 확보하고 있다. 다른 process 와 메모리 공유를 하지 않는다.
'''
from subprocess import *
import time

#Popen("C:\\Windows\\System32\\calc.exe")      #응용프로그램 실행
#call("C:\\Windows\\System32\\notepad.exe")    #응용프로그램 실행
#Popen(['ping', 'www.google.com'])

'''
Thread
Light Weight process라고도 할 수 있다. process와 달리 같은 process 내에서 자원(메소드/함수)를 공유할 수 있다. 
'''
import threading

def run(id):
    for i in range(10):
        print('id:{} --> {}'.format(id, i))
        time.sleep(0.3)

#thread를 사용하지 않은 경우
#run('일')
#run('이')  #일 --> 0~9, 이 --> 0~9 로 순차적으로 진행, 일차적 진행

#thread를 사용한 경우
#th1 = threading.Thread(target=run, args='일')
#th2 = threading.Thread(target=run, args='이')

#th1.start()
#th2.start()
#th1.join() #사용자 정의 스레드가 종료될때까지 메인 스레드 종료를 대기시킴
#th2.join()


#thread를 사용한 경우(반복문)
ths = []
for i in range(2):
    th = threading.Thread(target=run, args=(i,))
    th.start()
    ths.append(th)

for th in ths:
    th.join()

print('프로그램 종료')