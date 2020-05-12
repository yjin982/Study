#txt 파일을 읽어 dict로 저장

with open('mydict.txt', 'r') as ff:
    aa = eval(ff.read())    #보안 취약
    print('aa는', aa)
    print('aa의 타입은', type(aa))
    
import ast
with open('mydict.txt', 'r') as ff:
        aa = ff.read()
        print('aa는', aa)
        print('aa의 타입은', type(aa))
        
        bb = ast.literal_eval(aa) #보안 보장 
        print('bb는', bb)
        print('bb의 타입은', type(bb))