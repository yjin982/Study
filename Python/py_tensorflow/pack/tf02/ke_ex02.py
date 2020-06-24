'''
    복수 레이어 운영
'''
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import Adam

# 논리회로(XOR gate) 모델 작성
# 1. 데이터 수집 및 가공
x = np.array( [[0, 0], [0, 1], [1,0], [1, 1]] )
y = np.array( [0, 1, 1, 0] )   # 2차원이어도 괜찮 [[0],[1],[1],[0]]

# model = Sequential([
#     Dense(input_dim=2, units=5),  # 하나의 레이어에 뉴런 하나를 쓴 것. 레이어를 추가하려면 dense를 추가
#     Activation('relu'),  # 활성화함수 시그모이드
#     Dense(units=1),  # 하나의 레이어에 뉴런 하나를 쓴 것. 레이어를 추가하려면 dense를 추가
#     Activation('sigmoid'),
# ])

# 또는
model = Sequential()
# model.add(Dense(input_dim=2, units=5))
# model.add(Activation('relu'))
# model.add(Dense(units=1))
# model.add(Activation('sigmoid'))
# 또는 이렇게 쓰기도 가능
model.add(Dense(5, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


model.compile(optimizer=Adam(learning_rate=0.01), loss='binary_crossentropy', metrics=['accuracy'])

# 모델 파라미터 확인
print(model.summary())
# 총 파람수 = ((입력수 + bias편향(=1)) * 유닛수) + (입력수 + bias(=1)) * 유닛수) + ...
# 21 = ( (2 + 1) * 5 ) + ( (5+1) * 1 )


history = model.fit(x, y, batch_size=1, epochs=100, verbose=2) # epochs 학습 횟수, 
 
loss_metrics = model.evaluate(x, y)
print('lose_metrics :', loss_metrics)  # loss = 실제값과 예측값의 차이. 작을수록 좋음, 분류 정확도
 
pred1 = model.predict(x)
print('pred1 :\n', pred1)
pred2 = (model.predict(x) > 0.5).astype('int32')
print('pred2 :\n', pred2)



# 참고
print('\n\n')
print(model.weights)  # dense/kernel, bias값 확인 가능
print('model의 fit을 받아서 모니터링 결과를 볼 수 있음.', history)
print(history.history)  # {'loss': [], 'accuracy':[]} / acc라고 쓰면 history.history['acc']라고 해야 나옴


# 시각화
import matplotlib.pyplot as plt
plt.plot(history.history['loss'])
plt.plot(history.history['accuracy'])
plt.xlabel('epoch')
plt.show()


import pandas as pd
dd = pd.DataFrame(history.history)
dd.plot(figsize=(8, 5))
plt.grid(True)
plt.gca().set_ylim()
plt.show()