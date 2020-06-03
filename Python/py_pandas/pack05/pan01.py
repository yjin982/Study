'''
    교차 테이블 작성
      행과 열로 구성되는 교차표. 변수들간에 유의미한 차이 파악이 용이하다.
      범주형데이터 이어야 함
'''
import pandas as pd

ytrue = pd.Series([2, 0, 2, 2, 0, 1, 1, 1, 1, 2])
ypred = pd.Series([2, 1, 1, 2, 0, 1, 0, 1, 0, 0])

kai = pd.crosstab(ytrue, ypred, rownames=['True'], colnames=['Pred'], margins=True)
print(kai)
print('예측 정확도 : ', (1+2+2) / 10)
print()


#descriptive 읽어서 
des = pd.read_csv('../testdata/descriptive.csv') #거주지역을 숫자로 저장한 데이터
data = des[['resident', 'gender', 'level', 'pass']]  #범주형만 꺼내기
table = pd.crosstab(data.resident, data.gender)
print(table)

table2 = pd.crosstab([data.resident, data.gender], data.level)
print(table2)