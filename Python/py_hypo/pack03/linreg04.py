'''
    아이리스 데이터로 선형회귀 연습
'''
import pandas as pd
import statsmodels.formula.api as smf
from matplotlib.pylab import plt
import seaborn as sns

iris = sns.load_dataset('iris')
print(iris.head(2))
print(iris.corr())


# 단순 선형회귀 모델 작성  sepal_length와 sepal_width : (r - -0.117570)
result = smf.ols(formula='sepal_length ~ sepal_width', data=iris).fit()
print(result.summary())
# P>|t| : 0.152 > 0.05 독립변수로써 부적절, Prob (F-statistic):  0.152 > 0.05 모델도 부적절,  R-squared:  0.014 < 0.49 설명력이 좋지 않다.
print('결정계수 :', result.rsquared)
print('p value :', result.pvalues[1])


print()
result2 = smf.ols(formula='petal_length ~ petal_width', data=iris).fit()
print(result2.summary())
# P>|t| : 0 < 0.05 독립변수로써 적절, Prob (F-statistic):  4.68e-86 < 0.05 모델도 적절,  R-squared:  0.927 > 0.49 설명력이 좋다.
print('결정계수 :', result2.rsquared)
print('p value :', result2.pvalues[1])

print('\n\n')
print('실제값 :', iris.petal_length[0], ', 예측값 :', result2.predict()[0]) # 실제값 : 1.4 , 예측값 : 1.529546131874886


# 새로운 데이터(petal_width)로 petal_length를 예측
new_data = pd.DataFrame({'petal_width':[0.2, 1.2, 2.1]})
y_pred = result2.predict(new_data)
print(iris.head(3)['petal_length'])
print(y_pred)
print('\n\n')


# 다중 선형 회귀모델 작성
result3 = smf.ols(formula='sepal_length ~ petal_length + sepal_width + petal_width', data=iris).fit()
print(result3.summary())
# P>|t| : 0 < 0.05 다른 독립변수와 같이 있으면 서로 영향을 주어서 단독일때와 다를 수 있음 -> 독립 변수를 어떤 것을 쓰냐에 따라서 결과가 판이하게 바뀔 수도 있다 -> 그래서 차원축소 등 방법 실행
# Prob (F-statistic):  8.59e-62 < 0.05 모델 적절,  R-squared:  0.859 > 0.49 설명력이 좋음.
print('결정계수 :', result3.rsquared)
print('p value :\n', result3.pvalues)



print()
# ※독립변수가 너무 많을 때
col_selected = '+'.join(iris.columns.difference(['sepal_length', 'species'])) # 빼고 싶은 이름만 적어서
print(col_selected)
formula = 'sepal_length ~ ' + col_selected # R 이라면 sepal_length ~ . 이렇게 했던거 
result4 = smf.ols(formula=formula, data=iris).fit()
# print(result4.summary())