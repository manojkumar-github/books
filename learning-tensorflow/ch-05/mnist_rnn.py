import tensorflow as tf

#Import MNIST Data
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/data", one_hot=True)

# Define some parameters
element_size = 28 # dimension of each vector in the sequence
time_steps = 28 # number of such elements in the sequence
num_classes = 10
batch_size = 128
hidden_layer_size = 128

# to save tensor-board model summaries
LOG_DIR = "logs/RNN_with_summaries"

# create placeholders for inputs, labels
_inputs = tf.placeholder(tf.float32, shape=[None, time_steps, element_size], name = 'inputs')
y = tf.placeholder(tf.float32, shape=[None, num_classes], name = 'labels')

# when we load data with built-in MNIST loader, it comes in unrolled form - a vector of 784 pixels
# therefore, we have to reshape the data to 3D form that is required for RNN during training

batch_x, batch_y = mnist.train.next_batch(batch_size)
# Reshape data to get 28 sequences of 28 pixels
batch_x = batch_x.reshape(batch_size, time_steps, element_size)

def variable_summaries(var):
    with tf.name_scope('summaries'):
        mean = tf.reduce_mean(var)
        tf.su
