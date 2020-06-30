'''
    MNIST dataset 손글씨 이미지 분류 예측
'''
import tensorflow as tf

''' data load / 처리 준비 / train, test 분류'''
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
# print(x_train.shape, y_train.shape, '   ', x_test.shape, y_test.shape) # (60000, 28, 28) (60000,)     (10000, 28, 28) (10000,)

# 숫자로 이미지 확인하기
# import sys
# for i in x_train[3]:
#     for j in i:
#         sys.stdout.write('%s '%j)
#     sys.stdout.write('\n')
# 
# import matplotlib.pyplot as plt
# plt.imshow(x_train[0].reshape(28, 28), cmap='Greys')
# plt.show()

x_train = x_train.reshape(60000, 784).astype('float32')
x_test = x_test.reshape(10000, 784).astype('float32')

# 정규화
x_train /= 255
x_test /= 255
# print(x_train[0])

# onehot 처리
# print(set(y_train))  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}  = 10개의 label
y_train = tf.keras.utils.to_categorical(y_train, 10) # label을 onehot 인코딩
y_test =  tf.keras.utils.to_categorical(y_test, 10)
# print(y_train[0])  # 5 -> [0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]

# train data의 일부를 validation data로 사용
x_val = x_train[50000:60000]  # validation data
y_val = y_train[50000:60000]
x_train = x_train[0:50000]
y_train = y_train[0:50000]
# print(x_val.shape, x_train.shape) # (10000, 784) (50000, 784)



# ''' 모델 작성'''
# model = tf.keras.Sequential()
# model.add(tf.keras.layers.Dense(units=1024, input_shape=(784,) ))
# model.add(tf.keras.layers.Activation('relu'))
# model.add(tf.keras.layers.Dropout(0.2))
# 
# model.add(tf.keras.layers.Dense(units=512))
# model.add(tf.keras.layers.Activation('relu'))
# model.add(tf.keras.layers.Dropout(0.2))
# 
# model.add(tf.keras.layers.Dense(units=10))
# model.add(tf.keras.layers.Activation('softmax'))
# print(model.summary())
# 
# model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
# 
# ''' 모델 학습 '''
# history = model.fit(x_train, y_train, batch_size=128, epochs=1000, verbose=2, callbacks=[tf.keras.callbacks.EarlyStopping(patience=3)], validation_data=(x_val, y_val))
# print(history.history)
# 
# import matplotlib.pyplot as plt
# plt.plot(history.history['loss'], label='loss')
# plt.plot(history.history['val_loss'], 'r--', label='val loss')
# plt.xlabel('epochs')
# plt.ylabel('loss')
# plt.legend()
# plt.show()
# 
# ''' 모델 평가 '''
# score = model.evaluate(x_test, y_test, batch_size=128, verbose=1)
# print('evaluate loss : {:.3f}, evaluate acc : {}'.format(score[0], score[1]))
# 
# # 모델 저장하고 지우고 불러와서 하기
# model.save('mnist_model.hdf5')
# del model
model = tf.keras.models.load_model('mnist_model.hdf5')


''' 예측 '''
import numpy as np
print(x_test[:1], x_test[:1].shape)  # (1, 784)
pred = model.predict(x_test[:1])

print('pred : {}'.format(pred))
print('pred : {}'.format( np.argmax(pred, 1) ))
print('실제값 : {}'.format( np.argmax(y_test[:1], 1) ))

import matplotlib.pyplot as plt
plt.imshow(x_test[:1].reshape(28, 28), cmap='Greys')
plt.show()



''' 내가 그린 손글씨 읽기 '''
from PIL import Image
im = Image.open('num.png')
img = np.array(im.resize((28, 28), Image.ANTIALIAS).convert('L'))
# print(img)

# 정규화
data = img.reshape([1, 784])
data = data / 255
print(data)

plt.imshow(data.reshape(28, 28), cmap='Greys')
plt.show()

new_pred = model.predict(data)
print('pred : {}'.format(new_pred))
print('pred : {}'.format( np.argmax(new_pred, 1) ))