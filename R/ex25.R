# Support Vector Machine : 데이터 간의 경계를 찾는 알고리즘

set.seed(1)
(x <- matrix(rnorm(20 * 2), ncol = 2))
(y <- c(rep(-1, 10), rep(1, 10)))
(x[y==1, ] <- x[y==1, ] + 1)

plot(x, col = (3 - y))

library(e1071)
(dat <- data.frame(x = x, y = as.factor(y)))

(svmmodel <- svm(y ~ ., data = dat, kernel = 'linear', cost = 10, scale = FALSE))

plot(svmmodel, dat)
svmmodel$index #support vector로 참여한 행, 1  2  5  7 14 16 17
dat[c(1,  2,  5,  7, 14, 16, 17), ]
summary(svmmodel)


#best cost 찾기 - 교차검증(tune())을 이용
set.seed(1)
#(tune_out <- tune(svm, y ~ ., data = dat, kernel = 'linear', range = list(cost = c(0.001, 0.01, 0.1, 1, 10, 100))))
(tune_out <- tune(svm, y ~ ., data = dat, kernel = 'linear', range = list(cost = 10^(-3:2)))) #위와 같이 나열안하고 이렇게 써도 됨
summary(tune_out)

(bestmodel <- svm(y ~ ., data = dat, kernel = 'linear', cost = 0.1, scale = FALSE))
(bestmodel <- tune_out$best.model) #또는 이렇게
plot(bestmodel, dat)


#분류 예측
(xtest <- matrix(rnorm(20 * 2), ncol = 2))
(ytest <- sample(c(-1, 1), 20, rep = TRUE))
(xtest[ytest == 1, ] <- xtest[ytest == 1, ] + 1)

(testdata <- data.frame(x = xtest, y = as.factor(ytest)))

(ypred <- predict(bestmodel, testdata))
(table(예측값 = ypred, 실제값 = testdata$y))
(9 + 8) / nrow(testdata) # 정확도 85%
