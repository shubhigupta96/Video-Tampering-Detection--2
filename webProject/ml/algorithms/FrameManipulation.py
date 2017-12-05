import cv2
import sys
import os
import csv
from django.conf import settings
import shutil

def extract():
	videoPath = os.path.join(settings.MEDIA_ROOT,"test.mp4")		
	vidcap = cv2.VideoCapture(videoPath)
	folderPath = os.path.join(settings.MEDIA_ROOT,'frames')
	if os.path.exists(folderPath):
		shutil.rmtree(folderPath)
	os.mkdir(folderPath)
	count=0
	while True:
		success,image = vidcap.read()
		if success == False:
			break;
		imPath = os.path.join(folderPath,'frame%d.jpg'%count)
		cv2.imwrite(imPath, image) 
		count+=1
	return count


def tamperVideo(st,en):
	count = extract()
	videoPath = os.path.join(settings.MEDIA_ROOT,"test.mp4")		
	if os.path.exists(videoPath):
		os.remove(videoPath)
	folderPath = os.path.join(settings.MEDIA_ROOT,'frames')

	imPath = os.path.join(folderPath,'frame0.jpg')
	print imPath
	img = cv2.imread(imPath)	
	print img
	height , width , layers =  img.shape

	video = cv2.VideoWriter('video.mp4',-1,1,(width,height))
	i=0
	st-=1
	while i<st:
		imPath = os.path.join(folderPath,'frame%d.jpg'%count)
		video.write(cv2.imread(imPath)) 	
		i+=1
	i=en
	while i<count:
		imPath = os.path.join(folderPath,'frame%d.jpg'%count)
		video.write(cv2.imread(imPath)) 	
		i+=1
	
	cv2.destroyAllWindows()
	video.release()
