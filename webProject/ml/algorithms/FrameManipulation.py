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


def getNumberofFrames():
	folderPath = os.path.join(settings.MEDIA_ROOT,'frames')
	return len(os.walk(folderPath).next()[2])
	

def tamperVideo(st,en):
	count = getNumberofFrames()
	
	folderPath = os.path.join(settings.MEDIA_ROOT,'frames')
	j=0
	i=0
	st-=1
	while i<st:
		imPath = os.path.join(folderPath,'frame%d.jpg'%i)
		img  = cv2.imread(imPath)
		imPath = os.path.join(folderPath,'frame%d.jpg'%j)
		j+=1		 	
		i+=1
	i=en
	while i<count:
		imPath = os.path.join(folderPath,'frame%d.jpg'%i)
		img  = cv2.imread(imPath)
		imPath = os.path.join(folderPath,'frame%d.jpg'%j)
		j+=1		 	
		i+=1
	ct = j
	while j<count:
		imPath = os.path.join(folderPath,'frame%d.jpg'%j)
		os.remove(imPath)
		j+=1
	return ct