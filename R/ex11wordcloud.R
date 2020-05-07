#워드 클라우드 출력
library(KoNLP)
install.packages("wordcloud")
library(wordcloud)
Sys.setenv(JAVA_HOME="C:\\Program Files\\Java\\jdk-11.0.5")
library(rJava)

data <- readLines("testdata/")

ss = "해양 재난 스릴러 <씨 피버>가 5월 개봉을 확정하고 메인 포스터와 예고편을 공개했다. <씨 피버>는 망망대해의 바다, 미지의 생명체가 퍼뜨린 치사율 100% 열병에 감염된 선원들의 사투를 그린 해양 재난 스릴러로, <47미터>, <크롤>을 이어 흥행 돌풍을 일으킬 해양 재난 스릴러로 주목받고 있다. 메인 포스터에서는 바다 위 떠 있는 어선의 모습이 가장 먼저 시선을 사로잡는다. 어선이 뱃머리를 향하고 있는 바다는 이미 붉은 피로 물들어 있고, 그 아래 어두운 그림자를 뿜어내는 미지의 생명체의 모습, 여기에 '깊은 바다 아래 잠자던 죽음을 깨웠다'는 카피는 영화 속에 드리운 거대한 공포를 암시하며 더욱 기대감을 증폭시킨다. 그동안 <47미터>에서는 상어, <크롤>에서는 악어가 등장해 쫓고 쫓기는 공포를 선사했다면 <씨 피버>에는 더욱 새롭고 강력한 해양 생명체가 등장해 놀라움을 선사할 예정이다. 최초 공개된 메인 예고편은 미지의 생명체와 마주한 선박 내부의 이야기를 확인할 수 있다. 단순한 바다 열병인 줄 알았으나 미지의 존재가 가져다 준 치명적인 감염병으로 인해 선원들이 점차 혼란에 빠지기 시작하는 모습이 긴장감을 자아낸다. 해외 평단에서는 <씨 피버>를 두고 '혼란과 공포를 유발하는 스릴 넘치는 여정'(Flick Feast), '영화가 끝난 후에도 생각을 멈출 수 없는 악몽'(Collider), '새로운 장르의 클래식이 될 영화'(Solzy at the Movies), '<에일리언>과 <더 씽>을 떠올리게 한다'(SciFiNow)며 주목했다. <씨 피버>는 5월 개봉 예정이다. 해양생물의 행동 패턴을 연구하는 '시본'은 실습을 위해 어선 '니브 킨 오이르'호에 승선한다. 더 큰 수확을 얻기 위해 접근 금지 수역에 진입한 '니브 킨 오이르'호는 심해에 서식하던 미지의 생명체와 마주한다. 그 이후부터 선원들 사이에서 열병이 퍼지며 하나둘씩 죽음을 맞기 시작하는데…
재난 흥행 해양 해양 해양 에일리언 에일리언 혼란 바다 바다 공포 존재"

data <- extractNoun(ss)
data <- gsub("\\d+", "", data) #정규표현식
data <- base::Filter(function(x){nchar(x) >= 2}, data) #두 글자 이상
data

word <- table(data)
word

install.packages("RColorBrewer")
library(RColorBrewer)

display.brewer.all()
palete <- brewer.pal(9, "Set3")
windowsFonts(font=windowsFont("휴먼둥근헤드라인"))

wordcloud::wordcloud(names(word), freq = word, min.freq = 1, random.order = FALSE, random.color = TRUE, colors = palete)