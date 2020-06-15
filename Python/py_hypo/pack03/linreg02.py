'''
    01번 파일 계속
'''
#방법 4 : stats.linregress() 사용
from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

score_iq = pd.read_csv('../testdata/score_iq.csv')
# print(score_iq.info())

x = score_iq.iq      # 독립변수
y = score_iq.score # 종속변수

# 상관 계수 확인
print(np.corrcoef(x, y)) # 강한 양의 상관관계
# print(score_iq.corr())
plt.scatter(x, y)
# plt.show()

# 두 변수 간 인과관계가 있어 보이므로 회귀분석을 수행
model = stats.linregress(x, y)
print(model) # 기울기, 절편, r값, p값, 표준오차
print()

newx = 140
yhat = 0.65143 * newx + -2.85644
print('yhat :', yhat, '\n')

print(model.slope, model.intercept, model.pvalue)
'''    pvalue가 0.5 보다 작으면 독립변수로 의미있다   '''
