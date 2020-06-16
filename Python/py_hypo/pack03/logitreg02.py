'''
    날씨 정보 자료를 이용해 날씨 예보(내일 비 유무)
'''
import pandas as pd
from sklearn.model_selection._split import train_test_split
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
from nltk.chunk.util import accuracy
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)

data = pd.read_csv('../testdata/weather.csv')  # RainTomorrow 종속, yes/no를 숫자로 변경시켜야함.   나머지열 독립
# print(data)  # (366, 12)
data2 = pd.DataFrame()
data2 = data.drop(['Date', 'RainToday'], axis=1) # 제외할 칼럼
data2.RainTomorrow = data2.RainTomorrow.map({'Yes':1, 'No':0})
print(data2)

# train / test dataset으로 분리 (overfitting 과적합 방지)
train, test = train_test_split(data2, test_size=0.3, random_state=52)  #random_state == random.seed()
print(data2.shape, train.shape, test.shape) # (366, 10) (256, 10) (110, 10)


# 분류 모델
col_select = " + ".join(train.columns.difference(['RainTomorrow']))
my_formula = 'RainTomorrow ~ ' + col_select
# model = smf.glm(formula=my_formula, data=train, family=sm.families.Binomial()).fit()  # 분류를 위한 학습모델 생성
model = smf.logit(formula=my_formula, data=train).fit()

print(model.summary())  # P>|z| 0.05보다 큰 변수들은 독립변수로서 부적절하다고 볼 수 있다.
# print(model.params.values)
print('예측값  :', np.rint(model.predict(test)[:10].values))
print('실제값  :', test.RainTomorrow[:10].values)


# 분류 정확도  
from sklearn.metrics import accuracy_score
pred = model.predict(test)
print('분류 정확도 :', accuracy_score(test.RainTomorrow, np.around(pred)))  #0.8454545454545455

# ※ 'GLMResults' object has no attribute 'pred_tables'
conf_mat = model.pred_table()
print(conf_mat)
print('정확도 :', (conf_mat[0][0] + conf_mat[1][1]) / len(train))


