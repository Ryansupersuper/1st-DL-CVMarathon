from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import Input, Dense
from keras.models import Model

input = Input(shape=(28,28,1))