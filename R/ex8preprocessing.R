#데이터 전처리 : 수집된 원형 데이터를 분석의 목적에 맞게 가공하는 작업
install.packages("plyr")
library(plyr)

x <- data.frame(id = c(1,2,3,4,8), height = c(160, 171, 175, 162, 185))
y <- data.frame(id = c(5,4,1,3,8), weight = c(55, 73, 60, 57, 90))

join(x, y, by = 'id') #left join
join(x, y, by = 'id', type = 'inner') #inner join
join(x, y, by = 'id', type = 'full')  #full join

install.packages("dplyr")
library(dplyr)

std <- read.csv("testdata/ex_studentlist.csv")
head(std, 2)

#filter(dataframe, 조건1, 조건2)
filter(std, gender == '남', grade == 2)  #and 조건
filter(std, gender == '남' | grade == 2) #or 조건
length(filter(std, gender == '남', grade == 2)) #건수

arrange(std, age)        #정렬 asc
arrange(std, desc(age))  #정렬 desc
arrange(std, grade, age)

select(std, name, age)
select(std, name:age)
select(std, -(name:age))

#summarise() 집계, 소계
is.na(std) #결측치 확인 = true는 결측치
table(is.na(std))
table(is.na(std$age))

stddf <- na.omit(std)
table(is.na(stddf))
summarise(stddf, avgAge = mean(age, na.rm = TRUE))
summarise(stddf, sdAge = sd(age))
summarise(stddf, sumAge = sum(age))