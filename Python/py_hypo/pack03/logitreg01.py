'''
    로지스틱 회귀분석(Logistic Regression) : 지도학습 중 분류모델(이항분류)
      독립변수(연속형), 종속변수(범주형)
      logit변환(odds ratio의 결과에 log를 씌워 0 ~ 1 사이의 확률값을 반환
      
    시그모이드 함수(sigmoid function) 1 / ( 1 + e ** -x) 
'''    
import math
import numpy as np
def sigmoidFunc(x):
    return 1 / (1 + math.exp(-x))
# print(sigmoidFunc(1))     #0.7310585786300049
# print(sigmoidFunc(3))     #0.9525741268224334
# print(sigmoidFunc(-2))    #0.11920292202211755
# print(sigmoidFunc(0.2))  #0.549833997312478
# print(sigmoidFunc(0.8))  #0.6899744811276125
# print(np.around(sigmoidFunc(-0.02)))  #0.0
# print(np.around(sigmoidFunc(0.02)))   #1.0
# print(np.rint(sigmoidFunc(0.08)))        #1.0
# print()

'''  자동차 데이터로 분류 연습(연비와 마력수로 변속기 분류)
    연습1 : logit()
'''
import statsmodels.api as sm
import statsmodels.formula.api as smf

mtcars = sm.datasets.get_rdataset('mtcars').data
# print(mtcars)
mtcar = mtcars.loc[:, ['mpg', 'hp', 'am']]  #am:변속기 종류(자동,수동)  -> 종속
print(mtcar['am'].unique())  # 1 0


formula = 'am ~ hp + mpg'
result = smf.logit(formula=formula, data=mtcar).fit()
print(result.summary())
print('예측값       :', result.predict()[:10])
print('실제값       :', mtcar['am'][:10].values)
print('예측반올림 :', np.around(result.predict()[:10]))

# confusion matrix 혼동행렬  #https://www.geeksforgeeks.org/confusion-matrix-machine-learning/
conf_tab = result.pred_table()
print(conf_tab)  # 맞은걸 맞았다고 한 수 16, 틀린걸 틀렸다고 한 수 10

print('\n분류 정확도(Accuracy) :', (16 + 10) / len(mtcar))
print('분류 정확도(Accuracy) :', (conf_tab[0][0] + conf_tab[1][1]) / len(mtcar))  # 매번 예측이 다를 수 있으니까 
from sklearn.metrics import accuracy_score # 또는 따로 제공하는 함수
pred2 = result.predict(mtcar)
print('분류정확도 sklearn :', accuracy_score(mtcar['am'], np.around(pred2)))  # 0.8125 = 81%


print('\n\n\n')
'''  연습2 : glm()  '''
result2 = smf.glm(formula=formula, data = mtcar, family=sm.families.Binomial()).fit()  #family 이항분포이항분류, 기본은 가우시안
print(result2.summary())

glm_pred = result2.predict(mtcar[:5])
print('예측값        :', glm_pred.values)
print('예측반올림  :', np.around(glm_pred.values))
glm_pred2 = result2.predict(mtcar)
print('분류 정확도 :', accuracy_score(mtcar.am, np.around(glm_pred2)))  # 0.8125


print()
# 새로운 값으로 예측
newdf = mtcar.iloc[:2].copy() # 기존 데이터 일부 추출해 새 객체 생성 후 분류 작업
# print(newdf)
newdf.mpg = [10, 30]
newdf.hp = [100, 120]
print(newdf)
new_pred = result2.predict(newdf)
print('새로운 데이터에 대한 분류 결과')
print(np.around(new_pred))
print()

import pandas as pd
newdf2 = pd.DataFrame({'mpg':[10, 35], 'hp':[100, 125]})
print(newdf2)
new_pred2 = result2.predict(newdf2)
print('새로운 데이터에 대한 분류 결과')
print(np.around(new_pred2))


'''  머신러닝의 포용성   "머신러닝은 수학이 아니라 추론이다"
      100%의 정확한 값(=수학)이 아닌 주변값을 예측(=추론)하게 하는 것. ex) 강아지 사진을 가지고 학습을 시키다가 꼬리가 없는 강아지 사진을 넣어도 강아지로 분류 할 수 있도록
      그렇다고 정확성이 너무 떨어지면 분류 모델 성능이 떨어지므로 95~98% 정도는 나오게 해야함.
'''