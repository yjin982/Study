# 모듈의 멤버로 클래스
a = 10 #전역변수

def aa(): #함수
    pass

print(a) #스테이트먼트

class TestClass: #클래스, 접근지정자 X, 전부 public
    star = 1 #멤버변수 (public)
    
    def __init__(self):
        print('생성자') #자동 호출
    
    def __del__(self):
        print('소멸자') #자동 호출
    
    def printMsg(self): #메소드 (public)
        name = 'sugar' #지역변수
        print(name)
        print(self.star)


test = TestClass() #생성자 호출. instance
print(test.star)
print(TestClass.star) #프로토타입(원형) 클래스로 멤버를 직접 호출하는 일은 거의 없음

test.printMsg()              #Bound Method call
#TestClass.printMsg()    #error : missing argument
TestClass.printMsg(test) #Unbound Method call
print()

print(type(1))
print(type(test))
print(id(test))
print(id(TestClass))

#del test
#test.printMsg()