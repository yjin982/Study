# 자소 단위 생성
# https://github.com/wikibook/tf2/blob/master/Chapter7.ipynb
# jamotools(한글 자소단위로 분리 및 결합 라이브러리) 설치    pip install jamotools

# 자모 분리 테스트
import jamotools
import tensorflow as tf
import numpy as np 

path_to_file = tf.keras.utils.get_file('toji.txt', 'https://raw.githubusercontent.com/pykwon/etc/master/rnn_test_toji.txt')
#path_to_file = 'silrok.txt'
train_text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
s = train_text[:100]
print(s)

# 한글 텍스트를 자모 단위로 분리. 한자 등에는 영향 X
s_split = jamotools.split_syllables(s) # 100글자의 한글이 자모 단위로 분리됨
print(s_split)

# 자모 결합 테스트
s2 = jamotools.join_jamos(s_split)
print(s2)        # 결합된 결과
print(s == s2)   # True 분리 전후의 문장이 비교 결과 같음

# 자모 토큰화 : 텍스트를 자모 단위로 나눕니다. 지연 시간 필요.
train_text_X = jamotools.split_syllables(train_text)
vocab = sorted(set(train_text_X))
vocab.append('UNK')   # 사전에 정의되지 않은 기호가 있을 수 있으므로 'UNK'도 사전에 넣음
print ('{} unique characters'.format(len(vocab)))  # 179 unique characters

# vocab list를 숫자로 맵핑하고, 반대도 실행.
char2idx = {u:i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)

text_as_int = np.array([char2idx[c] for c in train_text_X])

# word2idx의 일부를 알아보기 쉽게 print.
print('{')
for char,_ in zip(char2idx, range(10)):
    print('  {:4s}: {:3d},'.format(repr(char), char2idx[char]))
print('  ...\n}')
    # {
    #   '\n':   0,
    #   '\r':   1,
    #   ' ' :   2,
    #   '!' :   3,
    #   '"' :   4,
    #   "'" :   5,
    #   '(' :   6,
    #   ')' :   7,
    #   ',' :   8,
    #   '-' :   9,
    #   ...
    # }

# 텍스트 안에 존재하지 않는 토큰을 나타내는 'UNK' 사용
print('index of UNK: {}'.format(char2idx['UNK']))   # 178

# 토큰 데이터 확인
print(train_text_X[:20]) # ㅈㅔ 1 ㅍㅕㄴ ㅇㅓㄷㅜㅁㅇㅢ ㅂㅏㄹ
print(text_as_int[:20])  # [69 81  2 13  2 74 82 49  2 68 80 52 89 62 68 95  2 63 76 54]

# 학습 데이터세트 생성
seq_length = 80
examples_per_epoch = len(text_as_int) // seq_length
char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)

char_dataset = char_dataset.batch(seq_length+1, drop_remainder=True)
for item in char_dataset.take(1):
    print(idx2char[item.numpy()])
    print(item.numpy())
    # ['ㅈ' 'ㅔ' ' ' '1' ' ' 'ㅍ' 'ㅕ' 'ㄴ' ' ' 'ㅇ' 'ㅓ' 'ㄷ' 'ㅜ' 'ㅁ' 'ㅇ' 'ㅢ' ' ' 'ㅂ'
    #  'ㅏ' 'ㄹ' 'ㅅ' 'ㅗ' 'ㄹ' 'ㅣ' '\r' '\n' '1' '8' '9' '7' 'ㄴ' 'ㅕ' 'ㄴ' 'ㅇ' 'ㅢ' ' '
    #  'ㅎ' 'ㅏ' 'ㄴ' 'ㄱ' 'ㅏ' 'ㅇ' 'ㅟ' '.' '\r' '\n' 'ㄲ' 'ㅏ' 'ㅊ' 'ㅣ' 'ㄷ' 'ㅡ' 'ㄹ' 'ㅇ'
    #  'ㅣ' ' ' 'ㅇ' 'ㅜ' 'ㄹ' 'ㅌ' 'ㅏ' 'ㄹ' 'ㅣ' ' ' 'ㅇ' 'ㅏ' 'ㄴ' ' ' 'ㄱ' 'ㅏ' 'ㅁ' 'ㄴ'
    #  'ㅏ' 'ㅁ' 'ㅜ' 'ㅇ' 'ㅔ' ' ' 'ㅇ' 'ㅘ' 'ㅅ']
    # [69 81  2 13  2 74 82 49  2 68 80 52 89 62 68 95  2 63 76 54 66 84 54 96
    #   1  0 13 20 21 19 49 82 49 68 95  2 75 76 49 46 76 68 92 10  1  0 47 76
    #  71 96 52 94 54 68 96  2 68 89 54 73 76 54 96  2 68 76 49  2 46 76 62 49
    #  76 62 89 68 81  2 68 85 66]    
    
