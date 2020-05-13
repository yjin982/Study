'''
파이썬의 GIL 정책으로 인해 스레드 작동이 제대로 안되는 경우가 발생
multiprocessing을 위한 클래스를 별도 제공
네트워크상의 병렬 처리를 지원 
'''
from multiprocessing import Pool
import time, os

def func(x):
    print('값', x, '에 대한 작업 pid =', os.getpid())  #현재 프로세스 아이디를 얻음
    time.sleep(1)
    return x * x

if __name__ == '__main__':
    startTime = int(time.time())
    
    #for i in range(10): #일반적인 방법으로 함수를 호출, 직렬처리
    #    print(func(i))
    
    p = Pool(4)  #멀티프로세싱 방법으로 함수를 호출, 병렬처리, (3~5 사이가 권장)
    print(p.map(func, range(10)))
    
    endTime = int(time.time())
    print('총 작업 시간 :', (endTime - startTime))
    

    