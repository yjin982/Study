'''
    나이브 베이지안 비 예측
    나이브 베이지안은 dataset의 모든 특징들이 동등하며 독립적이라고 가정한다. 
    예를 들어 사람들은 비가 오는 날에는 시간보다는 습도가 더 중요한 변수라고 생각할 수 있으나 나이브 베이지안 에서는 이런 사실을 무시하기 때문이다. 
    이런 가정에도 불구하고 분류학습에서 매우 정확한 결과 값을 유추할 수 있기 때문에 자주 사용되고 있다
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn import metrics
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)

df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/weather.csv')
print(df.head(3))

x = df[['MinTemp', 'MaxTemp', 'Rainfall', 'Humidity', 'Cloud']]
print(df['RainTomorrow'].unique()) # Yes No
label = df.RainTomorrow.apply(lambda x: 1 if x == 'Yes' else 0) #Yes/No를 1/0으로 치환 방법1
# label = df.RainTomorrow.map({'Yes':1, 'No':0})                     #Yes/No를 1/0으로 치환 방법2


# train / test  -   7/3=default test_size=0.3
x_train, x_test, y_train, y_test = train_test_split(x, label, random_state=0)


# predict
gmodel = GaussianNB()
gmodel.fit(x_train, y_train)
pred = gmodel.predict(x_test)
print('예측값 :', pred)


print()
# k-fold(교차검증) - 모델 학습시 입력자료를 k겹으로 나누어 학습과 검증을 함께 하는 방법
from sklearn import model_selection
cross_val = model_selection.cross_val_score(gmodel, x, label, cv=5) # 원본의 x, y를 사용
cross_val2 = model_selection.cross_val_score(gmodel, x_train, y_train, cv=5) # train data를 사용해도 됨(overfitting 의심되는 경우)
print(cross_val)
print(cross_val.mean())
print(cross_val2)
print(cross_val2.mean())


print()
# 분류 정확도
acc = sum(y_test == pred) / len(pred)
print('분류 정확도1 :', acc)
print('분류 정확도2 :', accuracy_score(y_test, pred))
cl_report = metrics.classification_report(y_test, pred)
print('분류 보고서 :\n', cl_report)


print()
# 새로운 자료로 예측
import numpy as np
print(x.tail(3)) #기존값을 수정해서 새 데이터 생성
my_weather = np.array([[10.5, 16.5, 0.0, 34, 1], [14.5, 30.9, 10.0, 69, 9], [16.2, 28.1, 2.6, 70, 2]])
print('새로운 값으로 예측', gmodel.predict(my_weather))