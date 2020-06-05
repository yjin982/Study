''' >>이원카이제곱<< 

    교차분할표 이용 
      - 두 개 이상의 변인(집단 또는 범주)을 대상으로 검정을 수행한다.
      - 분석대상의 집단 수에 의해서 독립성 검정과 동질성 검정으로 나뉜다.

    독립성(관련성) 검정
      - 동일 집단의 두 변인(학력수준과 대학진학 여부)을 대상으로 관련성이 있는가 없는가?
      - 독립성 검정은 두 변수 사이의 연관성을 검정한다.
      
    실습 
    귀무 : 교육수준과 흡연율 간에 관련이 없다. == 둘 사이는 독립이다.
    대립 : -------------------------  있다. 
'''
import pandas as pd
import scipy.stats as stats
datas = pd.read_csv('../testdata/smoke.csv')
print(datas['education'].unique(), '   ', datas['smoking'].unique()) 
# education 1대학원 2대졸 3고졸 / smoking 1꼴초 2보통 3비흡연 (숫자 뒤의 내용은 임의로 설정)

# 교차분할표
ctab = pd.crosstab(index=datas['education'], columns=datas['smoking'])
ctab.index = ['노예', '대졸', '고졸']
ctab.columns = ['꼴초', '보통', '비흡연']
print(ctab)
chi_result = [ctab.loc['노예'], ctab.loc['대졸'], ctab.loc['고졸']]

chi2, p, df, _ = stats.chi2_contingency(chi_result)
msg = '결과 : chi2:{}, p:{}, df:{}'
print(msg.format(chi2, p, df))
'''
    결과 : chi2:18.910915739853955, p:0.0008182572832162924, df:4
    
    📌해석
    pvalue가 유의수준 0.05보다 작으므로 귀무가설 기각. 교육수준과 흡연율은 관련이 있다.

    ※야트보정이 자동 처리됨
    ※분할표의 자유도가 1인 경우는 X^2 값이 약간 높게 계산된다.
    ※그래서 절대값 |O-E| 에서 0.5를 뺀 다음 제곱하며, 이 방법을 야트보정이라고 한다.
'''

print()
print()
print(chi_result)