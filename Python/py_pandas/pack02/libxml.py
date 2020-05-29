'''  웹에서 제공되는  xml 도서관 휴관일 정보 읽어오기   '''
import urllib.request as req
from bs4 import BeautifulSoup as bs
from future.backports.urllib.request import urlopen

url = 'http://openapi.seoul.go.kr:8088/sample/xml/SeoulLibraryTime/1/5/'
plainText = req.urlopen(url).read().decode()
xmlObj = bs(plainText, 'lxml')
libData = xmlObj.select('row')

for data in libData:
    name = data.find('lbrry_name').text
    addr = data.find('adres').text
    tel = data.find('tel_no').text
    print('도서관명 :', name)
    print('주소 :', addr)
    print('전화 :', tel, '\n')