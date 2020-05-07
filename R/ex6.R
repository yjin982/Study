#web scraping : 임의의 사이트에서 일정 데이터를 긁어오기
install.packages("httr")
install.packages("XML")
library(httr)
library(XML)

url <- "https://www.melon.com/song/popup/lyricPrint.htm?songId=10000"
source <- htmlParse(rawToChar(GET(url)$content))
source

lyrics <- xpathSApply(source, "//div[@class='box_lyric_text']", xmlValue)
lyrics <- gsub("[\r\n\t]","", lyrics)

lyrics