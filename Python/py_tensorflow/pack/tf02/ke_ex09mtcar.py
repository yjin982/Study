'''
    Keras로 자동차 연비 예측
'''
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)

dataset = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/auto-mpg.csv')
del dataset['car name'] 
print(dataset.head(2), '   ', dataset.shape)  # (398, 8)

##### 데이터 전처리
dataset['horsepower'] = dataset['horsepower'].apply(pd.to_numeric, errors='coerce') # errors='coerce' 강제 형 변환
# print(dataset.info())  # horsepower 자료 타입이 object, ?값이 포함되어 있어서 강제 변환 후에 데이터가 NaN으로 
# print(dataset.isna().sum())  # NaN확인
dataset = dataset.dropna()
print(dataset.shape)  # (392, 8)

# 시각화
sns.pairplot(dataset[['mpg', 'weight', 'horsepower']], diag_kind='kde')
plt.show()

# train / test
train_dataset = dataset.sample(frac=0.8, random_state=0)
test_dataset = dataset.drop(train_dataset.index)
print(train_dataset[:2], '   ', train_dataset.shape)  # (274, 8)
print(test_dataset[:2], '   ', test_dataset.shape)    # (118, 8)

train_stat = train_dataset.describe()
train_stat.pop('mpg') # 안빼도 괜춘
train_stat = train_stat.transpose()
print(train_stat)


# label : 'mpg'
train_labels = train_dataset.pop('mpg')
print('train_labels :', train_labels[:2].values)
test_labels = test_dataset.pop('mpg')
print('test_labels :', test_labels[:2].values)

# 표준화 : 수학공식으로 하기
def std_func(x):  # 표준화 처리 함수    
    return (x - train_stat['mean']) / train_stat['std']
# print(st_func(train_dataset[:3]))

std_train_data = std_func(train_dataset)
std_test_data = std_func(test_dataset)

print('\n\n\n')
# 모델 작성 후 예측
def building_model():
    network = tf.keras.Sequential([
        tf.keras.layers.Dense(units=64, input_shape=[7], activation=tf.nn.relu),
        tf.keras.layers.Dense(units=64, activation='relu'),
        tf.keras.layers.Dense(units=1, activation='linear')
    ])
    
    #opti = tf.keras.optimizers.RMSprop(0.001)
    opti = tf.keras.optimizers.Adam(0.001)
    network.compile(optimizer=opti, loss='mean_squared_error', metrics=['mean_squared_error', 'mean_absolute_error']) # mse원래는 mean_squared_error, mae는 mean_absolute_error
    
    return network


model = building_model()
print(model.summary())

# fit() 전에 모델을 실행해 볼 수도 있다.
print(model.predict(std_train_data[:3]).flatten())  # fit 전이기 때문에 결과는 신경쓰지 않음

# 모델 훈련
epochs = 2000

# 학습 조기 종료
early_stop = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5) # 몇번 참느냐
history = model.fit(std_train_data, train_labels, epochs=epochs, validation_split=0.2, verbose=2, callbacks=[early_stop])
# print(model.predict(std_test_data[:3]).flatten())

df = pd.DataFrame(history.history)
print(df.head(3))


# # history 객체에 저장된 통계치를 사용해 모델의 훈련 과정을 시각화 코드 
def plot_history(history):
    hist = pd.DataFrame(history.history)
    hist['epoch'] = history.epoch
    
    plt.figure(figsize=(8,12))
    
    plt.subplot(2,1,1)
    plt.xlabel('Epoch')
    plt.ylabel('Mean Abs Error [MPG]')
    plt.plot(hist['epoch'], hist['mean_absolute_error'],label='Train Error')
    plt.plot(hist['epoch'], hist['val_mean_absolute_error'],label='Val Error')
    plt.ylim([0,5])
    plt.legend()
    
    plt.subplot(2,1,2)
    plt.xlabel('Epoch')
    plt.ylabel('Mean Square Error [$MPG^2$]')
    plt.plot(hist['epoch'], hist['mean_squared_error'],label='Train Error')
    plt.plot(hist['epoch'], hist['val_mean_squared_error'],label='Val Error')
    plt.ylim([0,20])
    plt.legend()
    
    plt.show()

plot_history(history)


# 모델 평가
loss, mae, mse = model.evaluate(std_test_data, test_labels)
print('\ntest dataset으로 모델 평가')
print('mae : {:.3f}\nmse : {:.3f}\nloss : {:.3f}'.format(mae, mse, loss))

# 예측
# 주의 - 새로운 데이터로 예측을 원한다면, 표준화 작업을 선행
test_pred = model.predict(std_test_data).flatten()
print('pred :', test_pred[:5])

# 데이터 분포와 모델에 의한 선형회귀선 시각화
plt.scatter(test_labels, test_pred)
plt.xlabel('True value[mpg]')
plt.ylabel('pred value[mpg]')
plt.show()

# 오차 분포 확인(정규성 : 잔차항이 정규분포를 따르는지 확인)
err = test_pred
plt.hist(err, bins=20)
plt.xlabel('pred error[mpg]')
plt.show()