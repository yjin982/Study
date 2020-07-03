# 자연어 생성 : 단어 단위 생성
# 토지 또는 조선왕조실록 데이터 파일 다운로드
# https://github.com/wikibook/tf2/blob/master/Chapter7.ipynb
import tensorflow as tf
import numpy as np 

path_to_file = tf.keras.utils.get_file('toji.txt', 'https://raw.githubusercontent.com/pykwon/etc/master/rnn_test_toji.txt')
#path_to_file = 'silrok.txt'
# 데이터 로드 및 확인. encoding 형식으로 utf-8 을 지정해야합니다.
train_text = open(path_to_file, 'rb').read().decode(encoding='utf-8')

# 텍스트가 총 몇 자인지 확인합니다.
print('Length of text: {} characters'.format(len(train_text)))
print()

# 처음 100 자를 확인해봅니다.
print(train_text[:100])

# 훈련 데이터 입력 정제
import re
# From https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
def clean_str(string):    
    string = re.sub(r"[^가-힣A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", "", string)
    string = re.sub(r"\)", "", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    string = re.sub(r"\'{2,}", "\'", string)
    string = re.sub(r"\'", "", string)
    return string

train_text = train_text.split('\n')
train_text = [clean_str(sentence) for sentence in train_text]
train_text_X = []
for sentence in train_text:
    train_text_X.extend(sentence.split(' '))
    train_text_X.append('\n')
    
train_text_X = [word for word in train_text_X if word != '']

print(train_text_X[:20])  

# 단어 토큰화
# 단어의 set을 만듭니다.
vocab = sorted(set(train_text_X))
vocab.append('UNK')   # 텍스트 안에 존재하지 않는 토큰을 나타내는 'UNK' 사용
print ('{} unique words'.format(len(vocab)))

# vocab list를 숫자로 맵핑하고, 반대도 실행합니다.
word2idx = {u:i for i, u in enumerate(vocab)}
idx2word = np.array(vocab)

text_as_int = np.array([word2idx[c] for c in train_text_X])

# word2idx 의 일부를 알아보기 쉽게 print 해봅니다.
print('{')
for word,_ in zip(word2idx, range(10)):
    print('  {:4s}: {:3d},'.format(repr(word), word2idx[word]))
print('  ...\n}')

print('index of UNK: {}'.format(word2idx['UNK']))

# 토큰 데이터 확인. 20개만 확인
print(train_text_X[:20])  
print(text_as_int[:20])

# 기본 데이터셋 만들기
seq_length = 25  # 25개의 단어가 주어질 경우 다음 단어를 예측하도록 데이터를 만듦
examples_per_epoch = len(text_as_int) // seq_length
sentence_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)

# seq_length + 1 은 처음 25개 단어와 그 뒤에 나오는 정답이 될  1 단어를 합쳐 함께 반환하기 위함
# drop_remainder=True 남는 부분은 제거 속성
sentence_dataset = sentence_dataset.batch(seq_length + 1, drop_remainder=True)

for item in sentence_dataset.take(1):
    print(idx2word[item.numpy()])
    print(item.numpy())

# 학습 데이터셋 만들기
# 26개의 단어가 각각 입력과 정답으로 묶어서 ([25단어], 1단어) 형태의 데이터를 반환하기 위한 작업
def split_input_target(chunk):
    return [chunk[:-1], chunk[-1]]

train_dataset = sentence_dataset.map(split_input_target)
for x,y in train_dataset.take(1):
    print(idx2word[x.numpy()])
    print(x.numpy())
    print(idx2word[y.numpy()])
    print(y.numpy())

# 데이터셋 shuffle, batch 설정
BATCH_SIZE = 64
steps_per_epoch = examples_per_epoch // BATCH_SIZE
BUFFER_SIZE = 5000

train_dataset = train_dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)

# 단어 단위 생성 모델 정의
total_words = len(vocab)
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(total_words, 100, input_length=seq_length),
    tf.keras.layers.LSTM(units=100, return_sequences=True),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.LSTM(units=100),
    tf.keras.layers.Dense(total_words, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()

# 단어 단위 생성 모델 학습
from tensorflow.keras.preprocessing.sequence import pad_sequences

def testmodel(epoch, logs):
    if epoch % 5 != 0 and epoch != 49:
        return
    test_sentence = train_text[0]

    next_words = 100
    for _ in range(next_words):
        test_text_X = test_sentence.split(' ')[-seq_length:]
        test_text_X = np.array([word2idx[c] if c in word2idx else word2idx['UNK'] for c in test_text_X])
        test_text_X = pad_sequences([test_text_X], maxlen=seq_length, padding='pre', value=word2idx['UNK'])

        output_idx = model.predict_classes(test_text_X)
        test_sentence += ' ' + idx2word[output_idx[0]]
    
    print()
    print(test_sentence)
    print()

# 모델을 학습시키며 모델이 생성한 결과물을 확인하기 위해 LambdaCallback 함수 생성
testmodelcb = tf.keras.callbacks.LambdaCallback(on_epoch_end=testmodel)

history = model.fit(train_dataset.repeat(), epochs=50, 
                steps_per_epoch=steps_per_epoch, 
                callbacks=[testmodelcb], verbose=2)

model.save('rnnmodel.hdf5')
del model
from tensorflow.keras.models import load_model
model=load_model('rnnmodel.hdf5')

# 임의의 문장을 사용한 생성 결과 확인
test_sentence = '최참판댁 사랑은 무인지경처럼 적막하다'
#test_sentence = '동헌에 나가 공무를 본 후 활 십오 순을 쏘았다'

next_words = 500
for _ in range(next_words):
    # 임의 문장 입력 후 뒤에서 부터 seq_length 만킁ㅁ의 단어(25개) 선택
    test_text_X = test_sentence.split(' ')[-seq_length:]  
    
    # 문장의 단어를 인덱스 토큰으로 바꿈. 사전에 등록되지 않은 경우에는 'UNK' 코큰값으로 변경
    test_text_X = np.array([word2idx[c] if c in word2idx else word2idx['UNK'] for c in test_text_X])
    # 문장의 앞쪽에 빈자리가 있을 경우 25개 단어가 채워지도록 패딩
    test_text_X = pad_sequences([test_text_X], maxlen=seq_length, padding='pre', value=word2idx['UNK'])
    
    # 출력 중에서 가장 값이 큰 인덱스 반환
    output_idx = model.predict_classes(test_text_X) 
    test_sentence += ' ' + idx2word[output_idx[0]] # 출력단어는 test_sentence에 누적해 다음 스테의 입력으로 활용

print(test_sentence)


# LambdaCallback
# keras에서 여러가지 상황에서 콜백이되는 class들이 만들어져 있는데, LambdaCallback 등의 Callback class들은 
# 기본적으로 keras.callbacks.Callback class를 상속받아서 특정 상황마다 콜백되는 메소드들을 재정의하여 사용합니다. 
# LambdaCallback는 lambda 평션을 작성하여 생성자에 넘기는 방식으로 사용 할 수 있습니다. 
# callback 시 받는 arg는 Callbakc class에 정의 되어 있는대로 맞춰 주어야 합니다. 
# on_epoch_end메소드로 정의하여 epoch이 끝날 때 마다 확인해보도록 하겠습니다.
# 아래 처럼 lambda 함수를 작성하여 LambdaCallback를 만들어 주고, 이때 epoch, logs는 신경 안쓰시고 arg 형태만 맞춰주면 됩니다.
# from keras.callbacks import LambdaCallback
# print_weights = LambdaCallback(on_epoch_end=lambda epoch, logs: print(model.layers[3].get_weights()))