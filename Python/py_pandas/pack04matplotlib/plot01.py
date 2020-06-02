'''    시각화    '''
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')            #한글깨짐 방지
plt.rcParams['axes.unicode_minus'] = False  #마이너스부호 깨짐 방지

x = ['서울', '대전', '부산']  #문자열 list, tuple 가능, set은 불가
y = [5, 3, 7]
 
plt.plot(x, y)#가장 간단한 라인 플롯
plt.xlim([-1, 3]) #최소, 최대
plt.ylim([0, 10])
plt.yticks(list(range(0, 11, 3))) #레이블 값을 0~10까지 3씩
plt.show()



data = np.arange(1, 11, 2)  
print(data) #구간이 4개가 생김
plt.plot(data) #y축 값만 준 경우
#좌표 찍기
x = [0, 1, 2, 3, 4]
for a, b in zip(x, data):
    plt.text(a, b, str(b)) #(x,y) 지점에 data 값으로 좌표찍기
plt.show()     #x축은 구간값이 자동으로    
 
 
plt.plot(data)
plt.plot(data, data, c='r') #같은값 두개 줬을때
plt.show()


x = np.arange(10)
y = np.sin(x) #x에 대한 사인값
print(x, y)
plt.plot(x, y) #꺽은 선으로 나옴
plt.plot(x, y, 'bo') #'bo' 파란 점(산점도)
plt.plot(x, y, 'r+') #'r+'빨간 +모양 점
plt.plot(x, y, 'g:') #'g--' 초록색 --선, 'g:' 초록색 점선
# c="색", lw="선두께" linewidth="선두께", marker='마커종류', 'ms'='마커크기'  markersize='마커크기'  ... ...
plt.show()


'''    Hold : 하나의 차트 영역에 복수의 plot을 지정. 그림을 겹쳐 출력 가능    '''
x = np.arange(0, np.pi*3, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.plot(x, y_sin, 'r')
plt.plot(x, y_cos, 'b')
plt.scatter(x, y_cos) #산점도
plt.xlabel('x축')
plt.ylabel('y축')
plt.title('Hold 가능')
plt.legend(['sine', 'cosine']) #범례
plt.show()


'''    subplot : figure를 여러개로 나눔    '''
plt.subplot(2, 1, 1)
plt.plot(x, y_sin)
plt.title('Sine')
 
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')
plt.show()


'''    그래프를 파일로 저장후 읽기    '''
name = ['a', 'b', 'c', 'd', 'e']
kor = [80, 55, 78, 88, 90]
eng = [60, 70, 98, 85, 40]

plt.plot(name, kor, 'ro-')
plt.plot(name, eng, 'bs-')
plt.ylim([0, 100])
plt.title('시험 점수')
plt.legend(['국어', '영어'], loc=4)
plt.grid(True)

fig = plt.gcf()   #차트를 이미지로 저장할 준비
plt.show()
fig.savefig('aaa.png') #이미지 저장

#이미지 읽기
from matplotlib.pyplot import imread
img = imread('aaa.png')
plt.imshow(img)
plt.show()