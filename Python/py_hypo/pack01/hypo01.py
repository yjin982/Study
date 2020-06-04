'''
    분산 / 표준편차의 중요성 - 데이터의 치우침을 표현하는 대표적인 값 중 하나
    
    💬 기대값 : 어떤 확률을 가진 사건을 무한 반복할 때 얻을 수 있는 값의 평균으로써 기대할 수 있는 값. 간단하게 평균이라 생각 가능 
'''
import scipy.stats as stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
print(stats.norm(loc=1, scale=2).rvs(10)) #정규분포를 따르는 난수 발생, loc 기대값💬, scale 표준편차, rvs(random values sampling)
print()

centers = [1, 1.5, 2]
col = ['pink', 'lightgreen', 'lightblue']

std = 0.1 #표준편차
data_1 = [] 

for i in range(3):
    data_1.append(stats.norm(loc=centers[i], scale=std).rvs(100))
    print(data_1)
    plt.plot(np.arange(len(data_1[i])) + i * len(data_1[i]), data_1[i], 'o', c=col[i])
plt.show()


std = 2 #표준편차(또는 분산)은 클수록 데이터가 섞여있는 수가 많아져 패턴을 찾기가 어려움
data_1 = [] 

for i in range(3):
    data_1.append(stats.norm(loc=centers[i], scale=std).rvs(100))
    print(data_1)
    plt.plot(np.arange(len(data_1[i])) + i * len(data_1[i]), data_1[i], 'o', c=col[i])
plt.show()