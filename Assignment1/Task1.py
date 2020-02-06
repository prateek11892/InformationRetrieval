import nltk
import util
import os
from nltk.tokenize import word_tokenize 

## For Query AND ##
def AND(postingList1, postingList2):
	pl1 = 0
	pl2 = 0
	result_List = []
	comparison_counter = 0
	while pl1 < len(postingList1) and pl2 < len(postingList2):
		comparison_counter += 1
		if postingList1[pl1] == postingList2[pl2]:
			result_List.append(postingList1[pl1])
			pl1 = pl1 + 1
			pl2 = pl2 + 1
		else:
			if postingList1[pl1] > postingList2[pl2]:
				pl2 = pl2 + 1
			else:
				pl1 = pl1 + 1
	return result_List, comparison_counter

## For Query OR ##
def OR(postingList1, postingList2):
	pl1 = 0
	pl2 = 0
	result_List = []
	comparison_counter = 0
	while pl1 < len(postingList1) and pl2 < len(postingList2):
		comparison_counter += 1
		if postingList1[pl1] == postingList2[pl2]:
			result_List.append(postingList1[pl1])
			pl1 = pl1 + 1
			pl2 = pl2 + 1
		else:
			if postingList1[pl1] > postingList2[pl2]:
				result_List.append(postingList2[pl2])
				pl2 = pl2 + 1
			else:
				result_List.append(postingList1[pl1])
				pl1 = pl1 + 1
	while pl1 < len(postingList1):
		result_List.append(postingList1[pl1])
		pl1 = pl1 + 1
	while pl2 < len(postingList2):
		result_List.append(postingList2[pl2])
		pl2 = pl2 + 1
	
	return result_List, comparison_counter

## For Query NOT ##
def NOT(postingList, filename_list):
	result_list = [x for x in filename_list if x not in postingList]
	return result_list

## For Query AND NOT ##
def ANDNOT(postingList1, postingList2):
	pl1 = 0
	pl2 = 0
	result_List = []
	comparison_counter = 0
	while pl1 < len(postingList1) and pl2 < len(postingList2):
		comparison_counter += 1
		if postingList1[pl1] > postingList2[pl2]:
			pl2 = pl2 + 1
		elif postingList1[pl1] == postingList2[pl2]:
			pl1 = pl1 + 1
			pl2 = pl2 + 1
		else:
			result_List.append(postingList1[pl1])
			pl1 = pl1 + 1
	return result_List,comparison_counter

## For Query OR NOT ##
def ORNOT(postingList1, postingList2, filename_list):
	postingList2 = NOT(postingList2, filename_list)
	result_List = OR(postingList1, postingList2)
	comparison_counter = result_list[1]
	return result_List[0],comparison_counter

##	##	##	##
path = os.getcwd() + '\\20_newsgroups'

dict_tokens = {}

collection, filename_list = util.readFromPath(path)

for tupleVal in collection:

	filename = tupleVal[0]
	text = tupleVal[1]

	# Tokenization - word_tokenize
	tokens = nltk.word_tokenize(text)

	# Punctuation Removal
	stripped = util.removePunctuation(tokens)

	# Lemmatization
	lemmatized_words = util.lemmatization(stripped)

	# Stopword removal
	filtered_text = util.removeStopwords(lemmatized_words)

	# Removing duplicate words from the text
	unique_words = list(set(filtered_text))

	# Creating inverted index 
	# Structure - {word, (frequency, postingList)}

	for w in unique_words:
		if w in dict_tokens.keys():
			frequency,postingList = dict_tokens[w]
			count = frequency + 1
			postingList.append(int(filename))
			dict_tokens[w] = (count, postingList)
		else:
			postingList = []
			postingList.append(int(filename))
			dict_tokens[w] = (1,postingList)

# Sorting the posting List corresponding to each word(key)
for key in dict_tokens.keys():
	postingTuple = dict_tokens[key]
	postingTuple[1].sort()
	dict_tokens[key] = (postingTuple[0], postingTuple[1])

print("Tokenization Done")
print("Punctuation Removal Done")
print("Lemmatization Done")
print("Stopword Removal Done")
print("Duplicate word Removal Done")
print("Inverted index created")
'''
Assuming AND NOT > OR NOT > AND > OR
Assuming no stopwords would be entered in the input string
'''
string = "bible AND believer AND atheism"
#string = "science AND technology OR good"
#string = "science AND technology AND bad"
#string = "science AND technology AND good"
#string = "science AND technology OR address AND NOT music"
#string  = "good AND point"

# Splitting the input string
splitted_string = string.split()

# Lemmatization of input string
list_string = util.lemmatizationWithoutLower(splitted_string)

