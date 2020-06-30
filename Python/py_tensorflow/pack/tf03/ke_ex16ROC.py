'''
    iris dataset으로 best 분류 예측 모델 작성, ROC 커브 출력
'''
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import roc_curve, auc
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing.tests.test_data import n_features

''' data load '''
iris = load_iris()

x = iris.data   # == iris['data']  <= feature, <class 'numpy.ndarray'>
y = iris.target # == species = {0, 1, 2} <= label, <class 'numpy.ndarray'>

names = iris.target_names  # ['setosa' 'versicolor' 'virginica']
feature_names = iris.feature_names # ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']


''' label one hot encode '''
onehot = OneHotEncoder() # 또는 keras의 to_categorical(), numpy의 np.eye(), pandas의 pd.get_dummies()
y = onehot.fit_transform(y[:, np.newaxis]).toarray()
# print(y.shape)  # (150,) -> (150, 3)

''' feature 표준화 : 모델의 성능 향상'''
scaler = StandardScaler()
x_scale = scaler.fit_transform(x)
# print(x_scale[:2])

''' train test '''
x_train, x_test, y_train, y_test = train_test_split(x_scale, y, test_size=0.3, random_state=1)
n_features = x_train.shape[1]  
n_classes = y_train.shape[1]   # x(4)와 y(3)의 열값 취함 == 입력수 4, 출력수 3


''' n개의 모델을 생성 '''
def create_custom_model(input_dim, output_dim, out_nodes, n, model_name='model'): # n=히든레이어 갯수
    def create_model():
        model = Sequential(name=model_name)
        
        for _ in range(n):
            model.add(Dense(units=out_nodes, input_dim=input_dim, activation='relu'))
        
        model.add(Dense(units=output_dim, activation='softmax'))
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
        
        return model
    
    return create_model

models = [create_custom_model(input_dim=n_features, output_dim=n_classes, out_nodes=10, 
                                                n=n, model_name='model_{}'.format(n)) for n in range(1, 4)]

# 모델 생성 확인
# for create_model in models:
#     print()
#     create_model().summary()

''' 모델 훈련 '''
history_dict = {}
for create_model in models:
    model = create_model()
    print('Model name : {}'.format(model.name)) # 모델 이름 확인
    
    historys = model.fit(x_train, y_train, batch_size=5, epochs=50, verbose=0, validation_split=0.3)
    
    score = model.evaluate(x_test, y_test, verbose=0)
    print('test dataset loss : {:.3f}, acc : {:.3f}\n'.format(score[0], score[1]))
    
    history_dict[model.name] = [historys, model]
    

''' 시각화 '''
# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
# 
# for model_name in history_dict:
#     print('{} history_dict : {}'.format( model_name, history_dict[model_name][0].history['acc'] )) # 확인
#     val_acc = history_dict[model_name][0].history['val_acc']   # validation data로 값 얻기
#     val_loss = history_dict[model_name][0].history['val_loss']
#     
#     ax1.plot(val_acc, label=model_name)
#     ax2.plot(val_loss, label=model_name)
# 
# ax1.set_ylabel('validaton acc')
# ax2.set_ylabel('validaton loss')
# ax2.set_xlabel('epochs')
# ax1.legend()
# ax2.legend()
# plt.show()


''' ROC 커브 작성 : 모델 성능을 확인(분류기에 대한 성능평가 기법 중 하나) '''
# plt.figure()
# plt.plot([0, 1], [0, 1], 'k--')
# 
# for model_name in history_dict:
#     model = history_dict[model_name][1]
#     y_pred = model.predict(x_test)
#     
#     fpr, tpr, _ = roc_curve(y_test.ravel(), y_pred.ravel())  # 실제값과 예측값을 차원 축소해서 넘겨줌
#     plt.plot(fpr, tpr, label='{}, AUC value : {:.3f}'.format(model_name, auc(fpr, tpr)) )
#     
# plt.xlabel('fpr') # false positive ratio
# plt.ylabel('tpr')
# plt.title('ROC Curve')
# plt.legend()
# plt.show()

''' KerasClassifier를 이용해서 모델 n개를 교차 검증할 수 있다.'''
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score # k-fold  교차검증이 필요
create_model = create_custom_model(input_dim=n_features, output_dim=n_classes, out_nodes=10, n=3)

estimator = KerasClassifier(build_fn=create_model, epochs=50, batch_size=10, verbose=0) # 모델 생성
scores = cross_val_score(estimator, x_scale, y, cv=10)
print('scores : {}'.format(scores))
print('accuracy mean : {:.3f}, std : (+/- {:.3f})'.format(scores.mean(), scores.std()))


print('\n\n')
''' 위 결과 모델 3(4개의 레이어 사용)이 가장 우수한 모델로 판정 '''
model = Sequential()
model.add(Dense(units=10, activation='relu', input_dim=4))
model.add(Dense(units=10, activation='relu'))
model.add(Dense(units=10, activation='relu'))
model.add(Dense(units=3, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])

model.fit(x_train, y_train, batch_size=10, epochs=50, verbose=2)
print(model.evaluate(x_test, y_test))

y_pred = np.argmax(model.predict(x_test), axis=1).reshape(-1, 1)  # onehot을 원래 결과값으로
y_real = np.argmax(y_test, axis=1).reshape(-1, 1)
print('예측값 : {}'.format( y_pred.flatten() ))
print('실제값 : {}'.format( y_real.flatten() ))
print('분류 실패 수 : {}'.format( (y_pred.flatten() != y_real.flatten()).sum() ))


print('\n\n')
from sklearn.metrics import confusion_matrix, classification_report
from sklearn import metrics
print('- confusion matrix\n{}'.format( confusion_matrix(y_real, y_pred) ))
print('- metrices accuracy : {:.3f}'.format( metrics.accuracy_score(y_real, y_pred) ))
print('- classification_report\n{}'.format( classification_report(y_real, y_pred) ))

print()
''' 새 값으로 분류 '''
new_x = [ [5.1, 3.5, 1.4, 0.2], [1.9, 3.1, 1.4, 1.2], [1.9, 3.9, 3.4, 2.2] ]
new_x = scaler.fit_transform(new_x)
new_pred = model.predict(new_x)
print('new x predict : {}'.format( np.argmax(new_pred, axis=1).reshape(-1, 1).ravel() ))
