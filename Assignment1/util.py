import os
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

def readFromPath(path):
	collection = []
	filename_list = []
	for foldername in os.listdir(path):
	    complete_path = path+"/"+ foldername
	    for filename in os.listdir(complete_path):
	        f = open(complete_path+"/"+filename, "r")
	        data = f.read()
	        collection.append((filename,data))
	        filename_list.append(int(filename))
	print("Corpus collection done")
	return collection, filename_list

def removePunctuation(tokens):
	table = str.maketrans('', '', string.punctuation)
	stripped = [w.translate(table) for w in tokens]
	return stripped


def stemming(text_list):
	ps = PorterStemmer()
	stemmed_words = []
	for w in text_list:
		stemmed_words.append(ps.stem(w))
	return stemmed_words

def lemmatization(text_list):
	lem = WordNetLemmatizer()
	lemmatized_words = []
	for w in text_list:
		w = w.lower()
		word = lem.lemmatize(w)
		lemmatized_words.append(word)
	return lemmatized_words

def removeStopwords(text_list):
	stop_words=set(stopwords.words("english"))
	filtered_text = []
	for w in text_list:
		if w not in stop_words:
			filtered_text.append(w)
	return filtered_text

def lemmatizationWithoutLower(text_list):
	lem = WordNetLemmatizer()
	lemmatized_words = []
	for w in text_list:
		word = lem.lemmatize(w)
		lemmatized_words.append(word)
	return lemmatized_words
