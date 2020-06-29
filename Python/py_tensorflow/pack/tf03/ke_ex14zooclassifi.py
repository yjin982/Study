'''
    softmax로 다항분류 - 동물 type 분류
'''
import numpy as np

xy = np.loadtxt('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/zoo.csv', delimiter=',')
print('xy :', xy[:1], type(xy), xy.shape) # (101, 17)

# feature, label 분류
x_data = xy[:, 0:-1]  # feature
y_data = xy[:, [-1]]  # label
print('x  :', x_data[:1])
print('y  :', y_data[:5].flatten(), set(y_data.ravel()))  # set 으로 유일한 값(분류할 값) 찾기

# one hot 처리
from tensorflow.keras.utils import to_categorical
nb_classes = 7
# y_one_hot = to_categorical(y_data, num_classes=nb_classes)
# print('one hot y :', y_one_hot[:1]) 
# print()
print(x_data.shape, y_data.shape)
# 모델 생성
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
model = Sequential()
model.add(Dense(units=32, activation='relu', input_shape=(16, )))  # units이 input보다 큰거는 상관 없지만 작으면 병목현상이 생길 수 있으므로 주의
model.add(Dense(units=32, activation='relu'))
model.add(Dense(units=nb_classes, activation='softmax'))
model.summary()
# model.compile(optimizer='adam', loss='categorical_crossentropy', metrics='acc')
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='acc')

# history = model.fit(x_data, y_one_hot, batch_size=10, epochs=100, verbose=2, validation_split=0.2)
history = model.fit(x_data, y_data, batch_size=10, epochs=100, verbose=2, validation_split=0.2)

# print('평가 [loss, acc] : {}'.format(model.evaluate(x_data, y_one_hot)))
print('평가 [loss, acc] : {}'.format(model.evaluate(x_data, y_data)))

# 시각화
import matplotlib.pyplot as plt
history_dict = history.history
plt.plot(history_dict['loss'], 'skyblue', label='train_loss')
plt.plot(history_dict['val_loss'], 'yellowgreen', label='val_loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend()
plt.show()

plt.plot(history_dict['acc'], 'pink', label='train_acc')
plt.plot(history_dict['val_acc'], 'orange', label='val_acc')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend()
plt.show()

print()
pred_datas = x_data[:5]
preds = [np.argmax(i) for i in (model.predict(pred_datas))]
print('예측값들 :', preds)
print('실제값들 :', y_data[:5].flatten())


# 새로운 값으로 예측
# print(x_data[4:6, :])
new_data = np.array([[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 12, 1, 0, 0]])
print(new_data.flatten())
print('new_data 예측값 :', [np.argmax(i) for i in (model.predict(new_data))])