andnot_removed_list = []
ptr = 0
total_comparison_counter = 0
while ptr < len(list_string):
	if list_string[ptr] == 'AND':
		if list_string[ptr+1] == 'NOT':
			if (dict_tokens[list_string[ptr - 1]])[1] in andnot_removed_list:
				andnot_query_output_list = ANDNOT((dict_tokens[list_string[ptr - 1]])[1], (dict_tokens[list_string[ptr + 2]])[1])
				andnot_removed_list.remove((dict_tokens[list_string[ptr - 1]])[1])
				andnot_removed_list.append(andnot_query_output_list[0])			
				total_comparison_counter += andnot_query_output_list[1]
				ptr = ptr + 3
			else:
				andnot_query_output_list = ANDNOT(andnot_removed_list[len(andnot_removed_list) - 1], (dict_tokens[list_string[ptr + 2]])[1])
				andnot_removed_list.remove(andnot_removed_list[len(andnot_removed_list) - 1])
				andnot_removed_list.append(andnot_query_output_list[0])			
				total_comparison_counter += andnot_query_output_list[1]
				ptr = ptr + 3
		else:
			andnot_removed_list.append("AND")
			ptr = ptr + 1
	elif list_string[ptr] == 'OR':
		andnot_removed_list.append("OR")
		ptr = ptr + 1
	elif list_string[ptr] == 'NOT':
		andnot_removed_list.append("NOT")
		ptr = ptr + 1
	else:
		andnot_removed_list.append((dict_tokens[list_string[ptr]])[1])
		ptr = ptr + 1

ornot_removed_list = []
ptr = 0
while ptr < len(andnot_removed_list):
	if andnot_removed_list[ptr] == 'OR':
		if andnot_removed_list[ptr+1] == 'NOT':
			if andnot_removed_list[ptr - 1] in ornot_removed_list:
				ornot_query_output_list = ORNOT(andnot_removed_list[ptr - 1],andnot_removed_list[ptr + 2], filename_list)
				ornot_removed_list.remove(andnot_removed_list[ptr - 1])
				ornot_removed_list.append(ornot_query_output_list[0])
				total_comparison_counter += ornot_query_output_list[1]
				ptr = ptr + 3
			else:	
				ornot_query_output_list = ORNOT(ornot_removed_list[len(ornot_removed_list) - 1],andnot_removed_list[ptr + 2], filename_list)
				ornot_removed_list.remove(ornot_removed_list[len(ornot_removed_list) - 1])
				ornot_removed_list.append(ornot_query_output_list[0])
				total_comparison_counter += ornot_query_output_list[1]
				ptr = ptr + 3
		else:
			ornot_removed_list.append("OR")
			ptr = ptr + 1
	elif list_string[ptr] == 'AND':
		ornot_removed_list.append("AND")
		ptr = ptr + 1
	else:
		ornot_removed_list.append(andnot_removed_list[ptr])
		ptr = ptr + 1

and_removed_list = []
ptr = 0
while ptr < len(ornot_removed_list):
	if ornot_removed_list[ptr] == 'AND':
		if ornot_removed_list[ptr - 1] in and_removed_list:
			and_query_output_list = AND(ornot_removed_list[ptr - 1], ornot_removed_list[ptr + 1])
			and_removed_list.remove(ornot_removed_list[ptr - 1])
			and_removed_list.append(and_query_output_list[0])
			total_comparison_counter += and_query_output_list[1]
			ptr = ptr + 2
		else:
			and_query_output_list = AND(and_removed_list[len(and_removed_list) - 1], ornot_removed_list[ptr + 1])
			and_removed_list.remove(and_removed_list[len(and_removed_list) - 1])
			and_removed_list.append(and_query_output_list[0])
			total_comparison_counter += and_query_output_list[1]
			ptr = ptr + 2
	elif list_string[ptr] == 'OR':
		and_removed_list.append("OR")
		ptr = ptr + 1
	else:
		and_removed_list.append(ornot_removed_list[ptr])
		ptr = ptr + 1

or_removed_list = []
ptr = 0
while ptr < len(and_removed_list):
	if and_removed_list[ptr] == 'OR':
		if and_removed_list[ptr - 1] in or_removed_list:
			or_query_output_list = OR(and_removed_list[ptr - 1], and_removed_list[ptr + 1])
			or_removed_list.remove(and_removed_list[ptr - 1])
			or_removed_list.append(or_query_output_list[0])
			total_comparison_counter += or_query_output_list[1]
			ptr = ptr + 2
		else:
			or_query_output_list = OR(or_removed_list[len(or_removed_list) - 1], and_removed_list[ptr + 1])
			or_removed_list.remove(or_removed_list[len(or_removed_list) - 1])
			or_removed_list.append(or_query_output_list[0])
			total_comparison_counter += or_query_output_list[1]
			ptr = ptr + 2
	else:
		or_removed_list.append(and_removed_list[ptr])
		ptr = ptr + 1

print("The number of docs retrieved:", len(or_removed_list[0]))
print("Total number of comparisons:",total_comparison_counter)
print("The list of documents retrieved :", or_removed_list[0])
