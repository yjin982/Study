''' 위키피디아 자료 읽기 '''
import urllib.request as req
from bs4 import BeautifulSoup

url = 'https://ko.wikipedia.org/wiki/%EC%9D%BC%EB%B0%98%EC%83%81%EB%8C%80%EB%A1%A0_%EA%B0%9C%EB%A1%A0'
wiki = req.urlopen(url)
soup = BeautifulSoup(wiki, 'lxml')
##mw-content-text > div > p:nth-child(3)
#print(soup.select('#mw-content-text > div > p'))

newsurl = 'https://news.v.daum.net/v/20200528030102663'
news = req.urlopen(newsurl)
soup2 = BeautifulSoup(news, 'lxml')
print(soup2.select_one('div#kakaoIndex > a').text)

datas = soup2.select('div#kakaoIndex > a')
for i in datas:
    href = i.attrs['href']
    text = i.string
    print('href : {},  text : {}'.format(href, text))
print()


#find메소드로 가져오기
datas2 = soup2.findAll('a')
for i in datas2[:2]: #앞에서부터 2개만 가져오기
    text = i.string
    print(text)

##harmonyContainer > section > p:nth-child(4)
datas3 = soup2.select('#harmonyContainer > section > p')
for i in datas3[2:5]:
    print(i.string)

