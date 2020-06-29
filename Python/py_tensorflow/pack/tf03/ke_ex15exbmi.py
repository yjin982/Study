'''
    bmi 데이터로 분류
'''
import numpy as np
import pandas as pd

datas = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/bmi.csv')
datas = datas.replace({'label':{'fat':0, 'normal':1, 'thin':2}})
print(datas.head(2), datas.shape) # (20000, 3)
print()

# === 정규화 === # 미작업시 분류 정확도가 낮아짐
datas['height'] /= 200
datas['weight'] /= 100
print(datas.head(3), '\n')
# ========== #

# feature, label
x_data = datas.iloc[:, :2]
y_data = datas.iloc[:, [-1]]
x_data = x_data.to_numpy()

# one-hot
from tensorflow.keras.utils import to_categorical
y_onehot = to_categorical(y_data)

print('x :\n', x_data[:2])
print('y :\n', y_onehot[:2])

# == train / test == #
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_data, y_onehot, test_size=0.3, random_state=0)
# ============ #

# 모델생성
from tensorflow.keras import models
from tensorflow.keras import layers

model = models.Sequential()
model.add(layers.Dense(units=64, activation='relu', input_shape=(2,)))
model.add(layers.Dropout(0.2)) # 지정된 비율만큼(=20%)의 데이터를 학습에서 제외함.
# Dropout : overfitting 방지 목적
# 신경망 모델이 복잡해질 때 가중치 감소만으로는 어려운데 드롭아웃 기법은 뉴런의 연결을 임의로 삭제하는 것이다. 훈련할 때 임의의 뉴런을 골라 삭제하여 신호를 전달하지 않게 한다. 테스트할 때는 모든 뉴런을 사용한다.
# ======= #
model.add(layers.Dense(units=32, activation='relu'))
model.add(layers.Dropout(0.2))

model.add(layers.Dense(units=3, activation='softmax'))
model.summary()

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])

# early stopping  #
from tensorflow.keras.callbacks import EarlyStopping
es = EarlyStopping(monitor='val_loss', patience=5, verbose=1, mode='min', baseline=0.05)  # 0.05(baseline)보다 작은 값(mode)이 연속적으로 5회(patience) 이상 나오면 학습 조기종료
# ========== #


hist = model.fit(x_train, y_train, batch_size=64, epochs=1000, verbose=2, validation_split=0.2, callbacks=[es])
# sparse_categorical_crossentropy - onehot 인코딩 아닐 때


print('\n평가 [loss, acc] : {}\n'.format(model.evaluate(x_test, y_test)))

# 예측
pred = model.predict(x_test)
print('pred :', pred[0])
print('y test :', y_test[0])
print('pred sum :', np.sum(pred[0]))
print('pred argmax :', np.argmax(pred[0]))

print()
print('pred :', pred[10])
print('y test :', y_test[10])
print('pred sum :', np.sum(pred[10]))
print('pred argmax :', np.argmax(pred[10]))
print()


# new data
print('new 예측값1 :', np.argmax(model.predict(np.array([[187/200, 55/100]])), axis=1))
print('new 예측값2 :', np.argmax(model.predict(np.array([[155/200, 65/100]])), axis=1))