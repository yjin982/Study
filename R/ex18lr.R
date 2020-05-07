#회귀분석모형의 적절성을 위한 조건
#1) 정규성 : 잔차항이 정규분포를 따라야 한다.
#2) 독립성 : 독립변수의 값이 서로 관련되어 있지 않아야 한다.
#3) 선형성 : 독립변수의 변화에 따라 종속변수도 일정 패턴으로 변화하지 않아야 한다.
#4) 등분산성 : 독립변수의 모든 값에 대한 오차들의 분산이 일정해야 한다.
#5) 다중공선성 : 다중회귀분석을 할 때 3개 이상의 독립변수 간에 강한 상관관계로 인한 문제가 발생하지 않아야 한다.

women
plot(weight ~ height, data = women)

(fit <- lm(weight ~ height, data = women))
abline(fit, col = 'red')

summary(fit) # Multiple R-squared(결정계수, *설명력*):  0.991 
plot(fit)

par(mfrow = c(2,2))
plot(fit)
# (1,1) 선형성 관련 차트(패턴을 가지면 좋지 못한 모델) / (1,2) 정규성 관련
# (2,1) 등분산성 / (2,2) Cook's distance