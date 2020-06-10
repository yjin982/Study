import scipy.stats as stats
import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt
import urllib.request
'''
    일원분산분석 : 집단 구분 요인 1
    
    ex) 그룹별(3개) 네과목 시험점수 평균 차이 검정
    귀무 : 그룹별 시험점수 차이가 없다.
    대립 : -------------------- 있다.
'''
url = 'https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/group3.txt'
data = np.genfromtxt(urllib.request.urlopen(url), delimiter=',') # print(type(data)) # ndarray 형태 데이터

gr1 = data[data[:, 1] == 1, 0] #집단이 1인 데이터만 빼기
gr2 = data[data[:, 1] == 2, 0]
gr3 = data[data[:, 1] == 3, 0]

# 정규성 확인, 0.05보다 크면 정규성 만족
print(stats.shapiro(gr1)[1])
print(stats.shapiro(gr2)[1])
print(stats.shapiro(gr3)[1])

# 그룹 간 데이터들의 분포를 시각화
plot_data = [gr1, gr2, gr3]
plt.boxplot(plot_data)
# plt.show()

# 일원분산분석 방법1
f_statistic, p_value = stats.f_oneway(gr1, gr2, gr3)
print('일원 분산 분석 결과    f통계량:%f, p value:%f'%(f_statistic, p_value))
'''    p-value가 0.05보다 작으므로 그룹별 시험점수 차이가 있다라는 의견이 통계적으로 유의하다.    '''

# 일원분산분석 방법2 - Linear Model을 속성으로 사용
# data2 = pd.read_csv(urllib.request.urlopen(url)) # print(type(data2)) # Dataframe 형태 데이터 
# data2.columns = ['value', 'group'] #이렇게 따로 가져온 경우 결과값이 다르게 나옴. 왜?
data2 = pd.DataFrame(data, columns=['value', 'group'])
lmodel = ols('value ~ C(group)', data2).fit() #group이 범주형이라는 것을 알려줘야함 => C(...)
print(anova_lm(lmodel))

'''    PR(>F):0.043589가 0.05보다 작으므로 귀무기각    '''


print()
'''
    이원분산분석 (two way anova): 집단 구분 요인 2
    
    귀무 : 관측자와 태아수 그룹에따라 태아의 머리둘레에 차이가 없다. 
    대립 : ---------------------------------------------- 있다.
'''
url = 'https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/group3_2.txt'
data = pd.read_csv(url)

# 시각화
plt.rc('font', family='malgun gothic')
data.boxplot(column='머리둘레', by='태아수', grid=True)
# plt.show() # (우리가 봤을때) 태아의 머리둘레는 차이가 있어보이지만 통계적으로 차이가 있는지, 관측자와 상호 작용이 있는제 분산분석으로 검정이 필요

formula = '머리둘레 ~ C(관측자수) + C(태아수) + C(태아수):C(관측자수)' # 좌:우   좌우가 상호작용
lmodel = ols(formula, data).fit() # fit()학습
print(anova_lm(lmodel))

'''  📌관측자수) PR(>F)  6.497055e-03 < 0.05 이므로 머리둘레에 차이가 있다.   
    C(태아수):C(관측자수)  PR(>F)   3.295509e-01 > 0.05 이므로 상호작용에 의한 머리둘레에 차이가 없다.
    관측자수와 태아수는 머리둘레에 영향을 미치나, 관측자수와 태아수에 상호작용에 의한 영향은 없다.
'''


formula2 = '머리둘레 ~ C(관측자수) + C(태아수)' # 상호작용 무시
lmodel2 = ols(formula2, data).fit() # fit()학습
print(anova_lm(lmodel2))

'''  📌관측자수) PR(>F)  6.316641e-03 < 0.05 이므로 머리둘레에 차이가 있다.   
    C(태아수) PR(>F)   1.006291e-32 < 0.05 이므로 머리둘레에 차이가 있다.
    관측자수와 태아수는 머리둘레에 영향을 미친다. 
'''