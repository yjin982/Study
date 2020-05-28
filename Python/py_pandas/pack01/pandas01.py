'''
    pandas module : 고수준의 자료구조(Series, DataFrame)을 지원
'''
from pandas import Series
import numpy as np

obj = Series([3, 7, -5, 4])
obj = Series((3, 7, -5, 4))
#obj = Series{(3, 7, -5, 4)} #error, set 타입 X
print(obj, type(obj), '\n')

obj2 = Series([3, 7, -5, 4], index=['a', 'b', 'c', 'd'])
print(obj2, type(obj2), '\n')
print(obj2.sum(), 'numpy기반 pandas sum, ', sum(obj2), '파이썬 기반 sum, ', np.sum(obj2), 'numpy sum')
print(obj2.mean(), obj2.std())
print()

print('배열값 출력 :', obj2.values)
print('색인          :', obj2.index, '\n')


'''슬라이싱'''
print(obj2['a'], ' ', obj2[0])      #값만
print(obj2[['a']], ' ', obj2[[0]]) #색인과 값
print()

print(obj2[['a', 'b']], '\n', obj2['a':'c'], '..')
print(obj2[2], '\n', obj2[2:4], '..')
print(obj2[[2, 1]])
print(obj2 > 0)
print('a' in obj2)
print('k' in obj2)
print()


'''dict'''
names = {'mouse':5000, 'keyboard':350000, 'monitor':550000}
print(names, type(names))
obj3 = Series(names)
print(obj3) #key가 인덱스명으로

obj3.index = ['마우스', '키보드', '모니터']
print(obj3)

obj3.name = '상품가격'
print(obj3)
print()


'''DataFrame'''
from pandas import DataFrame
df = DataFrame(obj3)
print(df, type(df), '\n') #name이 df에서 칼럼명으로 감

data = {
    'name':['서새봄', '원소풍', '이초홍', '김점례', '정강지'],
    'addr':('역삼동', '신길동', '역삼동', '역삼동', '서초동'),
    'age':(23, 25, 33, 20, 26),
}
print(data, type(data))

frame = DataFrame(data)
print(frame, type(frame))
print(frame['name'], ' \n', frame.name, type(frame.name)) #<class 'pandas.core.series.Series'>
print(DataFrame(data, columns=['addr', 'name', 'age']))
print()

frame2 = DataFrame(data, columns=['name', 'addr', 'age', 'tel'], index=['a', 'b', 'c', 'd', 'e'])
print(frame2) #tel은 결측치
frame2['tel'] = '111-1111'
print(frame2) #전체 tel이 바뀜

val = Series(['222-2222', '333-3333', '444-4444'], index=['b', 'c', 'e'])
frame2.tel = val #인덱스가 b, c, e인 값에 대해서만 시리즈데이터 형태를 이용해서 덮어쓰기
print(frame2)
print(frame2.T)        #전치
print(frame2.values) #matrix( [[]] 형태 )로 반환
#분류나 데이터 처리시에는 array로 하니까 dataframe으로 넣고 array로 바꿔서 처리하기도 가능
print(frame2.values[0, 1], frame2.values[0:1])
print()

# frame3 = frame2.drop('d') #d행을 삭제한 값을 줌
frame3 = frame2.drop('d', axis=0)
print(frame3)
frame4 = frame2.drop('tel', axis=1) #열삭제
print(frame4)
print()

print(frame3.sort_index(axis=0, ascending=False)) #행단위  sort
print(frame3.sort_index(axis=1, ascending=True))  #열단위  sort
print(frame3.rank(axis=0)) #사전순으로 가장 빠른 것이 1
print()

print(frame3.addr.value_counts()) #== frame3['addr'].value_counts()
print()

#문자열자르기
data = {
    'addr':['강남구 역삼동', '중구 신당동', '강남구 대치동'],
    'personcount':[23, 25, 15],
}
frame = DataFrame(data)
print(frame)
result1 = Series([x.split()[0] for x in frame.addr])
result2 = Series((x.split()[0] for x in frame.addr))
print('- 주소에서 구만 잘라서 반환\n', result1)
print('- 주소에서 구만 잘라서 튜플로 반환\n', result2)
print('- count -\n', result2.value_counts())
print()