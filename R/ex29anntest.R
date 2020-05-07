#다층 퍼셉트론 = MLP
install.packages("neuralnet")
library(neuralnet) 

iris$Species2[iris$Species == 'setosa'] <- 1
iris$Species2[iris$Species == 'versicolor'] <- 2
iris$Species2[iris$Species == 'virginica'] <- 3
iris$Species <- NULL
(idx <- sample(1:nrow(iris), 0.7 * nrow(iris)))
train <- iris[idx, ]
test <- iris[-idx, ]

normal_func <- function(x){ #정규화 함수
  return((x - min(x)) / (max(x) - min(x)))
}

(train_nor <- as.data.frame(lapply(train, normal_func)))
(test_nor <- as.data.frame(lapply(test, normal_func)))

(model <- neuralnet(Species2 ~ ., data = train_nor, hidden = 1))
plot(model)

#예측 : compute()
(model_result <- compute(model, test_nor[c(1:4)]))
