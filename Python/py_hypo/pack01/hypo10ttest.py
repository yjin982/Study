'''
    집단에 따른 검정 방법
'''
import numpy as np
import scipy.stats as stats

'''  수면제1 종류를 먹다가 수면제2 종류를 먹었을 때 수면시간의 변화여부 검정
     - 서로 다른 두 사람이 수면제를 복용한 경우 : 독립표본 t 검정
     - 한 사람이 수면제를 복용한 경우 : 대응표본 t 검정
'''
x1 = np.array([0.7, 0.3, 0.1, -0.3, 0.2]) #수면제1
x2 = np.array([1.0, 1.3, 0.3, -0.1, 0.8]) #수면제2

result = stats.ttest_ind(x1, x2)
print('독립표본 t 검정 : ', result)
if result.pvalue >= 0.05:
    print('수면제 종류에 따른 수면시간에 변화가 없다.') # 변화가 미미하다. 확실해 결론짓지말고 애매하게 써주는 것이 좋음. 그것이 확률이니까.
else:
    print('수면제 종류에 따른 수면시간에 변화가 있다.')

print()
result2 = stats.ttest_rel(x1, x2)
print('대응표본 t 검정 : ', result2)
if result2.pvalue >= 0.05:
    print('수면제 종류에 따른 수면시간에 변화가 없다.')
else:
    print('수면제 종류에 따른 수면시간에 변화가 있다.')
