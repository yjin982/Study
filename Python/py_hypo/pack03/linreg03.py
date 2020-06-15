'''    
    사용 빈도가 높은 회귀분석 모델 ols()
    가장 기본적인 결정론적 선형회귀 방법
    
    ※결정론적, 
'''
import pandas as pd

df = pd.read_csv('../testdata/drinking_water.csv')
print(df.head(3))
print(df.corr())  #적절성과 만족도가 0.766으로 가장 관련이 있다.

import statsmodels.formula.api as smf
# 단순 선형회귀
model = smf.ols(formula='만족도 ~ 적절성', data=df).fit() # r 스타일의 모델
print(model.summary())
# R-squared 결정계수, 설명력. 설명력이 (0.49이상) 좋다는 것은 실제 데이터가 회귀직선과 가깝게 있다는 것 = 의미 있는 모델이다
# F-statistic  적절성의 t값(19.340)의 거듭제곱한 것.   Prob (F-statistic) f값으로 부터 도출, 모델에 대한 pvalue, 0.05보다 작으면 유효한 모델
# AIC, BIC 모델 비교 관련
# P>|t| 독립변수에 대한 pvalue 0.05보다 작으면 독립변수로 쓸 수 있다.
# [0.025      0.975] 신뢰구간

print()
print('회귀 계수 :\n', model.params)
print('결정 계수 :', model.rsquared)
print('p value :\n', model.pvalues)
# print('예측값 :', model.predict()) # [3.73596305 2.99668687 3.73596305 2.25741069 2.25741069 ... 
print(df.만족도[0], model.predict()[0])  # 실제값:3, 예측값:3.7359...


# 시각화
from matplotlib.pylab import plt
import numpy as np
plt.scatter(df.적절성, df.만족도)
slope, intercept = np.polyfit(df.적절성, df.만족도, 1) # 1차원
print(slope, intercept)
plt.plot(df.적절성, slope*df.적절성+intercept, 'b', alpha=0.6)  # y = wx + b
plt.show()

print('\n\n')
# 다중 선형회귀
model2 = smf.ols(formula='만족도 ~ 적절성 + 친밀도', data=df).fit()
print(model2.summary())