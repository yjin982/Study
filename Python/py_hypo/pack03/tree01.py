'''
    Decision Tree
      트리구조의 그래프를 사용하여 최적의 결정을 할 수 있도록 하는 알고리즘 
      여러 가지 규칙을 순차적으로 적용하면서 독립 변수 공간을 분할하는 분류 모형이다. 분류(classification)와 회귀 분석(regression)에 모두 사용될 수 있다. 해석이 쉽다.
      Information Gain: 지정된 속성이 얼마나 잘 training example들간을 구분하는가에 대한 수치.
      Entropy: example들의 집합에서의 혼합성(impurity)을 나타냄. 노이즈가 정도를 수치로 표현. 0에 근사할수록 우수   ※https://frontjang.info/486
'''
from sklearn import tree
import pydotplus
import collections
from sklearn.metrics import accuracy_score

# 키와 머리길이로 성별 구분
x = [[180, 15], [177, 54], [156, 35], [174, 5], [166, 33]]
y = ['man', 'woman', 'woman', 'man', 'woman']


# model
model = tree.DecisionTreeClassifier(criterion='entropy', max_depth=None, random_state=0).fit(x, y)
print('훈련정확도 : {:.3f}'.format(model.score(x, y)))

pred = model.predict(x)
print(pred)
print('분류정확도 :', accuracy_score(y, pred))

# 새로운 값으로 예측
newdata = [[171, 88]]
newpred = model.predict(newdata)
print('예측 :', newpred)

# 시각화
label_names = ['height', 'hair_length']
dot_data = tree.export_graphviz(model, feature_names=label_names, filled=True, rounded=True)
graph = pydotplus.graph_from_dot_data(dot_data)
colors = ('red', 'orange')
edges = collections.defaultdict(list)

for e in graph.get_edge_list():
    edges[e.get_source()].append(int(e.get_destination()))
    
for e in edges:
    edges[e].sort()
    for i in range(2):
        dest = graph.get_node(str(edges[e][i]))[0]
        print('dest :', dest)
        dest.set_fillcolor(colors[i])

graph.write_png('tree.png')  # 차트 이미지 저장

# 이미지 가져오기
from matplotlib.pyplot import imread
import matplotlib.pyplot as plt
img = imread('tree.png')
plt.imshow(img)
plt.show()