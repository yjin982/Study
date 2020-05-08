#클래스의 상속
class Animal:
    def __init__(self):
        print('Animal constructor')
        
    def move(self):
        print('move your body')


class Dog(Animal):
    def __init__(self):
        print('dog constructor')
        
    def my(self):
        print('bow wow')

dog1 = Dog() #해당 클래스에 생성자가 있으면 그 생성자만 수행, 생성자가 없을 시에 부모 클래스의 생성자를 수행
dog1.my()
dog1.move()

class Cat(Animal):
    pass

cat1 = Cat()
cat1.move()

print('-' * 20)
#overriding
class Parent:
    def PrintData(self):
        pass #자식을 만들어서 오버라이딩하라는 의미

class Child1(Parent):
    def PrintData(self):
        print('At Child1 overriding')

class Child2(Parent):
    def PrintData(self):
        print('At Child2 재정의')
    
    def ForChild2(self):
        print('child2 고유 메소드')

c1 = Child1()
c1.PrintData()

c2 = Child2()
c2.PrintData()

print('-' * 20)
#다형성
honey = c1
honey.PrintData()
honey = c2
honey.PrintData()
honey.ForChild2()

print()
plist = [c1, c2]
for i in plist:
    i.PrintData()