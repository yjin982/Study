'''
    선형회귀 모형 계산
'''
import tensorflow as tf
import numpy as np

x = [1., 2., 3., 4., 5.]   # label이 실수니까
y = [1.2, 2.0, 3.0, 3.5, 5.5]

w = tf.Variable(tf.random.normal((1,)))
b = tf.Variable(tf.random.normal((1,)))

opti = tf.keras.optimizers.SGD()

def train_step(x, y):  # cost function
    with tf.GradientTape() as tape:
        hypo = tf.add(tf.multiply(w, x), b)  # wx + b
        loss = tf.reduce_mean(tf.square(tf.subtract(hypo, y))) # (hypo - y) ** 2 / n
    grad = tape.gradient(loss, [w, b])  # 미분처리
    opti.apply_gradients(zip(grad, [w, b]))
    return loss


w_val = []
loss_vals = []
for i in range(100): #학습
    loss_val = train_step(x, y)
    loss_vals.append(loss_val.numpy())
    
    w_val.append(w.numpy())
    #print(loss_val)
print(w_val)
print(loss_vals)

import matplotlib.pyplot as plt
plt.plot(w_val, loss_vals, '--o')
plt.xlabel('w')
plt.ylabel('cost')
plt.show()


# 직접 경사 하강법으로 b를 얻음
y_pred = tf.multiply(x, w) + b
print(y_pred.numpy())

plt.plot(x, y, 'ro')         # 실제값
plt.plot(x, y_pred, 'b-') # 예측값
plt.show()