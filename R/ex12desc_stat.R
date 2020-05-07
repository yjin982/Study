#통계분석 : 기술통계(Descriptive Statistics)
#자료를 정리 및 요약하는 기초적인 통계. 추론 통계의 기초자료로 쓰이기도 함

mean(1:5)
mean(1:5, trim = 0)
var(1:5)  #2.5
sum((1:5 - mean(1:5))^2) / 5       #2
sum((1:5 - mean(1:5))^2) / (5 - 1) #2.5 (r은 자유도를 n-1로 사용)
sd(1:5)

summary(1:5)
fivenum(1:5)

#표본 추출(sampleing)
#단순 임의 추출
sample(1:10, 5) #비복원
sample(1:10, 5, replace = TRUE) #복원
sample(1:10, 5, replace = TRUE, prob = 1:10)

#층화 추출
install.packages("sampling")
library(sampling)
str(iris)

kbs <- strata(c('Species'), size = c(3, 3, 3), method = 'srswor', data = iris) #비복원
sampling::getdata(iris, kbs)

#계통 추출
#생략


#분할표
ta1 <- c('a', 'b', 'c', 'a')
table(ta1)

x <- c('1', '2', '2', '1')
y <- c('a', 'b', 'a', 'b')
n <- c(3, 5, 8, 7)
df <- data.frame(x, y, n)
df

ta2 <- xtabs(n ~ x + y, data = df)
ta2

