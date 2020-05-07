# ANN - 인공신경망 알고리즘
install.packages("nnet")
library(nnet)
(input <- matrix(c(0, 0, 1, 1, 0, 1, 0, 1), ncol = 2)) #입력데이터
#(output <- matrix(c(0, 0, 0, 1))) #and
#(output <- matrix(c(0, 1, 1, 1))) #or
(output <- matrix(c(0, 1, 1, 0)))  #xor

#(ann <- nnet(input, output, maxit = 100, size = 1, decay = 0.001)) #maxit 학습횟수, size 레이어(뉴런갯수), decay 학습율
(ann <- nnet(input, output, maxit = 100, size = 2, decay = 0.001))
(result <- predict(ann, input))
#(ifelse(result > 0.5, 1, 0)) #결과가 and, or로 잘 나옴
(ifelse(result > 0.5, 1, 0)) # size=1 xor일때는 결과가 절반만 맞춤, size 2여도 맞출때도 아닐때도 있음