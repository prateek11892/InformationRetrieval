import os
import util
import operator
from collections import Counter

def editDistance(word1, word2):
	m = len(word1) + 1
	n = len(word2) + 1
	edit = [[0 for j in range(n)] for i in range(m)] 
	for j in range(n):
		edit[0][j] = j
	
	for i in range(1,m):
		edit[i][0] = i
		j = 1		
		for j in range(1,n):
			editList = []
			insert = edit[i][j-1] + 2
			delete = edit[i-1][j] + 1
			editList.append(insert)
			editList.append(delete)
			if word1[i - 1] == word2[j - 1]:
				replace = edit[i-1][j-1]
			else:
				replace = edit[i-1][j-1] + 3
			editList.append(replace)
			edit[i][j] = min(editList)
			j = j + 1
		i = i + 1
	return edit[m-1][n-1]

def readFromPath(path):
	wordList = []
	f = open(path, "r")
	#data = f.read()
	lines = f.readlines() 
	for line in lines:
		wordList.append(line.strip())
	return wordList
path = os.getcwd() + '\\english2\\english2.txt'

wordList = readFromPath(path)
print(len(wordList))
input_string = "i love cricket, 'but utna ni like karta"
k = 5
input_wordList = input_string.split()
input_wordList = util.removePunctuation(input_wordList)
input_wordList = util.lemmatization(input_wordList)

for input_word in input_wordList:
	dict_suggestions = {}
	if input_word not in wordList:
		for word in wordList:
			dist = editDistance(input_word, word)
			dict_suggestions[word] = dist
		sorted_d = sorted(dict_suggestions.items(), key=operator.itemgetter(1))
		i = 0
		print("Suggestions for the word:",input_word)
		while i < k:
			print(sorted_d[i])
			i = i + 1
