'''
멀티 프로세싱을 통한 웹 스크랩핑 : multiprocessing X
(스크랩핑:1번만 긁어옴, 크롤링:주기적으로 긁어옴)
'''
from bs4 import BeautifulSoup as bs
import time, requests

def get_link():
    #req = requests.get("https://beomi.github.io/beomi.github.io_old/") #보안문제로 다른걸로써야함
    html = req.text
    print(html)
    soup = bs(html, 'html.parser')
    
get_link()