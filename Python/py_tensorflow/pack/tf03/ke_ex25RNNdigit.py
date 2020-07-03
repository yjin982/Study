'''
    RNN 이해를 위해 4개의 숫자를 입력하고 그 다음 숫자 예측
'''
from tensorflow.keras import models
from tensorflow.keras import layers
import tensorflow as tf
import numpy as np

x, y = [], [] # sequence data 기억장소
for i in range(6):
    lst = list(range(i, i+4))
    x.append( list(map(lambda c:[c / 10], lst)) )
    y.append( (i + 4) / 10)
    
x = np.array(x)
y = np.array(y)

print(x.shape)  # (6, 4, 1)
print(y)

for i in range(len(x)):
    print(x[i], y[i])
print()



# 모델 만들기 RNN
model = models.Sequential([
        layers.SimpleRNN(units=10, activation='tanh', input_shape=(4, 1)),
        # 더 들어갈 수도 있음. 지금은 연습이라 그냥
        layers.Dense(units=1)
])
    
model.compile(optimizer='adam', loss='mse')
model.summary()

model.fit(x, y, epochs=100, verbose=0)
print('예측값 : ', model.predict(x).flatten())
print('실제값 : ', y.flatten())
print('새로운 예측 :', model.predict( np.array([[[0.6], [0.7], [0.8], [0.9]]]) ))
print('새로운 예측 :', model.predict( np.array([[[-0.2], [-0.1], [0.0], [0.1]]]) ))


print()
# LSTM으로 만들기
model = models.Sequential([
        layers.LSTM(units=10, activation='tanh', input_shape=(4, 1)),
        # 더 들어갈 수도 있음. 지금은 연습이라 그냥
        layers.Dense(units=1)
])    
model.compile(optimizer='adam', loss='mse')


model.fit(x, y, epochs=100, verbose=0)
print('예측값 : ', model.predict(x).flatten())
print('실제값 : ', y.flatten())
print('새로운 예측 :', model.predict( np.array([[[0.6], [0.7], [0.8], [0.9]]]) ))
print('새로운 예측 :', model.predict( np.array([[[-0.2], [-0.1], [0.0], [0.1]]]) ))


print()
# LSTM 단순화 시킨
model = models.Sequential([
        layers.GRU(units=10, activation='tanh', input_shape=(4, 1)),
        # 더 들어갈 수도 있음. 지금은 연습이라 그냥
        layers.Dense(units=1)
])
    
model.compile(optimizer='adam', loss='mse')

model.fit(x, y, epochs=100, verbose=0)
print('예측값 : ', model.predict(x).flatten())
print('실제값 : ', y.flatten())
print('새로운 예측 :', model.predict( np.array([[[0.6], [0.7], [0.8], [0.9]]]) ))
print('새로운 예측 :', model.predict( np.array([[[-0.2], [-0.1], [0.0], [0.1]]]) ))