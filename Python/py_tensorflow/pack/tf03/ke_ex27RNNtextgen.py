'''
    RNN으로 텍스트 생성
      기존 문서를 반영하여 다음 단어를 예측하고, 텍스트를 생성
'''
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np
from tensorflow.keras.layers import Embedding, Dense, SimpleRNN, LSTM
from tensorflow.keras.models import Sequential


text = '''경마장에 말이 뛰고 있다
    그의 말이 법이다
    가는 말이 고와야 오는 말이 곱다'''
tok = Tokenizer()
tok.fit_on_texts([text])
encoded = tok.texts_to_sequences([text])[0]
print(encoded) # [2, 1, 3, 4, 5, 1, 6, 7, 1, 8, 9, 1, 10] # 텍스트를 시퀀스화
print(tok.word_index) # {'말이': 1, '경마장에': 2, '뛰고': 3, '있다': 4, '그의': 5, '법이다': 6, '가는': 7, '고와야': 8, '오는': 9, '곱다': 10}

vocab_size = len(tok.word_index) + 1
print('단어집합의 크기 : %d'%vocab_size) # 11

# train data
sequences = list()
# [2, 1, 3, 4]
# [5, 1, 6]
# [7, 1, 8, 9, 1, 10]
for line in text.split(sep='\n'): # 라인단위로 먼저 자르고(문장 토큰화)
    encoded = tok.texts_to_sequences([line])[0]
    print(encoded)
    for i in range(1, len(encoded)):
        sequ = encoded[: i+1]
        #print(sequ)
        sequences.append(sequ) # 토큰이 어떤 토큰 다음으로 나올지 학습시키기 위해
print(sequences)
print('샘플 수 : %d'%len(sequences)) # 10


# feature, label 구하기
# '말이' 라는 말이 나오면 그 뒤에 무슨 말이 나올지 예측, 이때 '말이' = feature, 뒤에 나올 말이 label
print( max(len(i) for i in sequences )) # 6 : 샘플 중 가장 길이가 긴 값, 이걸 이용해서 padding

from tensorflow.keras.preprocessing.sequence import pad_sequences
max_len = max(len(i) for i in sequences)
sequences = pad_sequences(sequences, maxlen=max_len, padding='pre')
print(sequences)  # feature와 label이 같이 들어있다고 보면 됨. 마지막 컬럼, [[ 0  0  0  0  2  1] ... 에서 1


# 각 샘플의 마지막 요소값을 레이블로 사용하기 위해 분리
sequences = np.array(sequences)
x = sequences[:, :-1]  # feature
y = sequences[:, -1]   # label or class
# print(x); print(y)

# label : onehot encoding
from tensorflow.keras.utils import to_categorical
y = to_categorical(y, num_classes=vocab_size)
print(y) # [[0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0.] ...


# 모델
model = Sequential()
model.add(Embedding(vocab_size, 32, input_length=(max_len-1)))
model.add(LSTM(32))
model.add(Dense(units=32, activation='relu'))
model.add(Dense(units=vocab_size, activation='softmax'))
model.summary()

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x, y, epochs=150, verbose=1, batch_size=32)
print(model.evaluate(x, y))


# 모델이 정확하게 예측하는지 함수 작성
def sentence_generation(model, t, current_word, n): # n 반복횟수
    init_word = current_word
    sentence = ''
    
    for _ in range(n):
        encoded = t.texts_to_sequences([current_word])[0]  # 현재 단어에 대한 정수 인코딩  
        encoded = pad_sequences([encoded], maxlen=(max_len - 1), padding='pre')
        #result = model.predict_classes(encoded)
        result = np.argmax( model.predict(encoded) )
        #print(result)
        for word, index in t.word_index.items():
            #print('word : ' + str(word) + ', index : ' + str(index))
            if index == result: # 만약 예측한 단어의 인덱스와 동일한 단어가 있으면
                break
        current_word = current_word + ' ' + word # 현재단어 + 예측단어
        sentence = sentence + ' ' + word
        
    sentence = init_word + sentence
    return sentence

print('경마 : ', sentence_generation(model, tok, '경마', 1))
print('경마장에 : ', sentence_generation(model, tok, '경마장에', 1))
print('경마장에 : ', sentence_generation(model, tok, '경마장에', 5))
print('그의 : ', sentence_generation(model, tok, '그의', 2))
print('가는 : ', sentence_generation(model, tok, '가는', 3))