#제어문
no <- 7
no >= 2 + 2 * 2 | no < 5 %% 2
no >= 5 & no <= 10
no != 5

x <- 10
if(x >= 10){
  print('10 이상')
}else if(x >= 5){
  print("5 이상")
}else{
  print('etc')
}

ifelse(x >= 5, 'good', 'nice')

a <- 2
switch(a, mean(1:10), sd(1:10))

name <- c("kor", "eng", "mat", "kor")
which(name == 'kor') #조건에 맞는 결과 index를 반환

for(su in 1:9){
  res = 2 * su
  cat(2, '*', su, '=', res, '\n')
}

i <- 1
while(i < 10){
  res = 2 * i
  cat(2, '*', i, '=', res, '\n')
  i = i + 1
}

i <- 0
while(TRUE){
  i = i + 1
  print(i)
  if(i == 5) break
}

cnt <- 1
repeat{
  print(cnt)
  cnt = cnt + 2
  if(cnt > 10) break
}

#내장함수
seq(0, 5, by=1.5)

set.seed(42)  #난수값 고정
rnorm(1000, mean = 0, sd = 1) #정규분포를 따르는 난수 발생
hist(rnorm(1000, mean = 0, sd = 1))

runif(1000, min = 0, max = 100) #균등분포
hist(runif(1000, min = 0, max = 100))

sample(0:100, 10)


#사용자 정의 함수
fun1 <- function(){
  print('함수1')
}
fun1()

fun2 <- function(arg1){
  print(arg1)
  print('매개변수 사용')
  return(arg1 + 10)
}
fun2(5)

gugu_func <- function(dan){
  for(d in dan){
    for(i in 1:9){
      cat(d, '*', i, '=', d*i, ' ')
    }
    cat('\n')
  }
}
gugu_func(c(2:9))