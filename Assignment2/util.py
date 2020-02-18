import os
import string
import operator
from nltk.stem.wordnet import WordNetLemmatizer

# Lemmatizing the words present in the list containing text
def lemmatization(text_list):
	lem = WordNetLemmatizer()
	lemmatized_words = []
	for w in text_list:
		w = w.lower()
		word = lem.lemmatize(w)
		lemmatized_words.append(word)
	return lemmatized_words

# Read file from path and store the term frequency of each word present for each document
# Except for the folders FARNON and SRE and some hidden files
def readFromPath(path, not_to_read):
	document_dict = {}
	for foldername in os.listdir(path):
		if os.path.isdir(path+"/"+foldername):
		 	if foldername != "FARNON":
		 		complete_path = path+"/"+ foldername
		 		for filename in os.listdir(complete_path):
		 			word_counter = 0
		 			word_dict = {}
		 			if filename not in not_to_read:
		 				f = open(complete_path+"/"+filename, errors="ignore")
		 				for line in f:
		 					line_words = line.split()
		 					line_stripped = removePunctuation(line_words)
		 					line_list = lemmatization(line_stripped)
		 					for word in line_list:
		 						if word in word_dict.keys():
		 							word_counter = word_dict[word] + 1
		 						else:
		 							word_counter = 1
		 						word_dict[word] = word_counter
		 				document_dict[filename] = word_dict
		else:
			word_counter = 0
			word_dict = {}
			complete_path = path+"/"+ foldername
			if foldername not in not_to_read:
				f = open(complete_path, errors="ignore")
				for line in f:
					line_words = line.split()
					line_stripped = removePunctuation(line_words)
					line_list = lemmatization(line_stripped)
					for word in line_list:
						if word in word_dict.keys():
							word_counter = word_dict[word] + 1
						else:
							word_counter = 1
						word_dict[word] = word_counter
				document_dict[foldername] = word_dict
	print("Corpus collection done")
	return document_dict

# Store document length in a dictionary corresponding to each document.
def storeDocLength(path, not_to_read):
	doc_length_dict = {}
	for foldername in os.listdir(path):
		if os.path.isdir(path+"/"+foldername):
		 	if foldername != "FARNON":
		 		complete_path = path+"/"+ foldername
		 		for filename in os.listdir(complete_path):
		 			doc_length = 0
		 			if filename not in not_to_read:
		 				f = open(complete_path+"/"+filename, errors="ignore")
		 				for line in f:
		 					doc_length += len(line.split())
		 				doc_length_dict[filename] = doc_length
		else:
			doc_length = 0
			complete_path = path+"/"+ foldername
			if foldername not in not_to_read:
				f = open(complete_path, errors="ignore")
				for line in f:
					doc_length += len(line.split())
				doc_length_dict[foldername] = doc_length
	return doc_length_dict

# Parsing the input string
def parseInputString(input_string):
	wordList = input_string.split()					# Splitting the input string 
	wordList = removePunctuation(wordList)
	input_wordList = lemmatization(wordList)		# Lemmatizing the words
	input_string_length = len(input_wordList)		# Finding the length of input list
	return input_wordList,input_string_length

# Print top k documents on the basis of the sorted dictionary
def printTopK(dictionary, k):
	sorted_d = sorted(dictionary.items(), key=operator.itemgetter(1), reverse = True)
	k = 10
	i = 0
	while i < k:
		print(sorted_d[i])
		i = i + 1

# Find df corresponding to all the words in all the documents 
def findDfAllDocs(document_dict):
	df_dict = {}
	no_of_docs = 0
	for document in document_dict.keys():
		no_of_docs += 1
		df_counter = 0
		word_dict = document_dict[document]
		for word in word_dict.keys():
			if word in df_dict.keys():
				df_counter = df_dict[word] + 1
			else:
				df_counter = 1
			df_dict[word] = df_counter
	return df_dict, no_of_docs

# Removal of punctuations from the tokens list
def removePunctuation(tokens):
	table = str.maketrans('', '', string.punctuation)
	stripped = [w.translate(table) for w in tokens]
	return stripped
