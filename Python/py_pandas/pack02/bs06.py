''' 웹문서 일부 읽은 후 파일로 저장 '''
from bs4 import BeautifulSoup as bs
import urllib.request as req
import datetime

url = 'https://finance.naver.com/marketindex/'
findata = req.urlopen(url).read()
soup = bs(findata, 'lxml')

##exchangeList > li.on > a.head.usd > div > span.value
price = soup.select_one('div.head_info > span.value').text
print('미국 환율 :', price)

t = datetime.datetime.now()

fname = t.strftime('%Y-%m-%d_%H-%M-%S') + '.txt'
print(fname)

with open(fname, 'w', encoding='utf8') as f:
    f.write(price)