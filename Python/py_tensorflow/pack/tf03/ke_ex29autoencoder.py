'''
    Autoencoder(비지도학습의 일종)
      입력 데이터의 특징을 효율적으로 담아낸 새로운 이미지 생성
      부족한 이미지 학습 데이터를 만들 수 있다.
      인코더와 디코더 영역으로 분리된다.
'''
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, UpSampling2D
import numpy as np
import matplotlib.pyplot as plt

(x_train, _), (x_test, _) = mnist.load_data()
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1).astype('float32') / 255
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1).astype('float32') / 255
#print(x_train[:2])

# model


''' encoder : 고차원 입력 데이터를 저차원 벡터로 압축 '''
model = Sequential()
model.add(Conv2D(filters=16, kernel_size=3, padding='same', input_shape=(28, 28, 1), activation='relu'))
model.add(MaxPooling2D(pool_size=2, padding='same'))
model.add(Conv2D(filters=8, kernel_size=3, padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=2, padding='same'))
model.add(Conv2D(filters=8, kernel_size=3, padding='same', strides=2, activation='relu'))
# model.add(MaxPooling2D(pool_size=2, padding='same'))  #


''' decoder : 주어진 저차원 벡터의 압축을 해제 '''
model.add(Conv2D(filters=8, kernel_size=3, padding='same', activation='relu'))
model.add(UpSampling2D()) # 차원 확장, size=2주거나
model.add(Conv2D(filters=8, kernel_size=3, padding='same', activation='relu'))
model.add(UpSampling2D())
model.add(Conv2D(filters=16, kernel_size=3, activation='relu'))
model.add(UpSampling2D())
model.add(Conv2D(filters=1, kernel_size=3, padding='same', activation='sigmoid'))
model.summary()

model.compile(optimizer='adam', loss='binary_crossentropy')
model.fit(x_train, x_train, batch_size=128, epochs=10, verbose=2, validation_data=(x_test, x_test))

# 원본데이터로 부터 test할 랜덤 데이터 생성
random_test = np.random.randint(x_test.shape[0], size=5)

autoencoder_imgs = model.predict(x_test)

for i, image_idx in enumerate(random_test):
    # 실제값
    ax = plt.subplot(2, 7, i+1) #2행7열
    plt.imshow(x_test[image_idx].reshape(28, 28))
    ax.axis('off') #축은 안보이게
    
    #
    ax = plt.subplot(2, 7, 7+i+1) #2행7열
    plt.imshow(autoencoder_imgs[image_idx].reshape(28, 28))
    ax.axis('off')
    
plt.show()
    