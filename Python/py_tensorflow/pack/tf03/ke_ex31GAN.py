'''
    GAN : 생성적 적대 신경망 네트워크
      Noise -> Generator -> Fake image -> Descriminator -> 감별
                                  -> Real image
    DCGAN : MNIST
'''
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Input, Dense, Reshape, Flatten, Dropout
from tensorflow.keras.layers import BatchNormalization, Activation, LeakyReLU, UpSampling2D, Conv2D
from tensorflow.keras.models import Sequential, Model
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import os

if not os.path.exists("./gan_images"):
    os.makedirs('./gan_images')
    
np.random.seed(0)
tf.random.set_seed(0)

# fake 이미지 생성모델
generator = Sequential()
generator.add(Dense(128 * 7 * 7, input_dim=100, activation=LeakyReLU(0.2)))

generator.add(BatchNormalization()) # BatchNormalization : data의 배치를 정규화
generator.add(Reshape((7, 7, 128)))
generator.add(UpSampling2D())
generator.add(Conv2D(64, kernel_size=5, padding='same'))

generator.add(BatchNormalization())
generator.add(Activation(LeakyReLU(0.2)))
generator.add(UpSampling2D())
generator.add(Conv2D(1, kernel_size=5, padding='same', activation='tanh'))


# fake 이미지가 진짜 이미지인지 판별하는 모델
discriminator = Sequential()
discriminator.add(Conv2D(64, kernel_size=5, strides=2, padding='same', input_shape=(28, 28, 1)))
discriminator.add(Activation(LeakyReLU(0.2)))
discriminator.add(Dropout(0.3))

discriminator.add(Conv2D(128, kernel_size=5, strides=2, padding='same'))
discriminator.add(Activation(LeakyReLU(0.2)))
discriminator.add(Dropout(0.3))

discriminator.add(Flatten())
discriminator.add(Dense(1, activation='sigmoid'))


discriminator.compile(optimizer='adam', loss='binary_crossentropy')
discriminator.trainable = False # 학습 하지 못하게


# gan model 생성
ginput = Input(shape=(100, ))
dis_output = discriminator(generator(ginput))
gan = Model(ginput, dis_output)
gan.compile(optimizer='adam', loss='binary_crossentropy')
gan.summary()


def gan_train(epoch, batch_size, saving_interval):
    (x_train, _), (_, _) = mnist.load_data()
    x_train = x_train.reshape(x_train.shape[0], 28, 28, 1).astype('float32')
    x_train = (x_train - 127.5) / 127.5
    #print(x_train)
    true = np.ones( (batch_size, 1) )
    fake = np.zeros( (batch_size, 1) )
    
    for i in range(epoch):
        idx = np.random.randint(0, x_train.shape[0], batch_size)
        imgs = x_train[idx] # 실제 이미지 랜덤하게 가져오기
        d_loss_real = discriminator.train_on_batch(imgs, true) #판별 시작
        
        noise = np.random.normal(0, 1, (batch_size, 100))
        gen_imgs = generator.predict(noise) #예측한 값
        d_loss_fake = discriminator.train_on_batch(gen_imgs, fake)
        
        d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)
        g_loss = gan.train_on_batch(noise, true)
        print('epoch : %d,'%i, ' d_loss : %.4f,'%d_loss, ' g_loss:%.4f'%g_loss)
        
        if i % saving_interval == 0:
            noise = np.random.normal(0, 1, (25, 100))
            gen_imgs = generator.predict(noise)
            
            gen_imgs = 0.5 * gen_imgs + 0.5 # 이미지 축소
            
            fig, axs = plt.subplots(5, 5)
            count = 0
            for j in range(5):
                for k in range(5):
                    axs[j, k].imshow(gen_imgs[count, :, :, 0], cmap='gray')
                    axs[j, k].axis('off')
                    count += 1
            fig.savefig('gan_images/gan_mnist%d.png'%i)
            plt.show()
    

gan_train(2000, 32, 200)