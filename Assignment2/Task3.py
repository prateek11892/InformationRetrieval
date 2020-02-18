import math
import readHTML
import util

not_to_read = [".descs",".header",".musings","index.html"]

# Finding tf-idf dictionary for each document
def findTfIdfDictionary(document_dict, doc_length_dict, input_wordList):
	tf_idf_score = {}
	for document in document_dict.keys():
		total_score = 0
		N = doc_length_dict[document]
		word_dict = document_dict[document]
		term_dict = {}
		input_query_tfidf = []
		for term in input_wordList:		
			if term in word_dict.keys():
				tf = word_dict[term]
			else:
				tf = 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
			df = df_dict[term]
			normalizedTf = tf/N
			idf = 1 + math.log((no_of_docs/df),2)
			total_score = normalizedTf * idf
			term_dict[term] = total_score
			input_query_tfidf.append((1/input_string_length) * idf)
		tf_idf_score[document] = term_dict
	return tf_idf_score, input_query_tfidf

# Calculate the weighted tf idf score
def weightedTfIdfScore(path, query_word_list, tf_idf_score, a):
	file_title_dict = readHTML.findFileTitleDict(path)
	for document in file_title_dict.keys():
		title = file_title_dict[document]
		title_list = title.split()
		title_stripped = util.removePunctuation(title_list)
		title_list = util.lemmatization(title_list)
		for word in query_word_list:
			weightedScore = tf_idf_score[document][word]
			if word in title_list:
				weightedScore += (tf_idf_score[document][word] * a)
			tf_idf_score[document][word] = weightedScore
	return tf_idf_score

# Finding the cosine similarity
def findCosineSim(document_dict, input_query_tfidf, tf_idf_score, doc_tfidf):
	cosine_dict = {}
	for document in document_dict.keys():
		sum = 0
		i = 0
		denom = 0
		input_denom = 0
		word_list = document_dict[document]
		for word in input_wordList:
			sum += (input_query_tfidf[i] * tf_idf_score[document][word])
			input_denom += (input_query_tfidf[i] * input_query_tfidf[i])
			i += 1
		for word in word_list:
			tfidf_val = doc_tfidf[document][word]
			denom += (tfidf_val*tfidf_val)
		total_denom = math.sqrt(input_denom * denom)
		cosine_dict[document] = sum / total_denom
	return cosine_dict

path = os.getcwd() + '\\stories\\stories'
document_dict = util.readFromPath(path, not_to_read)
doc_length_dict = util.storeDocLength(path, not_to_read)

input_string = "command was not helping either"
#input_string = "saga of the best"
#input_string = "that our college doors"
#input_string = "population of 100 billion"
input_wordList, input_string_length = util.parseInputString(input_string)

# Calculate df for all docs
df_dict, no_of_docs = util.findDfAllDocs(document_dict)

# Find the tf idf for each document
doc_tfidf = {}
for document in document_dict.keys():
	word_list = document_dict[document]
	word_tfidf = {}
	for word in word_list:
		normalizedTf = word_list[word]/doc_length_dict[document]
		idf = 1 + math.log((no_of_docs/df_dict[word]),2)
		word_tfidf[word] = normalizedTf * idf
	doc_tfidf[document] = word_tfidf
#

tf_idf_score,input_query_tfidf = findTfIdfDictionary(document_dict, doc_length_dict, input_wordList)

# Assumption: all words in query are unique
#print("input_query_tfidf:",input_query_tfidf)

# Finding the cosine similarity
cosine_dict = findCosineSim(document_dict, input_query_tfidf, tf_idf_score, doc_tfidf)

k = 10
print("The top k documents without weightage to title:")
util.printTopK(cosine_dict, k)

path = os.getcwd() + '\\stories\\stories\\SRE\\index.html'
tf_idf_score = weightedTfIdfScore(path, input_wordList, tf_idf_score, a = 0.5)
path = os.getcwd() + '\\stories\\stories\\index.html'
tf_idf_score = weightedTfIdfScore(path, input_wordList, tf_idf_score, a = 0.5)

#print("tf_idf_score:",tf_idf_score["sretrade.txt"])
cosine_dict = findCosineSim(document_dict, input_query_tfidf, tf_idf_score, doc_tfidf)

print("The top k documents with weightage to title:")
util.printTopK(cosine_dict, k)
