'''
    CNN(Convolution nn)
      이미지, 텍스트 분류에 효과적. 그 중 이미지에 최적화 되어 있음. 연산량이 많기 때문에 속도가 떨어지는 단점이 있음
      ※convolution : feature extraction 역할
'''
import tensorflow as tf
from tensorflow.keras import datasets, layers, models

''' data load / 처리 준비 / train, test 분류'''
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
print(x_train.shape, y_train.shape, '   ', x_test.shape, y_test.shape) # (60000, 28, 28) (60000,)     (10000, 28, 28) (10000,)

# 흑백인지 컬러인지 구분하기 위해 차원 채널을 추가(3 -> 4차원)해줘야 함. 1-흑, 3-컬 
train_images = x_train.reshape( (60000, 28, 28, 1) )
train_images = train_images / 255  # 정규화
test_images = x_test.reshape( (10000, 28, 28, 1) )
test_images = test_images / 255
# 구글 이외의 제품일 경우 채널의 위치가 다를 수 있다.
# print(train_images[:1])
# print(test_images[:1])

# #숫자로 이미지 확인하기
# import sys
# for i in x_train[3]:
#     for j in i:
#         sys.stdout.write('%s '%j)
#     sys.stdout.write('\n')
#  
# import matplotlib.pyplot as plt
# plt.imshow(x_train[0].reshape(28, 28), cmap='Greys')
# plt.show()

# 모델 : convolution, relu, maxpooling

# feature extraction
model = models.Sequential()
model.add( layers.Convolution2D(filters=128, kernel_size=(3, 3), padding='valid', activation='relu', input_shape=(28, 28, 1)) ) # filters 필터 갯수(=입력수), kernel_size 필터 크기
model.add( layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)) ) # strides : pool이 이동하는 간격. 보통 pool_size와 같이 줌. 혹은 None을 써도 같은 효과
model.add( layers.Dropout(rate=0.2) ) # 과적합 방지
model.add( layers.Convolution2D(filters=64, kernel_size=(3, 3), activation='relu') )
model.add( layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)) ) # pool_size=2 라고 써도 같음
model.add( layers.Dropout(rate=0.2) )
model.add( layers.Convolution2D(filters=32, kernel_size=(3, 3), activation='relu') )
model.add( layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)) )
model.add( layers.Dropout(rate=0.2) )

# fully connected layer : 이미지의 주요 특징만 추출한  CNN 결과를 1차원으로 변경
model.add( layers.Flatten() )  

# 분류기로 분류 작업
model.add( layers.Dense(units=64, activation='relu') )
model.add( layers.Dropout(0.25) )
model.add( layers.Dense(units=32, activation='relu') )
model.add( layers.Dropout(0.25) )
model.add( layers.Dense(units=10, activation='softmax') )

print(model.summary())

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['acc']) # 내부적으로 자체 원핫 인코딩 하라고 지시하는 경우 sparse 추가

early_stop = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=5)
history = model.fit(train_images, y_train, batch_size=128, epochs=1, verbose=2, callbacks=[early_stop], validation_split=0.2)
# Epoch 72/100
# 375/375 - 58s - loss: 0.2953 - acc: 0.8982 - val_loss: 0.2889 - val_acc: 0.8977
 
history = history.history
print(history)
 
# 평가
train_loss, train_acc = model.evaluate(train_images, y_train, batch_size=128, verbose=2)
test_loss, test_acc = model.evaluate(test_images, y_test, batch_size=128, verbose=2)
 
print('train loss : {}, train acc : {}'.format(train_loss, train_acc))
print('test loss : {}, test acc : {}'.format(test_loss, test_acc))
# train loss : 0.20745638012886047, train acc : 0.9276666641235352
# test loss : 0.3042062819004059, test acc : 0.8938000202178955

# 모델 저장 후 읽기
model.save('fmnist_cnn_model.hdf5')
del model

model = tf.keras.models.load_model('fmnist_cnn_model.hdf5')


# 예측
import numpy as np
print('예측값 : {}'.format( np.argmax(model.predict(test_images[:1]))) ) # test_images[:1] == test_images[[0]]
print('실제값 : {}'.format( y_test[:1]) )

print('예측값 : {}'.format( np.argmax(model.predict(test_images[[1]]))) ) 
print('실제값 : {}'.format( y_test[1]) )


# 시각화
import matplotlib.pyplot as plt

def plot_acc(title=None):
    plt.plot(history['acc'])
    plt.plot(history['val_acc'])
    if title is not None:
        plt.title(title)
    plt.xlabel('epochs')
    plt.ylabel('acc')
    plt.legend(['train data', 'validation data'])

def plot_loss(title=None):
    plt.plot(history['loss'])
    plt.plot(history['val_loss'])
    if title is not None:
        plt.title(title)
    plt.xlabel('epochs')
    plt.ylabel('loss')
    plt.legend(['train data', 'validation data'])
        
plot_acc('acc')
plt.show()

plot_loss('loss')
plt.show()