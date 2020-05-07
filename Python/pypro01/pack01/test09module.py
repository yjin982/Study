''' 
module : 코드의 재사용을 가능하게 하며, 하나의 이름 공간으로 별도 관리가 가능하다 
모듈은 package 내에서 작성해야 한다.
'''
a = 10
print(a)
def aa():
    pass

import sys #표준 모듈 읽기
print(sys.path)

#sys.exit() #프로그램 강제 종료
print('exit')

import math
print(math.pi)
print(math.sin(math.radians(30))) # sign 30º

import calendar
calendar.setfirstweekday(6) #일요일을 맨 앞으로
calendar.prmonth(2020, 5)
 
import random
print('난수 출력 ')
print(random.random())
print(random.randrange(1, 10))

#랜덤 모듈로 부터 import하여서 현재 모듈의 멤버처럼 사용하기
from random import random, randrange #from 모듈명 import 멤버명(=전역변수, 클래서, 함수)
#from random import import * #모든 멤버, 비권장
print(random())
print(randrange(1, 10))   
#print(randint(1, 10)) #X


from turtle import *
p = Pen()
p.color('red', 'yellow')
p.begin_fill()
while True:
    p.forward(200)
    p.left(170)
    if abs(p.pos()) < 1:
        break
p.end_fill()
done()