# csv read, 미완성 코드 , 참조용
import tensorflow as tf
filename_queue = tf.train.string_input_producer(['파일1','파일2','...'],shuffle=False, name='filename_queue')

reader = tf.TextLineReader()
key, value = reader.read(filename_queue)

record_defaults = [[0.],[0.],[0.],[0.]] # 값이 없는 경우 dafault 설정 ( type 맞춰서 )
xy = tf.decode_csv(value,record_defaults=record_defaults)

# shffle 되기를 원하면 suffle_batch 를 이용
train_x_batch, train_y_batch = tf.train.batch([xy[0:-1],xy[-1:]],batch_size=10)

# X,Y,W,b, hypothesis, cost, optimizer, train  정의

sess = tf.Session()

# global variables initializer

coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(sess=sess,coord=coord)

for step in range(2001):
    x_batch, y_batch = sess.run([train_x_batch,train_y_batch])
    # 사용시 x_batch, y_batch 를 feed_dict 으로 전달하여 사용 (X: x_batch, Y: y_batch)
    # sess.run, step%10 print

coord.request_stop()
coord.join(threads)