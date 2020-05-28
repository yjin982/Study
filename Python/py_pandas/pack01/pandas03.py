'''
Pandas : NaN
'''
from pandas import Series, DataFrame
import numpy as np

df = DataFrame([[1.4, np.nan], [7, -4.5], [np.NaN, np.NAN], [0.5, -1]], columns=['1st', '2nd'])
print(df, '\n') #NaN(결측값)
print(df.drop(1))                      #1행 삭제
print(df.dropna())                    #NaN이 하나라도 포함된 행 삭제 (같은의미 => df.dropna(how='any')) 
print(df.dropna(how='all'))       #모두 결측치인 행 삭제
print(df.dropna(subset=['1st']))#칼럼명이  1st열에서 NaN이 있으면 그 행을 삭제
print(df.fillna(0))   #NaN을 0으로 채우기, 평균으로 채우기는 sklearn 모듈의 SimpleInputer를 이용

'''
기술적 통계와 관련된 함수
axis=1은 행, axis=0은 열
'''
print(df.sum())            #NaN은 연산에서 제외, 열의 합 (같은의미 =>df.sum(axis=0))
print(df.sum(axis=1))   #행의 합, NaN끼리의 연산은 0으로 처리
print(df.mean(axis=1)) #행의 평균 (같은 의미 =>df.mean(axis=1, skipna=True), Na빼고 구하려면 skipna를 False로 처리

#최대값
print(df.max())     # => axis=0
print(df.idxmax()) #최대값을 가진 인덱스를 반환
print(df.idxmin()) #최소값도 동일

#요약통계량
print(df.describe())
'''
            1st       2nd
count  3.000000  2.000000
mean   2.966667 -2.750000
std    3.521837  2.474874
min    0.500000 -4.500000
25%    0.950000 -3.625000
50%    1.400000 -2.750000
75%    4.200000 -1.875000
max    7.000000 -1.000000
'''

#구조 
print(df.info()) 
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   1st     3 non-null      float64
 1   2nd     2 non-null      float64
dtypes: float64(2)
memory usage: 192.0 bytes
None
'''

words = Series(['봄', '여름'])
print(words.describe()) #Series는 info가 없음
'''
count      2
unique     2
top       여름
freq       1
dtype: object
'''
