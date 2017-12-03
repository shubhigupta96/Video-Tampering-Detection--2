import cv2
from skimage.measure import compare_mse, compare_nrmse, compare_ssim, compare_psnr
import csv
import os
from random import randint
import math
"""
In Code References
https://stackoverflow.com/questions/45945258/compare-frame-of-video-with-another-image-python
http://scikit-image.org/docs/stable/api/skimage.measure.html
https://docs.opencv.org/3.2.0/d8/dc8/tutorial_histogram_comparison.html
"""
count = len(os.walk('frames').next()[2])


def getFeatures(im1,im2,isTampered):
	img1 = cv2.imread(im1)
	img2 = cv2.imread(im2)
	# MSE
	mse =  compare_mse(img1,img2)
	
	# PSNR
	psnr = 10.0*math.log10((255*255)/(mse*1.0));
	
	#Histogram Bhattacharya Distance
	
	hist1 = cv2.calcHist([img1],[0],None,[256],[0,256])
	hist2 = cv2.calcHist([img2],[0],None,[256],[0,256])
	histogram_compare = cv2.compareHist(hist1,hist2,3)


	features = {'mse':mse,'psnr':psnr,'histogram_compare':histogram_compare,'class':isTampered}
	return features


with open('data.csv', 'a') as csvfile:
	fieldnames = ['mse','psnr','histogram_compare','class']	
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	# writer.writeheader()
	
#	Non Tampered Frames
	i=0
	while i<count-1:
		im1 = 'frames/frame%d.jpg' %i
		im2 = 'frames/frame%d.jpg' %(i+1) 
		features = getFeatures(im1,im2,0)
		# print features
		writer.writerow(features)
		i+=1

#   Tampered Frames
	i=0
	while i<count-5:
		j = randint(i+2,count-1)
		im1 = 'frames/frame%d.jpg' %i
		im2 = 'frames/frame%d.jpg' %j 
		features = getFeatures(im1,im2,1)
		# print features
		writer.writerow(features)
		i+=1


