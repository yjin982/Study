#데이터 입출력
n <- scan()   #키보드에서 값 받기
sum(1:n)
ss <- scan(what = "") 
ss

df1 <- data.frame()
df1 <- edit(df1)
df1 <- df1[-1, ]             #행 삭제
df1 <- df1[,"bun"] <- NULL   #열삭제, "칼럼명"
df1 <- rbind(df1, c(10, 11)) #행추가
df1 <- cbind(df1, )          #열추가
df1

#file i/o
getwd() #현재 작업 경로
list.dirs()
list.files()

stud <- read.table("testdata/student.txt")  #파일 읽어오기
stud
stud1 <- read.table(file = "testdata/student1.txt", header = TRUE)
stud1
stud2 <- read.table(file = "testdata/student2.txt", header = TRUE, sep = ';')
stud2
stud3 <- read.table(file = "testdata/student3.txt", header = TRUE, sep = ' ', na.strings = '-')
stud3
stud4 <- read.csv(file = "testdata/student4.txt", header = TRUE, na.strings = '-')
stud4  #구분자가 , 일 경우 csv로 읽는 것이 편함

#엑셀파일 읽기
install.packages("xlsx")
library(rJava)
library(xlsx)
#Sys.setenv("JAVA_HOME='경로명...")
studex <- read.xlsx2(file = "testdata/student.xlsx", sheetIndex = 1)
studex <- read.xlsx2(file.choose(), sheetIndex = 1)
studex

#파일로 출력
sink("testdata/aaa.txt") #작업 전 파일명 지정
kbs <- 9  #저장 관련 작업
kbs
sink() #저장 종료

name <- c("관우", "장비")
age <- c(33, 35)
df <- data.frame(name, age)
df
write.table(df, "testdata/aaa1.txt", fileEncoding = 'utf-8')
write.csv(df, "testdata/aaa1.csv", fileEncoding = 'utf-8', row.names = FALSE, quote = FALSE)
