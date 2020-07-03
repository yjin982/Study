# CIFAR-10은 총 10개의 레이블로 이루어진 6만장의 칼라 이미지를 가지며 5만장은 트레이닝, 1만장은 테스트 용
# 10가지 클래스를 담고 있다.
# airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck

# CNN 레이어 추가
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Input, Flatten, Dense, Conv2D, \
                    Activation, Dropout, BatchNormalization, LeakyReLU
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import cifar10

NUM_CLASSES = 10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

y_train = to_categorical(y_train, NUM_CLASSES)
y_test = to_categorical(y_test, NUM_CLASSES)

# architecture -- CNN + Dense 
input_layer = Input(shape=(32,32,3))

conv_layer_1 = Conv2D(filters = 10, kernel_size = (4,4), \
                    strides = 2, padding = 'same')(input_layer)
conv_layer_2 = Conv2D(filters = 20, kernel_size = (3,3), \
                    strides = 2, padding = 'same')(conv_layer_1)

flatten_layer = Flatten()(conv_layer_2)

output_layer = Dense(units=10, activation = 'softmax')(flatten_layer)
model = Model(input_layer, output_layer)
print(model.summary())

print('CNN + Dense 레이어를 추가한 후')
x = Conv2D(filters = 32, kernel_size = 3, strides = 1, padding = 'same')(input_layer)
x = BatchNormalization()(x)
x = LeakyReLU()(x)

x = Conv2D(filters = 32, kernel_size = 3, strides = 2, padding = 'same')(x)
x = BatchNormalization()(x)
x = LeakyReLU()(x)

x = Conv2D(filters = 64, kernel_size = 3, strides = 1, padding = 'same')(x)
x = BatchNormalization()(x)
x = LeakyReLU()(x)

x = Conv2D(filters = 64, kernel_size = 3, strides = 2, padding = 'same')(x)
x = BatchNormalization()(x)
x = LeakyReLU()(x)

x = Flatten()(x)

x = Dense(128)(x)
x = BatchNormalization()(x)
x = LeakyReLU()(x)
x = Dropout(rate = 0.5)(x)

x = Dense(NUM_CLASSES)(x)
output_layer = Activation('softmax')(x)
model = Model(input_layer, output_layer)
print(model.summary())

# train
opt = Adam(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=128, epochs=10, shuffle=True, verbose=2)
print('test acc : %.4f'%(model.evaluate(x_test, y_test, verbose=0, batch_size=128)[1]))
print('test loss : %.4f'%(model.evaluate(x_test, y_test, verbose=0, batch_size=128)[0]))

# Epoch 10/10
# 391/391 - 84s - loss: 0.6747 - accuracy: 0.7627
# test acc : 0.5802
# test loss : 1.3904

print()
print('model.layers[6].get_weights():', model.layers[6].get_weights())

print()
CLASSES = np.array(['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck'])

pred = model.predict(x_test[:10])
pred_single = CLASSES[np.argmax(pred, axis = -1)]
actual_single = CLASSES[np.argmax(y_test[:10], axis = -1)]
print('예측값 : ', pred_single)
print('실제값 : ', actual_single)
    # 예측값 :  ['cat' 'ship' 'ship' 'ship' 'deer' 'frog' 'cat' 'frog' 'bird' 'automobile']
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