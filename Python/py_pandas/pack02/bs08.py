''' 네이버 급상승 인기 검색어 안 읽히는 버전 '''
import requests
import urllib.request as req
from bs4 import BeautifulSoup as bs

class goNaver():
    def starts(self):
        url = 'https://datalab.naver.com/keyword/realtimeList.naver?age=all'
        page = requests.get(url, headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'})
        soup = bs(page.text, 'lxml')
        #print(soup)   #<title>[접근 오류] 서비스에 접속할 수 없습니다.</title>
        #headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}
        #를 붙여줘야 제대로 읽어올 수 있음
        
        ##content > div > div.selection_area > div.selection_content > div.field_list > div > div > ul:nth-child(1) > li:nth-child(1) > div > span.item_title_wrap > span
        title = soup.select('span.item_title')
        print('네이버 실시간 검색어')
        count = 0
        for i in title:
            count += 1
            print(str(count) + ") " + i.string)
        
        
    def tes(self): #이거도 여전히 안됨
        url = 'https://datalab.naver.com/keyword/realtimeList.naver?age=all'
        datas = req.urlopen(url).read()
        soup = bs(datas, 'lxml')
        print(soup)


if __name__ == '__main__':
    goNaver().starts()
