import numpy as np
import pandas as pd
from PIL import Image
import sys

#get a list of all of the objid's in the database
zoo_data = pd.read_csv('../data/zoodata.csv', sep=',', header=0)
filenames = list(zoo_data.loc[:,'OBJID'])

image_arr = []

#convert all of the images to greyscale arrays of pixels and write those arrays to a file
for file in range(0,len(filenames)):
	im = Image.open('../data/images/' + str(filenames[file]) + '.jpg').convert('LA')
	objArr = np.array(im.getdata())
	im.close()

	objArr = objArr[:,0] / 255

	image_arr.append(objArr)

	if file % 10000 == 0:
		print('On file: ' + str(file))

#add an ending bracket to the file so it can be evaluated as an array of arrays of pixels (aka an array of "images")
sys.getsizeof(array)

print('Done')