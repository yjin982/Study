#연관분석 (장바구니 분석)
install.packages("arules")
library(arules)

(cust <- read.csv("testdata/priori_data2.csv", stringsAsFactors = FALSE))
cust$sangpum[cust$irum == '홍길동']  #홍길동이 구매한 상품들
(cust_list <- split(cust$sangpum, cust$irum)) #이름별 구매상품 자르기

(cust_tran <- as(cust_list, "transactions"))
(cust_rules <- apriori(cust_tran))
summary(cust_tran)

inspect(cust_rules)


#시각화를 해보기 위해 좀더 큰 데이터를 이용
(customer <- read.csv("testdata/priori_data.csv", stringsAsFactors = FALSE))
(customer_list <- split(customer$sangpum, customer$irum))
(customer_tran <- as(customer_list, "transactions")) #중복 데이터가 있어서 에러

(customer_list <- sapply(customer_list, unique))
(customer_tran <- as(customer_list, "transactions"))
summary(customer_tran)
arules::itemFrequency(customer_tran)
arules::itemFrequencyPlot(customer_tran, support = 0.01, main = '지지도 1% 이하의 항목들')
arules::itemFrequencyPlot(customer_tran, topN = 5, main = "지지도 상위 top 5 항목들들")


#연관규칙
(customer_rules <- apriori(customer_tran))
summary(customer_rules)
inspect(customer_rules)

(customer_rules <- apriori(customer_tran, parameter = list(support = 0.2, confidence = 0.2)))
inspect(customer_rules)
inspect(sort(customer_rules, by = 'lift')[1:5])

#시각화
install.packages("arulesViz")
library(arulesViz)
plot(customer_rules, method = 'grouped')
plot(customer_rules, method = 'graph')
plot(customer_rules, method = 'graph', control = list(type = 'items'))
plot(customer_rules, method = 'graph', engine = 'interactive')
