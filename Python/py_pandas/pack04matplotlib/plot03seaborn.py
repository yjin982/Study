'''    iris dataset으로 시각화    '''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


iris_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/iris.csv")
print(iris_data.info())


'''    1, 3번 칼럼으로 산점도 그리기    '''
# plt.scatter(iris_data['Sepal.Length'], iris_data['Petal.Length'])
# plt.xlabel('Sepal.Length')
# plt.ylabel('Petal.Length')
# plt.title('iris data')
# plt.show()


'''    밀도 추정 곡선    '''
# from pandas.plotting import scatter_matrix
# iris_col = iris_data.loc[:, 'Sepal.Length':'Petal.Width'] #Species 칼럼만 제외한 데이터
# scatter_matrix(iris_col, diagonal='kde') #hist, bar, ... 등을 쓸 수 있는데 그중에 kde(커널 밀도 추정 곡선)
# plt.show()


'''    꽃의 종류별 색 부여 후 산점도(산포도)로 출력    (산포도 숫자로 표현하면 상관계수)'''
# print(iris_data['Species'].unique()) #['setosa' 'versicolor' 'virginica']
colors = []
for s in iris_data['Species']:
    choice = 0
    if s == 'setosa':
        choice = 1
    elif s == 'versicolor':
        choice = 2
    elif s == 'virginica':
        choice = 3
    colors.append(choice)
    
# plt.scatter(iris_data['Sepal.Length'], iris_data['Petal.Length'], c=colors)
# plt.xlabel('Sepal.Length')
# plt.ylabel('Petal.Length')
# plt.title('iris data')
# plt.show()

# sns.pairplot(iris_data, hue='Species', height=2)
# plt.title('Seaborn iris data')
# plt.show()

'''    rugplot    '''
x = iris_data['Sepal.Length'].values
sns.rugplot(x)
plt.show()

'''    커널 밀도 함수    '''
sns.kdeplot(x)
plt.show()

