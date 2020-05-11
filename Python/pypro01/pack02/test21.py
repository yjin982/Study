# 예외 처리 : trt ~ except

def divide(a, b):
    return a / b

''' ... '''

try:
    c = divide(5, 2)
    #c = divide(5, 0)
    print(c)
    
    a = [1, 2]
    print(a[0])
    #print(a[3])
    
    f = open('c:/Work/abc.txt')
except ZeroDivisionError:
    print('두번째 숫자는 0을 주지 마시오')
except IndexError as e:
    print('참조 범위 오류 :', e)
except Exception as err:
    print('기타 에러 :', err)

print('exit')