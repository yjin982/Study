'''
    상관분석(r) : 두 개 이상의 변수(연속형) 간에 어떤 관계가 있는지 분석. 공분산을 표준화한 상관계수를 통해서 관계의 정도와 방향을 파악.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({'id1':(1, 2, 3, 4, 5), 'id2':(2, 3, -1, 7, 9)})
print(df)

# plt.scatter(df.id1, df.id2)
# plt.show()

print('\n공분산\n', df.cov())     # 관련 방향성은 제시하나 강도는 모호하다.(단위의 크기에 영향을 받음)
print('\n상관계수\n', df.corr())  # 공분산을 표준화, but 인과관계는 알 수 없다.




print('\n\n상품의 만족도 관계 확인')
data = pd.read_csv('../testdata/drinking_water.csv')
print(data.head(), '\n')

# 각 요소의 표준편차 출력
print(np.std(data.친밀도))
print(np.std(data.적절성))
print(np.std(data.만족도))

print()
# 히스토그램으로 시각화
# plt.hist([np.std(data.친밀도), np.std(data.적절성), np.std(data.만족도)])
# plt.show()

# 공분산 추출
# print(np.cov(data.친밀도, data.적절성))  # numpy는 np.cov(변수1, 변수2) #변수 2개까지 밖에 안됨
# print(np.cov(data.친밀도, data.만족도))
print(data.cov())   # dataframe을 이용하면 변수 2개 이상일때도 가능

print()
# 상관계수 출력
# print(np.corrcoef(data.친밀도, data.적절성))
print(data.corr())
print(data.corr(method='pearson'))    # 변수가 등간, 비율 척도 이고 정규성을 따를 때 default
# print(data.corr(method='spearman')) # 변수가 서열 척도 이고 정규성을 따르지 않을 때
# print(data.corr(method='kendall'))     # 스피어만과 유사

# 상관계수를 시각화 (heatmap 색으로 표현)
import seaborn as sns
plt.rc('font', family='malgun gothic')            #한글깨짐 방지
plt.rcParams['axes.unicode_minus'] = False  #마이너스부호 깨짐 방지


sns.heatmap(data.corr())
plt.show()