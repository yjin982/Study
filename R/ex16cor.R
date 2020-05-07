# 공분산 상관계수
hf <- read.csv("testdata/galton.csv", header = TRUE, stringsAsFactors = FALSE)
str(hf)

hf_son <- subset(hf, sex=='M')
head(hf_son)
hf_son <- hf_son[c('father', 'height')]
head(hf_son)

#표본 공분산 수식
f_mean = mean(hf_son$father)
s_mean = mean(hf_son$height)
(cov_num <- sum((hf_son$father - f_mean) * (hf_son$height - s_mean))) # 편차곱의 합
(cov_xy <- cov_num / (nrow(hf_son) - 1)) # 공분산 2.368441

# 공분산 함수
cov(hf_son$father, hf_son$height) # 2.368441
aa <- cor(hf_son$father, hf_son$height) # 상관계수(r) 0.3913174
plot(height ~ father, data = hf_son)
abline(lm(height ~ father, data = hf_son))


install.packages("corrgram")
library(corrgram)
corrgram()
