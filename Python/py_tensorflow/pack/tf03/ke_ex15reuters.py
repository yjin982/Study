'''  텍스트 다중 분류 - 로이터 뉴스 토픽 분류
    46가지 토픽으로 라벨이 달린 11,228개의 로이터 뉴스로 이루어진 데이터셋. IMDB 데이터셋과 마찬가지로, 각 뉴스는 (같은 방식을 사용한) 단어 인덱스의 시퀀스로 인코딩되어 있습니다.
'''
from tensorflow.keras.datasets import reuters
(train_feat, train_label), (test_feat, test_label) = reuters.load_data(num_words=10000) # 자주 등장하는 단어 10000개 사용
print(train_feat[:3])
print(train_label[:3])
print(train_feat.shape, train_label.shape, test_feat.shape) # (8982,) (8982,) (2246,)
print()

# 리스트로 된 로이터 데이터의 실제 값 보기 #
word_index = reuters.get_word_index()
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])
decode_re = ' '.join([reverse_word_index.get(i - 3, '?') for i in train_feat[0]])
print(decode_re, '\n\n')
# =================== #

# feature : list => vector
import numpy as np
def vector_seq(sequence, dim = 10000):
    results = np.zeros((len(sequence), dim))  # 0행렬 생성
    for i, seq in enumerate(sequence):
        results[i, seq] = 1.
    return results
x_train = vector_seq(train_feat)  # train_feat를 벡터화
x_test = vector_seq(test_feat)   # test_feat를 벡터화
print(x_train, x_train.shape)
print(x_test, x_test.shape)


# # self one hot encoding
# def to_onehot(labels, dim = 46):
#     res = np.zeros((len(labels), dim))
#     for i, label in enumerate(labels):
#         res[i, label] = 1
#     return res
# one_hot_train_label = to_onehot(train_label)  # label을 onehot 처리
# one_hot_test_label = to_onehot(test_label)    
# print(one_hot_test_label[0])
# 
# keras가 제공하는 one hot encoder
from tensorflow.keras.utils import to_categorical
one_hot_train_label = to_categorical(train_label)
one_hot_test_label = to_categorical(test_label)
# print(one_hot_test_label[0])


# 모델 작성
from tensorflow.keras import models
from tensorflow.keras import layers

model = models.Sequential()
model.add(layers.Dense(units=64, activation='relu', input_shape=(10000, )))
model.add(layers.Dense(units=64, activation='relu'))
model.add(layers.Dense(units=46, activation='softmax'))
model.summary()
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics='acc')


# 모델 훈련 시 검증데이터(validation data)를 사용
x_val = x_train[:1000]
partial_x_train = x_train[1000:]

y_val = one_hot_train_label[:1000]
partial_y_train = one_hot_train_label[1000:]


# 학습
history = model.fit(partial_x_train, partial_y_train, batch_size=128, epochs=20, validation_data=(x_val, y_val))

# loss
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(loss)+1)
print(loss)

# 시각화
import matplotlib.pyplot as plt
plt.plot(epochs, loss, 'bo', label='train loss')
plt.plot(epochs, val_loss, 'r--', label='train val loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend()
plt.show()
print(loss)

# acc
acc = history.history['acc']
val_acc = history.history['val_acc']
epochs = range(1, len(acc)+1)
print(acc)

# 시각화
plt.plot(epochs, acc, 'bo', label='train acc')
plt.plot(epochs, val_acc, 'r--', label='train val acc')
plt.xlabel('epochs')
plt.ylabel('acc')
plt.legend()
plt.show()


print()
# 모델 평가
m_eval = model.evaluate(x_test, one_hot_test_label)
print('model evaluate :', m_eval)

# 예측
pred = model.predict(x_test)
print('pred :', pred[0])
print('pred sum :', np.sum(pred[0]))
print('pred argmax :', np.argmax(pred[0]))