import tensorflow as tf

# 플레이스 홀더 정의
# 정수 자료형 3개를 가진 배열(을 입력받을 것이라고 명시)
a = tf.placeholder(tf.int32,[3])

# 배열의 모든 값을 2배(값*2)하는 연산 정의
b = tf.constant(2) # 상수 2
x2_op = a*b

# 세션 시작
sess = tf.Session()

# 플레이스 홀더에 값을 넣고 실행
# x2_op는 파이썬의 lambda 같은 개념
# 정수형 자료 3개 배열을 입력받을 것이라 명시한 a 에 각 값을 넣고
# x2_op 연산에 값을 매핑하여 run
r1 = sess.run(x2_op, feed_dict={a:[1,2,3]})
print(r1)
r2 = sess.run(x2_op,feed_dict={a:[10,20,10]})
print(r2)