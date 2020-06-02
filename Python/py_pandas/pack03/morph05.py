'''
    BOW(Bag Of Word)
      문서가 가지는 모든 단어, 문맥, 순서를 무시하고 일괄적으로 단어에 대해 빈도수를 부여해 feature vector화를 함    
      count(CountVectorizer) 기반과 TF-IDF(TfidfVectorizer) 기반으로 나뉜다.
    
    CountVectorizer - 문서를 토큰 리스트화 후, 각 문서에서 토큰의 출현빈도를 카운트하고 BOW 인코딩 벡터를 만듦
    TfidfVectorizer - 단어의 가중치를 조정한 BOW 벡터를 만듦
    [※ feature - 머신러닝에서 입력변수]
'''
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

count_vec = CountVectorizer(analyzer='word')#min_df 최소 빈도수
contents = ['How to format my hard disk', 'hard disk format format problems']
#            [[   1    1    1       1     1 0 1]    [1      2      1  0 0    1          0     ]]
a = count_vec.fit_transform(contents) #count 벡터 생성
print(a)
print(count_vec.get_feature_names()) #['disk', 'format', 'hard', 'how', 'my', 'problems', 'to']
print(a.toarray()) #[[1 1 1 1 1 0 1] [1 2 1 0 0 1 0]]
print()


tfidf_vec = TfidfVectorizer(analyzer='word', min_df=1)
b = tfidf_vec.fit_transform(contents)
print(b)
print(tfidf_vec.get_feature_names())
print(b.toarray())