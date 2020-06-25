'''
    당뇨병 관련 자료로 이항분류
'''
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
import pandas as pd
import  numpy as np
import matplotlib.pyplot as plt
import  tensorflow as tf
import  os


np.random.seed(0)

dataset = np.loadtxt('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/diabetes.csv', delimiter=',')
print(type(dataset), '  ', dataset.shape) # (759, 9)

# train / test 분리
x_train = dataset[:700, 0:8]
x_test = dataset[700:, 0:8]
y_train = dataset[:700, 8]
y_test = dataset[700:, 8]
print(np.unique(y_train)) # [0. 1.]

# train / test 분리 2
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(dataset[:, :8], dataset[:, -1], test_size=0.3, random_state=1)

# 모델 구성1
model = Sequential()
model.add(Dense(64, input_dim=8, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
history = model.fit(x_train, y_train, batch_size=32, epochs=100, verbose=2)
scores = model.evaluate(x_test, y_test)
print('%s : %.2f%%'%(model.metrics_names[1], scores[1] * 100))
print(x_test[:1])

new_x = [[0.05, 0.84, 0.39, -0.69, 0., -0.10, -0.03, -0.10]]
pred = model.predict(new_x)
# print('예측결과 :', pred)
print('예측결과 :', np.where(pred.flatten() > 0.5, 1, 0))

plt.plot(history.history['loss'])
plt.xlabel('epochs')
plt.show()


# 모델 구성2 - 유연성이 더 좋음
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model

inputs = Input(shape=(8, ))
output1 = Dense(64, activation='relu')(inputs)
output2 = Dense(32, activation='relu')(output1)
output3 = Dense(16, activation='relu')(output2)
output4 = Dense(1, activation='sigmoid')(output3)
model = Model(inputs, output4)

# 이 아래는 같음
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
history = model.fit(x_train, y_train, batch_size=32, epochs=100, verbose=2)
scores = model.evaluate(x_test, y_test)
print('%s : %.2f%%'%(model.metrics_names[1], scores[1] * 100))
print(x_test[:1])

new_x = [[0.05, 0.84, 0.39, -0.69, 0., -0.10, -0.03, -0.10]]
pred = model.predict(new_x)
# print('예측결과 :', pred)
print('예측결과 :', np.where(pred.flatten() > 0.5, 1, 0))

plt.plot(history.history['loss'])
plt.xlabel('epochs')
plt.show()
