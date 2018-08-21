import numpy as np
import urllib
from PIL import Image
import matplotlib.pyplot as plt

#for loop on array of filenames that is saved to a file to do this for every image
im = Image.open('star.jpg').convert('LA')
objArr = np.array(im.getdata())
objArr = objArr[:,0] / 255

#feed it to the network ig. will prob import this from the main network.

im.close()