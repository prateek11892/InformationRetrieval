import math
import readHTML
import util
import operator

not_to_read = [".descs",".header",".musings","index.html"]

# Calculate the weighted tf idf score
def weightedTfIdfScore(path, query_word_list, tf_idf_score, a):
	file_title_dict = readHTML.findFileTitleDict(path)
	for document in file_title_dict.keys():
		title = file_title_dict[document]
		title_list = title.split()
		title_stripped = util.removePunctuation(title_list)
		title_list = util.lemmatization(title_stripped)
		weightedScore = tf_idf_score[document]
		for word in query_word_list:
			if word in title_list:
				weightedScore += (tf_idf_score[document] * a)
		tf_idf_score[document] = weightedScore
	return tf_idf_score

# Find df corresponding to each word in the input query list
def findDfInputQuery(input_wordList, document_dict):
	df_dict = {}
	no_of_docs = 0
	for word in input_wordList:
		df_counter = 0
		no_of_docs = 0
		for document in document_dict.keys():
			no_of_docs += 1
			#print(document)
			word_dict = document_dict[document]
			if word in word_dict.keys():
				df_counter = df_counter + 1
		df_dict[word] = df_counter
	return df_dict, no_of_docs

# Finding tf-idf score on basis of formula (tf/doc_length)*(1+log(Total_docs/df))
def findUnweightedTfIdfScore(document_dict, doc_length_dict, input_wordList, df_dict):
	tf_idf_score = {}
	for document in document_dict.keys():
		total_score = 0
		N = doc_length_dict[document]
		word_dict = document_dict[document]
		for term in input_wordList:
			if term in word_dict.keys():
				tf = word_dict[term]
			else:
				tf = 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
			df = df_dict[term]
			normalizedTf = tf/N
			idf = 1 + math.log((no_of_docs/df),10)
			total_score += normalizedTf * idf
		tf_idf_score[document] = total_score
	return tf_idf_score

# Find log normalized tf 
def findLogNormalizationTf(document_dict):
	for document in document_dict.keys():
		total_score = 0
		word_dict = document_dict[document]
		for term in word_dict.keys():
			tf = word_dict[term]
			logNormalizedTf = 1 + math.log((tf), 10)                                                                                                                                                                                                                                                                                                                                                                                                                                                             
			word_dict[term] = logNormalizedTf
		document_dict[document] = word_dict
	return document_dict

# Find double normalized K tf
def doubleNormalizationKTf(document_dict, K=0.5):
	for document in document_dict.keys():
		total_score = 0
		word_dict = document_dict[document]
		keymax = max(word_dict.items(), key=operator.itemgetter(1))[1]
		for term in word_dict.keys():
			tf = word_dict[term]
			doubleNormalizedTf = K + (1 - K)*(tf/keymax)
			word_dict[term] = doubleNormalizedTf
		document_dict[document] = word_dict
	return document_dict

# Find inverse document frequency smooth
def findIdfSmooth(df_dict, no_of_docs):
	idf_dict = {}
	for word in df_dict.keys():
		word_freq = df_dict[word]
		normalizedIdf = math.log((no_of_docs/(1 + word_freq)),10)
		idf_dict[word] = normalizedIdf
	return idf_dict

# Find max df from the df_dict
def findIdfMax(df_dict, max_df):
	idf_dict = {}
	for word in df_dict.keys():
		word_freq = df_dict[word]
		idfMax = math.log((max_df/(1 + word_freq)),10)
		idf_dict[word] = idfMax
	return idf_dict	

# Find tf-idf for all the variants
def variants(document_dict, input_wordList, idf_dict):
	tf_idf_score = {}
	for document in document_dict.keys():
		total_score = 0
		word_dict = document_dict[document]
		for term in input_wordList:
			if term in word_dict.keys():
				tf = word_dict[term]
			else:
				tf = 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
			idf = idf_dict[term]
			total_score += tf * idf
		tf_idf_score[document] = total_score
	return tf_idf_score

