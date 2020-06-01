''' 
    웹 뉴스 정보로 단어 임베딩하여 유사 단어 파악하기
'''
import pandas as pd
from konlpy.tag import Okt 

okt = Okt()

#다음 뉴스 웹에서 긁어와도 되나 텍스트파일로 저장하고 함
with open('daumnews.txt', mode='r', encoding='utf8') as f:
    #print(f.read())
    lines = f.read().split('\n') #엔터로 줄을 나눔
    print(len(lines))
      
wordDic = {}
  
for line in lines:
    datas = okt.pos(line)
    print(datas) #[('중국', 'Noun'), ('시', 'Modifier'), ('노', 'Noun'), ('백', 'Suffix') ...
    for word in datas:
        if word[1] == 'Noun': #명사일 경우
            print(word[0])
            #print(word[0] in wordDic) #wordDic안에 해당 단어가 있으면 True
            if not(word[0] in wordDic):
                wordDic[word[0]] = 0
            else:
                wordDic[word[0]] += 1
print(wordDic) #{'중국': 10, '노': 15, '코로나': 14, '백신': 16, '효과': 2, ...
  
  
keys = sorted(wordDic.items(), key=lambda x:x[1], reverse=True)
print(keys) #[('백신', 16), ('노', 15), ('코로나', 14), ('중국', 10),...
  
  
#dataframe에 담기
wordlist = []
countlist = []
  
for word, count in keys[:20]:#상위 20개만
    wordlist.append(word)
    countlist.append(count)
      
# print(wordlist)
# print(countlist)
df = pd.DataFrame()
df['word'] = wordlist
df['count'] = countlist
print(df)
 
'''
    단어 임베딩을 위해 품사 일부 제외
'''
results = []
with open('daumnews.txt', mode='r', encoding='utf8') as f:
    lines = f.read().split('\n') #엔터로 줄을 나눔
     
    for line in lines:
        datas = okt.pos(line, stem=True)
        #print(datas)
        temp = []
        for word in datas:
            if not word[1] in ['Punctuation', 'Determiner', 'Josa', 'Modifier', 'Number', 'Suffix', 'Alpha', 'Verb']:
                temp.append(word[0])
        temp2 = (' '.join(temp))
        results.append(temp2)
         
print(results)

    
    
    
#df를 파일로 저장, #저장 이후 주석처리
# with open('daumnews2.txt', mode='w', encoding='utf8') as fw:
#     fw.write('\n'.join(results))
#     print('저장 성공')


   
'''
    단어 임베딩(word embedding) 중 Word2vec(https://word2vec.kr/search/)
'''
from gensim.models import word2vec #pip install gensim

# # simple example
# sentence = [['python', 'language', 'program', 'computer', 'say']] #말뭉치
# model = word2vec.Word2Vec(sentence, min_count=1)
# # print(model.wv.most_similar('python')) #절대값 1에 가까울수록 친밀
# # [('computer', 0.13192933797836304), ('program', 0.047326263040304184), ('language', 0.004919953644275665), ('say', -0.22897902131080627)]
# # ==========


'''
    저장된 문서(daumnews2.txt)를 읽어 유사 단어 파악
'''
genObj = word2vec.LineSentence('daumnews2.txt') 
print(genObj) #<gensim.models.word2vec.LineSentence object at 0x0000028FB9289B88>
model = word2vec.Word2Vec(genObj, size=100, window=10, min_count=2, sg=1) 
# size:벡터 차원, window:주변단어 앞뒤로 10개 참조, min_count:출연 빈도 2미만인 것 제외, sg:분석방법 1 for skip-gram, otherwise CBOW.
# 중심단어로 주변단어를 예측 - skip gram, 주변단어로 중심단어를 예측 - CBOW
print(model) #Word2Vec(vocab=146, size=100, alpha=0.025)
model.init_sims(replace=True) #메모리 사용시 필요없는 메모리는 해제


# #모델은 한번 만들어 학습시키고 나면 저장하고 사용
# try:
#     model.save('daumnews_model.model') #모델 저장
#     print('ok')
# except Exception as e:
#     print('error ', e)


# 모델 읽기
model = word2vec.Word2Vec.load('daumnews_model.model')

# 단어별 유사도 확인
print(model.wv.most_similar(positive='백신'))
print(model.wv.most_similar(positive=['백신'], topn=3)) #가장 가까운 3개
print(model.wv.most_similar(positive=['백신', '교회'], negative=['개발', '확진'], topn=5)) #positive=[''] 이런 단어가 있을 확률, negative 이런 단어가 없을 확률
