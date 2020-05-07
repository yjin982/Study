# 집합 자료형 : String, List
# 1) String : 문자열 취급 (순서형)
print('-' *10, 'String', '-' *10)
s = 'sequence'
print(len(s))
print(s.count('e'))
print(s.find('e'), s.find('e', 3), s.rfind('e'))
print(s.startswith('s'))

ss = 'mbc'
print('mbc', id(ss))

# 1) String 슬라이싱
print(s[0], s[2:4], s[:3], s[3:])
print(s[-1], s[-4:-1], s[-4:], s[::2])
''' s[0] = 'k'  #error 수정불가 '''
ss = 'ice cream'
ss2 = ss.split(sep=' ')
print(ss2)
print(' '.join(ss2))

print('\n', '-' *10, 'List', '-' *10)
# 2) List : 배열과 유사, 순서가 있다. 변경가능, 여러 종류의 자료 허용
a = [1, 2, 3]
b = [10, a, 12.3, True, 'red']
print(a, id(a))
print(b, id(b))

print(b[0], b[1], b[1][:2])
b[0] = 'mem'
print(b)
b.remove('red') #값에 의한 삭제
print(b)
del b[3]          #순서에 의한 삭제
print(b)

family = ['mother', 'father', 'me']
family.append('sister')
family.remove('me')
family.insert(0, 'grandfa')
family.extend(['son', 'brother', 'ant'])
family += ['Mr', 'Miss']
print(family, len(family), family[0])

li = [[0, 1, 2], [3, 4, 5]]
print(li[0], ' ', li[0][0])

name = ['tom', 'james', 'oscar']
name2 = name
print(name, name2)
name[0] = 'sujan'
name2[1] = 'john'
print(name, name2)

import copy
name3 = copy.deepcopy(name) #새로운 객체의 주소를 기억
print(name, name3)
name[0] = 'kildong'
print(name, name3)

# stack
t1 = [1, 2, 3]
t1.append(4)
print(t1)
t1.pop()
print(t1)
t1.pop()
print(t1)

#queue
t1 = [1, 2, 3]
t1.append(4)
print(t1)
t1.pop(0)
print(t1)
t1.pop(0)
print(t1)