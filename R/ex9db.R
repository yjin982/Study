#DBMS(정형 데이터)와 연동
install.packages("DBI")
install.packages("RJDBC")
install.packages("RSQLite")
Sys.setenv(JAVA_HOME = "C:/Program Files/Java/jdk-11.0.5") #Sys.setenv(JAVA_HOME = "C:\\Program Files\\Java\\jdk-11.0.5")

library(rJava)
library(DBI)
library(RJDBC)
library(RSQLite)

#내장된 개인용 데이터베이스(SQLite)와 연동
conn <- dbConnect(RSQLite::SQLite(), ":memory:")
dbWriteTable(conn, "mtcars", mtcars) #테이블 생성
dbListTables(conn)  #테이블 목록 보기
query <- "select * from mtcars"
goodsAll <- dbGetQuery(conn, query)
goods <- dbGetQuery(conn, "select mpg, disp, hp from mtcars where mpg >= 21")
dbDisconnect(conn) #연결 끊기


#원격 데이터베이스와 연동 - MariaDB
#드라이버파일 연결
drv <- JDBC(driverClass = "org.mariadb.jdbc.Driver", classPath = "c:/Work/mariadb-java-client-2.5.4.jar")
conn <- dbConnect(drv, "jdbc:mysql://127.0.0.1:3306/test", "root", "123")
dbListTables(conn)

query <- "select * from sangdata"
goodAll <- dbGetQuery(conn, query)
goodAll
class(goodAll)
goodAll$sang
barplot(goodAll$su, col = rainbow(7), names.arg = goodAll$sang)

goods <- dbGetQuery(conn, "select * from sangdata where sang like '가죽%'")
goods
dbGetQuery(conn, "select * from sangdata order by code desc")

#레코드 추가
query <- "insert into sangdata values(10, '신상품', 3, 7000)"
dbSendUpdate(conn, query)

df <- data.frame(code = 11, sang = '아메리카노', su = 10, dan = 3500)
dbSendUpdate(conn, "insert into sangdata values(?,?,?,?)", df$code, df$sang, df$su, df$dan)

#레코드 수정
query = "update sangdata set sang='아이리스', su=13 where code=6"
dbSendUpdate(conn, query)

dbSendUpdate(conn, "update sangdata set sang=? where code=?", '밀크티', 10)

#레코드 삭제
dbSendUpdate(conn, "delete from sangdata where code=11")
dbSendUpdate(conn, "delete from sangdata where code=?", 10)


#여러 행의 자료(dataframe)를 입력하기 -> 함수로 반복문 처리
sangdf <- read.csv("testdata/sangpum.csv", header = TRUE, fileEncoding = 'utf-8')

library(dplyr) # %>% 명령을 이어주는 역할 연산자
#자료 추가 함수
func <- function(conn, table, df){
  batch <- apply(df, 1, FUN = function(x) paste0("'", trimws(x), "'", collapse = ",")) %>% 
    paste0("(",.,")", collapse = ",\n")

  query <- paste("insert into", table, 'values', batch) #build query
  dbSendUpdate(conn, query)
}

func(conn, "sangdata", sangdf)

dbDisconnect(conn)
