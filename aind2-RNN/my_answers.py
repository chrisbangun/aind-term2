import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras

import re
import string

# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series,window_size):
    # containers for input/output pairs
    X = []
    y = []
    output = window_size
    index = 0
    while output < len(series):
        X.append(series[index:output])
        y.append(series[output])
        output += 1
        index += 1

    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)
    
    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(step_size, window_size):
    model = Sequential()
    model.add(LSTM(5, input_shape=(window_size, 1)))
    model.add(Dense(1))


### TODO: list all unique characters in the text and remove any non-english ones
def clean_text(text):
    ASCII_LETTERS = string.ascii_letters
    ENGLISH_PUNCTUATION = ',.\'!?;:'

    # find all unique characters in the text
    uniques = ''.join(set(text))

    # remove as many non-english characters and character sequences as you can 
    for char in uniques:
        if char not in ASCII_LETTERS and char not in ENGLISH_PUNCTUATION:
            text = text.replace(char, ' ')

    # shorten any extra dead space created above
    text = text.replace('  ',' ')


### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text,window_size,step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []
    index = 0
    while index + window_size < len(text):
        inputs.append(text[index:index+window_size])
        outputs.append(text[index+window_size])
        index += step_size

    
    return inputs,outputs
