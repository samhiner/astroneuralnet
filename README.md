## The Code:

All of the code is in the src directory. The data directory contains the raw data (not uploaded to GitHub because it is massive, but I will document how to download everything)

### datadownloading.py
This will download all of the images you need to train the neural network. You only need to run it once but based on some napkin calculation it looks like it takes 44 hours (testing that now). To run it, you need to download the CSV file [here](https://data.galaxyzoo.org/). Choose the CSV.zip under Table 2 (or .gz if you really want). Put the unzipped CSV file into the data folder (make sure the name of it is zoodata.csv) and run this code to download the images.

### dataformatting.py (not done)
Run this once you finish running datadownloading.py. This will convert all of the images into arrays of the brightness of their pixels and append this to a file so the neural network will just be able to read the giant array of all image arrays from that file. No extra setup needed if you just ran datadownloading.py and didn't mess with pixelsarray.txt. I didn't just integrate this with datadownloading.py because that takes so long that I don't want to increase risk of failure. NOTE: I haven't run it yet because I am still waiting on dataformatting to run as you need all of the images downloaded for this to be able to get their arrays.

### neuralnetworktrain.py (nonexistent so far)
The actual neural network. Run this to train the model. Actually this will be a Jupyter Notebook that replaces dataformatting.py and trains the neural network (Storing JPEGs as lists is very resource inefficient so reading JPEGs needs to be done in chunks which are then read to the neural network and another chunk is done) ik it will take forever for the code to run but I'm out of options. Not updating rest of README bc I'm  tired and this could all change tomorrow.

### neuralnetworkeval.ipynb (nonexistent so far)
Once you have trained the neural network, use this for more in-depth testing. (Maybe give option to save on main network and if you do then you can go here and test on any image and stuff) 
