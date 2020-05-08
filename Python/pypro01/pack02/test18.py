# 상속
class Person:
    say = 'I am Iron Man'
    age = 34
    __house = '-> k.k <-'
    
    def __init__(self, age):
        print('Person Constructor')
        self.age = age
    
    def PrintInfo(self):
        print('age:{}, talk:{}'.format(self.age, self.say))
        
    def Hello(self):
        print('Hello')
        print(self.__house)
        
    @staticmethod
    def sugar(tel):
        print('tel :', tel)
        #print(self.say)
        
        
print(Person.say, Person.age)
print('ㅡ' * 20)

p = Person('42')
print(p.age)
p.PrintInfo()
p.Hello()


class Employee(Person):
    say = '우르롹끼'
    subject = '-침-'
    
    def __init__(self):
        print('Employee\' Constructor')
    
    def PrintInfo(self):
        print('Employee\'s PrintInfo')
    
    def EprintInfo(self):
        print(self.say, '|', super().say)
        super().PrintInfo()
        self.PrintInfo()
        self.Hello()
        #print(self.__house) #'Employee' object has no attribute '_Employee__house'
        #Private 이므로
print('ㅡ' * 20)


e = Employee()
print(e.say, '/', e.age, '/', e.subject)
print(e.EprintInfo())


class Worker(Person):
    def __init__(self, age):
        print('Worker\' Constructor')
        #부모 생성자를 명시적으로 호출
        super().__init__(age) #Bound Method Call
        
    def PrintInfo(self):
        print('Worker\'s PrintInfo')
        
    def WprintInfo(self):
        self.PrintInfo()
        super().PrintInfo()
print('ㅡ' * 20)


w = Worker('22')
print(w.say, '\\', w.age)
w.WprintInfo()
w.PrintInfo()


class Programmer(Worker):
    def __init__(self, age):
        print('Programmer\'s constructor')
        Worker.__init__(self, age) #Unbound Method Call
    
    def WprintInfo(self):
        print('At Programmer overriding')
print('ㅡ' * 20)

pr = Programmer('7')
print(pr.say, '    ', pr.age)
pr.WprintInfo()
pr.PrintInfo()


print('\n', '=' * 30)
print(type(12.3), '     ', type(pr), '     ', type(w))
print(Person.__bases__, '     ', Programmer.__bases__)

print('\n')
pr.sugar('123-1234')        #비권장
Person.sugar('123-1234') #권장
