import os
import util
import operator

not_to_read = [".descs",".header",".musings","index.html"]
def readFromPath(path):
	collection = []
	filename_list = []
	for foldername in os.listdir(path):
		if os.path.isdir(path+"/"+foldername):
		 	if foldername != "FARNON":
		 		complete_path = path+"/"+ foldername
		 		for filename in os.listdir(complete_path):
		 			word_set = set()
		 			if filename not in not_to_read:
		 				f = open(complete_path+"/"+filename, errors="ignore")
		 				for line in f:
		 					line_words = line.split()
		 					line_stripped = util.removePunctuation(line_words)
		 					line_list = util.lemmatization(line_stripped)
		 					for word in line_list:
		 						word_set.add(word)
		 				collection.append((filename,word_set))
		else:
			word_set = set()
			complete_path = path+"/"+ foldername
			#print("complete_path:",complete_path)
			if foldername not in not_to_read:
				f = open(complete_path, errors="ignore")
				for line in f:
					line_words = line.split()
					line_stripped = util.removePunctuation(line_words)
					line_list = util.lemmatization(line_stripped)
					for word in line_list:
						word_set.add(word)
				collection.append((foldername,word_set))
	print("Corpus collection done")
	return collection

path = 'C:/Users/PrateekAgarwal/Desktop/Second Semester/Information Retrieval/Assignment 2/stories/stories'
#path = 'C:/Users/PrateekAgarwal/Desktop/Second Semester/Information Retrieval/Assignment 2/test'
collection = readFromPath(path)

input_string = "command was not helping either"
#input_string = "that our college doors"
#input_string = "population of 100 billion"
input_wordList, input_string_length = util.parseInputString(input_string)

jaccard_dict = {}

for tup in collection:
	matched_counter = 0
	for input_word in input_wordList:
		filename = tup[0]
		word_set = tup[1]
		word_set_length = len(word_set)
		if input_word in word_set:
			matched_counter = matched_counter + 1
	intersection = matched_counter
	union = (word_set_length + input_string_length - matched_counter)
	'''print("Filename:",filename)
	print("intersection:",intersection)
	print("union:",union)'''
	jaccard_dict[filename] = (intersection/union)

util.printTopK(jaccard_dict,k=10)