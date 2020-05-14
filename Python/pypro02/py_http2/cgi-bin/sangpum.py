#마리아db의 테이블 출력
import MySQLdb, cgi

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    cursor.execute('select * from sangdata')
    
    print('Content-Type:text/html;charset=utf-8\n')    
    print('<html><body>상품 자료 <br>')
    print('<table><tr><th>코드</th><th>품명</th><th>수량</th><th>단가</th></tr>')
    
    datas = cursor.fetchall()
    for code, sang, su, dan in datas:
        print('''
        <tr>
            <td>{0}</td>
            <td>{1}</td>
            <td>{2}</td>
            <td>{3}</td>
        </tr>
        '''.format(code, sang, su, dan))
    print('''<tr><td colspan='4'>건수 : {0}<td></tr>'''.format(len(datas)))
    print('</table></body></html>')
        
except Exception as e:
    print(e)
finally:
    cursor.close()
    conn.close()