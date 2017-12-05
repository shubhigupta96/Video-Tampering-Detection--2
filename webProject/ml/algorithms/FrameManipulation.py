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


def tamperVideo():
	extract()