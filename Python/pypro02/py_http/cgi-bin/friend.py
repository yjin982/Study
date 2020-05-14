import cgi
form = cgi.FieldStorage() #key:value 타입으로 데이터가 들어옴
name = form['name'].value
phone = form['phone'].value
gen = form['gen'].value


print('Content-Type:text/html;charset=utf-8\n')
print('''
<html>
<body>
이름 : {0}, 전화 : {1}, 성별 : {2}<br>
<a href='../main.html'>메인으로 이동</a>
</body>
</html>
'''.format(name, phone, gen))