'''
    텐서플로 변수
'''
import tensorflow as tf
import numpy as np
f = tf.Variable(1.0)  # 변수형 텐서에 scalar값을 기억
v = tf.Variable(tf.ones((2, )))  # 변수형 텐서에 vector를 기억
m = tf.Variable(tf.ones((2, 1)))  # 변수형 텐서에 matrix를 기억  
print(f)
print(v, '   ', v.numpy())
print(m)

v1 = tf.Variable(1)  # 상수
print(v1)
v1.assign(10)
print(v1, '   ', v1.numpy(), '   ', type(v1))

v2 = tf.Variable(tf.ones(shape=(1)))  # 1차원 텐서
# v2.assign(20)  # ValueError: Shapes (1,) and () are incompatible
v2.assign([20])   # 1차원 텐서이므로 배열값을 할당
print(v2, '   ', type(v2))

v3 = tf.Variable(tf.ones(shape=(1,2)))  # 2차원 텐서
v3.assign([[30, 40]])
print(v3, '   ', type(v3))



v1 = tf.Variable([3])
v2 = tf.Variable([5])
v3 = v1 * v2 + 10
print(v3.numpy())

var = tf.Variable([1,2,3,4,5], dtype=tf.float32)
result1 = var + 10
print(result1)

w = tf.Variable(tf.ones(shape=(1,)))
m = tf.Variable(tf.ones(shape=(1,)))
w.assign([3])
m.assign([2])

def func1(x):   # 파이썬 함수
    return w * x + m
out_a1 = func1([3])
print(out_a1) # assign 전 4, assign후 11


 

w = tf.Variable(tf.zeros(shape=(1, 2)))
m = tf.Variable(tf.zeros(shape=(1,)))
w.assign([[2, 3]])

@tf.function   # autograph 기능 : 내부적으로 tf.Grahp + tf.Session을 해줌 -> 속도가 빨라짐, 디버깅은 좀 불편쓰~
def func2(x):
    return w * x + m
out_a2 = func2([3])
print(out_a2)


print('\n')
# 난수
w = tf.Variable(tf.keras.backend.random_normal([5, 5], mean=0, stddev=0.3))
print(w.numpy().mean())
print(np.mean(w.numpy()))
print(w)
b = tf.Variable(tf.zeros([5]))
print(b * w)

rand1 = tf.random.normal([4], 0 ,1)  # 4개 요소, 평균, 표준편차
print('rand1 :', rand1)
rand2 = tf.random.uniform([4], 0, 1) # 4개 요소, 최소, 최대
print('rand2 :', rand2)


# 변수 치환 좀 더 ... 
aa = tf.ones((2, 1))
print(aa.numpy())
m = tf.Variable(tf.zeros((2, 1)))
print(m.numpy())

m.assign(aa)  # 0을 다시 1로 치환
print(m.numpy())
m.assign(m + 10)
print(m.numpy())

m.assign_add(aa)
print(m.numpy())
m.assign_sub(aa)
print(m.numpy())