# 함수
# 인수 키워드 매핑
def showGugu(start, end = 5):
    for dan in range(start, end+1):
        print(str(dan) + '단 출력')
        
        
showGugu(2, 3); print()
showGugu(3); print()
showGugu(end=4, start=2); print()

# 가변 인수
def func1(*ar): #복수개의 데이터를 튜플로 받음
    print(ar)
    for i in ar:
        print('food :', i)

func1('bibigo', 'bibimbab', 'kimchi')

def func2(a, *ar):
    print(a, '/', ar)
    
func2('bibigo', 'bibimbab', 'kimchi')

def func3(a, b, *v1, **v2): #복수개의 데이터를 딕셔너리로 받음
    print(a, '|', b)
    print(v1, '|', v2)
    
func3(1, 2)
func3(1, 2, 3, 4, 5)
func3(1, 2, 3, 4, 5, m=6, n=7)

print()
# Closure (클로저)
# 클로저 적용 전
def out():
    count = 0
    def inn():
        nonlocal count
        count += 1
        return count
    print(inn())
    
out()
out()

#클로저 적용 후
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner #closure, 함수의 주소를 넘겨줌
    
add1 = outer()
print(add1())
print(add1())
print(add1())

add2 = outer()
print(add2())
print(add2())

print()
print('수량 * 단가 * 세금   결과 출력')
def outer2(tax):
    def inner2(num, price):
        amount = num * price * tax
        return amount
    return inner2 #함수밖에서 내부 함수에 지속적으로 참조 가능

a1 = outer2(0.1)
result1 = a1(5, 1000)
print(result1)
result2 = a1(10, 35000)
print(result2)

a2 = outer2(0.05)
result3 = a2(5, 1000)
print(result3)

print()
#일급함수 : 함수 안에 함수 작성 가능, 인자로 함수 전달 가능, 반환값으로 함수 가능
def fun1(a, b):
    return a + b
fun2 = fun1
print(fun2(3, 4))

def fun3(poo):
    def fun4():        #함수 안에 함수 작성
        print('inner function')
    fun4()
    return poo         #반환값이 함수
mster = fun3(fun1) #인자로 함수 전달
print(mster(3, 4))


print()
#lambda 함수
def sumnum(x, y):
    return x + y

print(sumnum(1, 2)) #일반함수
print((lambda x, y: x + y)(1, 2))

aa = (lambda x, y: x + y)
print(aa(1, 2))

bb = lambda a, num=10: a + num
print(bb(5))
print(bb(5, 6))

sun = lambda a, *tp, **di: print(a, tp, di)
sun(1, 2, 3, m=4, n=5)

li = [lambda a, b: a + b, lambda a, b: a * b]
print(li[0](3, 4))
print(li[1](3, 4))

#다른 함수에서 람다 사용
print(list(filter(lambda a: a < 5, range(10))))
print(list(filter(lambda a: a % 2, range(10))))

print()
#decorator 함수 장식자
def make2(fn):
    return lambda: 'hello -> ' + fn()

def make1(fn):
    return lambda: 'nice to meet you -> ' + fn()

def hello():
    return 'smith'

hi = make2(make1(hello))
print(hi())


@make2
@make1
def hello2():
    return 'WoW'

print(hello2())

hi2 = hello2() #hello2의 실행결과
print(hi2)
hi3 = hello2   #hello2의 주소
print(hi3())


print()
#재귀함수 : 함수 자신을 호출, 반복처리에 효과적
def countDown(n):
    if n == 0:
        print('complete')
    else:
        print(n, end=' ')
        countDown(n - 1)
        
countDown(10)

def tot(n):
    if n == 1:
        return 1
    return n + tot(n - 1)

result = tot(10)
print('sum is', str(result))

def fact(a):
    if a == 1:
        return 1
    print(a)
    return a * fact(a - 1)

result2 = fact(5)
print('5! is', result2)     # 5! = 5*4*3*2*1