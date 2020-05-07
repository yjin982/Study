#제어문 if
var = 10
if var >= 3:
    print('big')
    print('when true')
    if var > 5:
        print('5 over')
else:
    print('false')

print('계속 1')


score = 80
#score = int(input('점수 : ')) #키보드입력

if score >= 90:
    print('good')
elif score >= 70:
    print('nice')
else:
    print('not bad')

if 90 <= score <= 100:
    res = 'a'
elif 80 <= score < 90:
    res = 'b'
else:
    res = 'c'
print(res)

names = ['kildong', 'hany', 'sinbe']
if 'ildong' in names:
    print('friend name')
else:
    print('who is it?')

#참 if 조건 else 거짓
a = 'k.k'
b = 9 if a == 'house' else 11
print(b)

a = 11
b = 'iz' if a == 9 else 'soul'
print(b)

a = 6
re = a * 2 if a > 5 else a + 2
print(re)

a = 3
print((a + 2, a * 2)[a > 5]) #(참, 거짓)[조건]

#반복문 
#while
a = 1
while a <= 5:
    print(a, end = ' ')
    a += 1
print()

colors = ['red', 'green', 'blue']
a = 0
while a < len(colors):
    print(colors[a], end=' ')
    a += 1
print()

while colors:
    print(colors.pop(), end=' ')
print()


import time
sw = input('스위치를 누를까요?(y/n)')
if sw == 'y' or sw == 'Y' : 
    count = 5
    while 1 <= count:
        print('%d second left'%count)
        time.sleep(1)
        count -= 1
    print('BOMB!')
elif sw == 'n' or sw == 'N':
    print('canceled')
else:
    print('please press y or n')


a = 0
while a < 10:
    a += 1
    if a == 5:continue
    if a == 7:break
    print(a, end=' ')
else:
    print('while 수행') #while이 정상수행되는지를 확인, break 만나지 않으면 수행됨.
print()



import random
num = random.randint(1, 10) #난수발생
while True: #무한루프 == 1000, 1, -4
    print('1 ~ 10 사이의 컴이 가진 숫자를 입력하시오')
    guess = int(input())
    if guess == num:
        print('Success')
        break
    elif guess < num:
        print('press more bigger')
    elif guess > num:
        print('press more smaller')
    