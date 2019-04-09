import tensorflow as tf

# 반드시 (()) 로 인자를 사용해야 함
# 2행 2열 배열 생성(모든 요소0, 상수 Tensor)
# 바로 디버거로 값 확인 불가능
ta = tf.zeros((2,2))
# type은 Tensor (딥러닝에서 tensor는 다차원 배열로 나타내는 데이터를 의미)
# ex) RGB 이미지는 3차원 배열로 나타내는 Tensor

# print(ta.eval()) # 에러 발생

session = tf.InteractiveSession() # 상수Tensor 초기화
print(ta.eval())
session.close()