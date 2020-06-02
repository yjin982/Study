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
                              .replace('설국열차', '').replace('해빙', '').replace('언더워터', '').replace('날씨의 아이', '').replace('고양이의 보은', '')
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
#설국열차
Snowpiercer = movie_scrap('https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=62328&target=after')
 
movies = [underwater, Bluebeard, Weathering, TheCat, Snowpiercer]
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
print(Counter(words_basket).most_common(50)) #참고로 빈도수 높은 단어 확인
 
movies = [m.replace('사람', '') for m in movies] #이런식으로도 의미없는 단어 지우기 가능
print(movies, len(movies))
 
 
 
 
def word_separate(movies):
    result = []
    for mov in movies:
        words = okt.pos(mov)
        one_result = []
        for word in words:
            if word[1] in ['Noun', 'Adjective'] and len(word[0]) >= 2:
                one_result.append(word[0])
        result.append(' '.join(one_result))
    return result
 
word_list = word_separate(movies)
print(word_list, len(word_list))
 
 
print()
# 토큰 생성 후 벡터화
# 1) CountVectorizer
count = CountVectorizer(min_df=2) #두글자 미만 무시
print(count) 
cou_dtm = count.fit_transform(word_list).toarray()
print(cou_dtm)
cou_dtm_df = pd.DataFrame(cou_dtm, columns=count.get_feature_names(), index=['underwater', 'Bluebeard', 'Weathering', 'TheCat', 'Snowpiercer'])
print(cou_dtm_df) # 단어별 빈도수 
print()
 
# 2) TfidfVectorizer
idf_maker = TfidfVectorizer(min_df=2)
print(idf_maker) 
tfidf_dtm = idf_maker.fit_transform(word_list).toarray()
tfidf_dtm_df = pd.DataFrame(tfidf_dtm, columns=idf_maker.get_feature_names(), index=['underwater', 'Bluebeard', 'Weathering', 'TheCat', 'Snowpiercer'])
print(tfidf_dtm_df) # 단어들의 중요도를 알 수 있는 가중치로 출력
print()


# 코사인 유사도(수식)를 이용해 단어의 유사성 출력
def cosin_func(doc1, doc2):
    bunja = sum(doc1 *doc2) #코사인 유사도 공식의 분자값 계산
    bunmo = (sum(doc1 ** 2) * sum(doc2 ** 2)) ** 0.5 #코사인 유사도 공식의 분모값 계산
    return bunja / bunmo


res = np.zeros((5, 5))
for i in range(5):
    for j in range(5):
        res[i, j] = cosin_func(tfidf_dtm_df.iloc[i], tfidf_dtm_df.iloc[j].values)
        
df = pd.DataFrame(res, index=['underwater', 'Bluebeard', 'Weathering', 'TheCat', 'Snowpiercer'], columns=['underwater', 'Bluebeard', 'Weathering', 'TheCat', 'Snowpiercer'])
print(df) #숫자값이 높을 수록 유사도가 높음
