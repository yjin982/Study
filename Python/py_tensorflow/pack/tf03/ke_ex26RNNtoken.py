'''
    텍스트의 토큰화를 통해 컴퓨터가 인지할 수 있도록 텍스트를 숫자화
    코퍼스를 토큰화 => 토큰 : 단어별, 문장별, 형태소별로 텍스트를 나눌 때, 가장 작은 단위
'''
from tensorflow.keras.preprocessing.text import Tokenizer

# 문장을 단어수준으로 인덱싱
samples = ['The cat say on the mat.', 'The dog ate my homework.']

# 직접 토큰 분리해서 단어에 인덱스 번호를 달기
token_index = {}
for sam in samples:
    for word in sam.split(): # sep=' ' 를 생략, 공백을 기준으로 나누기 
        if word not in token_index:
            print(word)
            token_index[word] = len(token_index)
print(token_index)
# {'The': 0, 'cat': 1, 'say': 2, 'on': 3, 'the': 4, 'mat.': 5, 'dog': 6, 'ate': 7, 'my': 8, 'homework.': 9}

print()
# Tokenizer로 분리
tokenizer = Tokenizer() # 속성으로 num_words=5 : 빈도가 5 이상인 단어만 작업에 참여
tokenizer.fit_on_texts(samples) # 토큰처리
token_seq = tokenizer.texts_to_sequences(samples)  # 텍스트를 정수 인덱싱한 후 list로 반환
print(token_seq)  # 시작이 1부터, 특수문자는 빠짐. ['The cat say on the mat.' = [1, 2, 3, 4, 1, 5], 'The dog ate my homework.' = [1, 6, 7, 8, 9]]

print()
token_mat = tokenizer.texts_to_matrix(samples, mode='binary') # mode='binary'=> 이진벡터 처리, mode='count' => 갯수, mode='tfidf' 가중치, mode='freq' => 빈도수 
print(token_mat)

word_index = tokenizer.word_index # 각단어에 매겨진 인덱스값 확인 가능
print(word_index)
print('found %s unique tokens'%(len(word_index)))
print(tokenizer.word_counts) # 토큰의 갯수
print(tokenizer.document_count) # 문장의 갯수
print(tokenizer.word_docs)  # 'the': 2 the 는 두 개의 문장에서 나온다는 의미, 단어 출현에 대한 문장수

from tensorflow.keras.utils import to_categorical
token_onehot = to_categorical(token_seq[0], num_classes=6)
print(token_onehot) # 원핫처리


print()
text = "우리 공부하러 갈래 언어는 자바 파이썬 자바 만세"
t = Tokenizer()
t.fit_on_texts([text]) # 입력으로 [text]가 아닌 text를 넣을 경우 한 글자 단위 인코딩이 된다. ex 갈 : 1, 래 : 2
print(t.word_index)    # 각 단어에 대한 인코딩 결과 보기
#{'자바': 1, '우리': 2, '공부하러': 3, '갈래': 4, '언어는': 5, '파이썬': 6, '만세': 7}

print()
docs = ['먼저 텍스트의 각 단어를 나누어 토큰화 한다.', 
            '텍스트의 단어로 토큰화 해야 딥러닝에서 인식된다.',
            '토큰화 한 결과는 딥러닝에서 사용 할 수 있다.'
        ]
token = Tokenizer()
token.fit_on_texts(docs) # 전처리

print('단어 카운트 : {}'.format(token.word_counts))
print('문장 카운트 : {}'.format(token.document_count))
print('각 단어가 몇 개의 문장에 포함되어 있는가 카운트 : {}'.format(token.word_docs))
print('각 단어에 매겨진 인덱스 : {}'.format(token.word_index))

print()
# 텍스트를 읽고 긍정/부정 분류 예측
import numpy as np
docs = ['너무 재밌네요', '최고예요', '참 잘 만든 영화예요', '추천하고 싶은 영화네요', '한번 더 보고 싶네요', 
        '글쎄요', '별로네요', '생각보다 지루합니다', '연기가 좋지 않아요', '재미없어요' 
        ]   # feature

classes = np.array([1,1,1,1,1,0,0,0,0,0])   # label


token = Tokenizer()
token.fit_on_texts(docs)
print(token.word_index) # 단어 인덱스

x = token.texts_to_sequences(docs)
print('토큰을 정수 인덱스한 결과 :%s'%x)

from tensorflow.keras.preprocessing.sequence import pad_sequences
# 토큰 정수 인덱스 결과의 길이를 동일하게 한다.(padding)
padded_x = pad_sequences(x, maxlen=4)
print('패딩 후 : ', padded_x) # 오른쪽어서 부터 차츰 쌓여서 왼쪽으로 밀린다.


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, LSTM, Embedding 
# model을 만들어 보자 
word_size = len(token.word_index) + 1


model = Sequential()
# Embedding : 자연어를 수치화   = > 이후에 RNN에 넣는다.
model.add(Embedding(word_size, 8, input_length=4)) 
#model.add(Flatten())    # 차원을 떨어뜨린다. 
model.add(LSTM(32))
model.add(Dense(1, activation='sigmoid'))

print(model.summary())


model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(padded_x, classes, epochs=20, verbose=1)

print('accuracy : ', model.evaluate(padded_x, classes)[1])
print()
print('pred', model.predict(padded_x))
