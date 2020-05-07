#명목형 자료로 도수분포표 
df <- read.csv("testdata/ex_studentlist.csv")
df

#혈액형 자료로 빈도수
freq <- table(df$gender, df$bloodtype)
freq

rfreq <- prop.table(freq)
rfreq
rtable <- rbind(freq, rfreq)

rtable <- addmargins(rtable, margin = 1) #1:열에 대해서 소계
rtable <- addmargins(rtable, margin = 2) #2:행에 대해서 소계, margin안 주면 행열 모두에 소계 출력
rtable

#연속형 자료로 구간 나누기
factorHeight <- cut(df$height, breaks = 4)
factorHeight  #괄호는 이상이하, 대괄호는 미만초과

freqHeight <- table(factorHeight)
freqHeight <- rbind(freqHeight, prop.table(freqHeight)) #상대도수 행 추가
freqHeight
rownames(freqHeight)[2] <- "relaHeight"

cumFreq <- cumsum(freqHeight[2, ]) #누적 상대도수
cumFreq

freqHeight <- rbind(freqHeight, cumFreq)
rownames(freqHeight) <- c("도수", "상대도수", "누적도수")

#행의 합
freqHeight <- addmargins(freqHeight, margin = 2)



#문자열 처리와 정규표현식
ex_str <- "abcd한국12ABC345abc123-4567문자열"

#정규 표현식
sub("abc", "kbs_mbc", ex_str) #sub(pattern, replacement, 대상 문자열), 처음 하나만
gsub("abc", "kbs_mbc", ex_str) #gsub(pattern, replacement, 대상 문자열) 전체
gsub("[0-9]", "수", ex_str)

install.packages("stringr")
library(stringr)
str_extract(ex_str, "ab")
str_extract_all(ex_str, "ab")
str_extract_all(ex_str, "[0-9]")
str_extract_all(ex_str, "[0-9]+")
str_extract_all(ex_str, "[0-9]*")
str_extract_all(ex_str, "[0-9]?")
str_extract_all(ex_str, "[0-9]{2}")
str_extract_all(ex_str, "[0-9]{2,4}") #2,4 스페이스 주면 에러
str_extract_all(ex_str, "a")
str_extract_all(ex_str, "['a', 'b']")
str_extract_all(ex_str, "[^'a', 'b']")
str_extract_all(ex_str, "[^0-9]")
str_extract_all(ex_str, "['a-z']")
str_extract_all(ex_str, "['a-zA-Z']")
str_extract_all(ex_str, "['가-힣]")
str_extract_all(ex_str, "^a") #^은 [] 밖에 있으면 그걸로 시작하는, [] 안에 있으면 그걸 제외하는 
str_extract_all(ex_str, "^b")
str_extract_all(ex_str, "a$")
str_extract_all(ex_str, "열$")

str_sub(ex_str, 3, 6)


#문자열 더하기
paste('a', 'b')
paste('a', 'b', sep = '')
paste('a', 'b', sep = '+')
paste(rep('문제', 5))
paste(rep('문제', 5), 1:5, sep = '')
paste('Today is', date())

paste0('a', 'b')

d <- c("김길동", "신선해", "김길동")
str_replace(d, "김길동", "홍길동")
str_c("a", "bc")
str_split("aa-bb-cc", "-")
