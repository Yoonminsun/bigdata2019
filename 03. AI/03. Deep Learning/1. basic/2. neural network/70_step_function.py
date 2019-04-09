# 목적: 활성화 함수 - 계단 함수 (Step Function)
# coding: utf-8
import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    # x>0 이 True 이면 1, Fasle 이면 0
    # numpy.array(조건): 조건이 들어갈 경우 조건에 대하여 True 이면 1, False 이면 0
    return np.array(x>0,dtype=np.int)

# -5.0 ~ 5.0 까지 0.1 delta
# numpy.arange((start),stop,(step)): start이상, stop 미만 까지 step 간격의 값 array를 반환

# X = np.arange(-5.0, 5.0, 0.1)
X = np.arange(5,10,1)
Y = step_function(X)
plt.plot(X,Y)
plt.ylim(-0.1,1.1) # y축의 범위 지정
plt.show()