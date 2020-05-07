# iris dataset으로 의사결정나무 분류모델 작성
data("iris")

# train / test dataset으로 분리
set.seed(123)
idx <- sample(1:nrow(iris), nrow(iris) * 0.7)
train <- iris[idx, ]
test <- iris[-idx, ]
nrow(train) # 105
nrow(test)  # 45

install.packages("party")
library(party)

(iris_ctree <- ctree(Species ~ ., data = train))
plot(iris_ctree, type = 'simple')
plot(iris_ctree)

# predict
(pred <- predict(iris_ctree, test)) #예측값
test$Species                        #실제값

table(pred, test$Species)
(14 + 18 + 12) / nrow(test)  # 0.9777778 정확도


install.packages("caret")
install.packages("e1071")
library(caret)
library(e1071)
confusionMatrix(pred, test$Species)


(newdf <- iris[1, ])
newdf <- edit(newdf)        # 5, 7, 5, 7
predict(iris_ctree, newdf)  # virginica

##############################################

# RandomForest : 의사결정나무에서 파생된 앙상블 기법을 이용하는 알고리즘 모델
install.packages("randomForest")
library(randomForest)
(rmodel <- randomForest(Species ~ ., data = train))
(36 + 29 + 34) / nrow(train) # 0.9428571

(rmodel2 <- randomForest(Species ~ ., data = train, ntree = 200, mtry = 3, na.action = na.omit))
(36 + 30 + 34) / nrow(train) # 0.952381

# 중요 변수로 randomForest 작성
(rmodel3 <- randomForest(Species ~ ., data = train, importance = TRUE, na.action = na.omit))
importance(rmodel3)
varImpPlot(rmodel3)

(pred <- predict(rmodel3, test))
table(pred, test$Species)
(t <- table(observed = test[, 'Species'], predict = pred))
prop.table(t, margin = 1)
