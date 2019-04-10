import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

data = load_iris()

features = data.data
feature_names = data.feature_names
target = data.target
target_names = data.target_names

X = tf.placeholder(tf.float32,[None,4])
Y = tf.placeholder(tf.float32,[None,3])

train_data, test_data, train_label, test_label = train_test_split(features,target)

print('train_data:',train_data.shape)
print('train_label:',train_label.shape)
print('test_data:',test_data.shape)
print('test_data:',test_label.shape)
W = tf.Variable(tf.zeros([4,3]))
b = tf.Variable(tf.zeros([3]))

logit_y = tf.matmul(X,W) + b

softmax_y = tf.nn.softmax(logit_y)
cross_entropy = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(softmax_y),reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for i in range(1000):
    sess.run(train_step,feed_dict={X:train_data, Y:train_label})

correct_prediction = tf.equal(tf.argmax(softmax_y,1), tf.argmax(Y,1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
print("정확도: ",sess.run(accuracy,feed_dict={X:test_data, Y:test_label}))