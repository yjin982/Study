'''
    단순선형회귀 모델 : 작성방법 3가지
     - 공부 시간에 따른 성적 점수 예측하기
'''
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
import numpy as np

x_data = np.array([1,2,3,4,5], dtype=np.float32)
y_data = np.array([11,32,53,64,70], dtype=np.float32)
print(np.corrcoef(x_data, y_data)) # 상관관계 0.9743  ※상관관계가 0.3보다 작으면 회귀분석x

# 모델 작성 1 : 완전연결 모델 - Sequential
model = Sequential([
    Dense(units=1, activation='linear', input_dim=1),
    Dense(units=1, activation='linear'),
])

opti = optimizers.SGD(lr=0.001)
model.compile(opti, loss='mse', metrics='mse')  # mse(mean squared error) : 평균제곱오차, 수치가 작을수록 좋다.

model.fit(x=x_data, y=y_data, batch_size=1, epochs=10, verbose=2)
loss_metrics = model.evaluate(x=x_data, y=y_data)
print('loss_metrics :', loss_metrics)

from sklearn.metrics import r2_score
print('설명력(결정계수) :', r2_score(y_data, model.predict(x_data)))

print('실제값 :', y_data)
print('예측값 :', model.predict(x_data).flatten())
print('새로운 값 예측 :', model.predict([6.5, 2.1, 8.5]).flatten())


# 시각화
import matplotlib.pyplot as plt
plt.plot(x_data, model.predict(x_data), 'b', x_data, y_data, 'ko')
plt.show()


# 모델 작성 2 : function api를 사용 방법1에 비해 유연한 모델을 작성
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model

inputs = Input(shape=(1,))
#outputs = Dense(1, activation='linear')(inputs) # 히든 레이어 1개

output1 = Dense(5, activation='linear')(inputs)  
outputs = Dense(1, activation='linear')(output1) # 히든 레이어 2개 

model2 = Model(inputs, outputs)

opti = optimizers.SGD(lr=0.001) # 이하는  방법 1과 동일 
model2.compile(opti, loss='mse', metrics='mse')

model2.fit(x=x_data, y=y_data, batch_size = 1, epochs=100, verbose=1)

loss_metrics = model2.evaluate(x_data, y_data)
print('loss_metrics : ', loss_metrics)

print('실제값2 : ', y_data)
print('예측값2 : ', model2.predict(x_data).flatten())



print() 
# 모델 작성 3 - 1 : sub classing 사용 : Model을 상속 
class MyModel(Model):
    def __init__(self):
        super(MyModel, self).__init__()
        self.d1 = Dense(5, activation='linear')
        self.d2 = Dense(1, activation='linear') # 레이어 2개
    
    def call(self, x): # x : 입력 매개 변수  <== 모델.fit(), 모델.evaluate(), 모델.predict() 
        x = self.d1(x)
        return self.d2(x)
        
model3 = MyModel() # MyModel의 생성자가 호출        

opti = optimizers.SGD(lr=0.001) # 이하는  방법 1과 동일 
model3.compile(opti, loss='mse', metrics='mse')
model3.fit(x=x_data, y=y_data, batch_size = 1, epochs=100, verbose=1)

print('실제값3 : ', y_data)
print('예측값3 : ', model3.predict(x_data).flatten())

                 
print()
# 모델 작성 3 - 2 : sub classing 사용  : Layer을 상속
from tensorflow.keras.layers import Layer

class Linear(Layer):
    def __init__(self, units=1):
        super(Linear, self).__init__()
        self.units = units
        
    def build(self, input_shape): # build가 call를  호출
        self.w = self.add_weight(shape=(input_shape[-1], self.units),
                                 initializer = 'random_normal', 
                                 trainable = True)  # trainable = True : Back propagation   
        self.b = self.add_weight(shape=(self.units,),
                                 initializer = 'zeros', 
                                 trainable = True)
    
    def call(self, inputs):
        return  tf.matmul(inputs, self.w) + self.b
    
class MyMLP(Model):
    def __init__(self):
        super(MyMLP, self).__init__()
        self.linear1 = Linear(1) # 레이어 1개 
        #self.linear1 = Linear(2) # 레이어 2개
        #self.linear2 = Linear(1)
     
    def call(self, inputs): # Linear의  build를 호출
        return self.linear1(inputs) # 레이어 1개
        #x = self.linear_1(inputs)    # 레이어 2개  
        #return self.linear_1(x)
         
model4 = MyMLP()

model4.compile(opti, loss='mse', metrics='mse')
model4.fit(x=x_data, y=y_data, batch_size = 1, epochs=100, verbose=1) #MyMLP의 call호출

print('실제값4 : ', y_data)
print('예측값4 : ', model4.predict(x_data).flatten())



# 모델 작성 3 : sub classing을 사용