def split_input_target2(chunk):
    return [chunk[:-1], chunk[-1]]

train_dataset = char_dataset.map(split_input_target2)
for x,y in train_dataset.take(1):
    print(idx2char[x.numpy()])
    print(x.numpy())
    print(idx2char[y.numpy()])
    print(y.numpy())
    # ['ㅈ' 'ㅔ' ' ' '1' ' ' 'ㅍ' 'ㅕ' 'ㄴ' ' ' 'ㅇ' 'ㅓ' 'ㄷ' 'ㅜ' 'ㅁ' 'ㅇ' 'ㅢ' ' ' 'ㅂ'
    #  'ㅏ' 'ㄹ' 'ㅅ' 'ㅗ' 'ㄹ' 'ㅣ' '\r' '\n' '1' '8' '9' '7' 'ㄴ' 'ㅕ' 'ㄴ' 'ㅇ' 'ㅢ' ' '
    #  'ㅎ' 'ㅏ' 'ㄴ' 'ㄱ' 'ㅏ' 'ㅇ' 'ㅟ' '.' '\r' '\n' 'ㄲ' 'ㅏ' 'ㅊ' 'ㅣ' 'ㄷ' 'ㅡ' 'ㄹ' 'ㅇ'
    #  'ㅣ' ' ' 'ㅇ' 'ㅜ' 'ㄹ' 'ㅌ' 'ㅏ' 'ㄹ' 'ㅣ' ' ' 'ㅇ' 'ㅏ' 'ㄴ' ' ' 'ㄱ' 'ㅏ' 'ㅁ' 'ㄴ'
    #  'ㅏ' 'ㅁ' 'ㅜ' 'ㅇ' 'ㅔ' ' ' 'ㅇ' 'ㅘ']
    # [69 81  2 13  2 74 82 49  2 68 80 52 89 62 68 95  2 63 76 54 66 84 54 96
    #   1  0 13 20 21 19 49 82 49 68 95  2 75 76 49 46 76 68 92 10  1  0 47 76
    #  71 96 52 94 54 68 96  2 68 89 54 73 76 54 96  2 68 76 49  2 46 76 62 49
    #  76 62 89 68 81  2 68 85]
    # ㅅ
    # 66    

BATCH_SIZE = 64
steps_per_epoch = examples_per_epoch // BATCH_SIZE
BUFFER_SIZE = 5000

train_dataset = train_dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)

