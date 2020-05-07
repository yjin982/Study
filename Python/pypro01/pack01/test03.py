# 집합 자료형 : Tuple, Set, Dict
# 3) Tuple : 리스트와 유사. 읽기 전용
t = 'a', 'b', 'c', 'a'
print(t, t.count('a'), t.index('b'))
print(t[0])
#t.[0] = 's' #error 변경불가

#형변환 후 값변경
q = list(t)
q[0] = 'ㅅ'
t = tuple(q)
print(t)

t1 = (1, 2)
a, b = t1
b,a  = a, b
t1 = a, b
print(t1)

t2 = (1)
t3 = (1, )
print(t2, t3, type(t2), type(t3)) #t2 = <class 'int'>, t3 = <class 'tuple'>  | 요소값이 하나일때 주의


# 4) Set : 순서X, 중복 X
s1 = {1, 2, 3, 1}
print(s1)  #{1, 2, 3}
s2 = {3, 4}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1 - s2, s1 | s2, s1 & s2)
#print(s1[0]) #error index X
s2.add(5)
print(s2)
s2.update({6, 7})
s2.update((8, 9))
s2.update([10, 11])
print(s2)

s2.discard(7)
s2.remove(6)
s2.discard(7)    #해당값이 없어도 통과
#s2.remove(6) #error
print(s2)
s2.clear()
print(s2)

#set을 이용해 중복자료 제거
li = [1, 2, 1, 2]
s = set(li)
li = list(s)
print(li)

# 5) Dict : {key : value}, index X
dic1 = dict(k1 = 1, k2 = 'Mr.', k3 = 1.2)
print(dic1)
dic2 = {'python' : 'snake', 'java' : 'coffee', 'spring' : 'summer'}
print(dic2, len(dic2))
print(dic2['java'])
#print(dic2[0]) #error

dic2['c#'] = 'not use'
print(dic2)
del dic2['c#']
print(dic2)
dic2['java'] = 'programing lan'
print(dic2['java'])
print(dic2.get('java'))
print(dic2.keys())
print(dic2.values())