'''
    이원카이제곱 동질성 검정
    두 집단의 분포가 동일한가? 다른 분포인가? 를 검정하는 방법으로, 두 집단 이상에서 각 범주(집단) 간의 비율이 서로 동일한가를 검정하는 방법이다. 즉, 두 개 이상의 범주형 자료가 동일한 분포를 갖는 모집단에서 추출된 것인지 검정하는 방법이다.
      - 귀무가설 예) 모든 샘플들의 비율은 동일하다.
      - 독립성 검정은 두 변수 사이의 연관성을 검정하는데 비해, 동질성 검정은 하위 모집단 사이 특정 변수에 대한 분포의 동질성을 검정한다.
'''
import pandas as pd
import scipy.stats as stats

'''  실습) 교육방법에 따른 교육생들의 만족도 분석
    귀무 : 교육방법에 따른 교육생들의 만족도에 차이가 없다.
    대립 : -------------------------------------- 있다.
'''
data = pd.read_csv('../testdata/survey_method.csv')
# print(data['method'].unique()) #no  method[1, 2, 3]  survey[1, 2, 3, 4, 5]

ctab = pd.crosstab(index=data['method'], columns=data['survey'])
ctab.columns = ['매우만족', '만족', '보통', '불만족', '매우불만족']
ctab.index = ['방법1', '방법2', '방법3']
print(ctab)
chi2, p, df, exped = stats.chi2_contingency(ctab)
print('chi2 : {}\np : {}\ndf : {}\nexped :\n{}'.format(chi2, p, df, exped))
print('📌 해석 : p-value(0.5864574374550608)가 유의수준 α 0.05 보다 크므로 비유의하다. 귀무 채택\n')


'''  실습) 연령대별 sns 이용률의 동질성 검정
    20대에서 40대까지 연령대별로 서로 조금씩 그 특성이 다른 SNS 서비스들에 대해 이용 현황을 조사한 자료를 바탕으로 연령대별로 홍보전략을 세우고자 한다. 연령대별로 이용 현황이 서로 동일한지 검정해 보도록 하자
    귀무 : 연령대별로 이용현황이 서로 동일하다. 
    대립 : ------------------------동일하지 않다.
'''
snsdata = pd.read_csv('../testdata/snsbyage.csv')
# print(snsdata['age'].unique(), snsdata['service'].unique()) #age[1 2 3]:[20대 30대 40대]  service['F' 'T' 'K' 'C' 'E']

sns_ctab = pd.crosstab(index=snsdata['age'], columns=snsdata['service'])
print(sns_ctab)
chi2, p, df, exped = stats.chi2_contingency(sns_ctab)
print('chi2 : {}\np : {}\ndf : {}\nexped :\n{}'.format(chi2, p, df, exped))
print('📌 해석 : p-value(1.1679064204212775e-18)가 유의수준 α 0.05 보다 매우 작으므로 유의하다. 귀무 기각=연령대별로 이용현황이 서로 동일하지 않다.\n')