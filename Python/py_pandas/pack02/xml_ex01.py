''' XML 처리 기본모듈 '''
import xml.etree.ElementTree as etree

xml_f = open("my.xml", "r", encoding="utf8").read() #그냥 텍스트파일같이 통째로 읽은 상태
#print(xml_f)  #type : <class 'str'>

#엘리먼트 객체형식으로 바꾸기
root = etree.fromstring(xml_f)
#print(root) #<Element 'items' at 0x0000022256BC2318>
#print(root.tag)  #루트 엘리먼트 태그 이름
#print(len(root)) #엘리먼트 갯수

#스트링으로 받아서 바꾸지 말고 바로
xmlfile = etree.parse('my.xml')
#print(xmlfile)  #<xml.etree.ElementTree.ElementTree object at 0x000002F55CE797C8>
root = xmlfile.getroot()
#print(root.tag)
#print(root[0].tag, root[1].tag)   #루트 하위태그
#print(root[0][0].tag, root[0][1].tag) #루트 하위 item 안에 자식
#print(root[0][0].attrib)
#print(root[0][0].attrib.keys(), '/', root[0][0].attrib.get('id'))

myname = root.find('item').find('name').text
mytel = root.find('item').find('tel').text
#print(myname, mytel)

for child in root:
    #print(child.tag)
    for child2 in child:
        print(child2.tag, ' ', child2.attrib)
        
for e in root.iter('exam'):
    print(e.attrib)
    
print('-' * 30)

children = root.findall('item')
for c in children:
    re_id = c.find('name').get('id')
    re_name = c.find('name').text
    re_tel = c.find('tel').text
    re_exam = c.find('exam').attrib
    print(re_id, re_name, re_tel, re_exam)
    
