'''
    Navie Bayes Classification
      베이즈 정리(조건부 확률을 이용)를 적용한 확률 분류기. 텍스트 분류에 효과적(ex:스팸메일, 게시판 카테고리)
      머신러닝에서는 Feature가 주어졌을 때 label의 확률을 구하는데 사용
      P(L|featrue) = P(feature|L) P(L) / P(feature)
'''
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.preprocessing import OneHotEncoder

# 데이터 준비
x = np.array([1,2,3,4,5])
x = x[:, np.newaxis] # 차원 확대
# print(x)
y = np.array([1,3,5,7,9])

# 모델 생성
model = GaussianNB().fit(x, y)
# print(model)

# 예측
pred = model.predict(x)
print(pred)

# 새 값으로 예측
new_x = np.array([[0.5], [3.1], [15.0], [7.1]])
new_pred = model.predict(new_x)
print(new_pred)


print()
'''
    OneHotEncoding
      단 하나의 값만 True이고 나머지는 모두 False인 인코딩 희소 행렬의 일종
      분류 정확도를 올리기 위해 독립변수를 넣어줌
'''

x = np.array([1,2,3,4,5])
x = np.eye(x.shape[0]) # 정방행렬을 생성. 빈 값은 0으로 채움
print(x)  # 5x5 대각선은 1 나머지 0

# ===========
x = np.array([1,2,3,4,5])
x = x[:, np.newaxis] # 차원 확대
y = np.array([1,3,5,7,9])

# 모델 생성
model = GaussianNB().fit(x, y)

# 예측
pred = model.predict(x)
print(pred)

acc = metrics.accuracy_score(y, pred)
print('정확도 :', acc)

# 새 값으로 예측
new_x = np.array([[0.5], [3.1], [15.0], [7.1]])
new_pred = model.predict(new_x)
print(new_pred)
# ============

print()
# OneHotEncoder 이용 -> 나이브 베이즈 분류
x = np.array([1,2,3,4,5])
one_hot = OneHotEncoder(categories='auto')
# print(one_hot)
x = x[:, np.newaxis]
x = one_hot.fit_transform(x).toarray()
print(x) # 



