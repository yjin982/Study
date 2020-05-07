# 정규표현식
import re
ss = '1234 abc 가나다ABC_555_6 a b 123nbc'
print(ss)
print(re.findall(r'123', ss)) #return type => list
print(re.findall(r'[0-9]', ss))
print(re.findall(r'\d', ss))
print(re.findall(r'[0-9]+', ss)) #1회이상
print(re.findall(r'[0-9]*', ss))  #0회이상
print(re.findall(r'[0-9]{2}', ss))    #2회
print(re.findall(r'[0-9]{2,3}', ss)) #2회 또는 3회

print()
print(re.findall(r'.bc', ss)) # .모든문자
print(re.findall(r'^1+', ss))    #첫글자가 1
print(re.findall(r'[^1]+', ss)) #첫글자가 1이 아닌, ^는 [] 안에 있으면 부정
print(re.findall(r'[^0-9]+', ss))
print(re.findall(r'nbc$', ss))

a = re.match(r'123', ss)
print(a)
print(a.group())