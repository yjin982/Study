'''
    pandas의 기능
'''
from pandas import Series, DataFrame

'''재 색인 '''
data = Series(['가', '다', '나'], index=(1, 4, 2)); print(data)
data2 = data.reindex((1, 2, 4)); print(data2) #'가 다 나' 로 나오던 것이 '가 나 다'로 

'''재 색인 하면서 값 채우기'''
data3 = data2.reindex((1, 2, 3, 4, 5)); print(data3) #3과 5에 대해서 결측값(NaN)이 생김

data3 = data2.reindex((1, 2, 3, 4, 5), fill_value='힣'); print(data3)
print('-' * 20)
data3 = data2.reindex((1, 2, 3, 4, 5), method='ffill'); print(data3) #fffill == pad
data3 = data2.reindex((1, 2, 3, 4, 5), method='pad'); print(data3) #NaN값을 NaN있던 곳의 앞의 값으로 채움
print('-' * 20)
data3 = data2.reindex((1, 2, 3, 4, 5), method='bfill'); print(data3)     #NaN값을 NaN있던 곳의 다음의 값으로 채움
data3 = data2.reindex((1, 2, 3, 4, 5), method='backfill'); print(data3) #그래서 5의 값은 그 다음값이 없기때문에 NaN이 됨
print('-' * 20, '\n')

'''boolean 처리'''
import numpy as np
df = DataFrame(np.arange(12).reshape(4,3), index=['1월', '2월', '3월', '4월'], columns=['서울', '대전', '대구'])
print(df)
print(df['서울'] > 3)      #서울 열에서 3보다 큰 값에 대해서 True/False
print(df[df['서울'] > 3]) #
print()

print(df < 3) #전체 자료가 TorF로 출력
df[df < 3] = 0 #3보다 작은 값을 0으로 채우고 df로 출력
print(df)
print('-'  * 20, '\n\n')


'''
DataFrame 슬라이싱 관련 메소드
loc : 라벨 지원, iloc : 숫자 지원
'''
print(df.loc['3월'])  #3월 행 모든 열 --> ['3월', :]와 같은 의미
print(df.loc[:'2월']) #2월행 이하 출력
print(df.loc[:'2월', ['대전', '서울']]) #2월행 이하, 대전,서울열
print()

print(df.iloc[2])         #같은 의미 --> [2, :]
print(df.iloc[:3])        #3행 미만
print(df.iloc[:3, 2])    #3행 미만이면서 2열
print(df.iloc[:3, 1:3]) #3행 미만이면서 1이상 3미만열
print('-' * 20)

'''산술연산'''
s1 = Series((1, 2, 3), index=['a', 'b', 'c'])
s2 = Series((4, 5, 6, 7), index=['a', 'b', 'd', 'c'])
print(s1, '\n', s2)

print(s1 + s2) # --> s1.add(s2), numpy함수 계승, 같은 인덱스명끼리 계산이라 d는 NaN
#print(s1 * s2) #다른 연산도 동일

df1 = DataFrame(np.arange(9.).reshape(3, 3), columns=list('xyz'), index=['서울', '인천', '수원'])
print(df1)
df2 = DataFrame(np.arange(12.).reshape(4, 3), columns=list('xyz'), index=['서울', '인천', '가평', '수원'])
print(df2)
print()

print(df1 + df2) # -> df1.add(df2) but add는 NaN처리 가능 
print(df1.add(df2, fill_value=0))
print(df1.mul(df2, fill_value=0)) #다른 사칙 연산도 동일
print()

seri = df1.iloc[0]
print(seri)
print(df1 - seri) #dataframe과 series간에도 연산이 가능
