'''
    종양 관련 데이터로 종양 유무 분류
'''
from sklearn.datasets import load_breast_cancer
import numpy as np
from sklearn.metrics._classification import classification_report

cancer = load_breast_cancer()

x = cancer.data
y = cancer.target
print(cancer.feature_names)
print(x[:2], y[:2])
print(np.unique(y))  # 0, 1

# 훈련 테스트 데이터 분리
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y)

# 표준화 작업
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x_train)
scaler.fit(x_test)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)
print(x_train[:1])


from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), random_state=1)
mlp.fit(x_train, y_train)
pred = mlp.predict(x_test)
print('예측값 :', pred[:20])
print('실제값 :', y_test[:20])
print('분류 정확도 : {:.3f}'.format(mlp.score(x_test, y_test)))


from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))
