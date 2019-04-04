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
    # 각 가중치의 열갯수로 각 층의 뉴런 갯수를 정할 수 있음
    # 내적은 a 내적 b -> 결과가 a의 행갯수, b의 열갯수를 따르기 때문
    # 1*784 내적 1*50 -> 1*50 >은닉층1
    # 1*50 내적 1*100 -> 1*100 >은닉층2
    # 1*100 내적 1*10 -> 1*10 >출력층
    # 따라서 결국 출력이 10개가 나올 수 있는 것! (0~9의 이미지에 따라 판별하므로 10으로 설정)
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
network = init_network()
batch_size = 100
accuracy_cnt = 0
for i in range(0,len(x),batch_size):
    x_batch = x[i:i+batch_size]
    y_batch = predict(network,x_batch)
    p = np.argmax(y_batch,axis=1) # 1차원을 축으로 최대 값을 찾는다
    accuracy_cnt += np.sum(p == t[i:i+batch_size])

print("Accuracy:"+str(float(accuracy_cnt)/len(x)))