path = os.getcwd() + '\\stories\\stories'

document_dict = util.readFromPath(path, not_to_read)
doc_length_dict = util.storeDocLength(path, not_to_read)

input_string = "command was not helping either"
#input_string = "saga of the best"
#input_string = "that our college doors"
#input_string = "population of 100 billion"
input_wordList, input_string_length = util.parseInputString(input_string)

# df_dict, no_of_docs = findDfInputQuery(input_wordList, document_dict)
df_dict, no_of_docs = util.findDfAllDocs(document_dict)
k = 10

''' Try Variant 1
	unweighted tf-idf score
 	document_dict contains normalized tf
 	idf calculation on the basis of normalized inverse document frequency
'''
tf_idf_score = findUnweightedTfIdfScore(document_dict, doc_length_dict, input_wordList, df_dict)
print("The top K docs with unweighted score variant 1:")
util.printTopK(tf_idf_score, k)

''' Try Variant 1 b
	weighted tf-idf score
 	document_dict contains normalized tf
 	idf calculation on the basis of normalized inverse document frequency
'''
path = os.getcwd() + '\\stories\\stories\\SRE\\index.html'
tf_idf_score = weightedTfIdfScore(path, input_wordList, tf_idf_score, a = 0.5)
path = os.getcwd() + '\\stories\\stories\\index.html'
tf_idf_score = weightedTfIdfScore(path, input_wordList, tf_idf_score, a = 0.5)

print("The top K docs with weighted score:")
util.printTopK(tf_idf_score, k)

''' Try Variant 2 a
	unweighted tf-idf score
 	document_dict contains log normalization tf
 	idf_dict contains inverse document frequency smooth
'''
#df_dict, no_of_docs = findDfAllDocs(document_dict)
logNormalizedTf_dict = findLogNormalizationTf(document_dict)
idf_smooth_dict = findIdfSmooth(df_dict, no_of_docs)
tf_idf_score = variants(document_dict, input_wordList, idf_smooth_dict)

print("The top K docs with unweighted score with variant 2:")
util.printTopK(tf_idf_score, k)

''' Try Variant 2 b
	unweighted tf-idf score
 	document_dict contains log normalization tf
 	idf_dict contains inverse document frequency smooth
'''
path = os.getcwd() + '\\stories\\stories\\SRE\\index.html'
tf_idf_score = weightedTfIdfScore(path, input_wordList, tf_idf_score, a = 0.5)
path = os.getcwd() + '\\stories\\stories\\index.html'
tf_idf_score = weightedTfIdfScore(path, input_wordList, tf_idf_score, a = 0.5)

print("The top K docs with weighted score:")
util.printTopK(tf_idf_score, k)

''' Try Variant 3 a
	unweighted tf-idf score
 	document_dict contains double normalization K tf
 	idf_dict contains inverse document frequency max
'''
document_dict = doubleNormalizationKTf(document_dict)
max_df = max(df_dict.items(), key=operator.itemgetter(1))[1]
idf_dict = findIdfMax(df_dict, max_df)
tf_idf_score = variants(document_dict, input_wordList, idf_dict)

print("The top K docs with unweighted score with variant 3:")
util.printTopK(tf_idf_score, k)

''' Try Variant 3 b
	unweighted tf-idf score
 	document_dict contains double normalization K tf
 	idf_dict contains inverse document frequency max
'''
path = os.getcwd() + '\\stories\\stories\\SRE\\index.html'
tf_idf_score = weightedTfIdfScore(path, input_wordList, tf_idf_score, a = 0.5)
path = os.getcwd() + '\\stories\\stories\\index.html'
tf_idf_score = weightedTfIdfScore(path, input_wordList, tf_idf_score, a = 0.5)

print("The top K docs with weighted score:")
util.printTopK(tf_idf_score, k)
