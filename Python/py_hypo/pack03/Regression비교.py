'''
    Advertising.csv로 Regressor 정량적 예측모델 비교
'''
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRFRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

adver = pd.read_csv('../testdata/Advertising.csv')
print(adver.head(3))
x = np.array(adver.loc[:, 'tv':'newspaper'])
y = np.array(adver.sales)

print('\nKNeighborsRegressor')
kmodel = KNeighborsRegressor(n_neighbors=3).fit(x, y)
kpred = kmodel.predict(x)
print('k pred :', kpred[:5])
print('k r2   : {:.3f}'.format(r2_score(y, kpred)))


print('\nLinearRegression')
lmodel = LinearRegression().fit(x, y)
lpred = lmodel.predict(x)
print('l pred :', lpred[:5])
print('l r2   : {:.3f}'.format(r2_score(y, lpred)))


print('\nRandomForestRegressor')  # 배깅에 대표적인 모델
rmodel = RandomForestRegressor(n_estimators=100, criterion='mse').fit(x, y)
rpred = rmodel.predict(x)
print('r pred :', rpred[:5])
print('r r2   : {:.3f}'.format(r2_score(y, rpred)))


print('\nXGBRFRegressor')   # 부스팅에 대표적인 모델
xmodel = XGBRFRegressor(n_estimators=100).fit(x, y)
xpred = xmodel.predict(x)
print('x pred :', rpred[:5])
print('x r2   : {:.3f}'.format(r2_score(y, xpred)))
