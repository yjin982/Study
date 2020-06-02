'''    원격 db와 연동    '''
import MySQLdb
import numpy as np
import pandas as pd
import csv

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

conn = MySQLdb.connect(**config)
cursor = conn.cursor()
sql = "select jikwon_no, jikwon_name, buser_name, jikwon_jik, jikwon_pay from jikwon inner join buser on buser_num=buser_no"
cursor.execute(sql)

for (a, b, c, d, e) in cursor:
    print(a, b, c ,d, e)
    
with open('jik_data.csv', 'w', encoding='utf8') as f: #✔파일 저장시 close안해도 되는 with문, 쓰기모드w 읽기모드 r
    writer = csv.writer(f)
    for r in cursor:
        writer.writerow(r)
    print('저장 성공')

df1 = pd.read_csv('jik_data.csv', header=None, names=('번호', '이름', '부서', '직급', '연봉'))
print(df1.head(5))

df2 = pd.read_sql(sql, conn)
df2.columns = ('번호', '이름', '부서', '직급', '연봉')
print(df2.head(5))

print()
print(df2['직급'].value_counts())
print(df2.loc[:, ['연봉']].mean())

import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
jik_ypay = df2.groupby(['직급'])['연봉'].mean() #Series 로 반환
print(jik_ypay.index)
print(jik_ypay.values)

plt.pie(jik_ypay, labels=jik_ypay.index, labeldistance=0.5, counterclock=False, explode=(0.2, 0, 0.3, 0, 0), shadow=True)
plt.show()

cursor.close()
conn.close()
