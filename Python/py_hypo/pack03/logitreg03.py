'''
    분류 결과가 두 가지 이상인 경우 다항분류 모델을 사용 -> LogisticRegression 
'''
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection._split import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import datasets
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)

iris = datasets.load_iris()
print(iris.keys())
# print(iris.DESCR)
# print(iris.data, iris.data.shape)      # feature(독립변수)
# print(iris.target, iris.target.shape)  # label(class, 종속변수)


print()
# 참고 확률에 의해 꽃 종류가 결정되는 결정 간격 확인
log_reg = LogisticRegression()
x = iris.data[:, 3:]  # petal.width 만 작업에 참여
y = (iris['target'] == 2).astype(np.int)  # 0, 1로 target을 나눔
# print(x)
# print(y)
log_reg.fit(x, y) 
  
x_new = np.linspace(0, 3, 1000).reshape(-1, 1) #1000개의 난수 발생
# print(x_new, x_new.shape)  # (1000, 1)
y_proba = log_reg.predict_proba(x_new)
# print(y_proba)  # 확률값으로 출력 [[9.99250016e-01 7.49984089e-04] ...


# 시각화
import matplotlib.pyplot as plt
# plt.plot(x_new, y_proba[:, 1], 'r-', label='virginicar')
# plt.plot(x_new, y_proba[:, 0], 'b-', label='not virginicar')
# plt.legend()
# plt.show()
print(log_reg.predict([[1.5], [1.7]])) #[0 1]   not virginicar, virginicar로 분류
print(log_reg.predict([[2.5], [0.7]])) #[1 0]   <- [0.98465572 0.01534428] 가 [0]째가 크니까 1로
print(log_reg.predict_proba([[2.5], [0.7]])) # 확률값으로  [[0.02563061 0.97436939]   [0.98465572 0.01534428]]
'''
    결론적으로 LogisticRegression()은 출력 값이 두 개 이상인 경우에 있어 확률값이 큰 요소의 index가 출력
    LogisticRegression()은 다중 클래스(label)를 지원하도록 일반화되어있다. softmax를 사용
    
    ※Softmax(소프트맥스)는 입력받은 값을 출력으로 0~1사이의 값으로 모두 정규화하며 출력 값들의 총합은 항상 1이 되는 특성을 가진 함수※
'''


print('\n\n\n')
# ===========================================================
x = iris.data[:, [2, 3]] # 모든 행의 2,3열, petal.length, petal.width의 2 칼럼으로 꽃의 종류 3가지로 분류
y = iris.target
print(x[:3])
print(y[:3], '   ', set(y))

# train / test 나누기
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) #(105, 2) (45, 2) (105,) (45,)

# (지금은 꼭 필요한 건 아닌지만 필요할 때가 있는) 스케일링 (데이터 크기 표준화, 전체 자료의 분포를 평균 0, 분산 1이 되도록)
print(x_train[:3])  # [[3.5 1. ]  [5.5 1.8]  [5.7 2.5]]
print(x_test[:3])   # [[5.1 2.4]  [4.  1. ]  [1.4 0.2]]

sc = StandardScaler()
sc.fit(x_train)
sc.fit(x_test)
x_train = sc.transform(x_train)
x_test = sc.transform(x_test)

print(x_train[:3]) # [[-0.05624622 -0.18650096]   [ 1.14902997  0.93250481]   [ 1.26955759  1.91163486]]
print(x_test[:3])  # [[ 0.90797473  1.77175914]   [ 0.24507283 -0.18650096]   [-1.32178623 -1.30550673]]


print('\n\n\n')
# ===========================================================
# 분류 모델을 사용
ml = LogisticRegression(C=0.1, random_state=0) # C=모델에 패널티(L2 정규화)를 부여(overfitting 관련)
result = ml.fit(x_train, y_train)  # train 데이터로 모델 학습

# 모델 학습 후 객체를 저장
import pickle
fileName = 'final_model.sav'
pickle.dump(ml, open(fileName, 'wb'))
ml = pickle.load(open(fileName, 'rb'))

# 분류 예측
y_pred = ml.predict(x_test)
print('예측값 :', y_pred)
print('실제값 :', y_test)
print('분류 정확도1 :', accuracy_score(y_test, y_pred))

# confusion matrix
con_mat = pd.crosstab(y_test, y_pred, rownames=['예측값'], colnames=['관측값'])
print(con_mat)
print('분류 정확도2 :', (con_mat[0][0] + con_mat[1][1] + con_mat[2][2]) / len(y_test))
print('분류 정확도3 :', ml.score(x_test, y_test))

print('\n\n')
# 새로운 값으로 예측
new_data = np.array([[5.1, 2.4], [0.3, 0.3], [1.4, 3.4]])  #matrix로 했으니까
new_pred = ml.predict(new_data)
print('예측값 :', new_pred)
