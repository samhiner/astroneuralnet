## The Code:

All of the code is in the src directory. The data directory contains the raw data (not uploaded to GitHub because it is massive, but I will document how to download everything)

### datadownloading.py
This will download all of the images you need to train the neural network. You only need to run it once but based on some napkin calculation it looks like it takes 5 days (!) (about to test that). To run it, you need to download the CSV file [here](https://data.galaxyzoo.org/). Choose the CSV.zip under Table 2 (or .gz if you really want). Put the unzipped CSV file into the data folder and run this code to download the images.

### dataformatting.py (not done)
Will format the images into arrays once its done (if I don't decide to integrate this with the main neural network). Maybe it will do some other formatting tasks as well. You don't need to run this; it is imported by the neural network.

### neuralnetworktrain.py (nonexistent so far)
The actual neural network. Run this to train the model.

### neuralnetworkeval.py (nonexistent so far)
Once you have trained the neural network, use this for more in-depth testing. (Maybe give option to save on main network and if you do then you can go here and test on any image and stuff)