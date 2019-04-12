import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

data = load_iris()

# 수집 데이터 포맷 명시
# - 데이터 요약: 꽃의 종류와 그에 따른 특성
# - 고정 변수 명시: 4가지 특성 값
# - 종속 변수 명시: 꽃의 종류
# - 각각의 필드의 의미 명시
#   load_iris 의 출력값 : dict_keys([‘data’, ‘target’, ‘target_names’, ‘DESCR’, ‘feature_names’])
#   - data : 각 꽃의 특성(feature)
#   - target : 꽃이 어떤 종류인지 0,1,2 로 나타냄
#   - target_names : 꽃이 어떤 종류인지 이름으로 나타냄 (Setosa,Versicolor,Virginica)
#   - feature_names : data의 특성이 무엇을 의미하는지 나타냄
#                     [‘sepal length’,‘sepal width’,‘petal length’,‘petal width’]
features = data.data
target = data.target

# 변수 설정
X = tf.placeholder(tf.float32,[None,4]) # 입력 데이터 형태는 특성 4가지
Y = tf.placeholder(tf.float32,[None,3]) # 3가지 종류 분류

W = tf.Variable(tf.zeros([4,3]))
b = tf.Variable(tf.zeros([3]))

train_data, test_data, train_label1, test_label1 = train_test_split(features,target)
train_label=[]
test_label=[]

# label 형태가 0,1,2 중 1개의 값씩 들어가 있으므로
# 0 -> [1. 0. 0.]
# 1 -> [0. 1. 0.]
# 2 -> [0. 0. 1.]
# 처럼 해당 값을 인덱스로 하여 전처리 해줌
for i in range(len(train_label1)):
    val = [0.,0.,0.]
    val[train_label1[i]]=1.
    train_label.append(val)

for i in range(len(test_label1)):
    val = [0.,0.,0.]
    val[test_label1[i]]=1.
    test_label.append(val)

logit_y = tf.matmul(X,W) + b

# 활성화 함수 설정
softmax_y = tf.nn.softmax(logit_y)
# 손실함수 및 학습
cross_entropy = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(softmax_y),reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
print(train_data)
for i in range(1000):
    sess.run(train_step,feed_dict={X:train_data, Y:train_label})

# 결과 예측
correct_prediction = tf.equal(tf.argmax(softmax_y,1), tf.argmax(Y,1))

# 결과 검증
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
print("정확도: ",sess.run(accuracy,feed_dict={X:test_data, Y:test_label}))

# - 결과 출력
# (train_test_split 에서 random_state = True 가 default 이므로 계속 random으로 분리 하여 정확도가 조금씩 달라진다)
# 정확도:  0.94736844
# 정확도:  1.0
# 정확도:  0.9736842 ...
