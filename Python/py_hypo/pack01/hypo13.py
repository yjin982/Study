'''
    비율검정
      집단의 비율이 어떤 특정한 값과 유의한지 검정
      비율 차이 검정 통계량을 바탕으로 귀무가설의 기각여부를 결정.

    one-sample
    A회사에는 100명 중에 45명이 흡연을 한다. 국가 통계를 보니 국민 흡연율은 35%라고 한다. 이 때 비율이 다른지 검정
    귀무 : A회사와 국가통계 흡연율 비율이 같다
    대립 : ---------------------------- 같지 않다.
'''
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

count = np.array([45])
nobs = np.array([100])
val = 0.35

z, p = proportions_ztest(count, nobs, val)
print(z, p) #0.04442318 < 0.05
# 📌 귀무 기각. 비율은 같지 않다.




'''
    two-sample
    A회사 사람들 300명 중 100명이 커피를 마시고, B회사 사람들 400명 중 170명이 커피를 마셨다. 두 집단의 커피러 비율의 동일 여부를 검정하시오.
    귀무 : A회사와 B회사의 커피러 비율은 같다.
    대립 : --------------------------- 같지 않다.
'''
count = np.array([100, 170]) #실제 관측된 커피러
nobs = np.array([300, 400])  #전체 인원수
z, p = proportions_ztest(count, nobs, 0) #비율이 제시되지 않은 경우 value는 0
print(z, p) #0.013675 < 0.05
# 📌 귀무 기각. 비율은 같지 않다.