import tensorflow as tf

# 입력, 형태만 알려주는 placeholder로 정의
# X: 공부한 시간
X = tf.placeholder(tf.float32, shape=[None])

# 출력, 형태만 알려주는 placeholder로 정의
# Y: 국어 성적
Y = tf.placeholder(tf.float32,shape=[None])

# 변수 선언
# tf.random_normal: 0~1 사이의 정규확률 분포 값을 생성
W = tf.Variable(tf.random_normal([1]),name='weight')
b = tf.Variable(tf.random_normal([1]),name='bias')

# 가설식 정의 H(x) = Wx + b
hypothesis = X * W + b

# cost/loss function
# reduce_mean: 특정 차원을 제거한 모든 요소에 대한 평균 값, enumerative 타입
# loss function: 손실함수
#                => 각 데이터에 대한 예측값과 실제 관측값의 차이를 산술적으로 계산
cost = tf.reduce_mean(tf.square(hypothesis -  Y))

# Minimize, 최적화 함수
# GradientDescentOptimizer: 경사 하강법 적용
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

# 그래프 실행 준비
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# 그래프 실행, 500번 마다 화면 출력
for step in range(5001):
    cost_val,W_val,b_val,_ = sess.run([cost,W,b,train],feed_dict={X:[5,7], Y:[52,72]})
    if step%500 == 0:
        print(step,cost_val,W_val,b_val)

# 입력 X를 주고 예측 Y를 받아 화면 출력
print("예측Y : ",sess.run(hypothesis,feed_dict={X:[8]}))