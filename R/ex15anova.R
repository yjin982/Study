# 세 집단 평균 차이 검정(F검정 : ANOVA) 독립변수=범주형, 종속변수=연속형
# <실습>
# 3가지 교육방법을 적용하여 1개월 동안 교육받은 교육생 각 50명씩을 대상으로 실기시험을 실시하였다.
# 세 집단 간 실기 시험의 평균에 차이가 있는지 검정한다.

# 귀무 : 3가지 교육방법에 대한 실기시험의 평균에 차이가 없다.
# 대립 : 3가지 교육방법에 대한 실기시험의 평균에 차이가 없다.

data <- read.csv("testdata/three_sample.csv")
head(data, 2)
summary(data)
length(data$survey) # 150

(data2 <- subset(data, score <= 10)) #data 가공
length(data2$survey) # 88

boxplot(data2$score)
table(data2$method)


data2$method2[data2$method == 1] <- '방법1'
data2$method2[data2$method == 2] <- '방법2'
data2$method2[data2$method == 3] <- '방법3'
head(data2, 3)
table(data2$method2)

(x <- table(data2$method2))
(y <- tapply(data2$score, data2$method2, mean))
#   방법1    방법2    방법3 
# 4.187097 6.800000 5.610000 
# 위 결과에 대한 세 교육방법의 차이 여부를 확인 -> anova를 이용
# 선행조건 : 정규성 만족
hapiro.test(data2$score) # W = 0.97993, p-value = 0.1897, p > 0.05 이므로 정규분포를 만족

# 등분산성 만족 여부
bartlett.test(score ~ method, data = data2) # Bartlett's K-squared = 3.3157, df = 2, p-value = 0.1905, p > 0.05이므로 등분산성 만족
# == 세 집단의 평균점수가 동질이다.

install.packages("lattice")
library(lattice)
densityplot(score ~ method, data = data2) # (종속변수 ~ 독립변수 + ... , data)


# ANOVA 검정 방법 1
(result <- aov(score ~ method2, data = data2))
summary(result) # F value = 43.58, p value => Pr(>F) = 9.39e-14  < 0.05이므로 귀무 기각, 연구 채택

# ANOVA 검정 방법 2
(lmodel <- lm(score ~ method2, data = data2)) 
anova(lmodel)  # p value = 9.394e-14 *** < 0.05

# ANOVA 검정 방법 3
oneway.test(score ~ method2, data = data2, var.equal = TRUE) # p-value = 9.394e-14 < 0.05


# 사후검정 : 각 집단 간의 평균이나 비율의 차이를 확인
TukeyHSD(result)
#               diff        lwr        upr     p adj
#방법2-방법1  2.612903  1.9424342  3.2833723 0.0000000
#방법3-방법1  1.422903  0.7705979  2.0752085 0.0000040
#방법3-방법2 -1.190000 -1.8656509 -0.5143491 0.0001911
plot(TukeyHSD(result))