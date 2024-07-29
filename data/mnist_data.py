# data/mnist_data.py

import numpy as np
from tensorflow.keras.datasets import mnist

def load_data():
    # Load MNIST dataset
    (x_train, y_train), (x_val, y_val) = mnist.load_data()
    
    # Preprocess data
    x_train, x_val = x_train / 255.0, x_val / 255.0
    
    # Expand dimensions to match input shape of the model
    x_train = np.expand_dims(x_train, -1)
    x_val = np.expand_dims(x_val, -1)
    
    return x_train, y_train, x_val, y_val
