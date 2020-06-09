'''
    세 개 이상의 모집단에 대한 가설검정 – 분산분석
      ‘분산분석’이라는 용어는 분산이 발생한 과정을 분석하여 요인에 의한 분산과 요인을 통해 나누어진 각 집단 내의 분산으로 나누고 요인에 의한 분산이 의미 있는 크기를 크기를 가지는지를 검정하는 것을 의미한다.
      세 집단 이상의 평균비교에서는 독립인 두 집단의 평균 비교를 반복하여 실시할 경우에 제1종 오류가 증가하게 되어 문제가 발생한다.
      이를 해결하기 위해 Fisher가 개발한 분산분석(ANOVA, ANalysis Of Variance)을 이용하게 된다.
      종속 변수의 변화 폭(분산)이 독립변수에 의해 주로 기인하는지를 파악할 때 사용(=인과관계 파악시에)
      
      독립변수-범주형, 종속변수-수치형
'''
import scipy.stats as stats
import pandas as pd
from statsmodels.formula.api import ols  


'''  실습) 세 가지 교육방법을 적용하여 1개월 동안 교육받은 교육생 80명을 대상으로 실기시험을 실시. [일원분산분석(one way ANOVA) : 집단을 구분하는 요인이 1개]
    귀무 : 세 가지 교육방법에 따른 교육생들의 실기시험 점수의 평균은 차이가 없다.
    대립 :  -------------------------------------------------------- 있다.
'''
data = pd.read_csv('../testdata/three_sample.csv')
# print(data.describe()) #max 중 500 -> outlier 이상치

# 시각화, 박스그래프를 통해 이상치 확인
import matplotlib.pyplot as plt
plt.boxplot(data.score)
# plt.show()

data = data.query('score <= 100') #최대값 100이하인 것만 취함 = 이상치 제거
print(data.describe())

print()
# 정규성 확인
print(stats.shapiro(data.score)[1]) # 0.2986 > 0.05 정규성 만족 (정규성 만족 못할 경우 kruskal-wallis test)

# 등분산성 확인
result = data[['method', 'score']]
m1 = result[result.method == 1]
m2 = result[result.method == 2]
m3 = result[result.method == 3]

score1 = m1.score
score2 = m2.score
score3 = m3.score

print('등분산성 확인 : ', stats.levene(score1, score2, score3).pvalue, '> 0.05 = 등분산성 만족') #일반적, 모수 검정
print('등분산성 확인 : ', stats.bartlett(score1, score2, score3).pvalue, '> 0.05 = 등분산성 만족') #비모수 검정

# 정규성, 등분산성 만족이므로 ANOVA 사용 가능. 아니라면 welchi's ANOVA


print()
# 가공된 자료로 분산분석=anova
# 교차표 작성 : 교육 방법별 건수
data2 = pd.crosstab(index=data.method, columns='count')
data2.index = ['방법1', '방법2', '방법3']
print(data2)

# 교차표 작성 : 교육 방법별 만족 여부
data3 = pd.crosstab(index=data.method, columns=data.survey)
data3.index = ['방법1', '방법2', '방법3']
data3.columns = ['만족', '불만']
print(data3)

# F통계량을 얻기 위해 회귀분석 결과를 이용 (독립변수 1개)
import statsmodels.api as sm
reg = ols(formula='data["score"] ~ data["method"]', data=data).fit() # 단순 선형 회귀 모델 작성
# print(reg)
table = sm.stats.anova_lm(reg, type=1)
print(table) # PR(>F) <= pvalue 0.727597 > 0.05 귀무 채택
# 세 가지 교육방법(3집단)에 따른 실기시험에 평균의 차이가 없다.
# 세 집단간의 관계는 나오지만 그룹끼리의 관계(1과2, 2와3, 1과3)를 알기위해서는 사후검정이 필요

# F통계량을 얻기 위해 다중 회귀분석 결과를 이용(독립변수 복수)
# reg2 = ols(formula='data["score"] ~ data["method"] + data["survey"]', data=data).fit() # 다중 선형 회귀 모델 작성
# table2 = sm.stats.anova_lm(reg2, type=1) #type은 1 또는 2, 3이 가능
# print(table2) # PR(>F) <= pvalue 0.727597 > 0.05 귀무 채택
#df자유도        sum_sq제곱합 SSR     mean_sq제곱평균 MSR        F    PR(>F)
''' https://kkokkilkon.tistory.com/77 '''


print()
''' 
    분산분석은 전체 그룹 간의 평균값 차이가 유의미한지 검정가능하나, 어느 그룹의 평균값이 의미가 있는지는 알려주지 않는다. 그래서 사후검정(Post Hoc Test)를 한다.
    등분산성이 가정되었을 때 
      사후검정 민감도 Scheffe > Tukey > Duncan 순
      그 중에서 Tukey가 가장 일반적인 방법 -> 비교대상 표본수가 동일한 경우에 사용
    등분산이 가정되지 않았을 때 Dunnett T3 또는 Games-Howell를 사용
''' 
from statsmodels.stats.multicomp import pairwise_tukeyhsd
turkeyResult = pairwise_tukeyhsd(data.score, data.method)
print(turkeyResult)
# group1 group2 meandiff p-adj  lower   upper  reject=>이 True일 경우 유의미한 차이가 있다.
# ------------------평균차이----------------------------------
#      1      2      0.9725   0.9  -8.946   10.891   False=>그룹1과2사이에 유의미한 관계가 없다.
#      1      3      1.4904   0.9  -8.8184 11.7992  False
#      2      3      0.5179   0.9  -9.6127 10.6484  False

# 시각화
turkeyResult.plot_simultaneous()
plt.show()