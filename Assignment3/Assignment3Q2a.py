import os

path = os.getcwd() + '\\Q3\\IR-assignment-3-data.txt'

result_list = []
relevance_score_set = set()
f = open(path)									# open the file 
for line in f:									# read file line by line
	line_words = line.split()					# split the line by space
	if line_words[1] == 'qid:4':				# if the line is corresponding to qid:4
		relevance_score_set.add(line_words[0])	# add the different values of relevance score to a set relevance_score_set
		result_list.append(line_words)			# append whole row to the result_list
	else:
		break

result_list.sort()								# sort the result_list
result_list.reverse()							# reverse the result_list

fw = open('url_file.txt','a')					# open a new file 
for row_list in result_list:					# write the file in decreasing order of relevance score to obtain max DCG
	fw.write(' '.join(row_list))
	fw.write('\n')

fw.close()

# To calculate total number of such files possible
dict_relscore_count ={}						
for value in relevance_score_set:				# for each value in the set of relevance scores
	count = 0									
	for row_list in result_list:				
		if row_list[0] == value:	
			count += 1
	dict_relscore_count[value] = count 			# store the count of each relevance score
print(dict_relscore_count)

total_files = 1
for key in dict_relscore_count.keys():
	total_files = total_files * dict_relscore_count[key]	# calculate the total number of such files possible

print("Total number of such files possible:",total_files)