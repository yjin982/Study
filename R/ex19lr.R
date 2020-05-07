mtcars #데이터 이용, 32 by 11 

# 단순회귀 : 독립변수(x):1, 종속변수(y):1
# hp(마력수):x, mpg(연비):y

cor(mtcars$hp, mtcars$mpg) # -0.7761684 강한 음의 상관관계
plot(mpg ~ hp, data = mtcars)

(model1 <- lm(mpg ~ hp, data = mtcars)) #(Intercept)  30.09886           hp  -0.06823
summary(model1) # 모델의 p-value: 1.788e-07 < 0.05 이므로 좋은 모델이라 판단
abline(model1, col = 'blue')

confint(model1) # hp의 신뢰구간 : -0.08889465 ~ -0.0475619 중 -0.06823 값을 가지므로 신뢰구간 내에 존재
model1

# y = -0.06823 * x + 30.09886
cat('실제값 :', mtcars$mpg[1], mtcars$hp[1]) # mpg:21, hp:110
y = -0.06823 * 110 + 30.09886
cat('예측값 :', y) # mpg예측값:22.59356

#사용자가 예측하고 싶은 임의의 마력수에 대한 연비 예측
(mynew <- mtcars[c(1,2), ])
mynew <- edit(mynew)
(pred <- predict(model1, newdata = mynew))



# 다중회귀 : 독립변수(x):2, 종속변수(y):1
# hp(마력수):x, wt(차체무게):x, mpg(연비):y

cor(mtcars$wt, mtcars$mpg) # -0.8676594
cor(mtcars$wt, mtcars$hp)  # 0.6587479

(model2 <- lm(mpg ~ hp + wt, data = mtcars)) #(Intercept)  37.22727         hp -0.03177   wt -3.87783
summary(model2)  # p-value: 9.109e-12

# y = -0.03177 * hp + -3.87783 * wt + 37.22727
cat(mtcars$mpg[1], mtcars$hp[1], mtcars$wt[1])
y = -0.03177 * 110 + -3.87783 * 2.62 + 37.22727
cat('hp + wt에 대한 예측값 :', y) # 23.57266


#새로운 데이터로 예상 연비를 예측
(newData <- data.frame(hp = 110, wt = 2.62))
predict(model2, newdata = newData) # 23.57233 

(newData2 <- data.frame(hp = 75, wt = 3.44))
predict(model2, newdata = newData2) # 21.50456 

(newData3 <- data.frame(hp = 100, wt = 1.02))
predict(model2, newdata = newData3) # 30.09459 

(newData4 <- data.frame(hp = 300, wt = 5.0))
predict(model2, newdata = newData4) # 8.306232

