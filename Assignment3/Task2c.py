import os
import matplotlib.pyplot as plt

path = os.getcwd() + '\\Q3\\IR-assignment-3-data.txt'
f = open(path)
pr_data = []

total_relevant = 0

for line in f:
	line_list = line.split(" ")							# Split the line on basis of space
	if line_list[1] == 'qid:4':							# check for qid:4
		feature_75_val = line_list[76].split(":")[1]	# feature_75_val contains the value of the feature 75
		if line_list[0] == '0':							# if relevance score is zero
			pr_data.append([0, float(feature_75_val)])	# store it as [0,feature_75_val]
		else:
			pr_data.append([1, float(feature_75_val)])	# else, store it as [1, feature_75_val]
			total_relevant += 1							# this is counted as the relevant document
	else:
		break

pr_data = sorted(pr_data, key=lambda x: x[1], reverse=True)	# sort the list in reverse order of the feature 75 values to plot the precision recall curve.
print(pr_data)

count = 1		#	

precision_list = []
recall_list = []

classified = 0

for i in range(len(pr_data)):							# traverse the precision data list
	precision_list.append(classified/count)				# append to the precision list the ratio of classified documents and total count encountered
	recall_list.append(classified/total_relevant)		# append to the recall list the ratio of classified documents and the total relevant documents
	inner_list = pr_data[i]
	if inner_list[0] == 1:								# if value is 1, then that document is correctly classified
		classified += 1
	count += 1											# increase the count in either case

plt.xlabel('Precision')
plt.ylabel('Recall')
plt.title('Precision-Recall Curve')
plt.plot(recall_list, precision_list)
plt.show()
