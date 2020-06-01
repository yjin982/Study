''' 
    워드 클라우드
    신문사 사이트에서 검색 단어 입력 후 해당 단어 기사 정보 읽어 워드 클라우드 출력 
'''
from bs4 import BeautifulSoup as bs
import urllib.request                #url 문서 읽기 용
from urllib.parse import quote   #url의 한글 단어 인코딩용

keyword = input('검색어 입력 : ')
# keyword = '화재'   #귀찮으니 고정시키기
keyword = quote(keyword) 

targetUrl = 'https://www.donga.com/news/search?query=' + keyword
searchData = urllib.request.urlopen(targetUrl).read()
soup = bs(searchData, 'lxml') #한글이 깨진다면 from_encoding='utf8'

# 각 기사들의 a태그 셀렉터
# #content > div:nth-child(5) > div > div:nth-child(2) > div.t > p.tit > a
msg = ''
for title in soup.find_all('p', 'tit'): #p태그 tit클래스 중
    title_link = title.select('a')      #a 태그들
    article_url = title_link[0]['href'] #링크들만 뽑기
    
    source_article = urllib.request.urlopen(article_url).read() #각 a태그의 기사 내용을 읽기
    soup = bs(source_article, 'lxml', from_encoding='utf8')
    contents = soup.select('div.article_txt') #기사 본문
    for temp in contents:
        item = str(temp.find_all(text=True))
        #print(item)
        msg = msg + item
print(msg)



from konlpy.tag import Okt       #형태소 분석
from collections import Counter #컬렉션의 갯수 세주는 라이브러리

nlp = Okt()
nouns = nlp.nouns(msg) #명사별로 분할
result = []
for temp in nouns:
    if len(temp) > 1:
        result.append(temp)

print(result)
count = Counter(result)
# print(count) #Counter({'보험': 33, '시간': 27, '한국': 26, '삼성': 25, ...
tag = count.most_common(50) #빈도수 상위 50개
print(tag)


# pip install simplejson #결과를 새 창으로 띄우기 위함
# pip install pytagcloud #워드클라우드용 라이브러리
import pytagcloud

taglist = pytagcloud.make_tags(tag, maxsize=100) #클라우드 만들 대상, 글자 최소크기, 최대크기, 색상
# print(taglist)
# 이미지로 저장
pytagcloud.create_tag_image(taglist, 'morph04word.png', size=(1000, 700), fontname='malgun', rectangular=False)
#한글 지원이 안됨 
#C:\Anaconda3\Lib\site-packages\pytagcloud\fonts 경로에 보면 한글이 지원되는 글꼴이 없기때문에
#한글 지원되는 글꼴을 복붙하고 fonts.json에 등록해주기


# 저장된 이미지 읽기
import matplotlib.pyplot as plt #시각화를 위한 대표적 라이브러리
import matplotlib.image as mpimg

img = mpimg.imread('morph04word.png')
plt.imshow(img)
plt.show()


#브라우저로 출력 
import webbrowser
webbrowser.open('morph04word.png') 