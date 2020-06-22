'''
    iris로 군집분석
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import linkage, dendrogram

iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
print(iris_df.head(3))

from scipy.spatial.distance import pdist, squareform
distMatrix = pdist(iris_df.loc[:, ['sepal length (cm)', 'sepal width (cm)']])
print('distMatrix :', distMatrix)

row_dist = pd.DataFrame(squareform(distMatrix))
print('row_dist :\n', row_dist[:3])  # 150x150

row_cluster = linkage(distMatrix, method='complete')
print('row_cluster :\n', row_cluster[:3])

df = pd.DataFrame(row_cluster, columns=['id1', 'id2', '거리', '멤버수'])
print(df[:3])

row_dend = dendrogram(row_cluster)
plt.tight_layout()
plt.ylabel('euclidean distance')
plt.show()