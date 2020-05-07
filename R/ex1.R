# 변수 : type을 선언하지 않음
va <- 1
va <- 2
va = 3
4 -> va
cat(va)
va.first <- 10 # .이 있어도 그냥 변수명일뿐 객체 변수 멤버 지정 ㄴㄴ
va.second <- 20
cat(va.first + va.second)

rnorm(10) #난수 10개 발생
mean(rnorm(10)) # 평균

#데이터 유형
kbs <- 9
object.size(kbs)  #56 bytes
typeof(kbs)
typeof(9)
typeof(9.5)  #전부  "double" = 기본이 double
is(kbs)  #"numeric" "vector"  숫자형, 1차형배열의 요소

mbc <- as.integer(kbs)
is(mbc)     #"integer" "double" "numeric" "vector"  "data.frameRowLabels"
mbc <- 5L   # 정수
is(mbc)
typeof(mbc)  #"integer"
is.integer(mbc)

ss <- '홍길동동'
is.character(ss)

b <- TRUE
b <- T  #대문자로 쓰기, 비권장
b
is.logical(b)

aa <- NA #결측값 (값이 입력되지 않은 상태) missing value
is.na(aa)

sum(2,3)
sum(2,3,NA)  #NA 결측값이 있어서 계산 불가
sum(2,3, NA, na.rm = TRUE) # NA빼고 계산

typeof(NULL) #"NULL"
typeof(NA)   #"logical"
typeof(NaN)  #"double"
0 / 0        #NaN
Inf + -Inf   #NaN
Inf - Inf    #NaN

sum(2,3 NULL)    #에러
sum(2,3,NA)      #NA
sum(2,3, NaN)    #NaN

z <- 5.3 - 3i
z       #복소수
Re(z)   #실수만
Im(z)   #허수만
is.complex(z)


##Factor (요인형 변수)
kbs <- c('second', 'first', 'third', 'second')  #문자열 벡터
kbs     #"second" "first"  "third"  "second"
is.factor(kbs)      #FALSE
is.character(kbs)   #TRUE

mbc <- as.factor(kbs)
mbc     #second first  third  second   Levels: first second third
is.factor(mbc)   #TRUE
levels(mbc)      #"first"  "second" "third" 
summary(mbc)     # [1] first second  third  |  [2] 1      2      1 

plot(kbs)   #error 차트 그리기x
plot(mbc)   #차트 그리기 o

mbc2 <- factor(mbc, levels = c('third', 'first', 'second'))
mbc2  #Levels: third first second
plot(mbc2)
str(mbc2)  #Ordinal
str(mbc)   #Nominal


f <- function(){
  return('good')
}
f()
typeof(f)   #"closure"
