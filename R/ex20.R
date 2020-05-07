# 원격 DB의 자료(jikwon table)를 읽어 근무년수에 대한 연봉을 예측하는 단순선형회귀 모델 작성
Sys.setenv(JAVA_HOME="C:/Program Files/Java/jdk-11.0.5")
library(rJava)
library(DBI)
library(RJDBC)

drv <- JDBC(driverClass = "org.mariadb.jdbc.Driver", classPath = "c:/Work/mariadb-java-client-2.5.4.jar")
conn <- dbConnect(drv, "jdbc:mysql://127.0.0.1:3306/test", "root", "123")
dbListTables(conn)

query <- "select jikwon_no, jikwon_name, buser_num, jikwon_jik, jikwon_pay, date_format(now(), '%Y') - date_format(jikwon_ibsail, '%Y') + 1 as jik_ibsail, jikwon_gen, jikwon_rating from jikwon"
(jik <- dbGetQuery(conn, query))

jik$jik_ibsail <- as.numeric(jik$jik_ibsail)
cor(jik$jik_ibsail, jik$jikwon_pay)  # 0.9405737

(model <- lm(jikwon_pay ~ jik_ibsail, data = jik)) #(Intercept)  799.6    jik_ibsail  592.2 
summary(model) #p-value: 1.164e-14

func <- function(){
  ibsail <- readline("근무년수 : ")
  ibsail <- as.numeric(ibsail)
  newData <- data.frame(jik_ibsail=ibsail)
  predict(model, newdata = newData)
}
func()
