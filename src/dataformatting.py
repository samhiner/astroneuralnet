import numpy as np
import pandas as pd
from PIL import Image

#get a list of all of the objid's in the database
zoo_data = pd.read_csv('../data/zoodata.csv', sep=',', header=0)
filenames = list(zoo_data.loc[:,'OBJID'])

arr_file = open('../data/pixelsarray.txt' , 'a')

#convert all of the images to greyscale arrays of pixels and write those arrays to a file
for objID in filenames:
	im = Image.open('../data/images/' + str(objID) + '.jpg').convert('LA')
	objArr = np.array(im.getdata())
	im.close()

	objArr = objArr[:,0] / 255

	arr_file.write(str(list(objArr)) + ''',
	''')

#add an ending bracket to the file so it can be evaluated as an array of arrays of pixels (aka an array of "images")
arr_file.write(']')
arr_file.close()