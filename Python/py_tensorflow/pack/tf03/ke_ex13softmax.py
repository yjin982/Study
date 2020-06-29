'''
    다항분류 : softmax 활성화 함수 사용
'''
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(0)
xdata = np.random.random((1000, 12))  # feature 12개
ydata = np.random.randint(10, size=(1000, 1))
ydata = to_categorical(ydata, num_classes=10) # 정수값을 one hot encoding  # one-hot(원핫)인코딩이란? 단 하나의 값만 True이고 나머지는 모두 False인 인코딩. 즉, 1개만 Hot(True)이고 나머지는 Cold(False)
print(xdata[:2], xdata.shape)
print(ydata[:2], ydata.shape)


model = Sequential()
model.add(Dense(units=100, activation='relu', input_shape=(12, )))
model.add(Dense(units=50, activation='relu'))
model.add(Dense(units=10, activation='softmax'))
# print(model.summary())
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])  # label이 3개 이상이니까 catecorical_crossentropy


hist = model.fit(xdata, ydata, batch_size=32, epochs=500, verbose=2)
model_eval = model.evaluate(xdata, ydata)
print('model_eval     loss : {:.3f}, acc : {:.3f}'.format(model_eval[0], model_eval[1]))

print('예측값 : {}'.format([np.argmax(i) for i in model.predict(xdata[:5])]))
print('실제값 : {}\n'.format([np.argmax(i) for i in ydata[:5]]))


# 시각화
plt.plot(hist.history['loss'])
plt.plot(hist.history['acc'])
plt.show()


# 새로운 값으로 예측
x_new = xdata = np.random.random((1, 12))
pred = model.predict(x_new)
print('pred : {}'.format(pred))
print('pred argmax: {}'.format(np.argmax(pred))) # 제일 큰 값의 인덱스
print('pred 합 : {}'.format(np.sum(pred)))  # 확률값의 합이라서 1이어야함