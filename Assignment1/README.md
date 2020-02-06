# InvertedIndexCreation

To build a unigram inverted index on 20newsgroups dataset[https://archive.ics.uci.edu/ml/datasets/Twenty+Newsgroups]

## Task - 1
Provide support for the following commands:
1. x OR y
2. x AND y
3. x AND NOT y
4. x OR NOT y
where x and y will be taken as input from the user.
Output:
- the number of docs retrieved
- the minimum number of total comparisons done (if any)
- the list of documents retrieved.

### METHODOLOGY:
1.	Reading of all the files from all the folders and storing them as list of tuples with each tuple as a (filename, data as a string).
2.	For each file stored in the list, performing the following steps:
    - Tokenizing the data of each file.
    - From these tokens, removing the punctuation.
    - Lemmatizing each of the words.
    - Removal of stop words.
    - Keeping a list of unique words per document.
    - Iterating over the unique word list and creating the inverted index. Inverted index was created using a dictionary with words as keys of dictionary and corresponding to each word, we are storing a tuple of structure 				
        (frequency, posting list)
      The final structure of inverted index thus obtained is:
        {word, (frequency, posting list)}
    - At last, sorting the posting list corresponding to each of the word.
3.	Lemmatization of input string query.
4.	Evaluating the query on the basis of priority of the operators.

### PREPROCESSING STEPS:
1.	Tokenization
2.	Punctuation Removal
3.	Lemmatization
4.	Stopword Removal

### ASSUMPTIONS:
1.	The folder contains all the files with different names. No duplicacy of name is present in the folders as a whole.
2.	As operator NOT cannot exist as a unary operator, the priority of operators considered is: AND NOT > OR NOT > AND > OR
3.	No stopwords have been entered into the input string.
4.	The AND, NOT, OR have all been input in uppercase in the input string.
5.	The input query consists of the words present in the documents.


## Task - 2
Provide support for searching for phrase queries using Positional Indexes. (Build index only on comp.graphics and rec.motorcycles)


### METHODOLOGY:
1.	Reading of all the files from the folders (comp.graphics and rec.motorcycles) and storing them as list of tuples with each tuple as a (filename, data as a string).
2.	For each file stored in the list, performing the following steps:
    -	Tokenizing the data of each file.
    -	From these tokens, removing the punctuation.
    -	Lemmatizing each of the words.
    -	Iterating over the lemmatized word list and creating the positional index. Positional index was created using a dictionary with words as keys of dictionary and corresponding to each word, we are storing a tuple of structure 	
          (frequency, dictionary of documents)
      The dictionary of documents contains docID as key and the positions within the document as the value.
      The final structure of positional index thus obtained is:
          {word, (frequency, {docId, positional List})}
    -	Removal of empty key from the dictionary
3.	Evaluating the query two words at a time when they are only next to each other.

### PREPROCESSING STEPS:
1.	Tokenization
2.	Punctuation Removal
3.	Lemmatization

### ASSUMPTIONS:
1.	The folder contains all the files with different names. No duplicacy of name is present in the folders as a whole.
2.	The input phrase query contains atleast 2 words.
