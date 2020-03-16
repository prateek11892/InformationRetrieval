import os
import string
import operator
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

def createDocumentMapping(path):
	print("Entering createDocumentMapping")
	mapping_dict = {}
	count = 1
	for foldername in os.listdir(path):
		if os.path.isdir(path+"/"+foldername):
			complete_path = path+"/"+ foldername
			for filename in os.listdir(complete_path):
				mapping_dict[foldername+'-'+filename] = count
				count += 1
	print("Exiting createDocumentMapping")
	return mapping_dict

def convertTupToDict(tuple_list):
	dictionary = dict(tuple_list)
	return dictionary

def createSortedGdHighLowList(highLowList, sort_order, input_wordList):
	print("Entering createSortedGdHighLowList")
	for key in input_wordList:
		print("KEY:",key)
		highLowDict = highLowList[key]
		for internal_key in highLowDict.keys():		# internal_key can be High or Low
			print("INTERNAL_KEY:",internal_key)
			posting_list = highLowDict[internal_key]
			if len(posting_list) > 1:
				res = [tuple for x in sort_order for tuple in posting_list if tuple[0] == x[0]]
				posting_list = res
			highLowDict[internal_key] = posting_list
		highLowList[key] = highLowDict
	print("Exiting createSortedGdHighLowList")
	return highLowList

def readReviewFile(path):
	print("Entering readReviewFile")
	f = open(path, errors="ignore")
	review_list = []
	maxValue = 0
	for line in f:
		docIdReview = line.split()
		if maxValue < int(docIdReview[1]):
			maxValue = int(docIdReview[1])

	f = open(path, errors="ignore")
	for line in f:
		docIdReview = line.split()
		tup = (int(docIdReview[0]), (int(docIdReview[1])/maxValue))
		review_list.append(tup)

	review_list = Sort_Tuple(review_list)
	print("Exiting readReviewFile")
	return review_list

def readFromPath(path, mapping_dict, doc_length_dict):
	print("Entering readFromPath")
	document_dict = {}
	for foldername in os.listdir(path):
		if os.path.isdir(path+"/"+foldername):
			complete_path = path+"/"+ foldername
			for filename in os.listdir(complete_path):
		 		word_counter = 0
		 		word_dict = {}
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
		 				word_dict[word] = word_counter/(doc_length_dict[mapping_dict[foldername+'-'+filename]])
		 		document_dict[mapping_dict[foldername+'-'+filename]] = word_dict
	print("Corpus collection done")
	print("Exiting readFromPath")
	return document_dict


def createGlobalChampionList(document_dict):
	print("Entering createGlobalChampionList")
	globalChampionList = {}
	for key in document_dict.keys():
		word_dict = document_dict[key]
		for word_key in word_dict.keys():
			if word_key in globalChampionList.keys():
				posting_list = globalChampionList[word_key]
				doc_freq_tuple = (key, word_dict[word_key])
				posting_list.append(doc_freq_tuple)
				globalChampionList[word_key] = posting_list
			else:
				globalChampionList[word_key] = [(key,word_dict[word_key])]
	print("Exiting createGlobalChampionList")
	return globalChampionList

def sortGlobalChampionListTf(globalChampionList):
	print("Entering sortGlobalChampionListTf")
	for key in globalChampionList.keys():
		tup = globalChampionList[key]
		sortedTuple = Sort_Tuple(tup)
		globalChampionList[key] = sortedTuple
	print("Exiting sortGlobalChampionListTf")
	return globalChampionList

def Sort_Tuple(tup):  
	tup.sort(key = lambda x: x[1], reverse=True)
	return tup  

def createHighLowList(sortedGlobalChampionListTf,r):
	globalListHighLow = {}
	for key in sortedGlobalChampionListTf.keys():
		highLowdict = {}
		postingList = sortedGlobalChampionListTf[key]
		highLowdict['High'] = postingList[0:r]
		highLowdict['Low'] = postingList[r:]
		globalListHighLow[key] = highLowdict
	return globalListHighLow

# Lemmatizing the words present in the list containing text
def lemmatization(text_list):
	lem = WordNetLemmatizer()
	lemmatized_words = []
	for w in text_list:
		w = w.lower()
		word = lem.lemmatize(w)
		lemmatized_words.append(word)
	return lemmatized_words

# Removal of punctuations from the tokens list
def removePunctuation(tokens):
	table = str.maketrans('', '', string.punctuation)
	stripped = [w.translate(table) for w in tokens]
	return stripped

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

# Store document length in a dictionary corresponding to each document.
def storeDocLength(path, mapping_dict):
	doc_length_dict = {}
	for foldername in os.listdir(path):
		if os.path.isdir(path+"/"+foldername):
		 	complete_path = path+"/"+ foldername
		 	for filename in os.listdir(complete_path):
		 		doc_length = 0
		 		f = open(complete_path+"/"+filename, errors="ignore")
		 		for line in f:
		 			doc_length += len(line.split())
		 		doc_length_dict[mapping_dict[foldername+'-'+filename]] = doc_length
	return doc_length_dict

# Parsing the input string
def parseInputString(input_string):
	wordList = input_string.split()					# Splitting the input string 
	wordList = removePunctuation(wordList)
	input_wordList = lemmatization(wordList)		# Lemmatizing the words
	print("In lemmatization:::",input_wordList)
	input_string_length = len(input_wordList)		# Finding the length of input list
	return input_wordList,input_string_length

def getKeysByValue(dictOfElements, valueToFind):
	key = -1
	listOfItems = dictOfElements.items()
	#print(listOfItems)
	for item in dictOfElements.keys():
		if dictOfElements[item] == valueToFind:
			key = item
			break
	return key

def printTopK(dictionary, k, mapping_dict):
	sorted_d = sorted(dictionary.items(), key=operator.itemgetter(1), reverse = True)
	i = 0
	while i < k:
		key = getKeysByValue(mapping_dict, sorted_d[i][0])
		#print(str(sorted_d[i][0])+","+str(key))
		#print(sorted_d[i])
		print(key)
		i = i + 1
#print(lemmatization(['virtual','reality']))
