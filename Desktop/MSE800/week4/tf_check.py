import tensorflow as tf

# Load MNIST dataset (images of handwritten digits)
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Show the shape of data
print("Training data shape:", x_train.shape)
print("Training labels shape:", y_train.shape)
