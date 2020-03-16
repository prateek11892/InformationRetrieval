import os
import math

def calculateDCG(data_list):
	dcg = 0
	for i in range(len(data_list)):
		dcg += (int(data_list[i][0])/(math.log(i+2,2)))
	return dcg

def calculateDCG50(data_list):
	dcg = 0
	for i in range(50):
		dcg += (int(data_list[i][0])/(math.log(i+2,2)))
	return dcg

path = os.getcwd() + '\\Q3\\IR-assignment-3-data.txt'	
f = open(path)											# open the file
result_list = []

for line in f:
	line_words = line.split()							# split the line on basis of space
	if line_words[1] == 'qid:4':						# if line is corresponding to query id 4
		result_list.append(line_words)					# create a list containing all rows with qid:4
	else:
		break

original_list = result_list.copy()						# store copy of result_list
result_list.sort()										# sort the result_list
result_list.reverse()									# reverse the result_list

dcg50 = calculateDCG50(original_list)					# calculate the dcg of top 50 rows of original_list
idcg50 = calculateDCG50(result_list)					# calculate the idcg of top 50 rows of result_list
nDCG50 = dcg50/idcg50									# calculate the nDCG of top 50 rows

print("nDCG50:",nDCG50)

dcg = calculateDCG(original_list)						# calculate the dcg of whole dataset containing qid:4
idcg = calculateDCG(result_list)						# calculate the idcg of whole dataset containing qid:4
nDCG = dcg/idcg 										# calculate nDCG on whole dataset containing qid:4

print("nDCG:",nDCG)

