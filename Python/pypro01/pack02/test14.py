kor = 100

def abc():
    print('모듈의 멤버인 함수')

class my: #클래스도 모듈의 하나의 부품
    kor = 90
    
    def abc(self):
        print('클래스의 멤버 변수 메소드')
    
    def show(self):
        #kor = 77 
        print(kor) #윗줄 주석처리시 결과 100, 모듈내의 kor로 
        print(self.kor)
        self.abc()
        abc()
        
m = my()
m.show()

print()
class Our:
    a = 1

ol = Our()
print(ol.a) #>>> 1
ol.a = 2
print(ol.a) #>>> 2

oll = Our()
print(oll.a) #>>> 1
oll.b = 10
print(oll.b) #>>> 10

#print(ol.b)   #error
print(Our.a)   #>>> 1
#print(Our.b) #error

print(type(ol), type(oll), type(Our()), '\n') #>>> <class '__main__.Our'> 전부
''' 클래스는 새로운 type을 생성 '''


class singer:
    titlesSone = 'fighting song'
    
    def sing(self):
        msg = 'song is'
        print(msg, self.titlesSone, '☆LALILA☆')
        
exo = singer()
exo.sing()

nct127 = singer()
nct127.sing()
nct127.titlesSone = 'fire truck'
nct127.sing()
nct127.com = 'SuMan'
print('company :', nct127.com)

exo.sing()
#print('company :', exo.com) #error
