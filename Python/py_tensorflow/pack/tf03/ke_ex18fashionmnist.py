'''
    fashion MNIST dataset 손글씨 이미지 분류 예측
'''
import tensorflow as tf

''' data load / 처리 준비 / train, test 분류'''
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
print(x_train.shape, y_train.shape, '   ', x_test.shape, y_test.shape) # (60000, 28, 28) (60000,)     (10000, 28, 28) (10000,)

#숫자로 이미지 확인하기
import sys
for i in x_train[3]:
    for j in i:
        sys.stdout.write('%s '%j)
    sys.stdout.write('\n')
 
import matplotlib.pyplot as plt
plt.imshow(x_train[0].reshape(28, 28), cmap='Greys')
plt.show()
