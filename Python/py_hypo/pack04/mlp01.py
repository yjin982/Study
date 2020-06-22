'''
    Multi Layer Perceptron
      단층 Perceptron은 XOR 분류를 하지 못함. 하지만 층(Layer)를 늘리면 가능. 이를 MLP라고 함 
'''
import numpy as np
from sklearn.linear_model import Perceptron

feature = np.array([[0,0], [0, 1], [1, 0], [1,1]])
label = np.array([0, 1, 1, 0])

ml = Perceptron(max_iter=1000).fit(feature, label)
print(ml.predict(feature))


print()
# 다층 신경망 사용
from sklearn.neural_network import MLPClassifier

# ml2 = MLPClassifier(hidden_layer_sizes=50, verbose=2).fit(feature, label) #verbose 진행과정 프린트(Iteration 반복횟수, loss = 실제값과 예측값 차이),
ml2 = MLPClassifier(hidden_layer_sizes=(10, 10, 10), learning_rate_init=0.01, max_iter=100, random_state=1, verbose=1).fit(feature, label)  # hidden_layer_sizes=(10, 10, 10) 노드가 10개인 히든레이어를 3개를 준 것
print(ml2.predict(feature))