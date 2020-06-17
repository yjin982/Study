'''
    Support Vector 확인해보기
      많은 양의 데이터일지라도 초평면^을 구성하는 서포트 벡터는 일부 데이터만 사용하기 때문에 속도가 빠름
      전통적인 분류모델 중 분류 정확도가 우수하고, 이미지 분류에도 효과적이다. (= 딥러닝이 더 우수하다는 것)
      
      
    ※ n차원 공간 상에서 f 값이 1이 되는 x1, x2, …, xn 점들과 0이 되는 x1, x2, …,xn 점들을 두 그룹으로 분리하는 n차원 평면
'''
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='malgun gothic')

# 샘플데이터 형성
X, y = make_blobs(n_samples=50, centers=2, cluster_std=0.5, random_state=4)
y = 2 * y - 1

# 샘플데이터로 시각화
plt.scatter(X[y == -1, 0], X[y == -1, 1], marker='o', label="-1 클래스")
plt.scatter(X[y == +1, 0], X[y == +1, 1], marker='x', label="+1 클래스")
plt.xlabel("x1")
plt.ylabel("x2")
plt.legend()
plt.title("학습용 데이터")
plt.show()


from sklearn.svm import SVC

model = SVC(kernel='linear', C=1e10).fit(X, y)
xmin = X[:, 0].min()
xmax = X[:, 0].max()
ymin = X[:, 1].min()
ymax = X[:, 1].max()
xx = np.linspace(xmin, xmax, 10)
yy = np.linspace(ymin, ymax, 10)
X1, X2 = np.meshgrid(xx, yy)

z = np.empty(X1.shape)
for (i, j), val in np.ndenumerate(X1):
    x1 = val
    x2 = X2[i, j]
    p = model.decision_function([[x1, x2]])
    z[i, j] = p[0]


levels = [-1, 0, 1]
linestyles = ['dashed', 'solid', 'dashed']
plt.scatter(X[y == -1, 0], X[y == -1, 1], marker='o', label="-1 클래스")
plt.scatter(X[y == +1, 0], X[y == +1, 1], marker='x', label="+1 클래스")
plt.contour(X1, X2, z, levels, colors='k', linestyles=linestyles)
plt.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], s=300, alpha=0.3)

# 새로 예측할 테스트 데이터를 포함시켜서 시각화
x_new = [10, 2]
plt.scatter(x_new[0], x_new[1], marker='^', s=100)
plt.text(x_new[0] + 0.03, x_new[1] + 0.08, "테스트 데이터")
plt.xlabel("x1")
plt.ylabel("x2")
plt.legend()
plt.title("SVM 예측 결과")
plt.show()

# Support Vectors 값 출력
print(model.support_vectors_)