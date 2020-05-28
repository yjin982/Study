''' 기상청 날씨정보 xml 자료 읽기 '''
import urllib.request
import xml.etree.ElementTree as etree

''' 웹에서 파일 읽어오기
try:
    webdata = urllib.request.urlopen('http://www.kma.go.kr/XML/weather/sfc_web_map.xml')
    webxml = webdata.read()
    webxml = webxml.decode('utf-8')
    #print(webxml)
    
    with open('myweather.xml', mode='w', encoding='utf8') as f:
        f.write(webxml)
    
except Exception as e:
    print('error ', e)
finally:
    webdata.close()
'''


xmlfile = etree.parse('myweather.xml') #엘리먼트 객체로 읽기
root = xmlfile.getroot()
child = root.findall('{current}weather') #또는 root[0].tag

#날짜 얻기
for i in child:
    y = i.get('year')
    m = i.get('month')
    d = i.get('day')
    h = i.get('hour')
    print(y + '년 ' + m + '월 ' + d + '일 현재' + h + '시')

datas = []
for ch in root:
    #ch = {current}weather
    for i in ch:
        #i = {current}local
        local_name = i.text #지역명, 태그 안에 있는 내용 <>요기</>
        ta = float(i.get('ta'))
        desc = i.get('desc') #<local> 안의 attribute
        datas += [[local_name, ta, desc]] #리스트에 데이터 넣기
        
#print(datas)

#가져온 데이터를 데이터프레임에 넣기
from pandas import DataFrame
df = DataFrame(datas, columns=('지역', '기온', '기상상태'))
#print(df)



#웹 자료 읽어서 바로 출력
import urllib.request

webdata2 = urllib.request.urlopen('http://www.kma.go.kr/XML/weather/sfc_web_map.xml')
xmlfile2 = etree.parse(webdata2)
root = xmlfile2.getroot()

ndata = list(root[0].attrib.values()) #현재 날짜 읽기
print(ndata[0] + '년 ' + ndata[1] + '월 ' + ndata[2] + '일 ' + ndata[3] + '시')

for child in root:
    for subChild in child:
        print(subChild.text + ' : ' + subChild.attrib.get('ta') + '도')
        


#웹 이미지 읽기
imgUrl = 'https://images.unsplash.com/photo-1587455046156-c3b92dae4586?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80'
saveName = 'myimage.jpg'
urllib.request.urlretrieve(imgUrl, saveName)
