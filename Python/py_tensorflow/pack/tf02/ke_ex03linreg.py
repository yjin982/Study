'''
    회귀분석 예비 실습
      loss(cost, 손실)가 최소가 되는 기울기(weight) 구하기
'''
import tensorflow as tf
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]  # feature
y = [1, 2, 3, 4, 5]  # label(class)
# y = [2, 4, 6, 8, 10]  # w=2가 됨

weight_val = []
cost_val = []

for i in range(-30, 50):
    feed_w = i * 0.1 # 기울기값 = i * learning rate
    hypothesis = tf.multiply(feed_w, x) + 0   # y = wx + b
    cost = tf.reduce_mean(tf.square(hypothesis - y))    # 예측값-실제값의 전체 합 / n
    #print(cost.numpy())
    cost_val.append(cost)
    weight_val.append(feed_w)
    print(str(i) + ' |  cost : ' + str(cost) + ',    w : ' + str(feed_w))
    # w가 1인 지점이 cost가 0
    
# 시각화
plt.plot(weight_val, cost_val, 'o')
plt.xlabel('weight')
plt.ylabel('cost')
plt.show()