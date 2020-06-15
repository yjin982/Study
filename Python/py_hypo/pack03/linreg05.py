'''  통계학은 귀납적 추론이 대부분
    귀납적 추론 - 개별 사례를 모아서 일반적인 법칙(모델)을 생성 
    연역적 추론 - 이미 있는 사설이나 가정에 근거해서 논리적 추론에 의해서 결과를 얻는 방법
'''
'''
    mtcars 데이터를 가지고 선형 회귀분석 연습(ols)
'''
import statsmodels.api
import statsmodels.formula.api as smf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')

mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data
# print(mtcars) # 32x11
# print(mtcars.describe())
print(mtcars.corr())
print(np.corrcoef(mtcars.hp, mtcars.mpg)) # 마력수, 연비 상관관계 -0.77616837=반비례
print()

# 시각화
# plt.scatter(mtcars.hp, mtcars.mpg)
# plt.xlabel('마력수')
# plt.ylabel('연비')
# slope, intercept = np.polyfit(mtcars.hp, mtcars.mpg, 1) # R의 abline과 같은 효과
# print(mtcars.hp * slope + intercept)
# plt.plot(mtcars.hp, mtcars.hp * slope + intercept, 'r', alpha=0.4) #선형회귀식으로 선 긋기
# plt.show()


# 단순 선형회귀 분석
result = smf.ols(formula='mpg ~ hp', data=mtcars).fit()
print(result.conf_int(alpha=0.05)) # 95%
print(result.conf_int(alpha=0.01)) # 99%
# print(result.summary())
print(result.summary().tables[1])
# yhat = -0.0682 * x + 30.0989
print('예측 연비 :', -0.0682 * 110 + 30.0989)  # 22.5969
print('예측 연비 :', -0.0682 * 50 + 30.0989)    # 26.6889
print('예측 연비 :', -0.0682 * 200 + 30.0989)  # 16.4589

# msg(연비)는 hp(마력수) 값에 -0.0682 배 씩 영향을 받고 있다.
# 마력에 따라 연비는 증감한다라고 말할 수 있으나 이는 조심스럽다. 일반적으로 독립변수는 복수
# 모델이 제공한 값을 믿고 섣불리 판단하는 것은 곤란하다. 의사결정을 위한 참고 자료로 사용해야 한다.


print()
# 다중 선형 회귀분석
result2 = smf.ols(formula='mpg ~ hp + wt', data=mtcars).fit()
print(result2.summary())


print()
# 추정치 구하기 : 임의의 차체무게에 대한 연비 출력
print(np.corrcoef(mtcars.wt, mtcars.mpg)) #  -0.86765938
result3 = smf.ols(formula='mpg ~ wt', data=mtcars).fit()
print(result3.summary())
# 결정계수 :  0.753
#  모델의 p-value :  1.29e-10

# 추정치(예측값) 출력
pre = result3.predict()
print('추정치 :', pre[:3])
print('실제값 :', mtcars.mpg[:3].values)

# 전체 자료 비교
data = {
    'mpg' : mtcars.mpg,
    'mpg_pred' : pre,
}
df = pd.DataFrame(data)
print(df) # 실제 연비와 추정 연비가 대체적으로 비슷한 것을 알 수 있다.


print()
# 이제 새로운 데이터(차체 무게)로 연비를 추정
mtcars.wt = 6 # 차체 무게가 6톤이라면
rete = result3.predict(pd.DataFrame(mtcars.wt))
print('차체 무게가 6톤이라면 연비는?', rete[0])

mtcars.wt = 0.4 # 차체 무게가 400kg 이라면
rete = result3.predict(pd.DataFrame(mtcars.wt))
print('차체 무게가 6톤이라면 연비는?', rete[0])


print()
# 복수 차체무게에 대한 연비 예측
wt_new = pd.DataFrame({'wt':[6, 3, 1, 0.4, 0.3]})
pred_mpgs = result3.predict(wt_new)
print('예상 연비 :', np.round(pred_mpgs.values, 3))