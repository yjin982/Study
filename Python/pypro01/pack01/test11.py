# 사용자 정의 모듈 연습
'''
...
...
''' 
#여러 모듈 중 응용프로그램의 시작 모듈을 명시적으로 표시하기
if __name__ == '__main__':
        print('I AM a 최상위 메인 모듈')

import pack01.myMod1      #내가 만든 모듈은 패키지명을 써줘야함
print(dir(pack01.myMod1)) #myMod1이 가진 멤버를 보여줌

list1 = [1, 2]
list2 = [3, 4, 5]
pack01.myMod1.ListSum(list1, list2)

pack01.myMod1.honey()

from pack01 import myMod1
myMod1.honey()

from pack01.myMod1 import honey, dude, gvar
honey()
dude()
print(gvar)

#패키지가 다른 사용자 정의 모듈 사용
from etc.myMod2 import *
print('합', sums(5, 3))
print('차', subs(5, 3))

#외부파일 path 지정으로 사용
import myMod3
print('곱', myMod3.muls(5, 3))
from myMod3 import divs
print('제', divs(5, 3))