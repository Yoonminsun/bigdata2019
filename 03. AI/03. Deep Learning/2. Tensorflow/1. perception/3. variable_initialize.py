import tensorflow as tf

# 상수 텐서, 모든 요소값이 0인 3*3 행렬
W1 = tf.zeros((3,3))

# 변수 텐서, 모든 요소값이 0인 2*2 행렬
W2 = tf.Variable(tf.zeros((2,2)),name='weights')

session = tf.InteractiveSession() # 상수 텐서만 초기화 되므로
session.run(tf.global_variables_initializer()) # 변수 텐서를 초기화 하기 위한 구문
print(W1.eval())
print(W2.eval())

session.close()