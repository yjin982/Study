'''  네이버 영화에서 영화 순위 읽기  '''
'''  방법 1   '''
import urllib.request
from bs4 import BeautifulSoup as bs
url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
data = urllib.request.urlopen(url).read()
soup = bs(data, 'lxml')

##old_content > table > tbody > tr:nth-child(2) > td.title > div > a
# title = soup.select('div.tit3') 
# title = soup.select('div[class=tit3]') #또는 가독성을 높이기 위해서 이와 같이 써도 됨
# for tag in soup.select('div[class=tit3]'):
#     print(tag.text.strip())


'''  방법 2   '''
import requests   #읽으면서 정보를 읽고 싶을때, 근데 조심해야함
# data = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
# print(data.status_code, '   ', data.encoding) #200     MS949
# datas = data.text
# print(datas)

data = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.nhn").text
soup = bs(data, 'lxml')
# for tag in soup.findAll('div', 'tit3'):
#     #print(tag.text.strip())
#     print(tag.text[tag.find('"'):tag.find('"')].strip())

m_list = soup.findAll('div', {'class':'tit3'}) #또는 이렇게
# for i in m_list:
#     title = i.findAll('a')
#     print(str(title)[str(title).find('title="')+7:str(title).find('">')])


#참고
title = 'abcdefg'
print(title[title.find('b'):title.find('f')])

#순위 표시
count = 1
for i in m_list:
    title = i.find('a')
    print(str(count) + '위 : ' + title.string.strip())
    count += 1