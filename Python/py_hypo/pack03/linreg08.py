'''
회귀분석 문제 2) 
github.com/pykwon/python에 저장된 student.csv 파일을 이용하여 세 과목 점수에 대한 회귀분석 모델을 만든다. 
이 회귀문제 모델을 이용하여 아래의 문제를 해결하시오.
  - 국어 점수를 입력하면 수학 점수 예측
  - 국어, 영어 점수를 입력하면 수학 점수 예측
'''
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression
 
score = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/student.csv')
# print(score)

# temp = LinearRegression().fit(score.국어, score.수학)
# print(temp) 

kmmodel = smf.ols(formula='수학 ~ 국어', data=score).fit()
print(kmmodel.summary().tables[1])

yhat1 =  0.5705 * 90 + 32.1069
print(yhat1)
yhat2 =  0.5705 * 80 + 32.1069
print(yhat2)


new_kor = {'국어':[90, 80]}
pred_math = kmmodel.predict(new_kor)
print(score.국어.values[:8])
print(score.수학.values[:8])
print(np.round(pred_math.values))
print(kmmodel.summary().tables[0])
print('==' * 40)
print()




print('\n\n')
print('==' * 40)
kemmodel = smf.ols(formula='수학 ~ 국어 + 영어', data=score).fit()
print(kemmodel.summary().tables[1])

new_ke = {'국어':[90, 80], '영어':[70, 80]}
pred_math2 = kemmodel.predict(new_ke)
print(score.국어.values[:8])
print(score.영어.values[:8])
print(score.수학.values[:8])
print(np.round(pred_math.values))

yhat3 =  0.1158 * 90  + 0.5942 * 70 + 22.6238
print(yhat3)
yhat4 =  0.1158 * 80  + 0.5942 * 80 + 22.6238
print(yhat4)
print(kemmodel.summary().tables[0])


'''
회귀분석 문제 3) 
원격 DB의 jikwon 테이블에서 근무년수에 대한 연봉을 이용하여 회귀분석 모델을 작성하시오.
장고로 작성한 웹에서 근무년수를 입력하면 예상연봉이 나올 수 있도록 프로그래밍 하시오.
'''
print('\n\n\n\n\n')
import MySQLdb
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}
conn = MySQLdb.connect(**config)
sql = 'select timestampdiff(YEAR, jikwon_ibsail, now()) as gunmu, jikwon_pay from jikwon'
jik_data = pd.read_sql(sql, conn)

jikmodel = smf.ols(formula='jikwon_pay ~ gunmu', data=jik_data).fit()
print(jikmodel.summary())
new_pay = {'gunmu':[13, 10, 7]}
pred_jik = jikmodel.predict(new_pay)
print(jik_data.gunmu.values[:5])
print(jik_data.jikwon_pay.values[:5])
print(np.round(pred_jik.values))