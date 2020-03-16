import os
import math
import util

def findTfIdfDictionary(unionDocs, document_dict, doc_length_dict, input_wordList, input_string_length):
	tf_idf_score = {}
	for document in unionDocs:
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

def findDocTfIDf(unionLists, document_dict, doc_length_dict, no_of_docs, df_dict):
	doc_tfidf = {}
	for document in unionLists:
		word_list = document_dict[document]
		word_tfidf = {}
		for word in word_list:
			normalizedTf = word_list[word]/doc_length_dict[document]
			idf = 1 + math.log((no_of_docs/df_dict[word]),2)
			word_tfidf[word] = normalizedTf * idf
		doc_tfidf[document] = word_tfidf
	return doc_tfidf

# Finding the cosine similarity
def findCosineSim(unionDocs, document_dict, input_query_tfidf, tf_idf_score, doc_tfidf, input_wordList):
	cosine_dict = {}
	for document in unionDocs:
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


def union(final_union_list, lst):
	for item in lst:
		if item[0] not in final_union_list:
			final_union_list.append(item[0])
	return final_union_list

def findUnion(input_wordList, highLowList, list_type):
	final_union_list = []
	for i in input_wordList:
		lst = highLowList[i][list_type]
		final_union_list = union(final_union_list, lst)
	return final_union_list

def addGd(cosine_dict, review_dict):
	#print("cosine_dict::",cosine_dict)
	netscore_dict = {}
	for key in cosine_dict.keys():
		gd = review_dict[key]
		totalScore = gd + cosine_dict[key]
		netscore_dict[key] = totalScore
	#print("netscore_dict::",netscore_dict)
	return netscore_dict

path = os.getcwd() + '\\Q1\\20_newsgroups'

pathFavorableReviews = os.getcwd()+'\\Q1\\file.txt'
mapping_dict = util.createDocumentMapping(path)
#print("mapping_dict",mapping_dict)

review_list = util.readReviewFile(pathFavorableReviews)
review_dict = util.convertTupToDict(review_list)
#print("review_list:",review_list)
doc_length_dict = util.storeDocLength(path, mapping_dict)
#print("doc_length_dict:",doc_length_dict)
document_dict = util.readFromPath(path, mapping_dict, doc_length_dict)
#print("document_dict",document_dict)
globalChampionList = util.createGlobalChampionList(document_dict)
#print("globalChampionList:",globalChampionList)
sortedGlobalChampionList = util.sortGlobalChampionListTf(globalChampionList)
#print("sortedGlobalChampionList:",sortedGlobalChampionList)
r = 50
highLowList = util.createHighLowList(sortedGlobalChampionList, r)
#print("highLowList more:",highLowList['more']['High'])
#print("highLowList elaborate:",highLowList['elaborate']['High'])


df_dict, no_of_docs = util.findDfAllDocs(document_dict)

K = 10

#input_string = "virtual reality"
input_string = "more elaborate"

input_words, input_string_length = util.parseInputString(input_string)
print("input_words:",input_words)
#input_words = input_string.split()
unionLists = findUnion(input_words, highLowList, 'High')
print("unionLists:",unionLists)
if len(unionLists) < K:
	print("Union of High Lists is less than K")
	unionLowLists = findUnion(input_words, highLowList, 'Low')
	unionLists = list(set(unionLists) | set(unionLowLists))

doc_tfidf = findDocTfIDf(unionLists, document_dict, doc_length_dict, no_of_docs, df_dict)

tf_idf_score,input_query_tfidf = findTfIdfDictionary(unionLists, document_dict, doc_length_dict, input_words, input_string_length)


cosine_dict = findCosineSim(unionLists, document_dict, input_query_tfidf, tf_idf_score, doc_tfidf, input_words)
netscore_dict = addGd(cosine_dict, review_dict)
print("The documents are as follows:")
util.printTopK(netscore_dict, K, mapping_dict)
