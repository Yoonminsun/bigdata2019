import tensorflow as tf

X = tf.placeholder(tf.float32,shape=[None])
Y = tf.placeholder(tf.float32,shape=[None])

W = tf.Variable(tf.random_normal([1]),name='weight')

hypothesis = X * W

# 손실값
cost = tf.reduce_mean(tf.square(hypothesis - Y ))
# 경사하강법을 이용, 학습률 = 0.1
opt = tf.train.GradientDescentOptimizer(learning_rate=0.1)
# 위에서 설정한 경사하강법 으로 cost가 최소가 되는 값을 찾음
train = opt.minimize(cost)

with tf.Session() as sess:
    # 세션 초기화
    sess.run(tf.global_variables_initializer())

    for step in range(30):
        _, cost_val = sess.run([train,cost],feed_dict={X:[1,2,3],Y:[1,2,3]})
        print(step,cost_val,sess.run(W))