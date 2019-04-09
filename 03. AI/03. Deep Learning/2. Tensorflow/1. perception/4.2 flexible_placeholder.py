import tensorflow as tf

# 플레이스 홀더 정의
# 정수 자료형을 가진 배열, 크기는 None(을 입력받을 것이라고 명시)
# 크기가 None이면 placeholder.run 마다 flexible하게 값을 입력받을 수 있다, 생략도 같음
a = tf.placeholder(tf.int32,[None])

# 배열의 모든 값을 10배(값*10)하는 연산 정의
b = tf.constant(10) # 상수 10
x10_op = a*b

# 세션 시작
sess = tf.Session()

# 플레이스 홀더에 값을 넣고 실행
# x2_op는 파이썬의 lambda 같은 개념
# 정수형 자료 3개 배열을 입력받을 것이라 명시한 a 에 각 값을 넣고
# x2_op 연산에 값을 매핑하여 run
r1 = sess.run(x10_op, feed_dict={a:[1,2,3,4,5]})
print(r1)
r2 = sess.run(x10_op,feed_dict={a:[10,20]})
print(r2)