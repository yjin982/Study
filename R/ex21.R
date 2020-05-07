#로지스틱 회귀(이진 분류)
mydata <- read.csv("testdata/binary.csv") #400 by 4 데이터
summary(mydata)
table(mydata$admit, mydata$rank)
xtabs(formula = ~admit + rank, data = mydata)
str(mydata)

# 데이터 분리 : train dataset(학습데이터)-모델작성시, test dataset(검증(평가)데이터)-예측시
set.seed(1)
(idx <- sample(1:nrow(mydata), nrow(mydata) * 0.7))
train <- mydata[idx, ]
test <- mydata[-idx, ]
dim(train) # 280   4
dim(test)  # 120   4

# 분류 모델 작성
(lgmodel <- glm(formula = admit ~ ., data = train, family = binomial(link = 'logit')))
summary(lgmodel)

# 분류 예측
(pred <- predict(lgmodel, newdata = test, type = 'response'))
head(pred, 10)
head(ifelse(pred > 0.5, 1, 0), 10)
head(test$admit, 10)

# 분류 정확도 계산
result_pred <- ifelse(pred > 0.5, 1, 0)
(t <- table(result_pred, test$admit)) # 70, 8이 제대로 예측한 값, confusion matrix 작성
(70 + 8) / nrow(test)           # 0.65   분류 정확도
(t[1,1] + t[2,2]) / nrow(test)  # 0.65
sum(diag(t) / nrow(test))       # 0.65

# 임의의 수치로 분류 예측
my <- train[c(1:3), ]
my <- edit(my)
(new_pred <- predict(lgmodel, newdata = my, type = 'response'))
ifelse(new_pred > 0.5, 'admit', 'deny')
