'''
    와인의 맛, 등급, 산도 등을 측정해 레드와 화이트 와인 분류 모델
'''
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
import pandas as pd
import  numpy as np
import matplotlib.pyplot as plt
import  tensorflow as tf
import  os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 

# seed 고정
np.random.seed(0)
tf.random.set_seed(0)

wdf = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/wine.csv', header=None)
print(wdf.head(3), wdf.shape)
# print(wdf.isna().sum())

df = wdf.sample(frac=0.5)
print(df.iloc[:, 12].unique()) # [0, 1]
dataset = df.values
x = dataset[:, 0:12]  # feature
y = dataset[:, -1]     # label(class)


# 모델 
model = Sequential()
model.add(Dense(units=30, activation='relu', input_dim=12))
model.add(Dense(units=15, activation='relu'))
model.add(Dense(units=8, activation='relu'))

# model.add(Dense(units=30, activation='elu', input_dim=12))
# model.add(tf.keras.layers.BatchNormalization())  # 배치 정규화 - 그레디언트 소실과 폭주문제 해결
# model.add(Dense(units=15, activation='elu'))     # elu가 비교적 최근 기술
# model.add(tf.keras.layers.BatchNormalization())
# model.add(Dense(units=8, activation='elu'))
# model.add(tf.keras.layers.BatchNormalization())

model.add(Dense(units=1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])

# fit 이전에 훈련되지 않은 모델 정확도
before_loss, before_acc = model.evaluate(x, y)
print('훈련 되지 않은 모델 loss : {:5.2f},   정확도 : {:5.2f}%'.format(before_loss, before_acc*100))

# 모델 저장 폴더
MODEL_DIR = './model/'
if not os.path.exists(MODEL_DIR):
    os.mkdir(MODEL_DIR)
modelpath = 'model/{epoch:02d}-{val_loss:4f}.hdf5'

# 모델을 학습하면서 저장할 수 있음
# 모델 학습 시 모니터링의 결과를 파일로 저장
chkpoint = ModelCheckpoint(filepath=modelpath, monitor='val_loss', verbose=1, save_best_only=True)

# 학습 조기 종료
early_stop = EarlyStopping(monitor='val_loss', patience=5)

# 모델 실행
history = model.fit(x, y, batch_size=128, epochs=1000, verbose=2, validation_split=0.3, callbacks=[early_stop, chkpoint])
after_loss, after_acc = model.evaluate(x, y)
print('훈련 된 모델 loss : {:5.2f},   정확도 : {:5.2f}%'.format(after_loss, after_acc*100))


# 시각화
y_valloss = history.history['val_loss']
y_acc = history.history['acc']

x_len = np.arange(len(y_acc))
plt.plot(x_len, y_valloss, '-o', c='pink', ms=5)                   # 오차
plt.plot(x_len, y_acc, '-v', c='yellowgreen', markersize=5)   # 정확도
plt.show()