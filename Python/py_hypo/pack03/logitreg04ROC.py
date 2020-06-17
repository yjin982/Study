'''
    ROC(Receiver Operating Characteristic curve) 곡선 : 분류모델의 성능을 평가하는 그래프
    ROC 커브의 면적(AUC - Area Under the Curve:ROC 곡선 아래 영역)이 1에 가까울수록 (왼쪽 꼭지점에 다가갈수록) 좋은 성능이다.
    ROC 곡선(수신자 조작 특성 곡선)은 모든 분류 임계값에서 분류 모델의 성능을 보여주는 그래프입니다. 이 곡선은 다음 두 매개변수(TPR, FPR)를 표시합니다.
'''
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np

# 분류 연습용 샘플 데이터 작성
x, y = make_classification(n_samples=16, n_features=2, n_informative=2, n_redundant=0, random_state=0)
# n_samples 표본데이터수 n_features 독립변수의 수 n_informative 독립 변수 중 종속 변수와 상관 관계가 있는 성분의 수  n_redundant : 독립 변수 중 다른 독립 변수의 선형 조합으로 나타나는 성분의 수   random_state 난수고정
# print(x)  #[[ 2.03418291 -0.38437236]  [ 4.06377686  0.17863836] ...
# print(y)  #[0 1 0 1 1 0 0 0 1 0 1 0 1 1 0 1]  실제값

model = LogisticRegression().fit(x,y)
y_hat = model.predict(x)
print('y_hat :', y_hat)  #예측값

f_value = model.decision_function(x)  # 결정(판별)함수, 불확실성 측정 함수 
print(f_value)  #[ 0.37829565  1.6336573  -1.42938156  1.21967832  .... 
print()

df = pd.DataFrame(np.vstack([f_value, y_hat, y]).T, columns=['f', 'yhat', 'y'])
print(df)  # 0보다 작으면 0, 0보다 크면 1로 예측한 것 yhat
print()

# ROC 커브
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y, y_hat, labels=[1, 0]))

recall = 7 / (7 + 1)    # 민감도=재현율=참 양성 비율(TPR) = TP / TP+FN    :정답이 Positive인 것들 중에서 정말로 정답을 맞춘 수의 비율  -> y축이된다.
fallout = 1 / (1 + 7)  # 허위 양성 비율(FPR) = FP / FP+TN     : Negative인 것 중에서 모델이 Positive라고 잘못 예측한 것의 비율 -> x축이된다.

print(recall, fallout)


# 시각화, 그래프 그리기
from sklearn.metrics import roc_curve
fpr, tpr, threshold = roc_curve(y, model.decision_function(x))
print('fpr :', fpr)
print('tpr :', tpr)
print('threshold :', threshold) # 재현율을 높이기 위한 판단 기준

import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
plt.plot(fpr, tpr, 'o-', label='Logistic Regreession')
plt.plot([0,1], [0, 1], 'k--', 'random guess')
plt.plot([fallout], [recall], 'ro', ms=10)
plt.xlabel('위양성율(fpr:fallout)')
plt.ylabel('재현율(tpr:recall)')
plt.show()
