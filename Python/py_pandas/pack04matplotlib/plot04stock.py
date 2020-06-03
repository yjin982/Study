import pandas as pd
from pandas_datareader import data

''' 종목 읽기 '''
kosdaq = pd.read_pickle('kosdaq.pickle')
kospi = pd.read_pickle('kospi.pickle')
# print(kosdaq.head(10))
# print(kospi)

''' 야후 파이낸스에서 읽기  '''
start_date = '2018-01-01'
tickers = ['003380.KQ', '251270.KS'] #코스닥 현대건설기계, 코스피 넷마블게임즈
holding_df = data.get_data_yahoo(tickers[0], start_date)
# print(holding_df)
net_df = data.get_data_yahoo(tickers[1], start_date)
# print(net_df)

''' 파일로 저장  '''
holding_df.to_csv('holding.csv')
net_df.to_csv('net.csv')
# holding_df.to_pickle('holding.pickle')
# net_df.to_excel('net.xlsx')


'''  파일 읽기  '''
with open('holding.csv', 'r') as f:
    print(f.read())

print(pd.read_csv('net.csv'))


import matplotlib.pyplot as plt
# plt.plot(holding_df)
# plt.show()
# 
# plt.plot(net_df)
# plt.show()


'''    pandas가 plot 기능을 지원    '''
import numpy as np
np.random.seed(15)

df = pd.DataFrame(np.random.randn(10, 3), index=pd.date_range('1/1/2000', '1/1/2020', periods=10), columns=['a', 'b', 'c'])
print(df)

# df.plot() #꺽은선 그래프
# df.plot(kind='bar') #바 그래프,  box, ... 
df[:5].plot.bar(rot=15) #bar그래프, 글씨 기울기
plt.title('test')

plt.show()