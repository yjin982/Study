# 파일 i/o

import os

try:
    print(os.getcwd()) #현재 작업 경로
    
    '''파일 읽기'''
    #f1 = open(r'c:\Work\py_sou\pypro01\pack02\ftest.txt', mode = 'r', encoding = 'utf-8')
    f1 = open(r'ftest.txt', mode = 'r', encoding = 'utf-8') #현재 작업경로와 같은 경우
    print(f1)
    print(f1.read())
    f1.close()
    
    '''파일 저장'''
    f2 = open('ftest2.txt', mode = 'w', encoding = 'utf-8')
    f2.write('생각만 해도 무섭다\n')
    f2.write('얼굴을 찌푸렸지만\n')
    f2.write('너에게 얘기 못해 정말로\n')
    f2.close()
    print('save success')
    
    '''파일 추가'''
    f3 = open('ftest2.txt', mode = 'a', encoding = 'utf-8')
    f3.write('살짝 설렜어 난\n')
    f3.write('(그럴 일 없지만)\n')
    f3.close()
    print('append success')
    
    f4 = open('ftest2.txt', mode = 'r', encoding = 'utf-8')
    #print(f4.read())      #모든 파일 읽기
    #print(f4.readline()) #한 행씩 읽기
    print(f4.readlines())  #list type으로 전체 읽기
    f4.close()
    
except Exception as e:
    print(e)
    

#with 블럭 사용
try:
    '''파일 저장'''
    with open('ftest3.txt', mode = 'w', encoding = 'utf-8') as ff1:
        ff1.write('파이썬으로 문서 저장\n')
        ff1.write('with 블럭 사용\n')
        ff1.write('close() 문을 사용하지 않는다.\n')
    
    '''파일 읽기'''
    with open('ftest3.txt', mode = 'r', encoding = 'utf-8') as ff2:
        print(ff2.read())
except Exception as e:
    print(e)
    
    
#복합 객체(pickle) 저장 및 읽기
import pickle
try:
    dictdata = {'tom':'111-1111', 'kildong':'222-2222'}
    listdata = ['mouse', 'keyboard']
    tupledata = (dictdata, listdata) #복합 객체
    
    '''객체 저장'''
    with open('hi.dat', 'wb') as ff3: #바이너리로 저장, 메모리 절감효과
        pickle.dump(tupledata, ff3)  #target, file object
        pickle.dump(listdata, ff3)
        
    '''객체 읽기'''
    with open('hi.dat', 'rb') as ff4:
        a, b = pickle.load(ff4)
        print(a)
        print(b)
        c = pickle.load(ff4)
        print(c)
except Exception as e:
    print(e)