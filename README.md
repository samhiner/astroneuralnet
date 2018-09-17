## The Code:

All of the code is in the src directory. The data directory contains the raw data (not uploaded to GitHub because it is massive, but I will document how to download everything)

### datadownloading.py
This will download all of the images you need to train the neural network. You only need to run it once but based on some napkin calculation it looks like it takes 44 hours (testing that now). To run it, you need to download the CSV file [here](https://data.galaxyzoo.org/). Choose the CSV.zip under Table 2 (or .gz if you really want). Put the unzipped CSV file into the data folder (make sure the name of it is zoodata.csv) and run this code to download the images.

### dataformatting.py
Turns the images into 34 files which are lists of lists of the characteristics of a galaxy. So each nested list has the labels (what type it is) and features (pixels) of a galaxy. Split the list into 34 files because is takes about 13 GB of RAM to load 20,000 image lists (number of lists in each file) and I have 16 GB of RAM. If you are trying to run this on your computer, and you have a different amount of RAM, you can easily change how many files the script makes by editing the NUM_FILES variable at the top of the script.

### neuralnetwork.ipynb / neuralnetwork.py (not done)
These two files are the same code, but are just different representations depending on where it is needed. This may change in the future- the Notebook may offer more testing functionality for example, but that is not the case as of yet.
This is the actual neural network which trains on the 34 files. You can also run it against test data and save it here.
NOTE: If you edited the NUM_FILES constant in dataformatting, you will have to change the three constants, NUM_TRAINING_FILES, VALIDATION_SET, and TEST_SET here. The first one is you training set, the second one is the range for your validation set (range is start file to end file + 1) and the third one is the range for your test set.

### neuralnetworkeval.ipynb (nonexistent so far)
Once you have trained the neural network, use this for more in-depth testing. (Maybe give option to save on main network and if you do then you can go here and test on any image and stuff) 
