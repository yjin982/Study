# 다중 상속
class Tiger:
    data = '갓랑이'
    
    def Cry(self):
        print('어흥어흥')
    
    def Eat(self):
        print('떡 하나 주면 안 잡아 먹지')
    

class Lion:
    def Cry(self):
        print('갸르릉갸르릉')
    
    def Hobby(self):
        print('대형 애옹이')

class Liger1(Tiger, Lion): #다중 상속
    pass

class Liger2(Lion, Tiger):
    data = '혼종 만세'
    
    def Play(self):
        self.Cry()
        super().Cry()
        print(self.data)
        print(super().data)
        
    def Hobby(self):
        print('애옹이 박스를 좋아해')
        
        
aa = Liger1()
aa.Cry()      #Lion, Tiger 둘 다 있는 메소드 : 먼저 상속받은(쓴 순서에 따라) 클래스의 메소드를 취함
aa.Eat()      #Tiger로부터
aa.Hobby()  #Lion으로 부터

print('ㅡ'  * 20)
bb = Liger2()
bb.Play()
bb.Hobby()