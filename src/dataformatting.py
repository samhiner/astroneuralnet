import numpy as np
import pandas as pd
from PIL import Image
import scipy.ndimage

#makes it easy to change number of files the list made here should be split across
NUM_FILES = 34
objects_per_file = int(667944/NUM_FILES)

#get a list of filenames split into 14 groups
def get_filenames():
	#get a list nested list where every element has objid, and one-hot category for type
	raw_filenames = zoo_data.loc[:,['OBJID', 'SPIRAL','ELLIPTICAL', 'UNCERTAIN']]
	raw_filenames = raw_filenames.values.tolist()
	#split up list into 34 sublists (each sublist is a list of what images should be loaded into the memory at a specific time)
	filenames = []
	for x in range(0,NUM_FILES - 1):
		filenames.append(raw_filenames[objects_per_file * x : objects_per_file * (x + 1)])
	filenames.append(raw_filenames[(objects_per_file * NUM_FILES - 1):])

	return filenames

#convert an image to greyscale array of pixels
def get_img_px(file):
	im = Image.open('../data/images/' + str(file) + '.jpg').convert('LA')
	objArr = np.array(im.getdata())
	im.close()
	objArr = objArr[:,0] / 255
	objArr = scipy.ndimage.filters.gaussian_filter(objArr, 1)	
	return objArr

zoo_data = pd.read_csv('../data/zoodata.csv', sep=',', header=0)
zoo_data = zoo_data.reindex(np.random.permutation(zoo_data.index))
filenames = get_filenames()

#go through each of the 14 filename lists and get images for all of the files in each one and save them in a file one at a time
#so the [0] will be loaded into mem and saved to a file, then [1] and so on so there's not too much in the RAM at once
for x in range(0,len(filenames)):
	for file in filenames[x]:
		file.extend(get_img_px(file[0]))

	np.save(('../data/imagelist%s' % x), filenames[x])
	print('Finished Group %i' % x)
	filenames[x] = 0

print('Done')