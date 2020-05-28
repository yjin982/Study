''' bbq 홈페이지 자료 읽고 메뉴와 가격출력.  가격의 평균, 표준편차 구하기'''
import urllib.request as req
from bs4 import BeautifulSoup as bs

bbqurl = 'https://www.bbq.co.kr/menu/menuList.asp'
bbq = req.urlopen(bbqurl)

soup = bs(bbq, 'lxml')

#메뉴명의 셀렉터
#body > div.wrapper.scrolled > div.container > article > section > div.section-body > div > div:nth-child(37) > div.info > p.name
#메뉴 가격 셀렉터
#body > div.wrapper.scrolled > div.container > article > section > div.section-body > div > div:nth-child(37) > div.info > p.pay 

data1 = soup.select('div.box > div.info > p.name') #메뉴명
data2 = soup.select('div.box > div.info > p.pay')   #가격

name = []
pay = []

for i in data1:
    name.append(i.text)
    
for i in data2:
    pay.append(int(i.text.replace(',', '').replace('원', ''))) #가격에서 쉼표와 원을 빼고 숫자형으로 바꾸기

print(name)
print(pay)
data = {'name':name, 'pay':pay}

from pandas import DataFrame
df = DataFrame(data)
print(df)



### info 태그를 가지고 와서 돌리는 방법도 가능(info 안에 이름과 가격이 같이 들어있으므로)
bbqurl = 'https://www.bbq.co.kr/menu/menuList.asp'
bbq = req.urlopen(bbqurl)
soup2 = bs(bbq, 'lxml')
datas = []
info = soup2.select('div.info')


for i in info:
    tempPrice = i.select('p.pay')[0].text
    price = ''
    for j in tempPrice: #19,000원
        try:
            int(j)
            price += j  # 1    19    190    1900    ...
            #print(price)
        except:
            pass
    datas += [[i.select('p.name')[0].text, int(price)]]
    
df2 = DataFrame(datas, columns=['메뉴', '가격'])
print(df2)


print('가격 평균 : ', df2['가격'].mean())
print('가격 표준편차 : ', df2['가격'].std())