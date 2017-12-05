# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm,mlForm,TamperingForm
from django.conf import settings
from django.core.files.base import ContentFile
import os
from algorithms.FrameManipulation import extract,tamperVideo
from algorithms.ModelTraining import getResults
def home(request):
	form=UploadFileForm(request.POST or None)
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			path = os.path.join(settings.MEDIA_ROOT,"test.mp4")
			print form.cleaned_data['like']

			lines = form.cleaned_data['file'].readlines()

			with open(path,'w') as destination:
				for line in lines:
					destination.write(line)
			request.session['category'] = form.cleaned_data['like']	
			return HttpResponseRedirect('tamper')
	else:
		form = UploadFileForm()
	return render(request, 'base.html', {'form': form})


def tamper(request):
	val = extract()
	form  = TamperingForm(request.POST or None,val)
	cat = request.session.get('category')
	context = {
		'form' : form,
		'count': val,
	}
	print val,cat
	if form.is_valid():
		stValue = form.cleaned_data['start']
		enValue = form.cleaned_data['end']
		if stValue==0 and enValue==0:
			if cat=='ml_approach' :
				return HttpResponseRedirect('mlApproach')
			else:
				return HttpResponseRedirect('watermarking')
		tamperVideo(stValue,enValue)
	return render(request,'tampering.html',context)




def mlApproach(request):
	form = mlForm(request.POST or None)	
	context = {
		'form' : form,
	}
	if form.is_valid():
		result = getResults(form.cleaned_data['algorithms'],form.cleaned_data['features'])	
		ans=''
		if result==1:
			ans = 'Video is Tampered'
		else:
			ans = 'Video is not Tampered'
		context = {
			'result' : ans,
		}
		return render(request,'finalPage.html',context)
	return render(request,'mlPage.html',context)


def watermarking(request):
	return render(request,'watermarking.html')
