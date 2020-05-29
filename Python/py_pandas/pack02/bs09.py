''' 구글 검색 기능을 이용해 검색 결과(a 태그)의 갯수만큼 브라우저로 출력 '''
import requests
from bs4 import BeautifulSoup as bs
import webbrowser

def searchFunc(e):
    base_url = 'https://www.google.com/search?q={0}'
    searchWord = base_url.format(e)
    print(searchWord)
    plain_text = requests.get(searchWord, headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'})
    print(plain_text)
    
    soup = bs(plain_text.text, 'lxml')
    link_data = soup.select('div > div.r > a')
    
    for link in link_data[:3]:
        #print(link)
        #print(str(link).find('https'), ' ', str(link).find('onmousedown') - 2)
        urls = str(link)[str(link).find('https'):str(link).find('onmousedown')-2]
        print(urls)
        
        webbrowser.open(urls) #브라우저로 출력

search = input()
searchFunc(search)

#'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}