import tensorflow as tf
from keras.backend.tensorflow_backend import set_session

def share(simultaneous_users_count=2):
    """
    Allocates a fraction of the GPU memory for the current TensorFlow session based on the given number of simultaneous users
    """
    config = tf.ConfigProto()
    config.gpu_options.per_process_gpu_memory_fraction = 1.0 / simultaneous_users_count
    set_session(tf.Session(config=config))
