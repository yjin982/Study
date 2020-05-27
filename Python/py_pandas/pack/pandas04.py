import pandas as pd
import numpy as np

''' 행열 이동 '''
from matplotlib.pyplot import axis
df = pd.DataFrame(1000+np.arange(6).reshape(2,3), index=['대전', '서울'], columns=['2017', '2018', '2019'])
print(df, '\n')

df_row = df.stack()          #인덱스를 기준으로 칼럼 쌓기(그룹화 시키기)
print(df_row, '\n')
df_col = df_row.unstack() #전치와 비슷하게 생각하면 쉬움(전치와는 다르지만)
print(df_col)


'''중복 제거'''
data = { 'data1': ['a'] *4, 'data2':[1,1,2,2] }
df2 = pd.DataFrame(data)
print(df2, '\n')

result = df2.drop_duplicates()
print(result)


''' 구간 단위 설정  : 연속 데이터 범주화 '''
price = [10.3, 5.5, 7.8, 3.6] #이 데이터를 범주화
cut = [3, 7, 9, 11]     #구간 기준값
result_cut = pd.cut(price, cut) #데이터, 구간을 줌
print(result_cut)
print(pd.value_counts(result_cut)) #구간별 데이터 갯수
#[(9, 11], (3, 7], (7, 9], (3, 7]] <- [10.3, 5.5, 7.8, 3.6]
#Categories (3, interval[int64]): [(3, 7] < (7, 9] < (9, 11]]
#(a, b]은 a < x <= b  /  a초과 b이하 == 괄호가 초과미만 대괄호가 이상이하

datas = pd.Series(np.arange(1, 1001)) #데이터가 1~1000
result_cut2 = pd.qcut(datas, 3) #데이터에 대해서 구간의 갯수를 주고 자동으로 구간 설정
print(result_cut2)
#Categories (3, interval[float64]): [(0.999, 334.0] < (334.0, 667.0] < (667.0, 1000.0]]
print(pd.value_counts(result_cut2))


''' 자료 합치기(dataFrame 병합) '''
df1 = pd.DataFrame({'data1':range(7), 'key':['b', 'b', 'a', 'c', 'a', 'a', 'b']})
df2 = pd.DataFrame({'key':['a', 'b', 'd'], 'data2':range(3)})  #df1에는 d가 없고 df2에는 c가 없는 상황
print(pd.merge(df1, df2, on='key', how='inner')) #on에 있는 공통칼럼을 기준으로 merge, Sql에서 inner join과 같은 상황(=default이므로 on과 how없어도 동일한 결과)
print(pd.merge(df1, df2, on='key', how='outer')) #Sql에 비교화면 full outer join
print(pd.merge(df1, df2, on='key', how='left'))
print(pd.merge(df1, df2, on='key', how='right'))

# - 공통칼럼이 없는 경우 merge BUT 자료의 성격은 동일해야 함
df3 = pd.DataFrame({'key2':['a', 'b', 'd'], 'data2':range(3)}) #df1과 공통 칼럼이 없음
print(pd.merge(df1, df3, left_on='key', right_on='key2'))

#merge와 다름, 단순히 이어붙이기
print(pd.concat([df1, df2]))            #기본 : 열단위
print(pd.concat([df1, df2], axis=1)) #행단위

#np의 array 자료 이어붙이기
arr1 = np.arange(6).reshape(2, 3)
arr2 = np.arange(4, 10).reshape(2, 3)
arrs1 = np.concatenate([arr1, arr2])
print(arrs1)
arrs2 = np.concatenate([arr1, arr2], axis=1)
print(arrs2)
