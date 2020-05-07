# 카이제곱검정 중 일원카이제곱
# - 관찰도수가 기대도수와 일치하는 지를 검정하는 방법
# - 종류 : 적합도/선호도 검정
#    - chisq.test() 함수를 이용하여 관찰치와 기대빈도 일치여부 검정 
#    - 범주형 변수가 한 가지로, 관찰도수가 기대도수에 일치하는지 검정한다. 
# - CrossTable을 이용하지 않는 카이제곱으로 한 개의 변인(집단 또는 범주)을 대상으로 검정수행
 
# <적합도 검정 실습1> 
# 주사위를 60 회 던져서 나온 관측도수/기대도수가 아래와 같이 나온 경우에 
# 이 주사위는 적합한 주사위가 맞는가를 일원카이제곱 검정으로 분석하자.
#
# 귀무 가설 : 현재 주사위는 게임에 적합하다. 
# 대립 가설 : 현재 주사위는 게임에 적합하지 않다.

datas = c(4, 6, 17, 16, 8, 9) #관찰값1, #X-squared = 14.2, df(자유도) = 5, p-value = 0.01439
datas = c(11, 12, 10, 10, 8, 9) #관찰값2, #X-squared = 1, df = 5, p-value = 0.9626
chisq.test(datas) 

# 해석 방법 1) p-value 사용
# 유의 확률(p-value) 0.01439 이 유의 수준 0.05보다 미만이기 때문에 유의미한 수준(α=0.05)에서 귀무 가설을 기각할 수 있다.
# 따라서 '현재 주사위는 게임에 적합하다.' 라는 귀무가설을 기각하고 대립가설(H1)을 채택한다.
#
# 해석 방법 2) chi제곱 분포표
# chi제곱 분포표에 따르면(유의수준 0.05, df=5) 임계치가 11.071가 된다.
# X-squared = 14.2 (x축의 임의의 값)이므로 임계치의 우측에 존재하므로 귀무 가설 기각



# 이원카이제곱 검정 : 두 개 이상의 변인(집단 또는 범주)이을 대상으로 검정을 수행

# 부모의 학력수준에 따른 자녀의 대학 입학여부 검정
#
# 귀무 가설 : 부모의 학력수준과 자녀의 대학 입학 여부는 관련이 없다. (독립적이다)
# 대립 가설 : 부모의 학력수준과 자녀의 대학 입학 여부는 관련이 있다. (독립적이지 않다)

data <- read.csv("testdata/cleanDescriptive.csv", header = TRUE)
head(data)
x <- data$level2  #독립변수 : 부모 학력
y <- data$pass2   #종속변수 : 자녀 합/불

result <- data.frame(level = x, pass = y)
head(result)
dim(result)
table(result) #빈도수 확인

install.packages("gmodels")
library(gmodels)
CrossTable(x, y, chisq = TRUE) # Chi^2 =  2.766951     d.f. =  2     p =  0.2507057 

# p > 0.05 이므로 귀무 채택

chisq.test(x, y)   # X-squared = 2.767, df = 2, p-value = 0.2507



# 독립성 검정 - 설문조사 자료 이용
library(MASS)
data("survey")
head(survey)
head(survey[c('Sex', 'Exer')])
str(survey[c('Sex', 'Exer')])

# 성별과 운동량 자료로 검정
#
# 귀무 가설 : 성별과 운동량은 관련이 없다. (독립적이다)
# 대립 가설 : 성별과 운동량은 관련이 있다. (비독립적이다)

# 분할표 작성
table(survey$Sex, survey$Exer)
data1 <- xtabs(~Sex + Exer, data = survey)
chisq.test(data1)   # X-squared = 5.7184, df = 2, p-value = 0.05731
# p > 0.05 이므로 대립 기각, 귀무 채택


# 박수를 칠 때, 위에 올라가는 손은?
#
# 귀무 가설 : 박수칠 때 주로 사용하는 손이 없다.
# 대립 가설 : 박수칠 때 주로 사용하는 손이 있다.
data2 <- xtabs(~W.Hnd + Clap, data = survey)
chisq.test(data2)  # 경고, 검정방법이 정확하지 않을 수 있으니 다른 검정 방법을 사용하라는 것
# 실험 샘플 수가 적은 경우에 '카이제곱 approximation은 정확하지 않을수도 ...' 에러 발생

#검정 도구 변경 (비모수 검정)
fisher.test(data2)   # p-value = 0.0001413, alternative hypothesis: two.sided
# p < 0.05 이므로 귀무 기각


barplot(data2, horiz = TRUE, legend = row.names(data2))
mosaicplot(data2, color = c("skyblue2", "wheat2", "salmon2"))