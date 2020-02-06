import util
import nltk
import os
from nltk.tokenize import word_tokenize

''' 
Defining a method to calculate intersection of positional indexes
p1, p2 are internal dictionaries of respective words
'''
def positionalIndex(p1,p2,k):
	ptr1 = 0
	ptr2 = 0
	final_answer_list = []
	for key1 in p1.keys():
		if key1 in p2.keys():
			result_list = []
			list_position1 = p1[key1]
			list_position2 = p2[key1]
			ptr1 = 0
			ptr2 = 0
			while ptr1 < len(list_position1):
				while ptr2 < len(list_position2):
					if abs(list_position1[ptr1] - list_position2[ptr2]) <= k:
						result_list.append(list_position2[ptr2])
					elif list_position2[ptr2] > list_position1[ptr1]:
						break
					ptr2 = ptr2 + 1
				while len(result_list) != 0 and abs(result_list[0] - list_position1[ptr1]) > k:
					result_list.remove(result_list[0])
				for i in result_list:
					lst = [key1, list_position1[ptr1], i]
					final_answer_list.append(lst)
				ptr1 = ptr1 + 1
	return final_answer_list

def make_dict(answer_list, starting_index):
	ptr1 = 0
	dict_intermediate = {}
	while ptr1 < len(answer_list):
		inner_List = answer_list[ptr1]
		ptr2 = starting_index
		new_list = []
		while ptr2 < len(inner_List):
			new_list.append(inner_List[ptr2])
			ptr2 = ptr2 + 2
		dict_intermediate[answer_list[ptr1][0]] = new_list
		ptr1 = ptr1 + 1
	return dict_intermediate


path = os.getcwd() + '\\Q2'
dict_tokens = {}

collection, filename_list = util.readFromPath(path)

for tupleVal in collection:

	# Tokenization - word_tokenize
	tokens = nltk.word_tokenize(tupleVal[1])
	
	# Punctuation Removal
	stripped = util.removePunctuation(tokens)

	# Lemmatization
	lemmatized_words = util.lemmatization(stripped)

	# Creating of positional index
	# Positional index structure - {word, (frequency, {docId, positionList})}
	num_count = 0
	w = 0
	while w < len(lemmatized_words):
		if lemmatized_words[w] in dict_tokens.keys():
			tupleValue = dict_tokens[lemmatized_words[w]]
			count = tupleValue[0] + 1
			dict_positions = tupleValue[1]
			if tupleVal[0] in dict_positions.keys():
				list_position = dict_positions[tupleVal[0]]
				list_position.append(int(w))
				dict_positions[tupleVal[0]] = list_position
			else:
				list_position = []
				list_position.append(int(w))
				dict_positions[tupleVal[0]] = list_position
			dict_tokens[lemmatized_words[w]] = (count, dict_positions)
		else:
			list_position = []
			list_position.append(int(w))
			dict_positions = {}
			dict_positions[tupleVal[0]] = list_position
			dict_tokens[lemmatized_words[w]] = (1, dict_positions)
		w += 1

# Removing empty key from the dictionary
if '' in dict_tokens.keys():
	del dict_tokens['']

# User input string
#string = "very good"
string = "very good point"
#string = "space technology"

# Split input string
string_list = string.split()

# Lemmatizing the input string
lem_string = util.lemmatization(string_list)

list1 = positionalIndex(dict_tokens[lem_string[0]][1], dict_tokens[lem_string[1]][1], 1)

answer_dict = make_dict(list1, 1)

# Checking the lists for the matching of exact phrase query
x = 0
while x < len(lem_string) - 1:
	dict_intermediate = make_dict(list1, 2)
	delete = []
	for key in answer_dict:
		if key in dict_intermediate.keys():
			lst = answer_dict[key]
			pos_list = dict_intermediate[key]
			for i in pos_list:
				lst.append(i)
			answer_dict[key] = lst
		else:
			delete.append(key)
	for key in delete:
		del answer_dict[key]
	if len(answer_dict) == 0:
		break
	if (x+2) <= len(lem_string) - 1:
		list1 = positionalIndex(dict_intermediate, dict_tokens[lem_string[x+2]][1], 1)
	x = x + 1

print("Total number of documents retrieved:",len(answer_dict))
print("The list of documents retrieved :",answer_dict)
