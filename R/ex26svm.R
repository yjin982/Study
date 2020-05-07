# svm 모델로 iris 데이터 분류
library(e1071)

(x <- subset(iris, select =- Species))
(y <- iris$Species)

(svmmodel <- svm(Species ~ ., data = iris))
(svmmodel <- svm(x, y)) #위 방법과 결과 동일

dist(iris[, -5])           #데이터 간 거리
cmdscale(dist(iris[, -5])) #데이터 간 거리를 matrix형으로
plot(cmdscale(dist(iris[, -5])), col = as.integer(iris[, 5]))

(pred <- predict(svmmodel, x))
(table(pred, y))
(50 + 48 + 48) / nrow(x) #0.9733333
