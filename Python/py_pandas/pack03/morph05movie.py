''' 
    네이버 영화 네티즌 평점 자료로 영화 간 유사도 출력 
'''
from bs4 import BeautifulSoup as bs
import requests
from konlpy.tag import Okt
from collections import Counter
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer #

def movie_scrap(url):
    result = []
    for p in range(1, 11): # 1~10 페이지까지 읽기
        r = requests.get(url + '&page=' + str(p))
        soup = bs(r.content, 'lxml', from_encoding='ms949')
        title = soup.findAll('td', {'class':'title'})
        #print(title)
        sub_result = []
        for i in range(len(title)):#의미가 없는 단어들 제외시키기
            sub_result.append(title[i].text
                              .replace('\n', '').replace('\t', '').replace('신고', '').replace('-', '').replace('?', '').replace('.', '')
                              .replace('헝거게임 : 더 파이널', '').replace('해빙', '').replace('언더워터', '').replace('날씨의 아이', '').replace('고양이의 보은', '')
                              .replace('별점  총 10점 중', '').replace('영화', '').replace('입니다', '').replace('평점', ''))
        
        result = result + sub_result
    return ''.join(result)



#언더워터
underwater = movie_scrap('https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=160437&target=after')
#해빙
Bluebeard = movie_scrap('https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=137875&target=after')
#날씨의 아이
Weathering = movie_scrap('https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=181114&target=after')
#고양이의 보은
TheCat = movie_scrap('https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=37073&target=after')
#헝거게임 파이널
Hunger = movie_scrap('https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=100643&target=after')


movies = [underwater, Bluebeard, Weathering, TheCat, Hunger]
print(movies)

# 단어 빈도 수
words_basket = []
okt = Okt()

for mov in movies:
    words = okt.pos(mov)
    for word in words:
        if word[1] in ['Noun', 'Adjective'] and len(word[0]) >= 2:
            words_basket.append(word[0])
print(words_basket)
print(Counter(words_basket).most_common(50))
