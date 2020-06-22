'''
    Perceptron (인공 신경망)
'''
import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt
from statsmodels.sandbox.nonparametric.tests.ex_smoothers import pmod

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None);
print(df.head(3))
print(df.corr())

x = df.iloc[0:100, [0, 2]].values  #0~100행까지=setosa, versicolor만, 컬럼은 sepal.length, petal.length
y = df.iloc[0:100, 4].values
print(x[:2])
print(y[:2], np.unique(y)) 

y = np.where(y == 'Iris-setosa', -1, 1)  # Iris-setosa면 -1, 아니면 1
print(y)


# 시각화
plt.scatter(x[:50, 0], x[:50, 1], c='pink', marker='o', label='setosa')
plt.scatter(x[50:100, 0], x[50:100, 1], c='yellowgreen', marker='o', label='versicolor')
plt.xlabel('sepal.length')
plt.ylabel('petal.length')
plt.legend(loc='upper left')
plt.show()



# 퍼셉트론 알고리즘으로 만든 클래스
from pack04.nn01_1class import MyPerceptron
pmodel = MyPerceptron(eta=0.1, n_iter=10)  # 학습률 0.1, 10번 반복학습
pmodel.fit(x, y)
print(pmodel.predict(x))

print()
new_x = [[5.1, 1.4], [2.1, 7.4]]
print(pmodel.predict(new_x))


# Perceptron의 반복에 따른 대비 오차 시각화
plt.plot(range(1, len(pmodel.errors_)+1), pmodel.errors_, marker='o')
plt.show()  # 여섯번째 이후에 에러가 최소화 되면서 수렴이 됨. 샘플을 제대로 분류를 시작하는 모델이 완성.