# 자소 단위 생성 모델 정의
total_chars = len(vocab)
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(total_chars, 100, input_length=seq_length),
    tf.keras.layers.LSTM(units=400),
    tf.keras.layers.Dense(total_chars, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()

# 자소 단위 생성 모델 학습
from tensorflow.keras.preprocessing.sequence import pad_sequences

def testmodel2(epoch, logs):
    if epoch % 5 != 0 and epoch != 99:
        return
    
    test_sentence = train_text[:48]
    test_sentence = jamotools.split_syllables(test_sentence)

    next_chars = 300
    for _ in range(next_chars):
        test_text_X = test_sentence[-seq_length:]
        test_text_X = np.array([char2idx[c] if c in char2idx else char2idx['UNK'] for c in test_text_X])
        test_text_X = pad_sequences([test_text_X], maxlen=seq_length, padding='pre', value=char2idx['UNK'])
        output_idx = model.predict_classes(test_text_X)
        test_sentence += idx2char[output_idx[0]]
    
    print()
    print(jamotools.join_jamos(test_sentence))
    print()

testmodelcb = tf.keras.callbacks.LambdaCallback(on_epoch_end=testmodel2)

history = model.fit(train_dataset.repeat(), epochs=50, 
                    steps_per_epoch=steps_per_epoch, 
                    callbacks=[testmodelcb], verbose=2)
    # 제 1 편 어둠의 발소리
    # 1897년의 한가위.
    # 까치들이 울타리 안 감나무에 와서 안 간 간 간 간 간 간 간 간 간 간 간 간 간 간...
    # 262/262 - 15s - loss: 2.9280 - accuracy: 0.2009
    # ...
    # 262/262 - 9s - loss: 2.1082 - accuracy: 0.3526
    # Epoch 6/50
    # ...
    # 262/262 - 15s - loss: 0.0925 - accuracy: 0.9962
    # Epoch 42/50
    # ...
    # 262/262 - 9s - loss: 0.0677 - accuracy: 0.9962
    # Epoch 46/50
    # 제 1 편 어둠의 발소리
    # 1897년의 한가위.
    # 까치들이 울타리 안 감나무에 와서 안 분 지소 있는 것이들 생이는 싸월이지에 공선 어서  서엄을 바꼬 술을 집는  깅숭이의 
    # 양이는 것을 누는 내부이 있었다.
    # 팀서방도 모르는 없는 내이를 했고 마랑하는 것이다. 거서가  성할 것 같은 참만을 앞고 모음으로 동새 읽었다.
    # 한다. 키 그래, 이서
    # ...

model.save('rnnmodel2.hdf5')

# 임의의 문장을 사용한 생성 결과 확인
test_sentence = '최참판댁 사랑은 무인지경처럼 적막하다'
#test_sentence = '동헌에 나가 공무를 본 후 활 십오 순을 쏘았다'

test_sentence = jamotools.split_syllables(test_sentence)

next_chars = 500
for _ in range(next_chars):
    test_text_X = test_sentence[-seq_length:]
    test_text_X = np.array([char2idx[c] if c in char2idx else char2idx['UNK'] for c in test_text_X])
    test_text_X = pad_sequences([test_text_X], maxlen=seq_length, padding='pre', value=char2idx['UNK'])
    
    output_idx = model.predict_classes(test_text_X)
    test_sentence += idx2char[output_idx[0]]
    
print(jamotools.join_jamos(test_sentence))
    # Epoch 50/50
    # 262/262 - 9s - loss: 0.0875 - accuracy: 0.9860
    # 최참판댁 사랑은 무인지경처럼 적막하다 마두가 있는 놈을 차자가는 솔같은 따룸대 때 나며가아고 마자가는 소리를 한 것  아니라. 
    # 다람 싶언이라 소린 짓방이의 
    # 때잔승이의 그 언게 앞았으며  물을 알같에....  
    # 예, 놈부는 야부란 지소 운네, 울에 집에 있는 놈의 그러하지 아니요.
    # 더어만 것  그 여 음은 사람으로 집에 있는 성상에 가니와 
    # 안 선다. 삿박을 앞고 모음은 성동을  무어서 그렇다. 이 그래 몸모르겄은 딸라가 아니요. 한다. 한존 없는 내인이를 

# LambdaCallback
# keras에서 여러가지 상황에서 콜백이되는 class들이 만들어져 있는데, LambdaCallback 등의 Callback class들은 
# 기본적으로 keras.callbacks.Callback class를 상속받아서 특정 상황마다 콜백되는 메소드들을 재정의하여 사용합니다. 
# LambdaCallback는 lambda 평션을 작성하여 생성자에 넘기는 방식으로 사용 할 수 있습니다. 
# callback 시 받는 arg는 Callbakc class에 정의 되어 있는대로 맞춰 주어야 합니다. 
# on_epoch_end메소드로 정의하여 epoch이 끝날 때 마다 확인해보도록 하겠습니다.
# 아래 처럼 lambda 함수를 작성하여 LambdaCallback를 만들어 주고, 이때 epoch, logs는 신경 안쓰시고 arg 형태만 맞춰주면 됩니다.
# from keras.callbacks import LambdaCallback
# print_weights = LambdaCallback(on_epoch_end=lambda epoch, logs: print(model.layers[3].get_weights()))
