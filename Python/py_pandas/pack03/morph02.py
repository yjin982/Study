'''
    웹 문서를 읽어 형태소 분석
'''
import urllib
from bs4 import BeautifulSoup as bs
from konlpy.tag import Okt


okt = Okt()

#url = 'https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0' #wiki/이순신   이면 에러, 인코딩을 해줘야함
#검색단어를 입력받았다고 한다면 
#para = '이순신' #인코딩을 해야하니 이렇게 하지 말고
para = urllib.parse.quote('이순신')
url = 'https://ko.wikipedia.org/wiki/' + para
page = urllib.request.urlopen(url)
soup = bs(page.read(), 'lxml')
 
#셀렉터 #mw-content-text > div > p:nth-child(7)
wordlist = [] #명사들을 기억
for item in soup.select('#mw-content-text > div > p'):
    if item.string != None:
        #print(item.string.strip())
        temp = item.string
        wordlist += okt.nouns(temp)
 
print(wordlist)
print('wordlist 단어 수 : ', str(len(wordlist)), '\n')
 
 
 
wordDict = {} #단어의 발생 횟수 저장
for i in wordlist:
    if i in wordDict:
        wordDict[i] += 1
    else:
        wordDict[i] = 1
         
print(wordDict, '\n')
 
 
#중복은 배제하고 단어 보기 - set에 넣었다 빼기
setData = set(wordlist)
print('중복 없이 단어 보기 : ', setData)
print('단어 수 : ', len(setData), '\n')
 
 
#추가 분석을 하기 위해서는 pandas에 담기
import pandas as pd
wordlist_pd = pd.Series(wordlist)
print(wordlist_pd[:3])
print(wordlist_pd.value_counts()[:5], '\n')
 
wordDict_pd = pd.Series(wordDict)
print(wordDict_pd[:3])
print(wordDict_pd.value_counts()[:5], '\n')
 
 
#dataFrame
df1 = pd.DataFrame(wordlist, columns=['단어'])
print(df1.head(6), '\n')
 
df2 = pd.DataFrame([wordDict.keys(), wordDict.values()])
df2 = df2.T
df2.columns = ['단어', '빈도수']
print(df2.head(6), '\n')
print(df2.info(), '\n')
 
#file로 저장
df2.to_csv('이순신.csv', sep=',', index=False)
#file읽기
df3 = pd.read_csv('이순신.csv')
print(df3.head(3))
        