# CIFAR-10은 총 10개의 레이블로 이루어진 6만장의 칼라 이미지를 가지며 5만장은 트레이닝, 1만장은 테스트 용
# 10가지 클래스를 담고 있다.
# airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Input, Flatten, Dense, Conv2D
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import cifar10

NUM_CLASSES = 10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

print ("Training data:")
print ("Number of examples: ", x_train.shape[0])
print ("Number of channels:",x_train.shape[3]) 
print ("Image size:", x_train.shape[1], x_train.shape[2])
print ("Test data:")
print ("Number of examples:", x_test.shape[0])
print ("Number of channels:", x_test.shape[3])
print ("Image size:", x_test.shape[1], x_test.shape[2]) 
print(x_train.shape, x_train.dtype)
    # Training data:
    # Number of examples:  50000
    # Number of channels: 3
    # Image size: 32 32
    # Test data:
    # Number of examples: 10000
    # Number of channels: 3
    # Image size: 32 32
    # (50000, 32, 32, 3) uint8

# print(x_train[0])  #[[[ 59  62  63] [ 43  46  45] ...
# print(y_train[0])  #[6]

plt.figure(figsize=(12,4))
plt.subplot(131)   # 1행 3열 중 1열 
plt.imshow(x_train[0], interpolation="bicubic")
plt.subplot(132)
plt.imshow(x_train[1], interpolation="bicubic")
plt.subplot(133)
plt.imshow(x_train[2], interpolation="bicubic")
plt.show()

x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

y_train = to_categorical(y_train, NUM_CLASSES)
y_test = to_categorical(y_test, NUM_CLASSES)
print(x_train[54, 12, 13, 1])  # 0.36862, 인덱스 54의 이미지에서 (12, 13) 위치에 해당하는 픽셀의 초록 채널 값을 의미

# architecture -- Sequential model 이용(CNN X)
# model = Sequential([
#     Dense(200, activation='relu', input_shape = (32, 32, 3)),
#     Flatten(),
#     Dense(150, activation='relu'),
#     Dense(NUM_CLASSES, activation='softmax'),
# ])
# print(model.summary())

# architecture -- function API 이용
input_layer = Input((32,32,3))
x = Flatten()(input_layer)
x = Dense(200, activation = 'relu')(x)
x = Dense(150, activation = 'relu')(x)
output_layer = Dense(NUM_CLASSES, activation = 'softmax')(x)
model = Model(input_layer, output_layer)
print(model.summary())

# train
opt = Adam(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=128, epochs=10, shuffle=True, verbose=2)
print('test acc : %.4f'%(model.evaluate(x_test, y_test, verbose=0, batch_size=128)[1]))
print('test loss : %.4f'%(model.evaluate(x_test, y_test, verbose=0, batch_size=128)[0]))

print()
CLASSES = np.array(['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck'])

pred = model.predict(x_test[:10])
pred_single = CLASSES[np.argmax(pred, axis = -1)]
actual_single = CLASSES[np.argmax(y_test[:10], axis = -1)]
print('예측값 : ', pred_single)
print('실제값 : ', actual_single)
    # 예측값 :  ['dog' 'truck' 'ship' 'airplane' 'frog' 'frog' 'frog' 'frog' 'dog' 'ship']
    # 실제값 :  ['cat' 'ship' 'ship' 'airplane' 'frog' 'frog' 'automobile' 'frog' 'cat' 'automobile']
print('분류 실패 수 : ', (pred_single != actual_single).sum())

# 시각화
fig = plt.figure(figsize=(15, 3))
fig.subplots_adjust(hspace=0.4, wspace=0.4)

for i, idx in enumerate(range(len(x_test[:10]))):
    img = x_test[idx]
    ax = fig.add_subplot(1, len(x_test[:10]), i + 1)
    ax.axis('off')
    ax.text(0.5, -0.35, 'pred = ' + str(pred_single[idx]), \
            fontsize=10, ha='center', transform=ax.transAxes) 
    ax.text(0.5, -0.7, 'act = ' + str(actual_single[idx]), \
            fontsize=10, ha='center', transform=ax.transAxes)
    ax.imshow(img)
plt.show()