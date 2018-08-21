import pandas as pd
import urllib

#converts time based sky position to degrees
def time_to_deg(time, ra = True):
	if time[0] == '-':
		time = time[1:]
		neg = True
	else:
		neg = False

	time = time.split(':')
	time = list(map(float, time))
	a = time
	#forumlas for right ascension vs declination
	if ra:
		degrees = (time[0] + (time[1] / 60) + (time[2] / 3600)) * 15
	else:
		degrees = time[0] + (time[1] / 60) + (time[2] / 3600)

	if neg:
		degrees = -degrees

	return degrees

#downloads image of sky at x position (ra, dec) and saves is as the objID
	#ra and dec are '00:00:00' (string). objid is 000000000000000000 (int64).
def download_image(ra, dec, objID):
	ra = time_to_deg(ra, True)
	dec = time_to_deg(dec, False)
	urllib.request.urlretrieve('http://skyservice.pha.jhu.edu/DR7/ImgCutout/getjpeg.aspx?ra=' + str(ra) + '&dec=' + str(dec) + '&scale=0.39612&opt=&width=128&height=128', '../data/images/' + str(objID) + '.jpg')	

#columns are [OBJID, RA, DEC, NVOTE, P_EL, P_CW, P_ACW, P_EDGE, P_DK, P_MG, P_CS, P_EL_DEBIASED, P_CS_DEBIASED, SPIRAL, ELLIPTICAL, UNCERTAIN]
zoo_data = pd.read_csv('../data/zoodata.csv', sep=',', header=0)

#get a picture of every object in the database and download it
for x in range(667944):
	image = zoo_data.loc[x]
	download_image(image[1], image[2], image[0])