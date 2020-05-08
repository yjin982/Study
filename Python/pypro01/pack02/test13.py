class Car:
    handle = 0
    speed = 0
    
    def __init__(self, name, speed): #self == 생성되는 객체
        self.speed = speed
        self.name = name # 프로토타입의 멤버가 아님
    
    def showData(self):
        km = '킬로미터'
        msg = '속도:' + str(self.speed) + km
        return msg
    
print(Car.handle)
print(Car.speed)
#print(Car.name) #error

print('__tom\'s car__')
car1 = Car('tom', 10) #name, speed를 argument로 지정해야함
print(car1.name, car1.handle, car1.speed)
car1.color = 'black'
print('color :', car1.color) #car1만의 멤버 

print('__sam\'s car__')
car2 = Car('sam', 20)
print(car2.name, car2.handle, car2.speed)
#print('color :', car2.color) #error

print(Car.showData(car1), '==', car1.showData())
print(Car.showData(car2), '==', car2.showData())

print()
print(id(Car), id(car1), id(car2), '\n') #전부 다 주소가 다름

car1.speed = 88
car2.speed = 110
print(car1.showData(), car2.showData())

Car.handle = 1
print(car1.handle, car2.handle) #1 1
car1.handle = 3
print(car1.handle, car2.handle) #3 1