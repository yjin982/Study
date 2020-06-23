'''
    상수(constant())와 변수(Variable())
      상수 : 텐서(일반적인 상수값)를 직접 기억,
      변수 : 텐서가 저장된 주소를 기억 
'''
import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

a = 10
print(a, '/', type(a))
print()

b = tf.constant(10)
print(b, '/', type(b))
print()

c = tf.Variable(10)
print(c, '/', type(c))
print('=' * 40)

print()
# node1 = tf.constant(3.0, tf.float32)
# node2 = tf.constant(4.0)
node1 = tf.Variable(3.0, tf.float32)
node2 = tf.Variable(4.0)
print(node1)
print(node2)

node3 = tf.add(node1, node2)
print(node3, '\n')


print('=' * 40)
v = tf.Variable(1)

@tf.function
def find_next_odd():
    abc()    # auto graph 지원 함수가 다른 함수를 호출하면 (호출당한)해당 함수도 오토그래프
    v.assign(v + 1)
    if tf.equal(v % 2, 0):
        v.assign(v + 10)

def abc():
    print('abc')

find_next_odd()
print(v.numpy())


print('=' * 40)
# 1 ~ 3까지 숫자 증가
def func():
    temp = tf.constant(0)
    num = 1
    for _ in range(3):
        #temp = tf.add(temp, num)  # 누적
        temp += num
    return temp

a = func()
print(a.numpy(), '   ', np.array(a))


# 위와 달리 constant가 함수 밖에 있을 때
temp = tf.constant(0)
def func2():
    num = 1
    global temp # <- 추가 코드
    for _ in range(3):
        temp = tf.add(temp, num)
    return temp
b = func2()
print(b.numpy()) #UnboundLocalError: local variable 'temp' referenced before assignment


def func3():
    temp = tf.Variable(0)
    num = 1    
    for _ in range(3):
        #temp = tf.add(temp, num)
        temp.assign_add(num)
    return temp
c = func3()
print(c.numpy())


temp = tf.Variable(0)  #<- 오토그래프 위로 올리면 에러 없어짐
@tf.function   # 오토그래프를 쓰니까 뜨는 에러
def func4():
    num = 1    
    for _ in range(3):
        temp.assign_add(num)
    return temp
d = func4()
print(d.numpy()) #ValueError: tf.function-decorated function tried to create variables on non-first call.


print('=' * 40)
# 구구단 출력
# @tf.function
def gugu1(dan):
    num = 0
    #aa = tf.constant(5)  # 오토그래프 쓰면 못 씀
    #print(aa.numpy())    # 오토그래프 내에서는 _.numpy() 가 실행이 안됨
    for _ in range(9):
        num = tf.add(num, 1)
        print('{} * {} = {:2}'.format(dan, num, dan*num)) #TypeError: unsupported format string passed to Tensor.__format__
        # 오토그래프 내에서 포멧도 안됨
gugu1(4)


print()
# @tf.function
def gugu2(arg):
    for i in range(1, 10):
        result = tf.multiply(arg, i)
        print('{} * {} = {:2}'.format(arg, i, result)) #TypeError: unsupported format string passed to Tensor.__format__
        # 오토그래프 내에서 포멧도 안됨
gugu2(4)