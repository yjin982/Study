'''
    다중 선형회귀, 텐서보드(= 모델의 구조 및 학습 진행 결과를 시각화를 해줌)
'''
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
import numpy as np
import matplotlib.pyplot as plt

x_data = np.array( [[70, 85, 80], [71, 89, 88], [50, 45, 70], [99, 90, 90], [50, 15, 10]] )
y_data = np.array( [80, 85, 55, 95, 20] )

model = Sequential()
# model.add(Dense(1, input_dim=3, activation='linear'))  # 레이어 1
model.add(Dense(10, input_dim=3, activation='linear', name='a'))  # 레이어 복수
model.add(Dense(10, activation='linear', name='b'))
model.add(Dense(1, activation='linear', name='c'))
print(model.summary())

from sklearn.metrics import r2_score
print('설명력(결정계수) :', r2_score(y_data, model.predict(x_data)))

opti = optimizers.Adam(lr=0.01)
model.compile(optimizer=opti, loss='mse', metrics=['mse'])

# 텐서보드 : 시행착오를 최소화 할 수 있다.
from tensorflow.keras.callbacks import TensorBoard
tb = TensorBoard(
        log_dir = '.\\mylog',
        histogram_freq = True,
        write_graph = True,
)

history = model.fit(x_data, y_data, batch_size=1, epochs=1000, verbose=0, callbacks=[tb]) # 학습하면서 학습된 내용을 이미지로 보여줌

# 텐서보드 내용 보려면 아나콘다창에서 log파일이 있는 해당 디렉토리로 이동 후에
# tensorboard --logdir mylog
# 그러면 텐서보드를 볼 수 있는 서버가 실행됨.

plt.plot(history.history['loss'])
plt.xlabel('epochs')
plt.ylabel('loss')
plt.show()

print(model.predict(x_data))
x_new = np.array( [[20, 30, 70], [100, 70, 30]] )
print('예상 점수 :', model.predict(x_new))


