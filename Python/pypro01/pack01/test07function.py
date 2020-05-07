# 함수 : 실행 단위
# 내장 함수
print(sum([3,5,7]))
print(int(1.7), float(4), str(5) + 'five')
print(round(1.2), round(1.6))

import math
print(math.ceil(1.2), math.ceil(1.6))    #2, 2 정수 근사치 중 큰 수
print(math.floor(1.2), math.floor(1.6)) #1, 1 정수 근사치 중 작은 수

x = [10,20,30]
y = ['a', 'b']
for i in zip(x, y):
    print(i)
else:
    print()

''' ... 다른 여러가지 내장 함수들 ... '''

# 사용자 정의 함수
def Dofunc1():
    print('Dofunc1')
Dofunc1()        #함수 호출
print(Dofunc1) #함수의 주소
kkhoues = Dofunc1
kkhoues() #함수 주소 치환


def Dofunc2(a, b):
    print('Dofunc2')
    result = Dofunc3(a, b) #함수가 함수를 호출가능 - 일급함수를 지원
    return result

def Dofunc3(m, n):
    temp = m + n
    return temp

mster = Dofunc2
print(mster(5, 6))
print(mster('대한', '민국'))

print(globals()) #현재 사용 중인 객체 목록

def isOdd(arg):
    return arg % 2 == 1 #홀수만 리턴

myDict = {x:x * x for x in range(11) if isOdd(x)}
print(myDict)


print()
# 전역, 지역 변수
player = 'kildong' #global

def funcSoccer():
    name = 'son'   #local
    player = 'hunmin'
    print(name, player)

funcSoccer()
print(player)
#print(name)

print()
a = 10
b = 20
c = 30
print('1) a:', a, 'b:', b, 'c:', c)

def funcTemp():
    b = 55
    print('2) a:', a, 'b:', b, 'c:', c)
    
    def funcTemp2():
        #c = 66
        global c     #전역변수로 선언
        nonlocal b #부모 함수의 멤버로 치환
        print('3) a:', a, 'b:', b, 'c:', c)
        c = 66 #로컬변수일시 error : local variable 'c' referenced before assignment, c는 지역변수이지만 출력후 초기화하기때문에 에러가 발생하게됨
        b = 70
        
    funcTemp2()
    print('4) a:', a, 'b:', b, 'c:', c)

funcTemp()
print('n) a:', a, 'b:', b, 'c:', c)

