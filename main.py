import random  # Generating random numbers
import numpy as np  # It offers efficient arrays and mathematical operations
import tensorflow as tf  #  Framework for machine learning and deep learning

# Downloads a text file containing Shakespeare's works and prepares it for use.
filepath = tf.keras.utils.get_file(
    "shakespeare.txt",
    "https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt",
)

# Transforms the downloaded data into a usable format
# filepath is the path to the text file
# the "rb" parameter indicates that the file is read in binary mode
text = open(filepath, "rb").read().decode(encoding="utf-8")
