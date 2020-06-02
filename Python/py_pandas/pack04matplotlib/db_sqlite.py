'''   개인용 RDBMS    '''
import sqlite3

sql = "create table if not exists test(product varchar(10), maker varchar(10), weight real, price integer)"

#conn = sqlite3.connect('testdb')
conn = sqlite3.connect(':memory:') #물리적으로 생성하지 않고 메모리상(ram)에서만 사용할 시
conn.execute(sql)
conn.commit()

data1 = ('마우스', '삼성', 12.5, 5000)
data2 = ('키보드', '엘지', 32.5, 10000)
data3= [('모니터', '삼성', 4500.5, 45000), ('메모리', '인텔', 12.5, 1210000)]
stmt = 'insert into test values(?, ?, ?, ?)' #✔sqlite 에서는 물음표로 매핑
conn.execute(stmt, data1)
conn.execute(stmt, data2)
conn.executemany(stmt, data3) #✔여러개 데이터 한꺼번에 줄 때
conn.commit()


#읽기
cursor = conn.execute('select * from test')
rows = cursor.fetchall()
# print(rows)
for r in rows:
    print(r)

# 방법 1 cursor로 읽어서 
import pandas as pd
df1 = pd.DataFrame(rows) #이 방식은 별도로 컬럼명을 써줘야함
print(df1)


# 방법 2 read_sql 이용
df2 = pd.read_sql('select * from test', conn)
print(df2)

cursor.close()
conn.close()