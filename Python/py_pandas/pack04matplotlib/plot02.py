'''    시각화 계속    '''
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False 

'''    sub plot    '''
fig = plt.figure() #차트 영역 객체 선언
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2) #1행 2열 공간의 두번째
 
ax1.hist(np.random.randn(10), bins=10, alpha=0.4) #히스토그램, bin 구간 간격, alpha 투명도
ax2.plot(np.random.randn(10))
plt.show()


'''    막대 그래프    '''
data = [50, 80, 100, 30, 90]
plt.bar(range(len(data)), data) #막대 그래프, 넓이, 데이터값
plt.show()

errdata = np.random.rand(len(data))
plt.barh(range(len(data)), data, alpha=0.6, xerr=errdata) # 가로 막대그래프, xerr 편차 에러값 신뢰 구간 등을 표시하면 좋음 
plt.show()


'''    원형 그래프    '''
plt.pie(data, explode=(0, 0, 0.1, 0, 0), colors=['pink', 'yellow', 'cyan']) #explode 원에서 조금 삐져나오게(파이빼먹는거처럼)
plt.title('원형')
plt.show()

'''    박스 차트   이상치 발견할 때 효과적(평균으로부터 데이터가 얼마나 떨어져 있는지)    '''
plt.boxplot(data)
plt.show()


''''    버블 차트    '''
n = 30
np.random.seed(10)
x = np.random.rand(n)
y = np.random.rand(n)
color = np.random.rand(n)
scale = np.pi * (20 * np.random.rand(n)) ** 2
plt.scatter(x, y, s=scale, c=color)
plt.show()


'''    시계열 차트    '''
import pandas as pd
df = pd.DataFrame(np.random.randn(1000, 4), index=pd.date_range('1/1/2000', periods=1000), columns=list('abcd'))
df = df.cumsum() #데이터 누적 시키면
plt.plot(df)
plt.show()