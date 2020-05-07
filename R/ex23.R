# KNN(K-Nearest Naighbors) 분류 모형
install.packages("ggvis")
library(ggvis)

iris %>% ggvis(~Petal.Length, ~Petal.Width, fill = ~factor(Species))

# 데이터 정규화(0 ~ 1 사이 구간 내의 데이터를 재구성)
# 수식 : (요소값 - 최소값) / (최대값 - 최소값)

iris[1:4] 
func_normal <- function(x){
  num <- x - min(x)
  m_m <- max(x) - min(x)
  return(num / m_m)
}
test_df <- data.frame(x = c(1,2,3,4,5))
func_normal(test_df)
lapply(test_df, func_normal)

test_df <- data.frame(x = iris[1:4])
func_normal(test_df)
lapply(test_df, func_normal)

##########
normal_d <- as.data.frame(lapply(iris[1:4], func_normal))
head(normal_d, 2)  #정규화 데이터
head(iris[1:4], 2) #원 데이터
summary(normal_d)
df <- data.frame(normal_d, Species = iris$Species) #정규화 데이터에 Species 추가

# 데이터 분리
set.seed(123)
idx <- sample(1:nrow(df), 0.7 * nrow(df))
train <- df[idx. ]
test <- df[-idx, ]

# KNN 모델
library(class)
(model1 <- knn(train = train[, -5], test = test[, -5], cl = train$Species, k = 3))
(model2 <- knn(train = train[, -5], test = test[, -5], cl = train$Species, k = 7))

(t <- table(model1,test$Species))
(acc <- (t[1:1] + t[2,2] + t[3:3]) / nrow(test))


library(gmodels)
CrossTable(x = test$Species, y = model2, prop.chisq = FALSE)
