#형태소 분석 : KoNLpy 사용
install.packages("KoNLP")
install.packages("tm")
install.packages("Sejong")
install.packages("hash")
install.packages("tau")
install.packages("devtools")

library(rJava)
library(KoNLP)

useNIADic()   #형태소 분석 사전
sen <- "최광지 홍패는 고려가 멸망하기 3년 전인 창왕 1년(1389) 발급한 과거 합격증이다. 최광지는 그해 문과에서 전체 6등에 해당하는 '병과 제3인'에 올랐다. 홍패는 홍화씨 등으로 붉게 염색한 종이에 발급한 문과·무과 합격증으로, 생원·진사 시험 합격자에게는 흰 종이에 쓴 문서인 백패를 줬다."
extractNoun(sen)  #명사만 추출

SimplePos22(sen)  #품사 태깅
SimplePos09(sen)

sen2 <- "아버지는 방으로 들어가시고, 고양이는 방에서 살금살금 돈을 물고 나온다."
ss = SimplePos09(sen2)


library(stringr)
ext_n = str_match(ss, '([가-힣]+)/N')
ext_n

ext_m = str_match(ss, '([가-힣]+)/M')
ext_m

