# ANN : perceptron
library(nnet)

(df <- data.frame(x1 = c(1:6), x2 = c(6:1), y = factor(c('n', 'n', 'n', 'y', 'y', 'y'))))
model1 <- nnet(y ~ ., df, size = 1)
model1
summary(model1)

library(devtools)
source_url('https://gist.githubusercontent.com/fawda123/7471137/raw/466c1474d0a505ff044412703516c34f1a4684a5/nnet_plot_update.r')
plot.nnet(summary(model1))

model1$fitted.values #분류모델 적합값
predict(model1, df)
ifelse(predict(model1, df) > 0.5, 1, 0)

(p <- predict(model1, df, type = 'class'))
table(p, df$y)


# iris data
set.seed(123)
(idx <- sample(1:nrow(iris), 0.7 * nrow(iris)))
train <- iris[idx, ]
test <- iris[-idx, ]

model_iris1 <- nnet(Species ~ ., train, size = 1) #은닉층 1개
model_iris1 # a 4-1-3 network with 11 weights = 4개 input이 들어가서 3개 output으로 나옴
plot.nnet(summary(model_iris1))

model_iris2 <- nnet(Species ~ ., train, size = 3) #은닉층 3개
model_iris2
plot.nnet(summary(model_iris2))
