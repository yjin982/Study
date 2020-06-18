'''
    RandomForest 분류분석 
      여러 개의 의사결정트리를 조합(ensemble)해 분류 예측 성능을 극대화
'''
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)

df = pd.read_csv('../testdata/titanic_data.csv')
print(df.head(3), df.shape)  # (891, 12)
print(df.isnull().sum()) # null인 값 갯수

# df = df.drop(['Cabin', 'Embarked'], axis=1)
# print(df.isnull().sum())
# df = df.dropna(subset=['Age'])
df = df.dropna(subset=['Age', 'Cabin', 'Embarked'])
print(df.shape)

df_x = df[['Pclass', 'Age', 'Sex']]
print(df_x.head(3))

# Scaling
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
df_x.loc[:, 'Sex'] = LabelEncoder().fit_transform(df_x['Sex']) # female:0, male:1
df_y = df['Survived']

# Pclass를 first.class, second.class, third.class
import numpy as np
df_x2 = pd.DataFrame(OneHotEncoder().fit_transform(df_x['Pclass'].values[:, np.newaxis]).toarray(), columns=['f_class', 's_class', 't_class'], index=df_x.index)
df_x = pd.concat([df_x, df_x2], axis=1)
print(df_x.head(3))

train_x, test_x, train_y, test_y = train_test_split(df_x, df_y)
model = RandomForestClassifier(criterion='entropy', n_estimators=500) # n_estimators의사결정 트리 수
fit_model = model.fit(train_x, train_y)
pred = fit_model.predict(test_x)

print('예측값 :', pred[:5])              # [0 0 0 0 0]
print('실제값 :', test_y.values[:5]) # [0 1 0 1 1]
print('분류 정확도1 :', sum(test_y == pred) / len(test_y))


from sklearn.metrics import accuracy_score
print('분류 정확도2 :', accuracy_score(test_y, pred))