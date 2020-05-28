import numpy as np
import pandas as pd

data = {
    'city':['뉴욕', '서울', '뉴욕', '서울'], 
    'year':[2010, 2011, 2012, 2012], 
    'pop':[3.3, 2.5, 3.0, 2.0]
}
df = pd.DataFrame(data)

''' 행/열 별 연산 '''
print(df.pivot('city', 'year', 'pop')) #pivot(행, 열, 계산칼럼)
#또는
print(df.set_index(['city', 'year']).unstack()) #잘쓰지는 않음


''' 그룹화 '''
sums = df.groupby(['city']) #city기준으로 다른 칼럼을 그룹화 
print(sums.sum())             #해서 합
print(df.groupby(['city']).sum()) #간단히 한줄로
print(df.groupby(['city', 'year']).mean()) #두 컬럼을 기준으로 평균값


''' 피벗 테이블 '''
print(df.pivot_table(index=['city'])) #city별 pop과 year에 대한 평균, aggfunc=np.mean 옵션 준것과 동일(aggfun는 평균(mean)이 default)
print(df.pivot_table(index=['city', 'year'], aggfunc=np.mean))
print(df.pivot_table(index=['city', 'year'], aggfunc=[len, np.mean])) #길이와 평균 둘다 구할 경우 (함수줄때 괄호 없어야 함)

print(df.pivot_table(values=['pop'], index=['city']))       #city별 pop에 대한 평균, values 옵션은 values= 를 안써도 괜찮
print(df.pivot_table(['pop'], index='city', aggfunc=len)) #city별 pop에 대한 건수
print(df.pivot_table(['pop'], index='year', columns='city')) #행은 year
print(df.pivot_table(['pop'], index='year', columns='city', margins=True)) #소계
print(df.pivot_table(['pop'], index='year', columns='city', margins=True, fill_value=0)) #NaN처리
