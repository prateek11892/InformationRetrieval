## Task - 1 : Static quality ordering
Consider the 20newsgroup dataset[https://archive.ics.uci.edu/ml/datasets/Twenty+Newsgroups] for this question. Download this[https://github.com/prateek11892/InformationRetrieval/blob/master/Assignment3/file.txt] file containing the number of favourable reviews for each of the documents in the corpus. The first column of this file denotes the doc no. and the second column denotes the corresponding number of favourable reviews.The doc no. 1-1000 belong to alt.athiesm, the next 1000(i.e. 1001-2000) belong to comp.graphics and so on.

You need to implement static quality ordering on the above corpus. You have to extract a static quality score for each document from the number of favourable reviews as provided above. Maintain a global champion list for each term sorted by a common ordering (i.e. static
quality score). This champion list for a term ‘t’ is made up of two posting lists consisting of a disjointed set of documents. The first list is the high list containing documents with highest tf values for ‘t’ and the second list is the low list containing other documents having term ‘t’. You need to define a suitable heuristic to select the minimal efficient value of ‘r’ where ‘r’ is the
number of documents to be contained in the high list.

You need to return K documents (where K will be given at runtime). During query processing, only the high lists of query terms are scanned first to compute net scores and return as output. If less than K documents are returned then go for low lists. Report proper analysis for all the values of ‘r’ that you tried and the reason behind choosing that value of ‘r’.

### METHODOLOGY:
1.	Reading of all the files from all the folders and storing them as dictionary of dictionary with structure as {docnumber,{word, tf}}
2.	Read the reviews file and store it as a dictionary of normalized reviews {docno, normalizedScore}
3.	Create a global champion list for each word from the dictionary obtained in Step 1
4.  Sort this global champion list on the basis of normalized tf value.
5.  Take a value of r and segregate the global champion list into high and low list corresponding to each word.
6.  Find df of all words in the docs.
7.  Lemmatization of input string query.
8.  Finding union of high lists of all the input query terms. If this union contains less than k terms, then traverses the low lists as well and unions the high and low lists of the query terms. 
9.  From this union, the cosine of the query is done with the documents present in the union. From this, the top k documents are retrieved on the basis of netscore calculated as
Netscore = g(d) + cosine score  

### PREPROCESSING STEPS:
1.	Tokenization
2.	Punctuation Removal
3.	Lemmatization

## Task - 2 : Concept of DCG, IDCG and nDCG
Use the data file provided here[https://drive.google.com/file/d/1aG_sOmDqN2cIx0ChUdxfGjdSVZAt7LGA/view]. This has been taken from Microsoft learning to rank dataset, which can be found here[https://www.microsoft.com/en-us/research/project/mslr/?from=http%3A%2F%2Fresearch.microsoft.com%2Fen-us%2Fprojects%2Fmslr%2Fdownload.aspx]. Read about the dataset carefully, and what all it contains.
1.  Make a file having URLs in order of max DCG. State how many such files could be made.
2.  Compute nDCG
    -  At 50
    -  For the whole dataset.
For the above two questions, results have to be produced for qid:4 only and consider the relevance judgement labels as the relevance score.
3.  Assume a model that simply ranks URLs on the basis of the value of feature 75 (sum of TF-IDF on the whole document) i.e. the higher the value, the more relevant the URL. Assume any non zero relevance judgment value to be relevant. Plot a Precision-Recall curve for query “qid:4”.

### METHODOLOGY:
#### Part(1)
1.	Reading of the file assignment-3-data.txt and appending all the rows to a list (result_list) corresponding to the qid:4. Also make a set of relevance score values available.
2.	Reverse sort the list (result_list).
3.	Write this reverse sorted list to a file. Since the max DCG is the ideal DCG which is obtained in the decreasing order of the relevance score, therefore, this file denotes the order of rows which can generate the max DCG.
4.	To calculate the total number of such files possible, we need to compute the number of rows corresponding to each relevance score value. This can be obtained by multiplying the count of each relevance score counter. 

#### Part(2)
1.	Reading of the file assignment-3-data.txt and appending all the rows to a list (result_list) corresponding to the qid:4.
2.	Make a copy of the result_list and store it in another list named original_list. Reverse sort the list (result_list).
3.	For finding the nDCG at 50:
    - We take top 50 rows from the original_list and calculate dcg using the formula: ∑ (rel.score/log2(i+1))
    - Similarly calculate the idcg over the top 50 rows of result_list.
    - Divide dcg by idcg to obtain nDCG at 50.
4.	For finding the nDCG for whole dataset with qid:4:
    - We take all rows corresponding to qid:4 from the original_list and calculate dcg using the formula: ∑ (rel.score/log2(i+1))
    - Similarly calculate the idcg over all rows corresponding to qid:4 of result_list.
    - Divide dcg by idcg to obtain nDCG.
    
#### Part(3)
1.  Reading of the file assignment-3-data.txt and appending all the values of feature 75 of rows with qid:4 to the list on basis of whether the relevance score value is 0 or greater than 0. If 0 then append 0 and feature 75 value else, append 1 and feature 75 value. Also, keep a count of the total relevant rows on basis of metric that relevance scores greater than 0 are relevant.
2.	Separate the precision list and recall list on the basis of their definitions
3.	Plot the curve.
