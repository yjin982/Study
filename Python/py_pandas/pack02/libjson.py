'''  웹에서 제공되는  json 도서관 휴관일 정보 읽어오기   '''
import urllib.request as req
import json

url = 'http://openapi.seoul.go.kr:8088/sample/json/SeoulLibraryTime/1/5/'
plainText = req.urlopen(url).read().decode()
jsonData = json.loads(plainText) #json Decoding
#print(jsonData)            #plainText string -> jsonData dict

for i in range(5):
    print(jsonData['SeoulLibraryTime']['row'][i]['LBRRY_NAME'])
    
print()
#get()
libData = jsonData.get('SeoulLibraryTime').get('row')
for i in libData:
    name = i['LBRRY_NAME']
    addr = i.get('ADRES')
    tel = i['TEL_NO']
    print(name + '\t' + addr + '\t' + tel)