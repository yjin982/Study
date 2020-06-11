'''    가설검정 정리    '''
import MySQLdb
import ast
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols

with open('mariadb.txt', 'r')  as f:
    config = f.read()
config = ast.literal_eval(config) #dict 타입으로 전환
conn = MySQLdb.connect(**config)
cursor = conn.cursor()
sql = 'select jikwon_no, jikwon_name, jikwon_jik, jikwon_pay from jikwon where jikwon_jik="{}" and jikwon_pay >= 7500'.format('과장')
cursor.execute(sql)

for data in cursor.fetchall():
    print('%s %s %s %s'%data)
print()



# 교차분석(이원 카이제곱 검정) => 요인이 2개이니까 교차표 사용
df = pd.read_sql('select * from jikwon', conn)

print('각 부서(범주형)와 직원 평가점수(범주형) 간의 관련성 분석') # 범주형x범주형
print('귀무 : 부서와 평가점수는 관련이 없다.')
buser = df.buser_num
rating = df.jikwon_rating
ctab = pd.crosstab(buser, rating) #교차표
print(ctab)
chi, p, df, exp = stats.chi2_contingency(ctab) # 이원 카이제곱

print('chi:{:.4f}, p:{:.4f}, df:{}'.format(chi, p, df))
print('해석1 : 카이제곱표(자유도xP-value)에서 임계치 12.59 > 7.339이므로 귀무 채택')
print('해석2 : p value {:.4f}가 0.05보다 크므로 귀무채택. 부서와 평가점수는 관련이 없다고 볼 수 있다.\n\n'.format(p))



# 두 집단 이하의 평균 차이분석(t 검정) => 독립변수-범주형, 종속변수:연속형
print('10, 20번 부서 간 평균 연봉 차이 여부를 검정')
print('귀무 : 두 부서 간 연봉 평균에 차이가 없다.')
df_10 = pd.read_sql('select buser_num, jikwon_pay from jikwon where buser_num=10', conn)
df_20 = pd.read_sql('select buser_num, jikwon_pay from jikwon where buser_num=20', conn)
t_result = stats.ttest_ind(df_10.jikwon_pay, df_20.jikwon_pay)
print(t_result)
print('10번부서 연봉평균:', np.mean(df_10.jikwon_pay), '   20번부서 연봉평균:', np.mean(df_20.jikwon_pay))
print('해석 : p value {:.4f}가 0.05보다 크므로 귀무채택. 두 부서 간 연봉 평균은 차이가 없다고 볼 수 있다.\n\n'.format(t_result.pvalue))



# 세 집단 이상의 평균에 대한 분산분석(ANOVA, f 검정) => 독립변수-범주형, 종속변수:연속형
print('각 부서(4개) 간 평균 연봉 차이 여부를 검정') #집단을 나누는 기준이 하나이므로 one-way 
print('귀무 : 각 부서 간 연봉 평균에 차이가 없다.')
df_anova = pd.read_sql('select buser_num, jikwon_pay from jikwon', conn)
group1 = df_anova[df_anova.buser_num == 10].jikwon_pay
group2 = df_anova[df_anova.buser_num == 20].jikwon_pay
group3 = df_anova[df_anova.buser_num == 30].jikwon_pay
group4 = df_anova[df_anova.buser_num == 40].jikwon_pay

# 데이터 분포를 시각화
# plot_data = [group1, group2, group3, group4]
# plt.boxplot(plot_data)
# plt.show()


# 일원분산분석 1
f_sta, p_val = stats.f_oneway(group1, group2, group3, group4)
print('결과1   f:{:.4f}, p:{:.4f}'.format(f_sta, p_val))
print('해석 : p value {:.4f}가 0.05보다 크므로 귀무 채택. 각 부서간 평균 연봉 차이가 없는 걸로 볼 수 있다.\n'.format(p_val))

# 일원분산분석 2 : 선형모델 이용
lmodel = ols('jikwon_pay ~ C(buser_num)', data=df_anova).fit()  # fit()=>학습하라
table = sm.stats.anova_lm(lmodel, type=1) # type=1 일원이냐 이원이냐
print(table)
print('해석 : PR(>F) = (p value) 0.7407이 0.05보다 크므로 귀무채택\n\n')



# 사후 검정
from statsmodels.stats.multicomp import pairwise_tukeyhsd
result = pairwise_tukeyhsd(df_anova.jikwon_pay, df_anova.buser_num)
print(result) # reject 통계적의로 유의한지 여부
# 결과 시각화
result.plot_simultaneous() 
plt.show()
