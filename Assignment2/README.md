# DocumentRanking

To build a unigram inverted index on 20newsgroups dataset[https://archive.ics.uci.edu/ml/datasets/Twenty+Newsgroups]

## Task - 1 : Jaccard Coefficient based document retrieval
For each query, your system will output top k documents based on jaccard score.

### METHODOLOGY:
1.	Reading of all the files (except .descs, .header, .musings and index.html) from all the folders (except FARNON) and storing them as list of tuples with each tuple as a (filename, set of words in each file).
2.	For each word set stored in the tuple, performing the following steps:
    -	Check for each of the word present in the input query string.
        *	If the word is present in the word set, increment the counter.
    -	The counter will represent the no. of the words present in the document.
    -	Find the union of the words in document and 
    -	The Jaccard coefficient can be then be stored corresponding to each filename in a dictionary.	{filename, Jaccard_coefficient_val}
3.	Find out the top K documents on the basis of highest to lowest Jaccard coefficient values.

### PREPROCESSING STEPS:
1.	Tokenization
2.	Punctuation Removal
3.	Lemmatization

### ASSUMPTIONS:
1.	The folder contains all the files with different names. No duplicacy of name is present in the folders as a whole.

## Task - 2 : Tf-Idf based document retrieval
For each query, your system will output top k documents based on tf-idf-matching-score. Implement different versions of Tf-Idf based document retrieval then compare and analyze which performs better and why. Give special attention to the terms in the document title and analyze the change in result with and without attention to terms in title.

### METHODOLOGY:
1.	Reading of all the files (except .descs, .header, .musings and index.html) from all the folders (except FARNON) and storing them as dictionary of dictionary to store the term frequency with respect to each term and document. The data structure would something be like this: {filename, {term, term_frequency}}
2.	For each document, store the document length in a dictionary:{filename, document_length}
3.	Find the document frequency for all the terms present in all the documents and storing in the dictionary: {word, doc_freq}
4.	For each of the term present in the input query, find the unweighted tf-idf score using the formula:
    - Tf-idf = (tf/doc_length)X(1+log(Total no of docs/df))		{Log is base 10}
5.	Now summing up all the tf-idf score for all the terms present in the query and store the tf-idf score w.r.t each document.
6.	Find out the top K documents on the basis of highest to lowest Jaccard coefficient values. This will be unweighted tf-idf based document retrieval with normalized tf and normalized idf formula.
7.	To give weightage to title, parse the document index.html in SRE folder as well as outside to keep track of the document title in a dictionary.
8.	For each term in input query, if that term is present in the title, then increase the tf-idf score to 1.5 times the original tf-idf w.r.t each document. This will give us weighted tf-idf based document retrieval.
9.	This process is repeated with different tf-idf variants in Step 4.
10.	Variant – 2
    -	For each term in a document, log normalize the tf:
      * Tf = 1 + log(tf)
    -	Modify the idf to idf smooth:
      * Idf = log(Total docs/(1 + df))
11.	Variant – 3
    -	For each term in a document, double normalize K the tf:
      * Tf = K + (1-K)(tf/max(tf in doc.))	[K = 0.5]
    -	Modify the idf to idf max:
      * Idf = log((max(df))/(1+df))

### PREPROCESSING STEPS:
1.	Tokenization
2.	Punctuation Removal
3.	Lemmatization

### ASSUMPTIONS:
1.	The folder contains all the files with different names. No duplicacy of name is present in the folders as a whole.

## Task - 3 : Tf-Idf based vector space document retrieval
For each query, your system will output top k documents based on a cosine similarity between query and document vector. Give special attention to the terms in the document title and analyze the change in result with and without attention to terms in title.


### METHODOLOGY:
1.	Reading of all the files (except .descs, .header, .musings and index.html) from all the folders (except FARNON) and storing them as dictionary of dictionary to store the term frequency with respect to each term and document. The data structure would something be like this: {filename, {term, term_frequency}}
2.	For each document, store the document length in a dictionary:{filename, document_length}
3.	Find the document frequency for all the terms present in all the documents and storing in the dictionary: {word, doc_freq}
4.	For each of the term present in the input query, find the unweighted tf-idf score using the formula:
    - Tf-idf = (tf/doc_length)X(1+log(Total no of docs/df))		{Log is base 10}
5.	Now store all the tf-idf score for all the terms present in the query w.r.t each document and each term in a dictionary. This will work as a document vector.
6.	Find the query vector.
7.	Find the cosine similarity of the query with each of the document and store the cosine similarity w.r.t. each of the document.
8.	Find out the top K documents on the basis of highest to lowest Jaccard coefficient values. This will be unweighted tf-idf based document retrieval with normalized tf and normalized idf formula.
9.	To give weightage to title, parse the document index.html in SRE folder as well as outside to keep track of the document title in a dictionary.
10.	For each term in input query, if that term is present in the title, then increase the tf-idf score to 1.5 times the original tf-idf w.r.t each document and then find out the cosine similarity as in Step 7. This will give us weighted tf-idf based document retrieval.

### PREPROCESSING STEPS:
1.	Tokenization
2.	Punctuation Removal
3.	Lemmatization

### ASSUMPTIONS:
1.	The folder contains all the files with different names. No duplicacy of name is present in the folders as a whole.
2.	The input query contains each word only once in the query.

## Task - 4 : Edit Distance
Download the dictionary from [http://www.gwicks.net/dictionaries.htm] (UK ENGLISH - 65,000 words)
Take a sentence as input from user. For each non dictionary words present in the sentence suggest top k words on the basis of minimum edit distance. Cost of operations is defined as:
1.  Insert: 2
2.  Delete: 1
3.  Replace: 3

### METHODOLOGY:
1.	Reading of the file from the folder (english2) and storing them in a list (namely, wordList).
2.	For the input query, do the tokenization, removal of punctuation and lemmatization.
3.	For each word in the input string:
    -	Check whether the word is stored in the wordlist.
    -	If the word is not stored in the word list, then calculate the edit distance from all the words present in the wordList and store in the dictionary having the word and their corresponding edit distance with the current input word
    -	For all the words in the dictionary, sort the dictionary on the basis of the value (editDistance value) in the ascending order.
    -	From the sorted dictionary, select the top K values and display them.

### PREPROCESSING STEPS:
1.	Tokenization
2.	Punctuation Removal
3.	Lemmatization
