'''
    실습) 국가전체와 지역에 대한 인종 간 인원수로 독립성 검정 실습
    - 가설설정 - 
    두 집단(국가전체 - national, 특정지역 LA - la)의 인종 간 인원수의 분포가 관련이 있는가?
    귀무 : 국가전체와 지역에 대한 인종간 인원수는 관련이 없다. == 독립적이다
    대립 : ---------------------------------------- 있다. == 독립적이지 않다.
'''
import pandas as pd
import numpy as np
import scipy.stats as stats

national = pd.DataFrame(["white"] * 100000 + ["hispanic"] * 60000 + ["black"] * 50000 + ["asian"] * 15000 + ["other"] * 35000)
la = pd.DataFrame(["white"] * 600 + ["hispanic"] * 300 + ["black"] * 250 + ["asian"] * 75 + ["other"] * 150)

'''    방법 1 : 함수 이용    '''
na_table = pd.crosstab(index=national[0], columns='count')
la_table = pd.crosstab(index=la[0], columns='count')
na_table['count_la'] = la_table['count']
print(na_table) #크로스테이블 완성

chi2, p, df, pre = stats.chi2_contingency(na_table)
print('결과 = chi:{}, p:{}, df:{}'.format(chi2, p, df))

'''결과 = chi:18.099524243141698, p:0.0011800326671747886, df:4
    📌 해석 : p(0.0011) < α(0.05) 귀무 기각
'''

#p값을 구하는 공식은 정해져있지 않음. 그래서 꼭 알아야 할 필요는 없음
'''    방법 2: pvalue 구하기    
    검정통계량 계산식 sum((관측값 - 기대값))^2 / 기대값
''' 
observed = la_table #관측값
national_ratio = na_table / len(national)
expected = national_ratio * len(la) #기대값
print('\n===기대값===\n', expected)

chi_sqared_stat = (((observed - expected) ** 2) / expected).sum()
print('\n===chi_sqared_stat===\n',chi_sqared_stat)

# p-value구할시 필요한 것   # cdf() 누적분포함수 ✔,  pdf() 확률밀도함수, pmf() 확률질량함수
pv = 1 - stats.chi2.cdf(x=chi_sqared_stat, df=4)
print('\np-value : ', pv) #0.00113047
