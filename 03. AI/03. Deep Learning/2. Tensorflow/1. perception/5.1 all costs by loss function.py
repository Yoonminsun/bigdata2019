# 손실함수, 책4장 p111
# 나쁨 지표, 특정 함수들을 통해 가중치와 편향을 변경시켜
# classifier와 실데이터의 차이(gap)를 구하여 현재 신경망의 성능이 얼마나 나쁜지 나타냄
import tensorflow as tf
import matplotlib.pyplot as plt

X = [1,2,3] # y=x 선형
Y = [1,2,3]

W = tf.placeholder(tf.float32) # 가중치

hypothesis = X * W

# 경사 하강법 공식 (경사법_경사하강법 : 기울기를 이용하여 함수의 최솟값 찾음)
# reduce_mean: 특정 차원을 제거한 모든 요소에 대한 평균 값
# 딥러닝에서 cose 는 '손실'의 의미로 사용된다
cost = tf.reduce_mean(tf.square(hypothesis - Y))

with tf.Session() as sess:
    W_val = []
    cost_val = []

    for i in range(-30,50):
        # feed_W: 학습률 => 너무 크면 최적의 cost를 찾기 어렵고
        #                  너무 작으면 성능상의 문제가 발생한다
        feed_W = i * 0.1

        # 가중치 값을 fee_W 연산을 통해 변경해줌
        # 인자 => [계속 값 변화를 볼 연산,함수들], feed_dict={변동될 값: 값목록,값연산}
        curr_cost, curr_W = sess.run([cost,W],feed_dict={W: feed_W})
        W_val.append(curr_W)
        cost_val.append(curr_cost)
        # 가중치에 따른 손실값이 각 같은 인덱스에 append 됨됨
    plt.plot(W_val,cost_val)
    plt.show()


