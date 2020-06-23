'''
    iris로 지도/비지도 학습 간단 정리
'''
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

iris = sns.load_dataset('iris')
print(iris.head(3), '\n')

x_iris = iris.drop('species', axis=1)  # 종 칼럼은 뺌
y_iris = iris.species
print(x_iris[:3])
print(y_iris[:3].values, '\n')

x_train, x_test, y_train, y_test = train_test_split(x_iris, y_iris, random_state=1)


print('=' * 40)
# 지도학습 중 분류 
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
gmodel = GaussianNB().fit(x_train, y_train)  # feature, label
pred = gmodel.predict(x_test)
print('GaussianNB pred :', pred[:5])
print('GaussianNB acc  : {:.3f}\n'.format(accuracy_score(y_test, pred)))



# 비지도학습 중 차원축소(압축, PCA)
from sklearn.decomposition import PCA
pmodel = PCA(n_components=2, random_state=1).fit(x_train) # feature
x2d = pmodel.fit_transform(x_iris)
print(x2d[:2], '\n')  # 칼럼을 2개로 줄임

# 시각화
iris['pca1'] = x2d[:, 0]
iris['pca2'] = x2d[:, 1]
sns.lmplot('pca1', 'pca2', data=iris, hue='species')
plt.show()

print('=' * 40)
# 비지도학습 중 분류(=군집, 클러스터링)
from sklearn.mixture import GaussianMixture  # 클러스터링 알고리즘 중 하나
gmodel = GaussianMixture(n_components=3, covariance_type='full').fit(x_iris)  # feature
y_pred_g = gmodel.predict(x_iris)
print('GaussianMixture pred :', y_pred_g[:10])

iris['cluster'] = y_pred_g
sns.lmplot('pca1', 'pca2', data=iris, hue='species', col='cluster')
plt.show()