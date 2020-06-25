'''
    선형회귀
'''
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import Adam
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/Advertising.csv')
del data['no']
print(data.head(2), '   ', data.shape)
print(data.corr(), '\n')  # 상관관계

# 정규화 : 0 ~ 1 사이로 데이터 스케일링
from sklearn.preprocessing import MinMaxScaler, minmax_scale, StandardScaler
scaler = MinMaxScaler(feature_range=(0, 1), copy=True)  # 이게 기본값
xy = scaler.fit_transform(data)  # scaler.inverse_transform(xy)
print(xy[:2])

xy = minmax_scale(data, axis=0, copy=True)
print(xy[:2], '\n') # 이 함수는 따로 fit 안 해줘도 됨

# 데이터 분리
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(xy[:, 0:-1], xy[:, -1], test_size=0.3, random_state=123)  # x: tv~newspaper, y:sales
print(x_train[:2], '  ', x_train.shape)
print(y_train[:2], '  ', y_train.shape, '\n')

# 모델 생성
model = Sequential()
model.add(Dense(units=20, input_dim=3))
model.add(Activation('linear'))
model.add(Dense(units=10))
model.add(Activation('linear'))
model.add(Dense(units=1))
model.add(Activation('linear'))

# model.summary()  # 모델 구성 정보 
# tf.keras.utils.plot_model(model, to_file='model.png', show_shapes=True, show_layer_names=True) # 이미지로도 가능, GraphBiz가 설치되어있어야 가능


model.compile(optimizer=Adam(learning_rate=0.001), loss='mse', metrics=['mse'])  # 정량적일때 mse, 정성적일때 엔트로피
history = model.fit(x_train, y_train, batch_size=32, epochs=100, verbose=2, validation_split=0.2)  # validation_data = k-fold를 위해 내가 직접 데이터를 나눴을때, validation_split = 자동으로 f-fold 나눠줌, 비율 8:2로 20%를 검정으로
# loss: 0.0050 - mse: 0.0050 트레인에 대한 값   |  val_loss: 0.0042 - val_mse: 0.0042   검증(validation)에 대한 값
print('train :', history.history['loss'])  # train에 대한 loss


# 평가
loss = model.evaluate(x_test, y_test, batch_size=32)
print('test :', loss)  # 평가(test)에 대한 loss

# 예측
pred = model.predict(x_test)
print('real :', y_test[:5])
print('pred :', pred[:5].flatten())

# 설명력
from sklearn.metrics import r2_score
print('r2_score :', r2_score(y_test, model.predict(x_test)))