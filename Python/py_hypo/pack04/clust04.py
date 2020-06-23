'''
    밀도기반 클러스터링(density-based)
      밀도 기반 알고리즘은 "동일한 클래스에 속하는 데이터는 서로 근접하게 분포할 것이다"라는 가정을 기반으로 동작한다. 
     k-means와 달리 k를 결정하지 않아도 된다. 
     매개변수(min_sample, eps)를 잘 조절하면 우수한 클러스터링 수행 가능. 
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.datasets import make_moons #DBSCAN 연습용
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN

# 시각화 차트 그리기
def plotResult(x, y):
    plt.scatter(x[y==0, 0], x[y==0, 1], s=40, c='skyblue', label='cluster-1')
    plt.scatter(x[y==1, 0], x[y==1, 1], s=40, c='pink', label='cluster-2')
    plt.legend()
    plt.show()
    
# 데이터 생성
x, y = make_moons(n_samples=200, noise=0.05, random_state=0)
print(x[:2], y[:2])

plt.scatter(x[:, 0], x[:, 1])
plt.show()

# KMeans 클러스터링으로 한 경우
km = KMeans(n_clusters=2, random_state=0)
pred1 = km.fit_predict(x)
plotResult(x, pred1)


# DBSCAN 클러스터링으로 한 경우
dm = DBSCAN(eps=0.2, min_samples=5, metric='euclidean') # eps 두 샘플간 최대 거리, 한 점에서부터 거리 eps내에 점이 min_samples개 있으면 하나의 군집으로 인식
pred2 = dm.fit_predict(x)
plotResult(x, pred2)


