# IMPORTS

import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
from PIL import Image

# NEURAL NET SETUP

class NeuralNet:
	#create the neural network and specify learning and drop rates
		#learning_rate: impressionability of model
		#drop_rate: likelihood of throwing out a node with dropout regularization
	def __init__(self, learning_rate, drop_rate):
		self.model = keras.Sequential()
		self.model.add(keras.layers.Dense(50, activation='relu'))
		self.model.add(keras.layers.Dense(50))
		self.model.add(keras.layers.Dropout(drop_rate))
		self.model.add(keras.layers.Dense(3, activation='softmax'))

		self.model.compile(optimizer=tf.train.AdagradOptimizer(learning_rate), loss='categorical_crossentropy', metrics=['accuracy'])
	
	#train the neural net on data
		#data: numpy array where 1st column is objid, 2-5 are one-hot labels, and 6+ is pixels from the image.
		#epochs: number of times you train over the dataset
		#batch_size: number of samples you predict before updating gradient based on how the predictions went
	def train(self, data, epochs, batch_size):
		features = data[:, 4:]
		labels = data[:, 1:4]
		self.model.fit(features, labels, epochs=epochs, batch_size=batch_size)

	#evaluate the model's performance
		#data: numpy array where 1st column is objid, 2-5 are one-hot labels, and 6+ is pixels from the image.
	def test(self, data):
		features = data[:, 4:]
		labels = data[:, 1:4]
		scores = self.model.evaluate(features, labels, verbose = 0)
		return scores

	#save the model and weights to files for later use
	def save(self):
		model_json = self.model.to_json()
		with open('../data/nn/model.json', 'w') as file:
		    file.write(model_json)
		self.model.save_weights('../data/nn/model.h5')
		print('Model Saved!')

neural_net = NeuralNet(learning_rate=0.005, drop_rate=0.95)

#RUNNING THE NEURAL NET

#if you are editing these constants make sure no validation/test files are before training files. 
#reading training files starts at zero and goes to NUM_TRAINING_FILES so set the first x as training and import the rest for validation/testing
NUM_TRAINING_FILES = 10
VALIDATION_SET = [20, 21]
TEST_SET = [21, 34]

#main training loop. trains on each file and each validation file between each file
for file in range(0, NUM_TRAINING_FILES):
	print('''
	TRAINING SET %s/34 
	''' % str(file + 1))
	neural_net.train(np.load('../data/imagelist%s.npy' % file), 10, 50)
	for validation_file in range(VALIDATION_SET[0], VALIDATION_SET[1]):
		scores = neural_net.test(np.load('../data/imagelist%s.npy' % validation_file))
		print('Validation Accuracy: %s' % scores[1])
		print('Validation Loss: %s' % scores[0])

#test the neural network on all of the test files
print('''
	TEST SET:
''')
for test_file in range(TEST_SET[0], TEST_SET[1]):
	scores = neural_net.test(np.load('../data/imagelist%s.npy' % test_file))
	print('Final Accuracy: %s' % scores[1])
	print('Final Loss: %s' % scores[0])

neural_net.save();

#TODO: maybe some more testing ability? maybe do this in another file where you test on whole dataset for demonstration purposes.
#TODO: option to save file