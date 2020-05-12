import MySQLdb

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
    
    buserNum = input('부서번호 입력 : ')
    sql = 'select jikwon_no, jikwon_name, buser_num, jikwon_jik from jikwon where buser_num=%s'
    cursor.execute(sql, (buserNum, ))
    
    #sql문이 길어질 경우
    sql = '''
        select jikwon_no, jikwon_name, buser_num, jikwon_jik 
        from jikwon 
        where buser_num={0}
    '''.format(buserNum)
    cursor.execute(sql)
    
    datas = cursor.fetchall()
    print('사번 이름 부서번호 직급')
    for data in datas:
        print('%s %s %s %s'%data)    
    print('인원수 :', len(datas))
    
    '''
    for a, b, c, d in datas:
        print(a, b, c, d)
    '''
    
except Exception as e:
    print(e)
finally:
    cursor.close()
    conn.close()