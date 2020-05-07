# 거리 계산
(txt1 <- read.csv("testdata/cluster_ex.csv"))
plot(txt1[, c(2:3)], xlab = '국어', ylab = '영어', xlim = c(30,100), ylim = c(30,100))

text(txt1[,2], txt1[,3], labels = txt1[,1], cex = 0.8, pos = 1, col = 'blue')
text(txt1[,2], txt1[,3], labels = abbreviate(rownames(txt1)), cex = 0.8, pos = 2, col = 'blue')

points(txt1[1,2], txt1[1,3], col = 'red', pch = 19)
points(txt1[2,2], txt1[2,3], col = 'red', pch = 19)

(dist_mht <- dist(txt1[c(1:2), c(2:3)], method = 'manhattan')) #60
(dist_euc <- dist(txt1[c(1:2), c(2:3)], method = 'euclidean')) #50.9902

#군집분석
x <- c(1,2,2,4,5)
y <- c(1,1,4,3,4)
(xy <- data.frame(cbind(x, y)))

#덴드로그램 Dendrogram
(hc_sl <- hclust(dist(xy)^2, method = 'single'))
plot(hc_sl)

par(oma = c(3, 1, 1, 0)) #그래프 마진 주기
par(mfrow = c(1,3))      #그래프 1행2열
plot(hc_sl)
plot(hc_sl, hang = -1)

(hc_cl <- hclust(dist(xy)^2, method = 'complete')) #완전 연결법
plot(hc_cl) 
