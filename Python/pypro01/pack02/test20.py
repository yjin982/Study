#추상 클래스
from abc import *

class AbstractClass(metaclass=ABCMeta):
    #ABSMeta 클래스의 서브 클래스는 추상 클래스
    
    @abstractclassmethod
    def abcMethod(self): #추상 메소드
        pass
    
    def nomalMethod(self):
        print('AbstractClass 클래스의 일반 메소드')

#abs = AbstractClass() #추상 메소드를 가진 추상 클래스는 인스턴스화 할 수 없음
#abs.normalMethod()   #TypeError: Can't instantiate abstract class AbstractClass with abstract methods abcMethod

class Child1(AbstractClass):
    name = 'child1'
    
    def abcMethod(self):
        print('추상 메소드를 오버라이딩')

c1 = Child1()
print(c1.name)
c1.abcMethod()
c1.nomalMethod()


print('ㅡ' * 20)
class Child2(AbstractClass):
    name = 'child2 ...... '
    
    def abcMethod(self):     #오버라이딩 강제
        print('추상 메소드를 오버라이딩')
    
    def nomalMethod(self): #오버라이딩 선택
        print('노말 메소드도 오버라이딩')

c2 = Child2()
print(c2.name)
c2.abcMethod()
c2.nomalMethod()

print('ㅡ' * 20)
parent = AbstractClass
print(type(parent))
parent = c1
print(parent.name)
parent = c2
print(parent.name)

print('\n', 'ㅡ' * 20) #꼭 부모타입에만 넘겨줄 수 있는 것이 아님
temp = c1
print(temp.name)
temp = c2
print(temp.name)