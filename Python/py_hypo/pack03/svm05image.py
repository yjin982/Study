'''
    SVM 분류 모델로 얼굴 이미지 분류
'''
from sklearn.datasets import fetch_lfw_people
import matplotlib.pyplot as plt
from sklearn.metrics._classification import classification_report

faces = fetch_lfw_people(min_faces_per_person=60) # 한 사람당 60개 이미지
# print(faces) # {'data': array([[138.        , 135.66667   , 127.666664  , ...,   1.6666666 ,
print(faces.target_names) # ['Ariel Sharon' 'Colin Powell' 'Donald Rumsfeld' 'George W Bush' 'Gerhard Schroeder' 'Hugo Chavez' 'Junichiro Koizumi' 'Tony Blair']
print(faces.images.shape) # (1348, 62, 47)

# plot으로 이미지 보기
fig, ax = plt.subplots(3, 5)
# print(fig)  # Figure(640x480)
# print(ax.flat, '  ', len(ax.flat))  # 15

for i, axi in enumerate(ax.flat):
    axi.imshow(faces.images[i], cmap='bone')
    axi.set(xticks=[], yticks=[], xlabel=faces.target_names[faces.target[i]])  #xy 좌표값 없애고 얼굴 이름 출력
plt.show()

'''  PCA 주성분 분석
    이미지 전체가 아니라 주요 특징만을 추출한 이미지로 분류 작업을 수행 (cnn알고리즘)
'''
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline  # PCA 진행 후 SVC하도록 파이파라인 걸고

# 이미지 차원 축소
m_pca = PCA(n_components=150, whiten=True, random_state=0)  # whiten
m_svc = SVC()
model = make_pipeline(m_pca, m_svc)
print(model)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(faces.data, faces.target, random_state=1)
print(x_train.shape) # (1011, 2914)
print(y_train.shape) # (1011, )

model.fit(x_train, y_train)
yfit = model.predict(x_test)
# print('예측값 :', yfit[:10])


# 분류 보고서
from sklearn.metrics import classification_report
print(classification_report(y_test, yfit, target_names=faces.target_names))

# 분류 정확도
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
mat = confusion_matrix(y_test, yfit)
print('혼동행렬 :\n', mat)
print('분류 정확도 :', accuracy_score(y_test, yfit))  # 0.7952522255192879

# test 이미지 중 일부 자료로 예측한 값과 비교를 위한 시각화
# plt.imshow(x_test[0].reshape(62, 47), cmap='bone')


fig, ax = plt.subplots(4, 6)
# print(ax, len(ax))
for i, axi in enumerate(ax.flat):
    axi.imshow(x_test[i].reshape(62, 47), cmap='bone')
    axi.set(xticks=[], yticks=[])
    axi.set_ylabel(faces.target_names[yfit[i]].split()[-1], color='black' if yfit[i] == y_test[i] else 'red')
    fig.suptitle('pred', size=15)
plt.show()
 
    
# 클래스들 간의 오차행렬 시각화
import seaborn as sns
sns.heatmap(mat.T, annot=True, cbar=False, xticklabels=faces.target_names, yticklabels=faces.target_names)
plt.xlabel('True Label')
plt.xticks(rotation=15)
plt.ylabel('Predicted Label')
plt.show()
