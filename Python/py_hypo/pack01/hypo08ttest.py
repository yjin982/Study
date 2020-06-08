'''
    두 집단의 가설검정 – 실습 시 분산을 알지 못하는 것으로 한정하겠다.
     - 서로 독립인 두 집단의 평균 차이 검정(independent samples t-test)
     - 남녀의 성적, A반과 B반의 키, 경기도와 충청도의 소득 따위의 서로 독립인 두 집단에서 얻은 표본을 독립표본(two sample)이라고 한다.
'''
import pandas as pd
import scipy.stats as stats
from numpy import average

'''  실습) 남녀 두 집단 간 파이썬 시험의 평균 차이가 있는지 검정
    귀무 : 성별에 따른 시험의 평균 차이가 없다.  
    대립 : --------------------------- 있다.
'''
male = [75, 85, 100, 72.5, 86.5]
female = [63.2, 76, 52, 100, 70]

two_sample = stats.ttest_ind(male, female)
# two_sample = stats.ttest_ind(male, female, equal_var=True) #등분산성 만족(두 그룹간의 분산이 같다) True가 기본 
print(two_sample) #Ttest_indResult(statistic=1.233193127514512, pvalue=0.2525076844853278)

# ※값을 각각 얻을 수도 있음
sta, pv = stats.ttest_ind(male, female)
print(average(male))    #83.8
print(average(female)) #72.24

# 📌 p-value 0.25 > 0.05 귀무채택, 평균 차이 없다.


print()
'''  실습) 두 가지 교육방법에 따른 평균시험 점수에 대한 검정 수행 two_sample.csv
    귀무 : 교육방법에 따른 평균 점수 차이가 없다.
    대립 : ---------------------------- 있다.
'''
data = pd.read_csv('../testdata/two_sample.csv')

