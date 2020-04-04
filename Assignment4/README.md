## Task - 1 : 
Download the 20newsgroup dataset[https://archive.ics.uci.edu/ml/datasets/Twenty+Newsgroups] for this question. You need to pick documents of comp.graphics, sci.med,talk.politics.misc, rec.sport.hockey, sci.space.

Implement a cosine similarity measure with tf-idf weighting. Your index should contain the information that you will need to calculate the cosine similarity measure such as tf and idf values.

### METHODOLOGY:
1.  Reading of all the files from the required folders and storing them as dictionary of dictionary with structure as {docnumber,{word, tf}}
2.  Creating a mapping dictionary to assign unique name to each of the files present in different folders so as not to have collision in filenames.
3.  Find the document frequency for all the words present in the vocabulary.
4.  Find the tf-idf score corresponding to each of the document and its words. Tf-idf score has been found using the formula for the normalized tf and normalized idf.
5.  Generate the vocabulary vector using the tf_idf_score dictionary.
6.  Since the vocab_vector takes approximately 10 minutes to compute, the same has been stored using pickle.
7.  Let the user input the query.
8.  Apply the same preprocessing steps on the input query as the vocabulary and find the corresponding input query tf-idf.
9.  Generate the query vector.
10. Let the user input the value of k(top k documents), value of p(p% relevant documents) and relevant folder which can be treated as the ground truth folder to which the query belongs to.
11. Fetch k documents from the corpus using cosine similarity and this modified query vector.
12. The documents fetched in the first iteration will be the required documents.


### PREPROCESSING STEPS:
1.	Tokenization
2.	Punctuation Removal
3.	Lemmatization
4.  Stopword Removal

## Task - 2 : 
Implement the Rocchio Algorithm(with query refinement)
1.  You have to display top k (k should be at least 100) docs for the initial query.
2.  To provide feedback, you have to mark p% of k docs to be relevant. The p% selected documents would be from the folder which is assumed to be the Actual relevant set (Ground truth).
For e.g., if Ground Truth relevant are docs of the folder sci.med and k = 100 then, for p = 10%, you have to mark 10% of 100 i.e. 10 docs of sci.med as relevant from the top of the retrieved list of 100 docs.
3.  Show the revised top k results after performing relevance feedback. Mark the documents as * which were judged as relevant during the relevant feedback phase.
4.  Use α= 1, β= 0.75, and γ=0.25 as parameters for the Rocchio’s algorithm. For each iteration of the relevance feedback, you have to show top k docs and provide feedback in the same way as stated above.
5.  Consider the following queries & all documents inside the given folder as a relevant set (ground truth).
    - Query 1: Pretty good opinions on biochemistry machines
    - Relevant set 1: Documents inside folder sci.med
    - Query 2: Scientific tools for preserving rights and body
    - Relevant set 2: Documents inside folder talk.politics.misc
    - Query 3: Frequently asked questions on State-of-the-art visualisation tools
    - Relevant set 3: Documents inside folder sci.med
    - Report the following:
        *  PR curve plot for each of the queries. You have to plot the PR curve after each relevance feedback iteration. (Do around 3 to 4 feedback iterations)
        *  MAP for the above-mentioned query set after each relevance feedback iteration.
    - Note: This set of queries are just for reference, keep your code generalized to be able to accept different queries and mark whatever documents to be relevant as per our wish.
6.  In the report, show how the query vector changes (for this particular set of queries) after applying each iteration of the Rocchio Algorithm. Justify or explain the results after each iteration. Show a 2D TSNE plot of the vectors to demonstrate the difference. You can use Sklearn’s inbuilt functions to make this plot.

### METHODOLOGY:
1.  Reading of all the files from the required folders and storing them as dictionary of dictionary with structure as {docnumber,{word, tf}}
2.  Creating a mapping dictionary to assign unique name to each of the files present in different folders so as not to have collision in filenames.
3.  Find the document frequency for all the words present in the vocabulary.
4.  Find the tf-idf score corresponding to each of the document and its words. Tf-idf score has been found using the formula for the normalized tf and normalized idf.
5.  Generate the vocabulary vector using the tf_idf_score dictionary.
6.  Since the vocab_vector takes approximately 10 minutes to compute, the same has been stored using pickle.
7.  Let the user input the query.
8.  Apply the same preprocessing steps on the input query as the vocabulary and find the corresponding input query tf-idf.
9.  Generate the query vector.
10. Let the user input the value of k(top k documents), value of p(p% relevant documents) and relevant folder which can be treated as the ground truth folder to which the query belongs to.
11. Input the number of iterations to be performed.
12. For each iteration,
    -	Modify the query vector using the Rocchio SMART formula.(Except for the first iteration, where the initial query vector becomes the modified query vector too). Here, we make use of the centroid method which finds the centroid for a given set of documents.
    -	For the modified query vector, change the elements value to zero if the value comes out to be negative.
    -	Fetch k documents from the corpus using cosine similarity and this modified query vector.
    -	Fetch the ground truth set of documents from the relevant folder provided earlier.
    -	Get the feedback from the user to provide only the relevant documents to be selected from the relevant folder documents (marked with ** in beginning and end). Rest documents would automatically come under the non relevant documents category.
    -	Plot the precision and recall on the basis of documents retrieved.
    -	Calculate the value of MAP.
    -	Add the relevant as well as irrelevant documents to already annotated document set which won’t be used in next iteration.
    -	Plot the TSNE graph.


### PREPROCESSING STEPS:
1.	Tokenization
2.	Punctuation Removal
3.	Lemmatization
4.  Stopword Removal

### ASSUMPTIONS:
1.  The automated feedback selects the top p% documents from the relevant folder. If top k documents contain more than p% documents, then top p% documents are selected else all the documents of that particular folder retrieved are selected. (Automated feedback is done to ensure no trouble for typing down the relevant documents manually due to the reason being that p% of top k can be large).
2.  The query contains terms which are present in the docs.
3.  Top k documents are retrieved in the decreasing order of cosine similarity scores.
