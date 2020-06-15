'''
    선형 회귀
    독립변수 - 연속형, 종속변수 - 연속형
    
    회귀분석은 각 데이터에 대한 잔차제곱합이 최소가 되는 선형회귀식을 도출하는 방법
'''
import statsmodels.api as sm
from sklearn.datasets import make_regression
import numpy as np

np.random.seed(8)

# 방법 1 : make_regression 이용, 모델이 만들어지지는 않음, 선형회귀 연습을 위한 데이터셋
x, y, coef = make_regression(n_samples=50, n_features=1, bias=100, coef=True) # 데이터수, 독립변수, 절편, 기울기
print(x[:5])  # x가 -0.67283393 일 때        샘플 독립변수 자료
print(y[:5])  # y가  99.40304252라는 것     샘플 종속변수 자료=모델에 의해 나온 예측값
print(coef)  # 0.8872285585150852       기울기
# y = wx + b 라고 할 때,  0.8872285585150852 * x + 100 = 99.40304252
yhat = 0.8872285585150852 * -0.67283393 + 100  #실제값
print('yhat :', yhat)

yhat = 0.8872285585150852 * 1.1395335 + 100
print('yhat :', yhat)

new_x = 0.5
pred_yhat = 0.8872285585150852 * new_x + 100
print('pred_yhat :', pred_yhat, '\n\n') #새로운 값 new_x에 대한 선형회귀 예측값
# 기존 데이터에 의해 만들어진 예측값과 실제값의 차이가 크지 않기 때문에 새로운 x에 대한 예측값을 신뢰할 수 있다고 본다.


# 방법 2 : LinearRegression() 이용, 모델이 생성됨
from sklearn.linear_model import LinearRegression
xx = x
yy = y
model = LinearRegression() # copy_X=True, fit_intercept 상수항을 결정짓는 값, n_jobs=None, normalize=False
print(model)
fit_model = model.fit(xx, yy) # fit()으로 데이터를 학습하여 최적의 모형(모델)을 추정함
print(fit_model.coef_)        # 기울기 0.88722856
print(fit_model.intercept_) # 절편  100.00000000000001

# 예측값 구하기1 - 수식을 직접 적용
new_x = 0.5
pred_yhat2 = fit_model.coef_ * new_x + fit_model.intercept_
print('pred_yhat2 :', pred_yhat2, '\n')

# 예측값 구하기 2 - predict()이용
new_x = 0.5
pred_yhat3 = fit_model.predict([[new_x]]) # 입력값이 2차원 데이터이기 때문에 
print('pred_yhat3 :', pred_yhat3, '\n')


x_new, _, _ = make_regression(n_samples=5, n_features=1, bias=100, coef=True)
print(x_new)
pred_yhat4 = fit_model.predict(x_new)
print('pred_yhat4 :', pred_yhat4, '\n\n')


# 방법 3 : ols()
import statsmodels.formula.api as smf
import pandas as pd
x1 = xx.flatten() # dataframe에 담기위해 차원 축소 [50, 1] -> (50, )
# print(x1, x1.shape)
y1 = yy

data = np.array([x1, y1])
df = pd.DataFrame(data).T
df.columns = ['x1', 'y1']
print(df.head(3))

model2 = smf.ols(formula='y1 ~ x1', data=df).fit()
print(model2.summary()) # OLS Regression Results, 절편Intercept=100, 기울기x1=0.8872
print(df[:5])
print(model2.predict()[:5]) # 기존 데이터에 대한 예측값

# 새로운 값에 대한 예측 결과
# print('x1 :', x1[:2]) #x1 : [-0.67283393  1.1395335 ]
newx = pd.DataFrame({'x1':[-0.760, 1.149, 0.5]})
predy = model2.predict(newx)
print('predy :\n', predy)
