'''
    SVM으로 XOR 분류
'''
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import svm, metrics


# x1, x2, xor
xor_data = [
    [0, 0, 0], 
    [0, 1, 1], 
    [1, 0, 1], 
    [1, 1, 0], 
]

xor_df = pd.DataFrame(xor_data, columns=['x1', 'x2', 'XOR'])  # x1, x2 = feature, XOR=label=종속변수
print(xor_df)
feature = np.array(xor_df.loc[:, :'x2'])
label = np.array(xor_df.loc[:, 'XOR'])
# print(feature)
# print(label)

print()
# 모델 생성
# 선형회귀
model = LogisticRegression().fit(feature, label)
pred = model.predict(feature)
print('pred :', pred) #[0 0 0 0]  선형분류이기 때문에 곡선을 그리지 못해서 절반만 맞춤
# SVM
model = svm.SVC().fit(feature, label)
pred = model.predict(feature)
print('pred :', pred) #[0 1 1 0]



print()
# 분류 리포트 작성
acc = metrics.accuracy_score(label, pred) # 정확도(실제값, 예측값)
print('분류 정확도 :', acc)  # 0.5
ac_report = metrics.classification_report(label, pred)
print(ac_report)  # precision정밀도    recall재현율  f1-score정밀도와 재현율의 조화평균   support신뢰도

