'''
    서로 대응인 두 집단의 평균 차이 검정(paired samples t-test)
      처리 이전과 처리 이후를 각각의 모집단으로 판단하여, 동일한 관찰 대상으로부터 처리 이전과 처리 이후를 1:1로 대응시킨 두 집단으로 부터의 표본을 대응표본(paired sample)이라고 한다.
      대응인 두 집단의 평균 비교는 동일한 관찰 대상으로부터 처리 이전의 관찰과 이후의 관찰을 비교하여 영향을 미친 정도를 밝히는데 주로 사용하고 있다. 집단 간 비교가 아니므로 등분산 검정을 할 필요가 없다.
'''
import scipy.stats as stats
import pandas as pd
import numpy as np

'''  특강이 시험 점수에 영향을 주었는지 검정하기
    귀무 : 특강 전후에 시험 점수는 차이가 없다. 
    대립 : -------------------------- 있다.
'''
np.random.seed(7)
x1 = np.random.normal(100, 10, 100) # 정규분포를 따르는 랜덤값
x2 = np.random.normal(97, 10, 100)  # (평균, 표준편차, 갯수)

import seaborn as sns
import matplotlib.pyplot as plt
sns.distplot(x1, kde=False, fit=stats.norm)
sns.distplot(x2, kde=False, fit=stats.norm)
# plt.show()
print(stats.ttest_rel(x1, x2).pvalue)

'''  📌해석
    pvalue 0.010843720488266774 < 0.05 이므로 귀무기각. 특강 전후에 시험점수 차이가 있다.
    => 특강이 시험점수에 영향을 주었다. 라는 의견을 받아들임
'''


'''  실습) 복부 수술 전 9명의 몸무게와 복부 수술 후 몸무게 변화
    귀무 : 복부 수술 전후 몸무게 차이가 없다. 
    대립 : ------------------------- 있다.
'''
baseline = [67.2, 67.4, 71.5, 77.6, 86.0, 89.1, 59.5, 81.9, 105.5]
follow_up = [62.4, 64.6, 70.4, 62.6, 80.1, 73.2, 58.2, 71.0, 101.0]

p_sample = stats.ttest_rel(baseline, follow_up)
print(p_sample.pvalue) 

'''  📌해석
    pvalue 0.006326650855933662 < 0.05 이므로 귀무 기각. 몸무게 차이가 있다.
'''
