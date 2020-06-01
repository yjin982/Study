''' 
    한글 형태소(단어로서 의미가 있는 최소한의 단위) 분석
    konlpy 라이브러리로 형태소 분석 가능. 품사 태깅
    corpus(말뭉치) : 자연어 처리를 위해 제공된 언어(문서) 집합
    
    실시간처리에는 부적합(속도가 느림)
'''

from konlpy.tag import Kkma
kkma = Kkma()
# print(kkma.sentences('여러분, 안녕하세요. 반갑습니다.')) # 이거도 corpus, 문장
# print()
# print(kkma.nouns(u'오늘 폭염이 주춤했지만 일부지방은 폭염 특보 속에 35도 안팎의 찜통더위가 기승을 부렸는데요.자세한 날씨, YTN 중계차 연결해 알아보겠습니다.')) #명사만
# print()
# print(kkma.pos(u'오류보고는 실행환경, 에러메세지와 함께'))#품사태깅


#==============
from konlpy.tag import Okt
okt = Okt()
a = okt.pos('멋진 봄은 엄청 무더운 여름과 한들한들 시원한 가을의 중간 계절이다.')
print(a)
a2 = okt.pos('멋진 봄은 엄청 무더운 여름과 한들한들 시원한 가을의 중간 계절이다.', stem=True) #형용사의 원형(어근)으로 출력
print(a2)
b = okt.nouns('멋진 봄은 엄청 무더운 여름과 한들한들 시원한 가을의 중간 계절이다.')
print(b)

'''
불용어 제거할 수 있는 라이브러리가 포함
불용어(stopwords) : [영어에서 the, is, a 등] 갖고 있는 데이터에서 유의미한 단어 토큰만을 선별하기 위해서는 큰 의미가 없는 단어 토큰을 제거하는 작업이 필요하다. 여기서 큰 의미가 없다라는 것은 문장 내에서는 자주 등장하지만 문장을 분석하는 데 있어서는 큰 도움이 되지 않는 단어들을 말한다
'''
import nltk
parser_ko = nltk.RegexpParser("NP:{<A.*>*<None>*}")#정규표현식으로 파서
p_ko = parser_ko.parse(a)
print(p_ko)
p_ko.draw()
