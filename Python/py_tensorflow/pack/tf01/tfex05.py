'''
    연산자와 기본 함수
'''
import tensorflow as tf
import numpy as np

x = tf.constant(7)
y = 3

result1 = tf.cond(x > y, lambda: tf.add(x, y), lambda: tf.subtract(x, y))
print(result1.numpy())

f1 = lambda: tf.constant(1)
f2 = lambda: tf.constant(2)
print(f1) # <function <lambda> at 0x000001CED6A1F828>
a = tf.constant(3)
b = tf.constant(4)

result2 = tf.case([(tf.less(a, b), f1)], default = f2)
print(result2, '\n')


# 관계 연산
print(tf.equal(1, 2).numpy())  # ==
print(tf.not_equal(1, 2)) # !=
print(tf.less(1, 2))  # <
print(tf.greater(1, 2)) # >
print(tf.greater_equal(1, 2)) # >=

# 논리연산
print(tf.logical_and(True, False))
print(tf.logical_or(True, False))
print(tf.logical_not(True, False))

print()
# 
a = tf.constant([1, 2, 2, 2, 3])
val, ind = tf.unique(a)
# Returns:   A tuple of Tensor objects (y, idx).   y: A Tensor. Has the same type as x.   idx: A Tensor of type out_idx.
print(val)
print(ind)

print()
# 차원 관련 
ar = [[1, 2], [3, 4]]
print(tf.reduce_sum(ar))    # 차원 축소 하면서 더하기
print(tf.reduce_mean(ar))  # 차원 축소 하면서 전체에 대한 mean 값
print(tf.reduce_sum(ar, axis=0)) # 차원 축소 하면서 행기준 합
print(tf.reduce_sum(ar, axis=1)) # 차원 축소 하면서 열기준 합

print()
t = np.array([[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]])
print(t.shape)  # 2면 2행 3열
print(tf.reshape(t, shape=[2, 6]))  # 2행 6열로 변경
print(tf.reshape(t, shape=[-1, 6])) # 열만 정하고 행은 자동
print(tf.reshape(t, shape=[2, -1])) # 행만 정하고 열은 자동


print()
print(tf.squeeze(t))   # 차원 축소, 열의 갯수가 1인 경우만 해당
print(tf.squeeze( [[1],[2],[3]] ))  # 3행 1열짜리가 (3,)으로

tarr = tf.constant( [[1, 2, 3], [4, 5, 6]] )  # (2, 3)
a = tf.expand_dims(tarr, 0)  # 첫번째 차원 확대
b = tf.expand_dims(tarr, 1)  # 두번째 차원 확대
c = tf.expand_dims(tarr, 2)  # 세번째 차원 확대
d = tf.expand_dims(tarr, -1)  # 상황에 따라 자동 차원 확대
print(tarr, tf.shape(tarr))  # (2, 3)
print(a, tf.shape(a))  # (1, 2, 3)
print(b, tf.shape(b))  # (2, 1, 3)
print(c, tf.shape(c))  # (2, 3, 1)
print(d, tf.shape(d))  # (2, 3, 1)


print('\n')
# one_hot
print(tf.one_hot([0, 1, 2, 0], depth=2))  # [[1. 0.]  [0. 1.]  [0. 0.]  [1. 0.]]
print(tf.one_hot([2, 5, 1, 1], depth=4)) #[[0. 0. 1. 0.]  [0. 0. 0. 0.]  [0. 1. 0. 0.]  [0. 1. 0. 0.]]
# 기본값으로 인덱스에 해당하는 위치에 1, 그렇지 않으면 0으로 표기한다.
# depth만큼 열의 갯수. [2, 5, 1, 1] 에서 2는 1행의 2열에 1, 나머지는 0으로 채우기, 5는 2행의 5열에 1을채워야 하는데 depth가 4이므로 전체 0으로 채워짐

print()
print(tf.cast([1,2,3,5], tf.float32)) # 정수를 실수로 형변환
a = 5
print(tf.cast(a > 7, tf.float32)) # a가 7보다 크면(조건이 참이면) 1.0, 아니면 0.0


print()
x = [1, 4]
y = [2, 5]
z = [3, 6]
print(tf.stack([x, y, z])) # 쌓아서 하나의 2차원 행렬인 것처럼 출력, axis=0행 단위, 1=열단위
print(tf.stack([x, y, z], axis=1))

print()
x = np.array([[0, 1, 2], [2, 1, 0]])
print(tf.ones_like(x))  # x와 같은 형태의 행렬을 1로 채워서 만듬
print(tf.zeros_like(x)) # x와 같은 형태의 행렬을 0으로 채워서 만듬