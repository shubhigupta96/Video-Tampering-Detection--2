import cv2
from skimage.measure import compare_mse, compare_nrmse, compare_ssim, compare_psnr
from PIL import Image
import sys
import csv
# https://stackoverflow.com/questions/45945258/compare-frame-of-video-with-another-image-python
# http://scikit-image.org/docs/stable/api/skimage.measure.html
# img1 = cv2.imread('img1.jpg')
# img2 = cv2.imread('img2.jpg')

# print compare_mse(img1, img2)

vidcap = cv2.VideoCapture('test.mp4')
count=0
while True:
	success,image = vidcap.read()
	if success == False:
		break;
	cv2.imwrite("frames/frame%d.jpg" % count, image) 
	count+=1

print "Part One Completed"
count = 3081
i=0
# while i<50:
# 	img1 = cv2.imread('frames/frame%d.jpg' %i)
# 	img2 = cv2.imread('frames/frame%d.jpg' %(i+1) )
# 	mse.append(compare_mse(img1,img2))
# 	i+=1

# i = 60

with open('data.csv', 'a') as csvfile:
	fieldnames = ['mse','histogram_mse','class']	
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	
#	Non Tampered Video

	i=0
	while i<count-1:
		featureVector = []
		img1 = cv2.imread('frames/frame%d.jpg' %i)
		img2 = cv2.imread('frames/frame%d.jpg' %(i+1) )
		

		mse =  compare_mse(img1,img2)
		#histogram
		histogram_mse = ....
		isTampered = 0
		writer.writerow(['mse':mse,'hisogram_mse':hisogram_mse,'class':isTampered])
		i+=1