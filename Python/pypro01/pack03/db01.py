# 원격 DB - MariaDB와 연동
import MySQLdb

#conn = MySQLdb.connect(host='127.0.0.1', user='root', password='123', database='test')
#print(conn)
#conn.close

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
    #print(conn)
    cursor = conn.cursor()   #sql문 수행을 위한 커서 객체
    
    
    '''전체 자료 읽기'''
    sql = 'select * from sangdata'
    cursor.execute(sql)
    
    #출력 1
    for data in cursor.fetchall():
        #print(data)   #tuple
        print('%s %s %s %s'%data)
    
    #출력 2
    for r in cursor:
        #print(r)
        print('c', r[0], r[1], r[2], r[3])
        
    #출력 3
    for (code, sang, su, dan) in cursor:
        print('-', code, sang, su, dan)
    
    #출력 4
    for (a, b, c, d) in cursor:
        print('=', a, b, c, d)
        
    
    '''부분 자료 읽기'''
    code = 3
    #sql = 'select * from sangdata where code=%s'
    #cursor.execute(sql, (code, )) #조건 값은 튜플로 주어야 함
    sql = "select * from sangdata where code='{0}'".format(code)
    cursor.execute(sql)
                   
    for data in cursor.fetchall():
        print('%s %s %s %s'%data)
    
    
except Exception as e:
    print(e)
finally:
    cursor.close()
    conn.close()
