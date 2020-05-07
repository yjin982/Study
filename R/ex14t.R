# 집단 간 평균/비율 차이 검정 [t 검정]
# 단일 모집단의 평균에 대한 가설검정(one samples t-test) - 1 
# 실습 예제) 여아 신생아 몸무게의 평균 검정 수행
# 여아 신생아의 몸무게는 평균이 2800(g)으로 알려져 왔으나 이보다 더 크다는 주장이 나왔다.
# 표본으로 여아 18명을 뽑아 체중을 측정하였 다고 할 때 새로운 주장이 맞는지 검정해 보자

# 귀무 : 여아 신생아 몸무게 평균은 2800(g)이다
# 대립 : 2800(g)보다 크다.

data <- read.csv("testdata/babyboom.csv", header = TRUE)
head(data, 3)

(temp <- subset(data, gender == 1))
(weight <- temp[[3]])

(avg <- mean(weight))
(s_dev <- sd(weight))
(n <- length(weight))

t.test(weight, mu = 2800, alternative = "greater") # t = 2.2332, df = 17, p-value = 0.01963
# p < 0.05 이므로 귀무 기각 = 몸무게 평균은 2800(g)보다 크다


### one sample t-test 평균 예제 도표 작성 ###
# t_value  직접 지정
h0 = 2800
t_value <- (avg - h0) / (s_dev / sqrt(n))  # 2.233188

par(mar=c(0,1,1,1))
x <- seq(-3, 3, by = 0.001)
y <- dt(x, df = n - 1)
plot(x, y, type="l", axes=F, ylim=c(-0.02, 0.38))
abline(h=0)

polygon(c(c_u, x[x > c_u], 3), c(0, y[x > c_u], 0), col=2)
text(c_u, -0.02, expression(t[0.05]==1.74))
text(1.8, 0.2, expression(alpha==0.05), cex=0.8)
arrows(1.8, 0.18, 1.8, 0.09, length=0.05)

polygon(c(t_value, x[x > t_value], 3), c(0, y[x > t_value], 0), density=20, angle = 45)
text(t_value, -0.02, paste("t=", round(t_value, 3)), pos=4)
text(2.65, 0.1, expression(plain(P)(T > 2.23)==0.019), cex=0.8)
arrows(2.7, 0.08, 2.5, 0.03, length=0.05)
### ###



# 서울시 강동구와 중구의 미세먼지 농도 평균 분포 차이 검정
install.packages("readxl")
library(readxl)

dustdata <- read_excel("testdata/localAverage.xlsx")
View(dustdata)
dustdata <- as.data.frame(dustdata)
(str(dustdata))

library(dplyr)
dustdata_anal <- dustdata %>% filter(dustdata$구분 %in% c("강동구", "중구"))
View(dustdata_anal)

t.test(data = dustdata_anal, 미세먼지 ~ dustdata_anal$측정소명)