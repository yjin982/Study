#다이어몬드 데이터를 이용해 계층/비계층 분석
library(ggplot2)
data("diamonds")
(t <- sample(1:nrow(diamonds), 1000))

#검정데이터
(test <- diamonds[t, ]) #1000 by 10
(mydia <- test[c("price", "carat", "depth", "table")]) #1000 by 4

#계층적 군집분석
(result <- hclust(dist(mydia), method = 'ave'))
plot(result, hang = -1)

#비계층적 군집분석 - k-means 알고리즘
(result2 <- kmeans(mydia, 3))
mydia$cluster <- result2$cluster
mydia

#변수간 상관관계
cor(mydia[, -5], method = 'pearson')
plot(mydia[,-5])

library(corrgram)
corrgram(mydia[, -5])
corrgram(mydia[, -5], upper.panel = panel.conf)
corrgram(mydia[, -5], lower.panel = panel.conf)

plot(mydia[c("carat", "price")], col = mydia$cluster)
points(result2$centers[,c("carat", "price")], col = c(3,1,2), pch = 8, cex = 5) #클러스터의 중심점
