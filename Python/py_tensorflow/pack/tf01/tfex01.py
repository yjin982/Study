'''   첫 텐서플로    '''
# GPU가 없으면 발생하는 경고메세지
# SSE 및 AVX 등의 경고는 소스를 빌드 하면 없어지지만, 명시적으로 경고 없애기
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# # 현재 시스템에 장착된 CPU/GPU 목록 확인
# from tensorflow.python.client import device_lib
# print(device_lib.list_local_devices())
# 
# # 텐서플로 버전 및 gpu 가능 여부
# print(tf.__version__)
# print(tf.keras.__version__)
# print('GPU 사용 가능 여부 : {}'.format('가능' if tf.config.list_physical_devices('GPU') else '불가능'))

'''
    tensor의 이해
      tensorflow의 기본 구성 요소. 데이터를 위한 컨테이너로 대개의 경우 수치 데이터를 다루는 수치용 컨테이너
      임의의 차원 갯수를 가지는 행렬의 일반화된 객체.
'''
# 상수 정의 (상수 텐서를 생성)
print(1)  # 파이썬의 상수값 1과 텐서의 상수값1은 다른 거임.
print(tf.constant(1))       # scala = 상수 = 0차원 텐서 = shape이 0
print(tf.constant([1]))     # vector = 1차원 리스트,배열 = 1차원 텐서
print(tf.constant([[1]]))   # matrix = 2차원 텐서 = 1행1열
print(tf.constant([[1, 2]]))# matrix = 2차원 텐서 = 1행2열

print(tf.rank(tf.constant(1.)), '  ', tf.rank(tf.constant([[1]])))   # 차원
print(tf.constant(1.).get_shape(), '  ', tf.constant([[1]]).get_shape())   # shape



a = tf.constant([1, 2])
b = tf.constant([3, 4])
c = a + b   # [4, 6], shape=(2, )
c = tf.add(a, b)  # 텐서플로가 지원하는 더하기 함수. 동일한 결과임
print(c, '  ', type(c)) # EagerTensor



# d = tf.constant([3])
# d = 3     # 텐서로 자동 변환
d = tf.constant([[3]]) # e의 결과가 2차원으로 됨
e = c + d # [4, 6] + 3
print(e)  # [7, 9]  # d의 차원을 늘려서 각 요소마다 더하기를 시행(broadcast 연산)

# 상수를 텐서화
print(7, type(7))
print(tf.convert_to_tensor(7))  # 명시적으로 텐서화, 타입지정 가능
print(tf.cast(7, dtype=tf.float32)) # 타입 명시 필수

# numpy의 ndarray와 tensor 사이에 자동 변환
import numpy as np
arr = np.array([1, 2])
print(arr, '  ', type(arr))
tfarr = tf.add(arr, 5)
print(tfarr, '  ', type(tfarr)) # 자동 형변환
print(tfarr.numpy(), '  ', type(tfarr.numpy())) # numpy 배열로 변환
print(np.add(tfarr, 3)) # 텐서가 넘파이 연산을 수행하면 결과가 넘파이가 됨. (자동 변환 후 연산)
