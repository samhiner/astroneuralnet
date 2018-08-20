import tensorflow as tf
from tensorflow import keras
import numpy as np
import h5py

# NEURAL NET DESIGN

class NeuralNet:
	#create the neural network
		#learning_rate: self-explanatory
		#drop_rate: likelihood of throwing out a node with dropout regularization (this is logarithmic btw so 0.9 and 0.99 are very different)
		#train_data: training dataset [features, labels]
		#val_data: validation dataset [features, labels]
	def __init__(self, learning_rate, drop_rate, train_data, val_data):
		self.train_features = train_data[0]
		self.train_labels = train_data[1]
		self.val_features = val_data[0]
		self.val_labels = val_data[1]

		self.model = keras.Sequential()
		self.model.add(keras.layers.Dense(100, activation='relu'))
		self.model.add(keras.layers.Dense(100))
		self.model.add(keras.layers.Dropout(drop_rate, noise_shape=None, seed=None))
		self.model.add(keras.layers.Dense(10, activation='softmax'))

		self.model.compile(optimizer=tf.train.AdagradOptimizer(learning_rate), loss='categorical_crossentropy', metrics=['accuracy'])

	#traing the neural net
		#epochs: number of times you will train over the dataset
		#batch_size: number of samples the algo views before updating the gradient
	def train(self, epochs, batch_size):
		self.model.fit(self.train_features, self.train_labels, epochs = epochs, batch_size = batch_size, validation_data=(self.val_features, self.val_labels))



# DATA FORMATTING

def smaller_split(data,size):
	return data[:size], data[size:]

def split_data(data, train_size = None, training = True):
	labels = data[:,0]
	labels = tf.keras.utils.to_categorical(labels)
	features = data[:,1:]
	features = features / 255

	if not training:
		return features, labels

	train_labels, val_labels = smaller_split(labels, train_size)
	train_features, val_features = smaller_split(features, train_size)
	return [train_features, train_labels], [val_features, val_labels]

#get the first half of the mnist data (second half is for testing) and shuffle it.
print('Getting Data...')
mnist_data = np.genfromtxt('https://dl.google.com/mlcc/mledu-datasets/mnist_train_small.csv', delimiter=',')
#mnist_data = mnist_data[:10001]
np.random.shuffle(mnist_data)

train_data, val_data = split_data(data = mnist_data, train_size = 18000)
print('Getting Data Complete.')


# RUNNING THE NEURAL NETWORK

print('Training Neural Net...')
myNet = NeuralNet(learning_rate = 0.076, drop_rate = 0.927, train_data = train_data, val_data = val_data)
myNet.train(epochs = 100, batch_size = 50)
print('Training Neural Net Complete.')

# TESTING THE NEURAL NETWORK

print('Getting Test Data...')
test_data = np.genfromtxt('https://dl.google.com/mlcc/mledu-datasets/mnist_test.csv', delimiter=',')
#test_data = test_data[10001:]
np.random.shuffle(test_data)
test_features, test_labels = split_data(data = test_data, training = False)
print('Getting Test Data Complete.')

score = myNet.model.evaluate(test_features, test_labels, batch_size = 128)
print('Test Loss: ' + str(score[0]))
print('Test Accuracy: ' + str(score[1]))

# SAVING THE NETWORK

if score[1] >= 0.95:
	myNet.model.save('mnist_over_95.h5')
	print('Network Saved!')
else:
	print('Network not accurate enough to save.')