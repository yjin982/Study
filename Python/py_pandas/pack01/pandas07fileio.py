import pandas as pd

''' 파일로 저장 '''
items = {'apple':{'count':10, 'price':1500}, 'orange':{'count':4, 'price':1000}}
df = pd.DataFrame(items)
#print(df)

#df.to_csv('result1.csv', sep=',')
#df.to_csv('result2.csv', sep=',', index=False) #저장시 색인 제외
#df.to_csv('result3.csv', sep=',', index=False, header=False) #저장시 색인,헤더 제외

data = df.T
#print(data)
#data.to_csv('result4.csv', sep=',', index=False, header=True)
redata = pd.read_csv('result4.csv')
#print(redata)


''' excel '''
df2 = pd.DataFrame({'data':[1,2,3,4,5]})

#엑셀 파일 저장
writer = pd.ExcelWriter('good.xlsx', engine='xlsxwriter')
df2.to_excel(writer, sheet_name='sheet1')
#writer.save()
#print('저장 성공')

#엑셀 파일 읽기 1
exf = pd.ExcelFile('good.xlsx')
#print(exf.sheet_names) #시트이름 반환
df3 = exf.parse('sheet1')
#print(df3)

#엑셀 파일 읽기2
df4 = pd.read_excel(open('good.xlsx', 'rb'))
df4 = pd.read_excel(open('good.xlsx', 'rb'), sheet_name='sheet1') #읽을때 시트 이름도 지정가능
#print(df4)

