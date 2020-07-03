'''
    RNN : 순환 신경망
      RNN의 경우는 은닉층의 결과가 다시 같은 은닉층의 입력으로 들어가도록 연결되어 있다. 이런 특성이 RNN이 순서 또는 시간이라는 측면을 고려할 수 있는 특징을 가져다주게 된다.
      NLP(자연어 처리) - 음성이나 텍스트를 인식하고 분석 처리하기에 효과적인 네트워크 혹은 모델이다.
      텍스트 분류, 품사태깅, 이미지 캡션, 기계 번역, 챗봇, 새로운 글(작곡) 작성 ...  
'''
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, LSTM, GRU, Dense

model = Sequential()
# model.add(SimpleRNN(units=3, input_shape=(2, 10))) # 2행 10열 자료로 출력 3개 수행
# model.add(SimpleRNN(units=3, input_length=2, input_dim=10))
model.add(LSTM(units=3, input_length=2, input_dim=10)) # LSTM에서도 똑같이 쓸 수 있음
''' 기존 RNN의 문제점이 입력된 데이터와 참고해야 할 데이터의 위치 차이가 커질 때 문맥을 연결하기 힘들어진다는 것이었습니다. 그렇다면 이 상호작용 구조가 이런 부분을 해결하는데 도움을 준다는 것을 예측해 볼 수 있습니다.'''
model.summary()

print()
model = Sequential()
# model.add(SimpleRNN(units=3, batch_input_shape=(8, 2, 10)))  # 
model.add(LSTM(units=3, batch_input_shape=(8, 2, 10)))
model.summary()


print()
model = Sequential()
model.add(LSTM(units=3, batch_input_shape=(8, 2, 10), return_sequences=True)) # return_sequences=True  false면 결과가 마지막 시퀀스에서만 나옴.
model.add(Dense(units=2, activation='softmax'))
model.summary() # Output Shape  (8, 2, 3)  == (배치사이즈, 시퀀스수, 출력수) == 시퀀스 2개짜리 묶음을 8개 만들어서 16개의 시퀀스를 만듦. 하나의 시퀀스 출력은 3개

