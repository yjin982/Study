'''
여러 줄 주석
'''
#한줄 주석
from builtins import type, isinstance, divmod
var1 = '안녕'
print(var1)

var1 = 5; print(var1);
var1 = '변수 선언시 type은 저장되는 자료에 의해 결정됨'
print(var1)

a = 10
b = 20.1
c = b
print(a, b, c)
print('주소 출력 : ', id(a), id(10), id(b), id(20.1), id(c))
print(a is b, a == b) # is : 주소비교, == 값비교
print(b is c, b == c) 

print()
A = 1; a = 2;
print(A, ' ', a)

print()
import keyword
print('예약어 : ', keyword.kwlist)

print('\n진법')
print(10, oct(10), hex(10), bin(10)) #10 0o12 0xa 0b1010
print(10, 0o12, 0xa, 0b1010)

print()
print(7, type(7))
print(7.1, type(7.1))
print(7 + 3j, type(7 + 3j))
print(True, type(True))
print('kbs', type('kbs'))
print((1,), type((1, )))
print([1], type([1]))
print({1}, type({1}))
print({'k' : 1}, type({'k' : 1}))

print(isinstance(a, int))
print(isinstance(a, float))

print('------- 연산자 -------')
v1 = 2
v1 = v2 = v3 = 5
print(v1, v2, v3)

v1 = 1, 2, 3 #(1, 2, 3) 튜플형
print(v1)
v2, v3 = 10, 20
print(v2, v3)

v1, v2 = 10, 20
v2, v1 = v1, v2
print(v1, v2)

print('------- packing -------')
v1, *v2 = [1, 2, 3, 4, 5]
print(v1) #1
print(v2) #[2, 3, 4, 5]

*v1, v2 = [1, 2, 3, 4, 5]
print(v1) #[1, 2, 3, 4]
print(v2) #5

*v1, v2, v3 = 1, 2, 3, 4, 5
print(v1) #[1, 2, 3]
print(v2) #4
print(v3) #5

print('------- 산술 연산자 -------')
print(5 + 3, 5 - 3, 5 * 3)
print(5 / 3, 5 // 3, 5 % 3, 5 ** 3)
print(divmod(5, 3)) #(1, 2) 몫과 나머지를 튜플형으로
print(3 + 4 * 5, (3 + 4) * 5)

print()
print('관계 연산 : ', end = '')
print(5 > 3, 5 == 3, 5 != 3)
print('논리 연산 : ', end = '')
print(5 > 3 and 4 <= 3, not(5 >= 3))
print('문자열 더하기 : ', end='')
print('한' + '국' + '만세')
print('한국' * 10)

print('누적 : ', end='')
a = 10
a = a + 1
a += 1 # ++, -- 증감연산자 없음
print(a)
print(a * -1, -a, --a)

print('bool 처리 : ', bool(0), bool(0.0), bool(1), bool(True), bool(False))
print('bool 처리 : ', bool(100), bool(-10), bool(None), bool(''), bool([]), bool({})) #bool에서 0을 제외한 나머지 숫자는 True

print()
print('kbs\tbs')
print('kbs\nbs')
print(r'kbs\tbs') #r = 이스케이프문자 무시
print(r'kbs\nbs')

print()
print(format(1.2345, '10.3f'))
print('나이가 %d입니다'%22)
print('나이가 %s입니다'%'스물')
print('나이가%d입니다 %s'%(22,'스물'))
print('나이가%s입니다 %s'%(22,'스물'))
print('나이가%d입니다 %s  %f'%(22,'스물', 22.5))

print('이름은 {} 나이는 {}'.format('하하하', 33))
print('이름은 {0} 나이는 {1}'.format('하하하', 33))
print('이름은 {1} 나이는 {0}'.format('하하하', 33))
print('이름은 {1} 나이는 {0}   {1}   {1}'.format('하하하', 33))
