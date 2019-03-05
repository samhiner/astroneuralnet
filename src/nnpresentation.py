import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import random

def setup_nn():
	model = keras.Sequential()
	model.add(keras.layers.Dense(50, activation='relu'))
	model.add(keras.layers.Dense(50))
	model.add(keras.layers.Dropout(0.95))
	model.add(keras.layers.Dense(3, activation='softmax'))
	model.compile(optimizer=tf.train.AdagradOptimizer(0.005), loss='categorical_crossentropy', metrics=['accuracy'])
	return model

#set up NN
model = setup_nn()
data = np.load('../data/imagelist32.npy')
model.fit(data[:, 4:], data[:, 1:4], verbose=0)
model.load_weights('../data/nn/model.h5')

#get predictions
predictions = model.predict(data[:, 4:])

#show predictions
print(predictions)
print(data[:, 1:4])

for x in range(len(predictions)):
	value_map = data[:, 4:][x].reshape((128, 128))
	plt.imshow(value_map)

	highest_confidence = max(predictions[x])
	predicted_category = list(predictions[x]).index(highest_confidence)

	if (predicted_category == 2 and random.randint(0, 1) == 1):
		continue

	guess_name = ['Spiral', 'Elliptical', 'Uncertain'][predicted_category]
	actual_name = ['Spiral', 'Elliptical', 'Uncertain'][list(data[:, 1:4][x]).index(1)]

	fontdict = {'fontsize': 30, 'fontweight' : 10, 'verticalalignment': 'baseline', 'horizontalalignment': 'center'}
	plt.title('Guess: %s, %.0f%%.\nActual: %s.' % (guess_name, highest_confidence * 100, actual_name), fontdict = fontdict)
	plt.show(block=False)
	plt.pause(5)
