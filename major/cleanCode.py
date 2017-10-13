from subprocess import check_output
import re 
import os
import csv
#https://stackoverflow.com/questions/20056548/printing-double-quotes-around-a-variable
#https://stackoverflow.com/questions/5900419/c-macro-expander
class cleanCode:
	def CppCode(self,filename):
		self.filename = filename
		self.match  = '# 15 '+'"%s"'%self.filename + '\n'
		os.system("cpp "+ self.filename +" > output.txt")
		code = open("output.txt").readlines()
		toPrint = False
		formattedCode = ""
		for line in code:
			if toPrint == True :
				if str(line) != "\n" and str(line) !=self.match and str(line) != "using namespace std;\n":
					formattedCode = formattedCode +line
			if str(line) == self.match:
				toPrint = True
		return formattedCode.replace("\n"," ") 


clean = cleanCode()
cleanCode = clean.CppCode('template.cpp')

with open('data.csv', 'a') as csvfile:
	fieldnames = ['code','binary_search','sorting']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writerow({'code':cleanCode,'binary_search':True,'sorting':False})