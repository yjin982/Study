'''
    의사결정트리로 iris 데이터셋 다항(품종) 분류
'''
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection._split import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import datasets
import pandas as pd
import numpy as np
import pydotplus
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)

iris = datasets.load_iris()
print(iris.keys())

# ===========================================================
x = iris.data[:, [2, 3]] # 모든 행의 2,3열, petal.length, petal.width의 2 칼럼으로 꽃의 종류 3가지로 분류
y = iris.target
print(x[:3])
print(y[:3], '   ', set(y))

# train / test 나누기
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) #(105, 2) (45, 2) (105,) (45,)

# (지금은 꼭 필요한 건 아닌지만 필요할 때가 있는) 스케일링 (데이터 크기 표준화, 전체 자료의 분포를 평균 0, 분산 1이 되도록)
print(x_train[:3])  # [[3.5 1. ]  [5.5 1.8]  [5.7 2.5]]
print(x_test[:3])   # [[5.1 2.4]  [4.  1. ]  [1.4 0.2]]

sc = StandardScaler()
sc.fit(x_train)
sc.fit(x_test)
x_train = sc.transform(x_train)
x_test = sc.transform(x_test)

print(x_train[:3]) # [[-0.05624622 -0.18650096]   [ 1.14902997  0.93250481]   [ 1.26955759  1.91163486]]
print(x_test[:3])  # [[ 0.90797473  1.77175914]   [ 0.24507283 -0.18650096]   [-1.32178623 -1.30550673]]


print('\n\n\n')
# ===========================================================
# 분류 모델을 사용
from sklearn.tree import DecisionTreeClassifier
ml = DecisionTreeClassifier(criterion='entropy', max_depth=5, random_state=0)
result = ml.fit(x_train, y_train)

# 분류 예측
y_pred = ml.predict(x_test)
print('예측값 :', y_pred)
print('실제값 :', y_test)
print('분류 정확도1 :', accuracy_score(y_test, y_pred))

# confusion matrix
con_mat = pd.crosstab(y_test, y_pred, rownames=['예측값'], colnames=['관측값'])
print(con_mat)
print('분류 정확도2 :', (con_mat[0][0] + con_mat[1][1] + con_mat[2][2]) / len(y_test))
print('분류 정확도3 :', ml.score(x_test, y_test))


# 시각화
# ==============================================================
from matplotlib.colors import ListedColormap
from matplotlib import font_manager
import matplotlib.pyplot as plt

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)      #그래프에서 한글깨짐 방지용
plt.rcParams['axes.unicode_minus'] = False  #마이너스부호 깨짐 방지

def plot_decision_region(X, y, classifier, test_idx=None, resolution=0.02, title=''):
    markers = ('s', 'x', 'o', '^', 'v')  # 점표시 모양 5개 정의
    colors = ('r', 'b', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    #print('cmap : ', cmap.colors[0], cmap.colors[1], cmap.colors[2])

    # decision surface 그리기
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    xx, yy = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))

    # xx, yy를 ravel()를 이용해 1차원 배열로 만든 후 전치행렬로 변환하여 퍼셉트론 분류기의 predict()의 안자로 입력하여 계산된 예측값을 Z로 둔다.
    Z = classifier.predict(np.array([xx.ravel(), yy.ravel()]).T)
    Z = Z.reshape(xx.shape) #Z를 reshape()을 이용해 원래 배열 모양으로 복원한다.

    # X를 xx, yy가 축인 그래프상에 cmap을 이용해 등고선을 그림
    plt.contourf(xx, yy, Z, alpha=0.5, cmap=cmap)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())

    X_test = X[test_idx, :]
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y==cl, 0], y=X[y==cl, 1], c=cmap(idx), marker=markers[idx], label=cl)

    if test_idx:
        X_test = X[test_idx, :]
        plt.scatter(X_test[:, 0], X_test[:, 1], c='', linewidth=1, marker='o', s=80, label='testset')

    plt.xlabel('표준화된 꽃잎 길이')
    plt.ylabel('표준화된 꽃잎 너비')
    plt.legend(loc=2)
    plt.title(title)
    plt.show()

x_combined_std = np.vstack((x_train, x_test))
y_combined = np.hstack((y_train, y_test))
plot_decision_region(X=x_combined_std, y=y_combined, classifier=ml, test_idx=range(105, 150), title='scikit-learn제공')




# graphviz
from sklearn import tree
from io import StringIO
dot_data = StringIO()  # 파일 흉내를 내는 역할(파일을 써야하는데 안쓰기 때문에)
tree.export_graphviz(ml, out_file=dot_data, feature_names=iris.feature_names[2:4])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())

graph.write_png('iris_tree.png')  # 차트 이미지 저장

# 이미지 가져오기
from matplotlib.pyplot import imread
img = imread('iris_tree.png')
plt.imshow(img)
plt.show()