#데이터 시각화
getwd()
setwd("C:/Work/rsou/pro01")

stu <- read.csv('testdata/ex_studentlist.csv')
head(stu)
names(stu)
class(stu)

barplot(stu$grade)
barplot(stu$grade, ylim = c(0,5), col = rainbow(4), main = '차트제목')
barplot(stu$grade, horiz = TRUE, xlab = '학년', ylab = '학생', col = c(1:5))

par(mfrow = c(1, 2))  #차트를 두개 그릴 공간을 확보
barplot(stu$grade, col = rainbow(7))
title(main = '1열')
barplot(stu[,4], col = rainbow(2), space = 2)
title(main = '2열')

par(mfrow = c(1,1))
dotchart(stu$grade, color = 2:5, lcolor = 'green', pch = 1:2, cex = 1.5)

df <- na.omit(stu) #na있는 행을 날림
pie(df$age, labels = df$age, lty = 1)

boxplot(stu$height, range = 1, notch = TRUE)
abline(h = 170, lty = 3, col = 'blue')

hist(stu$height, breaks = 5, col = 'red', prob = TRUE)
lines(density(stu$height))

price <- runif(10, min = 1, max = 100)
plot(price)

par(mfrow = c(2,2))
plot(price, type = 'l')
plot(price, type = 'o')
plot(price, type = 'h')
plot(price, type = 's')


#iris dataset
head(iris, 2)
attributes(iris)
pairs(iris[,1:4])

par(mar = c(1,1,1,1))
layout(matrix(c(1,0,2,3), 2, 2, byrow = TRUE), c(2, 1), c(1, 2))
#layout(matrix(c(2,0,1,3), 2, 2, byrow = TRUE), c(2, 1), c(1, 2)) #뒤에서 두개 c(2,1)은 행 비율, 뒤는 열 비율
plot(iris$Petal.Width) #첫번째 그림에 매트릭스(2, 0, >1<, 3)에 들어간 것
hist(iris$Sepal.Width)
boxplot(iris$Sepal.Length)

#3d그리기
install.packages("scatterplot3d")
library(scatterplot3d)

par(mfrow = c(1,1))
levels(iris$Species)
class(iris$Species)
ir_setosa = iris[iris$Species == 'setosa', ]
ir_versicolor = iris[iris$Species == 'versicolor', ]
ir_virginica = iris[iris$Species == 'virginica', ]

irdata <- scatterplot3d::scatterplot3d(iris$Petal.Length, iris$Sepal.Length, iris$Sepal.Width, type = 'n')
irdata$points3d(ir_setosa$Petal.Length, ir_setosa$Sepal.Length, ir_setosa$Sepal.Width, bg = 'red', pch = 21)
irdata$points3d(ir_versicolor$Petal.Length, ir_versicolor$Sepal.Length, ir_versicolor$Sepal.Width, bg = 'blue', pch = 23)
irdata$points3d(ir_virginica$Petal.Length, ir_virginica$Sepal.Length, ir_virginica$Sepal.Width, bg = 'yellow', pch = 25)
