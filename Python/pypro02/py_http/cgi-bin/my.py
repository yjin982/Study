import cgi
form = cgi.FieldStorage() #사용자가 입력한 자료 받기
irum = form['name'].value
nai = form['age'].value

print('Content-Type:text/html;charset=utf-8\n')
print('''
<html>
<body>
이름 : {0}, 나이 : {1}<br>

<a href='../main.html'>메인으로 이동</a>
</body>
</html>
'''.format(irum, nai))