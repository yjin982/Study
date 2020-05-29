import urllib.request, urllib.parse
from bs4 import BeautifulSoup as bs
import pandas as pd

url = 'http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp'
data = urllib.request.urlopen(url).read()
#print(data.decode('utf8')) #str

soup = bs(data, 'lxml')
#print(soup) #beautifulsoup 객체

title = soup.find('title').text
wf = soup.find('wf')
#<![CDATA[      ]]>
#CDATA 섹션 : Character Data'. 즉, '문자 데이터' 중  (Unparsed) Character Data'. 즉, '파싱하지 않는 문자 데이터(특수문자나 태그가 들어가 있어도 순수 데이터 인식하고 파싱하지 않음)
#print(title, wf)

city = soup.findAll('city')
cityDatas = []
for c in city:
    cityDatas.append(c.string)

df = pd.DataFrame()
df['city'] = cityDatas #city 컬럼 push

#tmef = soup.select_one('location > data > tmef ')
tmef = soup.select_one('location > province + city + data > tmef') #location 자식의 형제인 [province와 city와 data]의 직계 자식인 tmef

tempMins = soup.select('location > province + city + data > tmn') #첫번째 최저기온
tempDatas = []
for t in tempMins:
    tempDatas.append(t.text)
    
df['temp_min'] = tempDatas #최저기온 컬럼 push
df.columns = ['지역', '최저기온'] #컬럼 이름 바꿀려면

#파일로 저장
#df.to_csv('날씨.csv', index=False)

#슬라이싱 복습
print(df.head(3))
print(df[0:3])
print(df.tail(2))
print(df[-2:len(df)])


#DataFrame의 iloc
print(df.iloc[0], type(df.iloc[0])) #0행 Series타입
print(df.iloc[0:2], type(df.iloc[0:2, :])) #0행부터 2행전까지, 복수개일경우 dataframe타입
 
print(df.iloc[0:2, 0:1], type(df.iloc[0:2, 0:1])) #2행 1열만
print(df.iloc[0:2, 0:2], type(df.iloc[0:2, 0:2])) #2행 2열
 
print(df['지역'][0:3], type(df.지역[:3])) #컬럼명으로 3행까지, 타입은 series
print(df[:], df)
 
#DataFrame의 loc : 라벨값 기반
## iloc는 [0:3] -> 0~2행까지    /  loc는 [0:3] -> 0~3행까지
## 행 인덱스가 문자일 경우 df.loc['a':'c']한 것과 같기때문에 
print(df.loc[1:3]) #1행~3행
print(df.loc[[1, 3]]) #1행과 3행
print(df.loc[:, '지역']) #지역열의 전체행
 
print(df.loc[1:3, ['최저기온', '지역']]) #최저기온, 지역 열이면서 1~3행
print(df.loc[:, '지역'][1:4]) #지역열 전체 행 중에서 1~4행 전까지

print(df.info())
df = df.astype({'최저기온':int}) #칼럼 데이터 형식을 object에서 int로 바꿈
print(df.info())
print(df['최저기온'].mean())     #int로 바꿔서 평균
print(df['최저기온'].describe()) #기술통계 요약을 출력할 수 있음
  
print(df['최저기온'] >= 19)           #조건에 맞으면 True/아니면 False로 출력됨
print(df.loc[df['최저기온'] >= 19]) #조건에 맞는 행의 데이터만 출력
print(df.loc[(df['최저기온'] >= 18) & (df['최저기온'] < 19)]) #and 조건, or는 |
print(df.loc[df['최저기온'] >= 19, ['최저기온']][0:3]) #조건에 맞는 행 중에 컬럼은 최저기온만 0~2행만
print(df.sort_values(['최저기온'], ascending=True)) #데이터 정렬