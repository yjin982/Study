'''
    분류모델에서 과적합 방지를 위한 조치. 
      학습/평가 데이터로 분리 후 모델 작성
     k-fold를 이용해 모델 학습시 검증 작업 함께 실시
     PCA를 통한 feature 차원 축소
      학습 조기 종료
'''
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from bokeh.layouts import grid

iris = load_iris()
# print(type(iris))  #<class 'sklearn.utils.Bunch'>
# print(iris)
# print(iris.keys()) #dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names', 'filename'])

train_data = iris.data
train_lavel = iris.target
print(train_data[:3])
print(train_lavel[:3])

# 분류 모델
dt_clf = DecisionTreeClassifier()  # 다른 분류모델 적용 가능
dt_clf.fit(train_data, train_lavel)
pred = dt_clf.predict(train_data)  # train으로 학습하고 예측을 하게 해서 과적합 발생시키기
print('분류 정확도 :', accuracy_score(train_lavel, pred))


print()
# 과적합 방지 1 : train_test_split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=0)
dt_clf.fit(x_train, y_train)
pred2 = dt_clf.predict(x_test)
print('예측값 :', pred2[:3])
print('결과값 :', y_test[:3])
print('분류 정확도 : {:.3f}'.format(accuracy_score(y_test, pred2)))


print()
# 과적합 방지 2-1 : k겹(k-fold) 교차검증
# train_test_split 방법도 과적합 발생 가능함. ex)진짜 시험문제를 풀기 전에 모의 시험문제를 여러번(k) 풀어보는 것과 같다.
# train data 학습시 편중을 방지하기 위해 train data를 k번 만큼 쪼개서 학습 모델을 생성
from sklearn.model_selection import KFold
import numpy as np

feature = iris.data
label = iris.target
dt_clf = DecisionTreeClassifier(random_state=123)

kfold = KFold(n_splits=5) #KFold(n_splits=5, random_state=None, shuffle=False)

cv_acc = []
print('iris shape :', feature.shape)  #(150, 4)
# 전체 행 수가 150개. 학습 데이터는 그중 4/5(=120), 검증데이터는 1/5(=30)로 분할 해서 모델을 학습
n_iter = 0
for train_index, test_index in kfold.split(feature):
    # print(train_index, test_index)
    xtrain, xtest = feature[train_index], feature[test_index]
    ytrain, ytest = label[train_index], label[test_index]
    
    # 학습 및 예측
    dt_clf.fit(xtrain, ytrain)
    pred = dt_clf.predict(xtest)
    
    # 반복할 때마다 정확도 측정
    acc = accuracy_score(ytest, pred)
    n_iter += 1    
    train_size = xtrain.shape[0]
    test_size = xtest.shape[0]
    print('반복수:{}, 교차검증 정확도:{:.3f}, 학습데이터 크기:{}, 검증데이터 크기:{}'.format(n_iter, acc, train_size, test_size))
    
    cv_acc.append(acc)

print('평균 검증 정확도 : {:.3f}'.format(np.mean(cv_acc)))


print()
# 과적합 방지 2-2 : k겹(k-fold) 교차검증
# 불균형한 분포도※를 가진 label 집합을 위한 k-fold 교차검증 
# ※특정 레이블 값이 특이하게 많거나 적어서 분포가 왜곡된 데이터 집합. ex) 특정영화 리뷰에 빠 혹은 까의 리뷰가 많다. 혹은 악성메일 분류하는데 대부분은 정상메일이다. 등등
from sklearn.model_selection import StratifiedKFold 

feature = iris.data
label = iris.target
dt_clf = DecisionTreeClassifier(random_state=123)

skfold = StratifiedKFold(n_splits=5) #StratifiedKFold(n_splits=5, random_state=None, shuffle=False)

cv_acc = []
print('iris shape :', feature.shape)  #(150, 4)
# 전체 행 수가 150개. 학습 데이터는 그중 4/5(=120), 검증데이터는 1/5(=30)로 분할 해서 모델을 학습
n_iter = 0
for train_index, test_index in skfold.split(feature, label): #<<split에 label도 넣는게 다른 점
    # print(train_index, test_index)
    xtrain, xtest = feature[train_index], feature[test_index]
    ytrain, ytest = label[train_index], label[test_index]
    
    # 학습 및 예측
    dt_clf.fit(xtrain, ytrain)
    pred = dt_clf.predict(xtest)
    
    # 반복할 때마다 정확도 측정
    acc = accuracy_score(ytest, pred)
    n_iter += 1    
    train_size = xtrain.shape[0]
    test_size = xtest.shape[0]
    print('반복수:{}, 교차검증 정확도:{:.3f}, 학습데이터 크기:{}, 검증데이터 크기:{}'.format(n_iter, acc, train_size, test_size))
    
    cv_acc.append(acc)

print('평균 검증 정확도 : {:.3f}'.format(np.mean(cv_acc)))

# 과적합 방지 2-2 : 교차검증을 지원하는 함수를 사용
from sklearn.model_selection import cross_val_score
data = iris.data
label = iris.target

score = cross_val_score(dt_clf, data, label, scoring='accuracy', cv=5)
print('교차 검증별 정확도 :', np.round(score, 3))
print('평균 검증별 정확도 : {:.3f}'.format(np.mean(score)))


print()
# 과적합 방지 3 : 
# 모델 생성 시 최적의 속성값(hyper parameter)을 찾아 모델 생성. (DecisionTreeClassifier() 등 모델 함수에 들어갈 속성들의 최적의 값)
from sklearn.model_selection import GridSearchCV

# dict 타입으로 파라미터 후보값들을 준비
parameters = {'max_depth':[1, 2, 3], 'min_samples_split':[2, 3]}

grid_dtree = GridSearchCV(dt_clf, param_grid=parameters, cv=5, refit=True)  # refit 재학습
grid_dtree.fit(x_train, y_train)  # 내부적으로 복수개의 내부모델이 생성됨. 이를 모두 실행시켜 최적의 값을 찾는다.

import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)

scores_df = pd.DataFrame(grid_dtree.cv_results_)
print(scores_df)  # rank_test_score  가 1인 경우가 hyper parameter이다.
print('최적 속성값 :', grid_dtree.best_params_)
print('최고 정확도 : {:.3f}'.format(grid_dtree.best_score_))

hyper_dt_clf = grid_dtree.best_estimator_  #최적의 속성값으로 모델을 생성
print(hyper_dt_clf)
hyper_pred = hyper_dt_clf.predict(x_test)
print(hyper_pred[:3])
print('hyper_df_clf 정확도 : {:.3f}'.format(accuracy_score(y_test, hyper_pred)))
