#for target in object:
for i in [1, 2, 3, 4, 5]:
    print(i, end=' ')
else:
    print('end for\n')

colors = {'r', 'g', 'b'}
for c in colors:
    print(c, end = ' ')
else:
    print()


soft = {'java' : 'web', 'python' : 'data', 'c' : 'system'}
for i in soft.items():
    #print(i)
    print(i[0], i[1], end=' ')
else:
    print('-')
    
for k, v in soft.items():
    print(k, v, end=' ')
else:
    print()

for k in soft.keys():
    print(k, end = ' ')
else:
    print()

for v in soft.values():
    print(v, end = ' ')
else:
    print()

for n in [2, 3]:
    print('{}단'.format(n))
    for i in (1,2,3,4,5,6,7,8,9):
        print('{0} * {1} = {2}'.format(n, i, n*i))
else:
    print()

li = ['a', 'b', 'c']
for idx, d in enumerate(li):
    print(idx, d)
else:
    print()
    
datas = [1,2,3,4,5,6]
for i in datas:
    if i == 3:
        #continue
        break
    print(i, end=' ')
else:
    print('정상 종료')
print()


#문자열 검색 후 단어 수 출력
import re
ss = '''
영화 '쥬라기공원' 시리즈에 빠지지 않고 등장하는 공룡 중 하나가 높은 지능 을 갖고 자기보다 덩치 가 훨씬 더 큰 공룡 을 집단 사냥 을 하는 공룡 '랩터'(raptor)다. 
공룡 벨로키랍토르(Velociraptor)를 줄인 말인데, 사실 관객의 공포 를 불러일으킨 영악한 집단 사냥 기술 은 친척뻘인 공룡 '데이노니쿠스'(Deinonychus antirrhopus)를 모델 로 했다. 
영화 에서는 공포 공룡 랩터 로 묘사 됐지만 실제로는 '공포 무서운 발톱'이라는 뜻을 가진 공룡 데이노니쿠스 였던 것이다. 하지만 이 모델 공룡 데이노니쿠스 마저도 집단 사냥 을 한 것은 아니라는 연구 결과 가 나왔다.
'''
print(ss)
ss2 = re.sub(r'[^가-힣\s]', '', ss) #한글 이외에 공백처리
print(ss2)

ss3 = ss2.split(' ')
print(ss3)
print(len(ss3))
sdata = set(ss3)
print(len(sdata))

cnt = {} #단어의 발생 횟수를 dict type으로 저장
for i in ss3:
    if i in cnt :
        cnt[i] += 1
    else:
        cnt[i] = 1
#print(cnt)
print({k:y for k, y in cnt.items() if y > 1})


#dict 자료로 과일값 출력
price = {'apple':500, 'korea melon':600, 'water melon': 12000}
my = {'apple':2, 'water melon':1}
bill = sum(price[f] * my[f] for f in my)
print('total price : {} won'.format(bill))

print()
datas = [1, 2, 'a', True, 3]
li = [i * i for i in datas if type(i) == int]
print(li)

datas = {1, 1, 2, 2, 3}
se = {i * i for i in datas}
print(se)

id_name = {1:'tom', 2:'james'}
name_id = {val:key for key, val in id_name.items()}
print(name_id)

print()
temp = [1,2,3]
for i in temp:
    print(i, end=' ')
else:
    print()
print([i for i in temp])
print({i for i in temp})
print((i for i in temp))

temp2 = list()
for i in temp:
    temp2.append(i)
else:
    print(temp2)

temp3 = [i + 10 for i in temp]
print(temp3)

print()
aa = [(1, 2), (3, 4), (5, 6)]
for a, b in aa:
    print(a + b)
else:
    print('\n')

# range
print(list(range(1,6)))
print(tuple(range(1,6)))
print(set(range(1,6)))

for i in range(6):
    print(i, end = ' ')
else:
    print()

for i in range(2, 10):
    for j in range(1, 10):
        print('{0} * {1} = {2}'.format(i, j, i*j), end = ' ')
    print()
else:
    print()
