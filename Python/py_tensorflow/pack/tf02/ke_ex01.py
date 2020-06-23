import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import SGD, Adam, RMSprop

# 논리회로(OR gate) 모델 작성
# 1. 데이터 수집 및 가공
x = np.array( [[0, 0], [0, 1], [1,0], [1, 1]] )
y = np.array( [0, 1, 1, 1] )

# 2. 모델 생성(설정)
model = Sequential([
    Dense(input_dim=2, units=1),  # 하나의 레이어에 뉴런 하나를 쓴 것. 레이어를 추가하려면 dense를 추가
    Activation('sigmoid'),  # 활성화함수 시그모이드
])
# 또는 이렇게 작성
# model = Sequential()
# model.add(Dense(1, input_dim=2))
# model.add(Activation('sigmoid'))

# 3. 학습 프로세스 생성(컴파일)
model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])

# 4. 모델 학습
model.fit(x, y, batch_size=1, epochs=1000, verbose=1) # epochs 학습 횟수, 

# 5. 모델 평가
loss_metrics = model.evaluate(x, y)
print(loss_metrics)  # loss = 실제값과 예측값의 차이. 작을수록 좋음, 분류 정확도

# 6. 예측값 출력
pred1 = model.predict(x)
print('pred1 :\n', pred1)
pred2 = (model.predict(x) > 0.5).astype('int32')
print('pred2 :\n', pred2)
pred3 = np.argmax(model.predict(x), axis=-1)
print('pred3 :\n', pred3)