from django import forms
# from algorithms.ExtractFrame import extract
class UploadFileForm(forms.Form):
	CHOICES=[('ml_approach','Machine Learning Approach'),('watermarking','Watermarking Approach')]
	like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
	file = forms.FileField()
    # title = forms.CharField(max_length=50)

class mlForm(forms.Form):
	algoChoices = [('knn','KNN'),('decisionTree','Decision Tree'),('logReg','Logistic Regression'),('naiveBayes','Naive Bayes'),('randomForest','Random Forest'),('svm','SVM'),('neuralNet','neuralNetwork')]
	featureChoices = [('mse','Mean Square Error'),('psnr','Peak Signal to Noise Ratio'),('hist_compare','Histogram Compare'),('ssim','Structural Similarity Index'),('entropy','Entropy'),('displacedObjects','Number of Objects Displaced'),('avgObjArea','Average Object Area')]
	features = forms.MultipleChoiceField(choices = featureChoices,widget=forms.CheckboxSelectMultiple())  
	algorithms = forms.ChoiceField(choices=algoChoices,widget=forms.RadioSelect())
	
class TamperingForm(forms.Form):

	def __init__(self, value=100000, *args, **kwargs):
		super(SomeForm, self).__init__(*args, **kwargs)
		self.fields['start'].max_value = value
		self.fields['end'].max_value = value
	start = forms.IntegerField(min_value=0,max_value=100000)
	end  = forms.IntegerField(min_value=0,max_value=100000)
	# def clean_recipients(self):
	# 	s = self.cleaned_data['start']
	# 	e = self.cleaned_data['end']
	# 	if (e<s) or (s==0 and e>0):
	# 		raise forms.ValidationError("Incorrect Range!")