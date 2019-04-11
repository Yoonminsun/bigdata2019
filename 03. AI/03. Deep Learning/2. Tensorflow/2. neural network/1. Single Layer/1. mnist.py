# Data Source: www.kaggle.com/c/titanic
import tensorflow as tf

# MNIST 데이터를 다운로드
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/",one_hot=True)

# 수집 데이터 포맷 명시
# - 데이터 요약: 손글씨 숫자 이미지
# - 고정 변수 명시: 이미지의 픽셀 정보
# - 종속 변수 명시: 0~9 까지의 숫자 판별
# - 각각의 필드의 의미 명시

# 변수 설정
X = tf.placeholder(tf.float32, [None, 784]) # mnist 이미지 데이터의 형태는 28*28 = 784
Y = tf.placeholder(tf.float32, [None, 10])  # 0-9 숫자 분류 => 10 classes

# Logistic Classifier (Linear Classifier)
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))
# matmul : 행렬 내적(곱) _ 앞에서 배운 numpy.dot 과 같은 것
logit_y = tf.matmul(X,W) + b

# 활성화 함수 설정
# softmax와 cross-entropy 모델을 설정
softmax_y = tf.nn.softmax(logit_y)
cross_entropy = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(softmax_y),reduction_indices=[1]))
# 경사하강법으로 모델을 학습
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100) # 배치크기 100
    sess.run(train_step,feed_dict={X:batch_xs, Y:batch_ys})
    if i==0:
        print(batch_xs)
        print(batch_ys)

# 결과 예측
correct_prediction = tf.equal(tf.argmax(softmax_y,1), tf.argmax(Y,1))
print(correct_prediction)
# 결과 검증
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
print("정확도 : ",sess.run(accuracy,feed_dict={X: mnist.test.images, Y: mnist.test.labels}))