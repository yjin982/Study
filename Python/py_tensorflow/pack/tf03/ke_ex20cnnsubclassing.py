import tensorflow as tf
from tensorflow.keras import datasets, layers, models

''' data load / 처리 준비 / train, test 분류'''
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
print(x_train.shape, y_train.shape, '   ', x_test.shape, y_test.shape) # (60000, 28, 28) (60000,)     (10000, 28, 28) (10000,)

x_train = x_train.reshape( (60000, 28, 28, 1) )
x_train = x_train / 255.0  # 정규화
x_test = x_test.reshape( (10000, 28, 28, 1) )
x_test = x_test / 255.0

# 데이터 섞기
import numpy as np
np.random.seed(0)
x = np.random.sample( (5, 2) )
print(x)
# dataset = tf.data.Dataset.from_tensor_slices(x)
# print(dataset) # <TensorSliceDataset shapes: (2,), types: tf.float64>

dataset = tf.data.Dataset.from_tensor_slices(x).shuffle(buffer_size=10000, seed=0).batch(5) # batch(2)=2개씩 묶어서 나눔, 같은 사이즈를 주면 순서만 바꾼 상태 
# print(dataset)
for i in dataset:
    print(i)
    

# train data를 shuffle
train_dataset = tf.data.Dataset.from_tensor_slices( (x_train, y_train) ).shuffle(60000).batch(28)
test_dataset = tf.data.Dataset.from_tensor_slices( (x_test, y_test) ).batch(28) # test는 셔플필요 x
print(train_dataset, ' ', test_dataset, '\n\n')


# subclassing api로 모델 생성
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout
from tensorflow.keras import Model, datasets

class MyModel(Model):
    def __init__(self): # 모델 구성
        super(MyModel, self).__init__()
        self.conv1 = Conv2D(filters=32, kernel_size=(3, 3), padding='valid', activation='relu')
        self.pool1 = MaxPooling2D(pool_size=(2, 2))
        self.conv2 = Conv2D(filters=32, kernel_size=[3, 3], padding='valid', activation='relu')
        self.pool2 = MaxPooling2D(pool_size=(2, 2))
        self.flatten = Flatten(dtype='float64') # 안써도 됨
        
        self.dense1 = Dense(units=64, activation='relu')
        self.drop1 = Dropout(rate=0.3)
        self.dense2 = Dense(units=10, activation='softmax')
    
    def call(self, inputs): # init에서 선언한 레이어를 불러와 network을 구성
        net = self.conv1(inputs)
        net = self.pool1(net)
        net = self.conv2(net)
        net = self.pool2(net)
        net = self.flatten(net)
        
        net = self.dense1(net)
        net = self.drop1(net)
        net = self.dense2(net)
        
        return net
    
model = MyModel()
temp_input = tf.keras.Input( shape=(28, 28, 1) )
model(temp_input)

model.summary()

loss_obj = tf.keras.losses.SparseCategoricalCrossentropy()
optimizer = tf.keras.optimizers.Adam()

''' 일반적인 모델 학습 방법 '''
# model.compile(optimizer=optimizer, loss=loss_obj, metrics=['acc'])
# model.fit(x_train, y_train, batch_size=128, epochs=3, verbose=1, max_queue_size=10, workers=4, use_multiprocessing=True)
# score = model.evaluate(x_test, y_test)
# print('test loss : {:.3f}, test acc : {:.3f}'.format(score[0], score[1]))
# 
# # 예측
# print('예측값 : {}'.format( np.argmax(model.predict(x_test[:1], 1)) ))
''' =========== '''


'''  GradientTape을 사용한 모델 학습 방법
      model.compile, model.fit을 대신해 아래와 같이 기술(쪼끔 어렵) '''
      
train_loss = tf.keras.metrics.Mean()  # 가중치의 평균 계산
train_accuracy = tf.keras.metrics.SparseCategoricalAccuracy() # 분류 정확도 계산
test_loss = tf.keras.metrics.Mean()
test_accuracy = tf.keras.metrics.SparseCategoricalAccuracy()

@tf.function  # 그래프 안에서 돌려서 속도 향상을 도모
def train_step(images, labels): # cost가 최소가 되는 함수 
    with tf.GradientTape() as tape:
        predictions = model(images)
        loss = loss_obj(labels, predictions) # 예측값과 실제값의 차이를 구함
    
    gradients = tape.gradient(loss, model.trainable_variables) # loss를 최소화 하기 위한 미분값을 계산
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    
    train_loss(loss)
    train_accuracy(labels, predictions) # (실제값, 예측값)

@tf.function
def test_step(images, labels): # test니까 평가만 
    predictions = model(images)
    loss = loss_obj(labels, predictions)
    
    test_loss(loss)
    test_accuracy(labels, predictions) # (실제값, 예측값)


''' ==================== '''

EPOCHS = 3
for epoch in range(EPOCHS):
    for x_train, y_train in train_dataset:
        train_step(x_train, y_train)
    
    for x_test, y_test in test_dataset:
        test_step(x_test, y_test)
    
    akb = 'epochs : {},   train loss : {:.3f}, train acc : {:.3f},    test loss : {:.3f}, test acc : {:.3f}'
    print( akb.format(epoch+1, train_loss.result(), train_accuracy.result(), test_loss.result(), test_accuracy.result()) )
    
print('예측값 : {}'.format( np.argmax(model.predict(x_test[:1], 1)) ))
print('실제값 : {}'.format( y_test[:1].numpy() ))