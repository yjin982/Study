'''
    sklearn이 제공하는 Perceptron
'''
from sklearn import datasets
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
x = iris.data[:, [2, 3]]
y = iris.target
print(x[:3])
print(y[:3])

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)

sc = StandardScaler().fit(x_train)
x_train_std = sc.transform(x_train)
x_test_std = sc.transform(x_test)
print(x_train_std[:3])


# perceptron 객체 생성
ml = Perceptron(max_iter=100, random_state=1)  # 학습횟수 100
ml.fit(x_train_std, y_train)

# predict
y_pred = ml.predict(x_test_std)
print('실제값 :', y_test[:20])
print('예측값 :', y_pred[:20])
print('총 갯수 : %d, 오류 : %d'%(len(y_test), (y_test != y_pred).sum()))
print('분류 정확도 : {:.3f}'.format(accuracy_score(y_test, y_pred)))

