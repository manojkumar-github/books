import tensorflow as tf

h = tf.constant('Hello')
t = tf.constant(' Tensorflow!')

ht = h + t

#scope
with tf.Session() as sess: # acts as an interface to the externa tensorflow computation
    #run
    ans = sess.run(ht)

print ans # computates graph
print h + t