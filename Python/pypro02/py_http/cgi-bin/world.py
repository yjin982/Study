s1 = '자료 1'
s2 = 'second 자료'


print('Content-Type:text/html;charset=utf-8\n')
print('''
<html>
<body>
<h2>반가워여</h2>
자료 출력 : {0},  {1}<br>
<img src='../images/pawel.png' /><br>
<a href='../main.html'>메인으로 이동</a>
</body>
</html>
'''.format(s1, s2))