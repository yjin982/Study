import pandas as pd

''' 파일 읽기  csv '''
from pandas.tests.frame.test_sort_values_level_as_str import ascending
df = pd.read_csv('../testdata/ex1.csv')
#print(df, type(df)) #pandas로 읽으면 기본이 DataFrame

df = pd.read_table('../testdata/ex1.csv', sep=',') #table일 경우 sep = 구분자 필요
#print(df)

df = pd.read_csv('../testdata/ex2.csv', header=None) #헤더 없이 데이터만 있는 경우 
#print(df)

df = pd.read_csv('../testdata/ex2.csv', header=None, names=['a', 'b', 'c', 'd', 'e']) #내가 column에 이름 주기, 오른쪽부터 채워짐, 컬럼 갯수보다 더 주면 컬럼이 더 생기면서 값이 NaN으로 채워짐 
#print(df)

df = pd.read_csv('../testdata/ex2.csv', header=None, names=['a', 'b', 'c', 'd', 'e'], index_col='e') #컬럼을 인덱스로 줄 수 있다 
#print(df)


''' 파일 읽기 txt '''
df = pd.read_table('../testdata/ex3.txt')
#print(df)
df = pd.read_csv('../testdata/ex3.txt') #csv로 읽어오기도 가능
#print(df)

df = pd.read_csv('../testdata/ex3.txt', sep='\s+', skiprows=[1, 3]) #1과 3행은 빼고 구분자를 정규표현식으로
#print(df)

#구분자가 없어서 글자수,간격으로 끊기
df2 = pd.read_fwf('../testdata/data_fwt.txt', widths=(10, 3, 5), names=('날짜', '기업명', '주식'), encoding='utf8') #10자 3자 5자로 자르기
#print(df2)


''' chunk : 파일이 너무 커서 한꺼번에 못 읽어서 임의의 크기별로 읽기(대용량의 파일인 경우에 원하는 크기만큼 할당해서 읽기)'''
datas = pd.read_csv('../testdata/data_csv2.csv', header=None, chunksize=3) 
#print(datas) #chunk를 사용할 경우 TextFileReader object으로 받아옴

for p in datas:
    #print(p)
    print(p.sort_values(by=2, ascending=True)) #칼럼명 2 로 정렬해서 3개씩 출력 