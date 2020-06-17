'''
    BMI(체질량지수) 식을 이용해 무작위 자료를 작성 후 분류 모델에 적용하기
    BMI = 몸무게(kg) / 키**2(m)   75 / (1.7 * 1.7) = 25.95155709342561
'''

# import random
# def calc_bmi(h, w):
#     bmi = w / (h / 100) ** 2
#     
#     if bmi < 18.5: return 'thin'
#     if bmi < 23: return 'normal'
#     return 'fat'
# 
# # bmi 데이터 생성 후 파일로 저장
# fp = open('bmi.csv', 'w')
# fp.write('height,weight,label\n')
# random.seed(123)
# 
# # 무작위로 데이터 생성
# cnt = {'thin':0, 'normal':0, 'fat':0}
# for i in range(50000):
#     h = random.randint(150, 200)
#     w = random.randint(35, 100)
#     label = calc_bmi(h, w)
#     cnt[label] += 1
#     fp.write('{},{},{}\n'.format(h,w,label))
# fp.close()
# 
# print('saved', cnt)


# SVM으로 BMI 데이터 분류
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

tbl = pd.read_csv('bmi.csv')
print(tbl.tail(3))

# w, h의 단위가 다르기(kg과 cm) 때문에 정규화
label = tbl['label']
w = tbl['weight'] / 100  # 0~1사이로 정규화. 최대를 100으로 잡았기 때문에
h = tbl['height'] / 200

wh = pd.concat([w, h], axis=1)
print(wh.head(3))  # wh가 문제지 label이 답지가 됨.


# train / test 분리
data_train, data_test, label_train, label_test = train_test_split(wh, label)
# print(data_train.shape, data_test.shape) # (37500, 2) (12500, 2)


# model
# model = svm.SVC(C=10).fit(data_train, label_train)  # C= 숫자가 클수록 정확도 ↑
model = svm.LinearSVC(C=0.1).fit(data_train, label_train)  # SVC에 비해 속도가 향상되고 옵션도 다양한 진화된 버전
pred = model.predict(data_test)
print('예측값 :', pred)
print('실제값 :', label_test.values)

# 분류 정확도 확인
ac_score = metrics.accuracy_score(label_test, pred)
print('분류 정확도 :', ac_score)  # SVC = 0.99688
cl_report = metrics.classification_report(label_test, pred)
print('분류 보고서 :\n', cl_report)


# 시각화
tbl = pd.read_csv('bmi.csv', index_col=2)  # 3번째 컬럼을 인덱스로 넣음
# print(tbl.head(3))
fig = plt.figure() # 이미지 저장 선언

def scatter_func(lbl, color):
    b = tbl.loc[lbl]
    plt.scatter(b.weight, b.height, c=color, label=lbl)
    
scatter_func('fat', 'lightpink')
scatter_func('normal', 'skyblue')
scatter_func('thin', 'yellowgreen')
plt.legend()
# plt.savefig('bmi_test.png')
# plt.show()


'''
    ※ k-fold 교차검증 : 총 데이터 갯수가 적은 데이터 셋에 대해서 정확도 향상, train-test 나눠도 과적합 발생시 사용 가능, 과적합 방지
    기존의 train - test 나눈 데이터 셋에서 train 데이터셋을 다시 또 k개로 쪼개서 k-1개는 train 데이터, 남은 하나는 검증 데이터로 활용하는 것을 k번 반복
   ===================================='''
from sklearn import model_selection
cross_vali = model_selection.cross_val_score(model, data_train, label_train, cv=5) #cv=k 몇겹으로 할지
print('각각(5-fold)의 검증 정확도 :', cross_vali)
print('평균(5-fold) 검증 정확도 :', cross_vali.mean())

# ac_score 값과 cross_vali 값 차이가 많이 나면 과적합 상태라는 것