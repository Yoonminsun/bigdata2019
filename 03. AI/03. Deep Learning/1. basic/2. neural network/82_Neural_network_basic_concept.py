# 신경망 2계층
import numpy as np

X = np.array([1,2]) # 입력값으로 봄
X.shape

W = np.array([[1,3,5],[2,4,6]]) # 가중치로 봄
print(W)

print(W.shape)

Y = np.dot(X,W) # 행렬의 내적 (np.dot)
# 여기서는 입력값X 에 가중치W를 적용하여 각 은닉층값Y 를 구하는 과정이라 볼 수 있다.
print(Y)