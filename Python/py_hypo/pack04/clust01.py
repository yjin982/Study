'''  비지도학습 중 하나인 군집분석 Clustering(클러스터링)
      계층적 군집분석
        - 응집형, 분리형이 있음
      비계층적 군집분석
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')

np.random.seed(1)
var = ['x', 'y']
labels = ['dot0', 'dot1', 'dot2', 'dot3', 'dot4']
x = np.random.random_sample([5, 2])
df = pd.DataFrame(x, columns=var, index=labels)
print(df)

plt.scatter(x[:, 0], x[:, 1], s=50, c='skyblue', marker='o')
plt.grid(True)
plt.show()

from scipy.spatial.distance import pdist, squareform
distmatrix = pdist(df, metric='euclidean') # metric 기본 유클리디안
print(distmatrix)  # 1차원 배열로 거리 생성

row_dist = pd.DataFrame(squareform(distmatrix), columns=labels, index=labels)
print(row_dist)

from scipy.cluster.hierarchy import linkage # 응집형 계층적 클러스터링 수행
row_cluster = linkage(distmatrix, method='ward')
df = pd.DataFrame(row_cluster, columns=['cluster1', 'cluster2', 'distance', 'cluster member num'], index=['cluster%d'%(i+1) for i in range(row_cluster.shape[0])])
print(df)

# 시각화
from scipy.cluster.hierarchy import dendrogram
row_dend = dendrogram(row_cluster, labels=labels)
plt.tight_layout()
plt.ylabel('유클리드 거리')
plt.show()


print()
# 병합군집 알고리즘 모델
from sklearn.cluster import AgglomerativeClustering
ac = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
labels = ac.fit_predict(x)
print('군집 분류 결과 :', labels)


# 시각화
a = labels.reshape(-1, 1)
print(a)
x1 = np.hstack([x, a])
print(x1)

x_0 = x1[x1[:, 2] == 0, :]
x_1 = x1[x1[:, 2] == 1, :]
x_2 = x1[x1[:, 2] == 2, :]
print(x_0)

plt.scatter(x_0[:, 0], x_0[:, 1])
plt.scatter(x_1[:, 0], x_1[:, 1])
plt.scatter(x_2[:, 0], x_2[:, 1]) 
plt.legend(['cluster0', 'cluster1', 'cluster2'])
plt.show()