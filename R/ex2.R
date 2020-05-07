#자료형과 자료구조
x <- TRUE
x <- 5
x <- 5L
cat(mode(x), ' ', class(x))   #mode 성격, class 자료구조

ls()       #사용중인 변수
ls.str()   #사용중인 변수 자세히

rm(aa)        #변수 지우기
rm(b)
rm(list=ls()) #모든 변수 지우기 ,메모리는 확보되어 있는 상태, 가비지컬렉터가 나중에 삭제
gc()          #가비지컬렉터 콜


#package 사용
available.packages()
dim(available.packages())

install.packages("plyr")
#require(plyr)
library(plyr)
search()
ls("package:plyr")
remove.packages('plyr')


data()     #R이 제공하는 기본 데이터셋 목록 확인
Nile
hist(Nile, freq = FALSE)
lines(density(Nile))

?sum
help('mean')


#자료형 Vector : 1차원 배열의 자료구조
year <- 2020
is(year)
name <- 'tom'
is(name)
is.vector(name)  #TRUE
is.vector(year)  #TRUE

seq(1, 5)   #1 2 3 4 5   인덱스가 1부터
seq(1, 5, 2)
seq(1, 10, length.out = 4)  #1~10까지 4개만

rep(1:3, 3)       #123123123
rep(1:3, each=3)  #111222333

c(1:10)
c(1, 3, 5:7)
c(1:3, 10:16)
(c(1:10))
c(1, 'aa')   #type을 맞춤 1이 문자열이 됨
c(1, 2.5, TRUE, FALSE)  #1.0 2.5 1.0 0.0

age <- c(10, 20, 30)
names <- c("유비", "관우", "장비")
names(age) <- c("유비", "관우", "장비")
age           #유비 관우 장비 
              #10   20   30
age[1]
age['유비']
age[10] <- 50
age   #유비 관우 장비                                    
      #10   20   30   NA   NA   NA   NA   NA   NA   50 
age <- NULL
age  #참조가 사라짐

v1 <- c(13, -5, 20:30, 12, -2:3)
v1   #13 -5 20 21 22 23 24 25 26 27 28 29 30 12 -2 -1  0  1  2  3
v1[1]   #슬라이싱, 첨자를 이용해서 벡터 요소에 접근
v1[0]   #numeric(0)
v1[c(2,4,10:13)]   #-5 21 27 28 29 30

v1[-1]      #여집합
v1[-c(2,4)] 

v1[2:(length(v1)-10)]  #[2:(20-10)]
nrow(v1) #NULL -> matrix에서만 가능
NROW(v1) #20




a <- 1:5
a + 5 #각 요소에 더하기
a ^ 2 #각 요소에 거듭제곱 (1  4  9 16 25)
sqrt(a) #제곱근

a <- 1:3
b <- 4:6
cat(a, ' ', b)
a + b  #5 7 9
a[4] <- 2
b[4] <- 2 #a와 b 공통으로 2를 가지도록

union(a, b) #1 2 3 4 5 6   합집합, 중복x
c(a, b)     #중복허용
setdiff(a, b)   #차집합 a-b
intersect(a, b) #교집합

fac <- as.factor(a)    #숫자형 데이터를 범주형으로, levels "1","2","3": 1 2 3 2
fac <- as.integer(fac) #다시 숫자형으로


#matrix : 2차원 배열
a <- 1:8
dim(a)  #차원 확인,  NULL
dim(a) <- c(2,4)
a
#     [,1] [,2] [,3] [,4]
#[1,]    1    3    5    7
#[2,]    2    4    6    8
class(a)   #"matrix"
mode(a)    #"numeric"


m <- matrix(1:5)         #1열 5행으로 1~5까지
m <- matrix(1:9, nrow=3) #3열3행 ,열부터 채우기
m <- matrix(1:9, nrow=3, byrow = TRUE) # 행부터 채우기
m <- matrix(1:10, 2) #2열
m <- matrix(1:10, 3) # 경고메시지(들):데이터의 길이[10]가 행의 개수[3]의 배수가 되지 않습니다, 실행은 가능
m
cat(dim(m), ' ', mode(m), ' ', class(m))

m[1,] #1행만
m[,3] #3열만
m[1,3]
m[1, c(1,3)]
m[1, c(1:3)]

m[, -1]  #1열 제외
m[-1,-1] #1행1열 제외


#행렬 계산
a <- matrix(c(1,2,3,4), 2, 2)
b <- matrix(5:8, 2)

a + b
a * b    #요소끼리 단순곱 (하다마드곱)
a %*% b  #행렬곱
t(a)     #전치
solve(a) #역행렬


#array
d <- c(1:12)    #벡터는 dim(d)가 안됨
cat(d, ' ', class(d))       #1 2 3 4 5 6 7 8 9 10 11 12   integer
arr1 <- array(d)
cat(arr1, ' ', class(arr1)) #1 2 3 4 5 6 7 8 9 10 11 12   array
dim(arr1)     #12

arr2 <- array(1:12, dim=c(6,2))
arr2

arr3 <- array(1:12, dim=c(3,2,2)) #행, 열, 면
arr3
#, , 1면
#      [,1] [,2]
#[1,]    1    4
#[2,]    2    5
#[3,]    3    6
#, , 2면
#      [,1] [,2]
#[1,]    7   10
#[2,]    8   11
#[3,]    9   12

arr3[,,1]
arr3[,1,1]  #1 2 3
arr3[1,,1]  #1 4
arr3[1,1,1] #1


#list : 서로 다른 타입의 데이터 기억 가능(c의 구조체)
l1 <- list(1.0, 'tom', 80, 2.0, 'oscar', 94)
l1
class(l1) #"list"

unli <- unlist(l1)
unli   #list풀어서 전체가 문자열로 
class(unli)

num <- list(1:5, c(6, 8:10), c('a', 'b'))
num  #1~5 는 인덱스1에, 6,8,9,10이 인덱스 2에
num[1]
num[[1]]        #둘다 1 2 3 4 5로 나옴
class(num[1])   #"list"
class(num[[1]]) #"integer"

num[[1]][2]  #2

num2 <- list(x=1:5, y=6:10) #key붙이기
num2
num2$x
num2$x[1]
plot(num2)  #x축에 첫번째키, y축이 2번째 키

mem <- list(name='hong', age=22)

a <- list(1:5)
b <- list(6:10)
lapply(c(a,b), max)   #base의 lapply, a하고 b에 대해서 최대값
class(lapply(c(a,b), max)) #"list"
sapply(c(a,b), max)
class(sapply(c(a,b), max)) #"integer"


#주소관련
aa <- list()
tracemem(aa)     #"<000002018ED55A78>"
aa$b <- c(1,2,3) #tracemem[0x000002018ed55a78 -> 0x000002018d3ab658]: 
untracemem(aa)   #메모리 추적 해제


# Data frame : 컬럼 단위로 type이 달라도 됨, 가장 많이 쓰이는 데이터유형
no <- c(1,2,3)
name <- c('hong', 'lee', 'kim')
pay <- c(200, 250, 300)
df <- data.frame(bun=no, irum=name, pay=pay)
df  #테이블 형태로 출력
class(df) #data.frame
is(df)

df <- data.frame(irum=c('hong', 'lee', 'kim'), nai=c(20, 25, 30), row.names = c("one", "two", "three"))
df #열 이름이 one, two, three로

nrow(df)
ncol(df)
str(df)
summary(df)
head(df, n=2)
tail(df, n=2)

m <- matrix(1:6, nrow = 3)
mdf <- data.frame(m)