# coding: utf-8
import sys,os
sys.path.append(os.pardir) # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import pickle
from keras.datasets import mnist # keras: 딥러닝을 위한 dataset을 제공하는 모듈

def sigmoid(x):
    return 1/(1+np.exp(-x))

# 입력: [0.3,2.9,4.0]
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

def get_data():
    # 고정변수(x)      종속변수(t)
    #  11111            2
    #  00001
    #  11111
    #  10000
    #  11111
    (x_train, t_train), (x_test,t_test) = mnist.load_data()
    # 28*28 배열을 1*784 배열로 reshape 해준다. (한 줄로 만드는 작업)
    # 1111100001111111000011111
    x_train = x_train.reshape(60000,784).astype('float32')
    x_test = x_test.reshape(10000,784).astype('float')
    x_train /= 255 # 정규화로 0~255 를 0.0~1.0 범위로 변환
    # Shape 만 강조하기 위해 데이터 형식을 변환하는, 전처리(Pre-processing)
    x_test /= 255
    return x_test,t_test

def init_network():
    with open("sample_weight.pkl",'rb') as f:
        network = pickle.load(f) #가중치와 편향값이 배열로 정의된 파일
    return network

# 은닉층이 3계층
def predict(network,x):
    W1, W2, W3 = network['W1'],network['W2'],network['W3']
    b1,b2,b3 = network['b1'],network['b2'],network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)

    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)

    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y

x,t = get_data()
print(x)
network = init_network()
accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network,x[i])
    p = np.argmax(y) # 확률이 가장 높은 원소의 인덱스를 얻음
    if p == t[i]:
        accuracy_cnt += 1

print("Accuracy:"+str(float(accuracy_cnt)/len(x)))
