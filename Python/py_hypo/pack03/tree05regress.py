'''  ※regression 연속형 데이터 예측
    DecisionTreeRegressor & RandomForestRegressor 모델로 연속형 자료 예측
'''
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_boston
from sklearn.metrics import r2_score  # 결정계수
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)

boston = load_boston()
# print(boston.DESCR)  # (506x13) MEDV : 종속변수(집값) 그외 독립변수
dfx = pd.DataFrame(boston.data, columns=boston.feature_names)
dfy = pd.DataFrame(boston.target, columns=['MEDV'])
df = pd.concat([dfx, dfy], axis=1)
print(df.head(3), '\n')

# 상관관계 파악하기
print(df.corr())

# MEDV와 상관관계가 강한 칼럼 일부 선택
cols = ['MEDV', 'RM', 'PTRATIO', 'LSTAT']
# sns.pairplot(df[cols])
# plt.show()

x = df[['LSTAT']].values  # 하위층 비율, 강한 음의 관계
y = df['MEDV'].values
print(x[:3])
print(y[:3])

print()
# 실습1 : DecisionTreeRegressor
model = DecisionTreeRegressor(max_depth=3).fit(x, y)
print('predict :', model.predict(x)[:5]) # 예측값
print('realval :', y[:5].ravel())            # 실제값

r2 = r2_score(y, model.predict(x))
print('설명력(결정계수) :', r2)  # 0.699 약 70%의 설명력을 가짐. regression에서는 정확도가 아니라 설명력으로 해석

print()
# 실습2 : RandomForestRegressor
model2 = RandomForestRegressor(n_estimators=1000, criterion='mse').fit(x, y)  # 예측에서는 주로 mse(평균제곱오차), 분류할때 gini나 entropy
print('predict :', model2.predict(x)[:5]) # 예측값
print('realval :', y[:5].ravel())              # 실제값

r22 = r2_score(y, model2.predict(x))
print('설명력(결정계수) :', r22)


# 시각화
plt.scatter(x, y, c='lightgray', label='train data')  # 좀 더 크고 선명한 차트 그리기
plt.scatter(x, model2.predict(x), c='magenta', label='predict data')
plt.xlabel('LSTAT')
plt.ylabel('MEDV')
plt.legend()
plt.show()

print()
# 새 값으로 예측
import numpy as np
# print(x[:3].T)
x_new = np.array([[10], [15], [1]])
print(x_new.T, '의 예상 집 값 :', model2.predict(x_new))

