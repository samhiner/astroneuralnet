import numpy as np
import pandas as pd
from PIL import Image

#get a list of filenames split into 14 groups
def get_filenames():
	#get a list of all of the OBJIDs in the database
	raw_filenames = list(zoo_data.loc[:,'OBJID'])

	#split up list of OBJIDs into 34 sublists (each sublist is a list of what images should be loaded into the memory at a specific time)
	filenames = []
	for x in range(0,33):
		filenames.append(raw_filenames[20000 * x : 20000 * (x + 1)])
	filenames.append(raw_filenames[(20000 * 33):])

	return filenames

#convert an image to greyscale array of pixels
def get_img_px(file):
	im = Image.open('../data/images/' + str(file) + '.jpg').convert('LA')
	objArr = np.array(im.getdata())
	im.close()
	objArr = objArr[:,0] / 255
	return objArr

zoo_data = pd.read_csv('../data/zoodata.csv', sep=',', header=0)
zoo_data = zoo_data.reindex(np.random.permutation(zoo_data.index))
filenames = get_filenames()

#go through each of the 14 filename lists and get images for all of the files in each one and save them in a file one at a time
#so the [0] will be loaded into mem and saved to a file, then [1] and so on so there's not too much in the RAM at once
for x in range(0,len(filenames)):
	filelist = []
	for file in filenames[x]:
		form_file = [file]
		#TODO add labels (spiral, etc) to form_file. maybe in get_filenames function.
		form_file.extend(get_img_px(file))
		filelist.append(form_file)
	np.save(('../data/imagelist%s' % x), filelist)			
	print('Finished Group %i' % x)

print('Done')