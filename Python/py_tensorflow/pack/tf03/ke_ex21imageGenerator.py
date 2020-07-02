'''
    이미지 보강
      
'''
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import  tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import os

np.random.seed(0)
tf.random.set_seed(0)

# train/test, 정규화
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(-1, 28, 28, 1).astype('float32') / 255
x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255
# print(x_train.shape, y_train.shape, x_test.shape)
# print(x_train[0])

# y 원핫인코딩
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# # 이미지 보강 예)
# #   기존 이미지를 좌우대칭, 약간의 회전, 기울기, 확대축소, 평행이동 등의 작업을 수행하여 다양한 이미지로 모델 학습
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# img_generate = ImageDataGenerator(rotation_range=10, width_shift_range=0.1, height_shift_range=0.1, shear_range=0.5, zoom_range=0.1, horizontal_flip=True, vertical_flip=True)
# augument_size = 100
# x_augment = img_generate.flow( 
#         np.tile(x_train[0].reshape(28, 28), 100).reshape(-1, 28, 28, 1), 
#         np.zeros(augument_size),
#         batch_size=augument_size,
#         shuffle=False).next()[0]
#         
# plt.figure( figsize=(10, 10) )
# for c in range(100):
#     plt.subplot(10, 10, c+1)
#     plt.axis('off')
#     plt.imshow(x_augment[c].reshape(28, 28), cmap='gray')
# plt.show()

from tensorflow.keras.preprocessing.image import ImageDataGenerator
img_generate = ImageDataGenerator(rotation_range=10, width_shift_range=0.1, height_shift_range=0.1, shear_range=0.5, zoom_range=0.1, horizontal_flip=True, vertical_flip=False)
augment_size = 30000
randidx = np.random.randint(x_train.shape[0], size=augment_size)
x_augment = x_train[randidx].copy()
y_augment = y_train[randidx].copy()

x_augment = img_generate.flow(x_augment, np.zeros(augment_size), batch_size=augment_size, shuffle=False).next()[0]
# 원래 x_train에 image augument된 x_augment를 추가
x_train = np.concatenate( (x_train, x_augment) )
y_train = np.concatenate( (y_train, y_augment) )

# train data늘리기  60000 -> 60000 + augment_size
print(x_train.shape, '  ', y_train.shape)

model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(filters=32, kernel_size=(3, 3), input_shape=(28, 28, 1), padding='same', activation='relu'),
        tf.keras.layers.MaxPool2D(pool_size=(2, 2)),
        tf.keras.layers.Dropout(rate=0.3),
        tf.keras.layers.Conv2D(filters=64, kernel_size=(3, 3), padding='same', activation='relu'),
        tf.keras.layers.MaxPool2D(pool_size=(2, 2)),
        tf.keras.layers.Dropout(rate=0.3),
        tf.keras.layers.Flatten(),
        
        tf.keras.layers.Dense(units=128, activation='relu'),
        tf.keras.layers.Dropout(rate=0.25),
        tf.keras.layers.Dense(units=64, activation='relu'),
        tf.keras.layers.Dropout(rate=0.25),
        tf.keras.layers.Dense(units=10, activation='softmax'),
    ])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
model.summary()


# 모델 최적화 설정
MODEL_DIR = './mymnist/'

if not os.path.exists(MODEL_DIR): # 폴더 없으면 생성
    os.mkdir(MODEL_DIR)

# 모델 저장
modelpath = MODEL_DIR + '{epoch:02d}-{val_loss:.4f}.hdf5'
chkpoint = ModelCheckpoint(filepath=modelpath, monitor='val_loss', verbose=1, save_best_only=True)
earlystop = EarlyStopping(monitor='val_loss', patience=3)


# train
history = model.fit(x_train, y_train, batch_size=128, epochs=100, verbose=0, callbacks=[earlystop, chkpoint], validation_split=0.2)
print('train acc : %.4f'%(model.evaluate(x_train, y_train)[1]))
print('train loss : %.4f'%(model.evaluate(x_train, y_train)[0]))
print('test acc : %.4f'%(model.evaluate(x_test, y_test)[1]))
print('test loss : %.4f'%(model.evaluate(x_test, y_test)[0]))

# 시각화
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot( history.history['acc'], marker='o', c='red', label='Test acc')
plt.plot( history.history['val_acc'], marker='+', c='blue', label='val acc')
plt.xlabel('epochs')
plt.ylim((0.5, 1))
plt.legend(loc='lower right')

plt.subplot(1, 2, 2)
plt.plot( history.history['loss'], marker='o', c='red', label='Test loss')
plt.plot( history.history['val_loss'], marker='+', c='blue', label='val loss')
plt.xlabel('epochs')
plt.ylim((0.5, 1))
plt.legend(loc='upper right')
plt.show()
