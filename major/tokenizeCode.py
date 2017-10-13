import scipy 
import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
# print dir(scipy)
# import sklearn

trainCode = []
binary_class = []
sorting_class = []

with open("data.csv") as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		trainCode.append(str(row['code']))
		binary_class.append(row['binary_search'])
		sorting_class.append(row['sorting'])

# train_set = ("The sky is blue.", "The sun is bright.")
count_vectorizer = CountVectorizer()
count_vectorizer.fit_transform(trainCode)
count = count_vectorizer.transform(trainCode)

# print count.todense()


tfidf = TfidfTransformer(norm="l2")
tfidf.fit(count)

# print "IDF:", tfidf.idf_

tf_idf_matrix = tfidf.transform(count)
print tf_idf_matrix.todense()