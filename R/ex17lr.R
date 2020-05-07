# 선형회귀 모델
# 독립변수가 종속변수에 미치는 영향을 파악하고 이를 통해 독립변수의 일정한 값에 대응되는 종속 변수 값을 예측하는 모델 산출 알고리즘
(df <- data.frame(workhour = 1:7, totalpay = seq(10000, 70000, by = 10000)))
plot(totalpay ~ workhour, data = df, pch = 20, col = 'red')

# 최적의 선형회귀 선을 얻기 위한 선형회귀식 필요. 기울기와 절편을 구해야함
(abc <- lm(totalpay ~ workhour, data = df)) # (Intercept)=-5.5e-12 : 절편     workhour=1.0e+04 : 기울기

grid()
abline(abc, col = 'lightblue', lwd = 2)

#수식으로 결과 예측 : y = wx + b     ==>    y = 1.0e+04 * w + -5.5e-12
wh = 2.345
result <- 1.0e+04 * wh + -5.5e-12
cat('예측 결과 : ', result)

predict(abc)
predict(abc, data.frame(workhour = c(6.7, 7, 8.9, 10.234123)))
