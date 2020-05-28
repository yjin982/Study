''' HTML/XML 전용 처리 모듈 : BeautifulSoup '''
from bs4 import BeautifulSoup as bs

html_data = '''
<html>
<body>
<h1>뷰티풀라이플</h1>
<p>웹 페이지 분석</p>
<p>원하는 자료를 추출가능</p>
</body>
</html>
'''
#print(html_data, type(html_data)) #현재는 str

soup = bs(html_data, 'html.parser')
#print(soup) #<class 'bs4.BeautifulSoup'>

h1 = soup.html.body.h1
print(h1, '      ', h1.string) #태그째로 보기, 태그안 텍스트만 보기

p1 = soup.html.body.p
print(p1, '      ', p1.string)

#다음 p 태그를 찍기 위해서는  sibling
p2 = p1.next_sibling.next_sibling #p1.next_sibling 까지만 했을때는 </p> 그 다음 <p> 를 가기 위해서 한번더 시블링 탐색
print(p2, '      ', p2.text)
print()

html_data2 = '''
<html>
<body>
<h1 id="title">뷰티풀라이플</h1>
<p>웹 페이지 분석</p>
<p id="my">원하는 자료를 추출가능</p>
</body>
</html>
'''
soup2 = bs(html_data2, 'lxml')
print(soup2.p.string, '      ', soup2.find('p').string) #최초로 만나는 p태그
print(soup2.find('p', id='my').text) #id를 가지고 추출
print(soup2.find(id='title').text)    #태그없이 속성으로만 찾기도 가능
print()


html_data3 = '''
<html>
<body>
<h1 id="title">뷰티풀라이플</h1>
<p>웹 페이지 분석</p>
<p id="my">원하는 자료를 추출가능</p>
<div>
<a href="https://www.naver.com">naver</a>
<a href="https://www.daum.com">daum</a>
</div>
</body>
</html>
'''
soup3 = bs(html_data3, 'lxml')
#print(soup3.prettify()) #들여쓰기로 보여주기
print(soup3.find_all(['a']), '      ', soup3.find_all('a'), '      ', soup3.findAll(['a'])) #여러개인 태그 찾기
links = soup3.findAll(['a']) #리스트타입으로 들어옴
for i in links:
    href = i.attrs['href']
    text = i.text  #또는 string
    print(href, '      ', text)
    
print(soup3.find_all(['p', 'h1'])) #복수개 태그 얻기 가능
print(soup3.find_all(string=['원하는 자료를 추출가능', '웹 페이지 분석', '뷰티풀라이플'])) #string이 같은 태그를 찾기



#정규표현식 가능
import re
links2 = soup3.find_all(href=re.compile(r'^ht')) #ht로 시작하는 문자열
print(links2)
for h in links2:
    print(h.attrs['href']) #href의 속성값들만 출력
print()



#css 셀렉터 이용
html_data4 = '''
<html>
<body>
    <div id="hello">
        <a href="https://www.naver.com">naver</a>
        <span>
            <a href="https://www.google.com">google</a>
            <i>
                <a href="https://www.kakao.com">kakao</a>
            </i>
        </span>
        <ul class="world">
            <li>아녕</li>
            <li>나이쑤뚜미뚜</li>
        </ul>
        <ul class="funk">
            <li>hell</li>
            <li>cell</li>
        </ul>
    </div>
    <div id="sea">
        <b>b태그입뉘당</b>
        <a href="https://www.daum.com">daum</a>
    </div>
</body>
</html>
'''
soup4 = bs(html_data4, 'lxml')
a = soup4.select_one('div a') #div 아래에 자식 a 하나만
print('a :', a)

a = soup4.select_one('div#sea a') #div중 id가 sea인 div 아래에 자식 a 하나만
print('a :', a)

b = soup4.select_one('div#hello a').string
print('b : ', b)

c = soup4.select_one('div#hello span a').string #span 바로 아래 a 없고 i안에만 있어도 찾기 가능
print('c : ', c)

d = soup4.select_one('div#hello span > a').string #span의 직계 자식
print('d : ', d)

e = soup4.select('div#hello ul.world > li')
print('e : ', e)
for kk in e:
    print(kk.string)