'''
    집단 간 차이분석
     - 평균 또는 비율 차이를 분석
      - 모집단에서 추출한 표본정보를 이용하여 모집단의 다양한 특성을 과학적으로 추론할 수 있다.
      
    ※T-test와 ANOVA의 차이
     - 두 집단 이하의 변수 = T-test = 검정통계량 T값
     - 세 집단 이상의 변수 = ANOVA = 검정통계량 F값
    
    단일 모집단의 평균에 대한 가설검정(one samples t-test)
    어느 한 집단의 평균은 0인지 검정하기(정규분포를 따르는 난수 사용)
    귀무 : 자료들의 평균은 0이다.
    대립 : ------------- 0이 아니다.
'''
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(150)
mu = 0
n = 10
x = stats.norm(mu).rvs(n)
print(x, '\n', np.mean(x))
# sns.distplot(x, kde=False, rug=True, fit=stats.norm) #시각화
# plt.show()

result = stats.ttest_1samp(x, popmean=0) #데이터x, popmean 예상 평균값
print(result) #Ttest_1sampResult(statistic=1.1067537454808531, pvalue=0.2971033827639922) statistic 검정통계량(t value)
# 📌 p-value 0.29 > 0.05 이므로 귀무 채택 == 자료들의 평균은 0이다.

result2 = stats.ttest_1samp(x, popmean=0.8) #데이터x, popmean 예상 평균값
print(result2) #Ttest_1sampResult(statistic=1.1067537454808531, pvalue=0.2971033827639922) statistic 검정통계량(t value)
# 📌 p-value 0.0360 < 0.05 이므로 귀무 기각 == 자료들의 평균은 0.8이 아니다.


'''  실습 예제 1)
    A중학교 1학년 1반 학생들의 시험결과가 담긴 파일을 읽어 처리 (국어 점수 평균검정) student.csv
    귀무 : 국어 점수 평균이 80이다. (평균값 임의로 설정)
    대립 : ---------------80이 아니다.
'''
data = pd.read_csv('../testdata/student.csv')
# print(data)
kor_result = stats.ttest_1samp(data.국어, popmean=80)
print(kor_result) # Ttest_1sampResult(statistic=-1.3321801667713213, pvalue=0.19856051824785262)
# 📌 p-value 0.1985 > 0.05 이므로 귀무 채택 == 국어 평균은 80이다.


'''  실습 예제 2)
    여아 신생아 몸무게의 평균 검정 수행 babyboom.csv
    여아 신생아의 몸무게는 평균이 2800(g)으로 알려져 왔으나 이보다 더 크다는 주장이 나왔다. 표본으로 여아 18명을 뽑아 체중을 측정하였다고 할 때 새로운 주장이 맞는지 검정해 보자.
    귀무 : 여아 신생아 몸무게 평균이 2800g이다
    대립 : ---------------------- 2800g이 아니다.
'''
data2 = pd.read_csv('../testdata/babyboom.csv')
# print(data2) #time  gender[1여아, 2남아]  weight  minutes
fdata = data2[data2.gender == 1] #여아데이터만 추출
print(np.mean(fdata.weight)) #3132.4

# 정규성 확인을 위한 시각화
sns.distplot(fdata.iloc[:, 2], fit=stats.norm) # 히스토그램같은 
plt.show()
stats.probplot(fdata.iloc[:, 2], plot=plt) #Q-Q plot : 회귀선과 실제 데이터
plt.show()

print(stats.shapiro(fdata.iloc[:, 2])) #샤피로-윌크 검정으로 정규성 확인 (The test statistic., p=0.01798),  p < 0.05 이므로 정규성을 따르지 않음
# 정규성을 따르지 않을 경우 원래는 t-test를 쓰면 안됨 => 정규성을 띄지 않을 때는 Wilcoxon 혹은  Mann-Whitney
# 그러나 집단이 하나이므로 Wilcoxon 검정은 할 수 없다.

baby_result = stats.ttest_1samp(fdata.weight, popmean=2800)
print(baby_result) #Ttest_1sampResult(statistic=2.233187669387536, pvalue=0.03926844173060218)
# 📌 p-value 0.0392 < 0.05 이므로 귀무 기각 == 여아 몸무게 평균은 2800g이 아니다(더 크다).