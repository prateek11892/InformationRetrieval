## Task - 1 : 
Download the 20newsgroup dataset[https://archive.ics.uci.edu/ml/datasets/Twenty+Newsgroups] for this question. You need to pick documents of comp.graphics, sci.med,talk.politics.misc, rec.sport.hockey, sci.space (5 classes) for text classification.

Implement the following algorithms for text classification:
1.  Naive Bayes
2.  kNN (vary k=1,3,5)

Feature selection techniques to be used with both algorithms:
1.  Tf-IDF
2.  Mutual Information

Implementation Points:
- Perform the data pre-processing steps.
- Split your dataset randomly into train: test ratio. You need to select the documents randomly for splitting. You are not supposed to split
documents in sequential order, for instance, choosing the first 800 documents in the train set and last 200 in the test set for the train: test
ratio of 80:20.
- Implement the TF-IDF scoring technique and mutual information technique for efficient feature selection.
- For each class - train your Naive Bayes Classifier and kNN on the training data.
- Test your classifiers on testing data and report the confusion matrix and overall accuracy .
- Perform the above steps on 50:50, 70:30, and 80:20 training and testing split ratios.
- Compare and analyze the performance of the above-mentioned two classification algorithms for both the feature selection techniques across different train: test ratios. Use graphs to report the performance comparison. Also, mention your inferences from the graphs . Example of a graph you can report - a graph showing the performance of kNN for different values of k.

### METHODOLOGY:

#### NAÏVE BAYES TEXT CLASSIFICATION
1.  Reading of all the files from the required folders with preprocessing techniques mentioned below and storing them as a dataframe.
2.	Divide the data into training and testing data.
3.	Find prior probability of each of the classes of training data. Since each class can have different number of documents, the prior probability will be different. Also storing the count of documents from each class from the training dataset.
4.	Create a class wise corpus which stores all the words encountered in all the documents of the class (including their multiple occurrences). This has to be done on training dataset.
5.	Find the universal vocabulary of the training set.

##### Feature Selection Method 1: Tf-IDf
6.	Find tf of all tokens of each class as number of times that token appears in the documents of that class.
7.	Find df of each of the token of the universal vocabulary as to into how many classes that token occurs.
8.	Find the tf-idf score corresponding to each of the class and its words. Tf-idf score has been found using the formula for the normalized tf and normalized idf (no of classes/df value).
9.	Sort the tf-idf dictionary in decreasing order of tf-idf value and find the top k words from each of the classes. Top k features have been found by taking the class having smallest size of the corpus and taking top 60% of those words.
10.	Find the conditional probability and prediction for Naïve Bayes according to the following:
    - For each row in testing data:
      - For each class in number of classes:
        - For each word in testing data document
          - If word is present in top k words of that folder, then take the tf of word of that class and assign it as the numerator for finding cmap.
          - Find the denominator as the sum of length of the corpus of the particular folder and length of universal vocab
          - Divide the numerator and denominator
          - Take log(base10)
          - Add to the probability this value.
        - Add the log of prior probability of that class to the probability.
        - Add this probability to a list so that all classes probability is at a single place.
      - Find the max of all the probability and assign the predicted class to the testing document.
11.	Calculate the accuracy of the model.
12.	Compute the confusion matrix of the model.

##### Feature Selection Method 2: Mutual Information
6.	Find the N11 value. It can be found by finding the frequency of each word of universal vocabulary corresponding to each of the classes. By frequency, it is meant that number of documents the term appears in a particular class.
7.	Find the N10 value. It can be found from the N11 values. The N10 value for a particular term in a particular class is the sum of all the frequency of that word occurring in other classes except the current class.
8.	Find the N01 value. This can be found by subtracting the N11 value from the total documents of the class.
9.	Find the N00 value. This can be found by subtracting N11 value and N10 value from the total number of training documents.
10.	Find the Mutual Information on the basis of parameters calculated above.
11.	Find top k features by sorting the mutual information values for each class in decreasing order and taking top 60% of those words.
12.	Find the conditional probability and prediction for Naïve Bayes according to the following:
    - For each row in testing data:
      - For each class in number of classes:
        - For each word in testing data document
          - If word is present in top k words of that class and tf dictionary of that class, then take the tf of word of that class and assign it as the numerator for finding cmap.
          - Find the denominator as the sum of length of the corpus of the particular folder and length of universal vocab
          - Divide the numerator and denominator
          - Take log(base10)
          - Add to the probability this value.
        - Add the log of prior probability of that class to the probability.
        - Add this probability to a list so that all classes probability is at a single place.
     -  Find the max of all the probability and assign the predicted class to the testing document.
13.	Calculate the accuracy of the model.
14.	Compute the confusion matrix of the model.

##### PREPROCESSING STEPS:
1.	Tokenization
2.	Punctuation Removal
3.	Lemmatization
4.  Stopword Removal

#### KNN TEXT CLASSIFICATION:

##### Feature Selection Methods: Tf-IDf & Mutual Information

1.	The feature selection methodology as done in the previous model are to be used as such. Hence at the start of the model KNN, we have the class wise top k features present each for Tf-Idf feature selection and Mutual Information feature selection.
2.	From the top k features classwise, we need to create for each doc of its class, the feature vector of its top k features and assign term frequency to each of the top features present in that doc.
3.	For each document vector, create the normalization factor by the dot product of the vector with itself.
4.	Normalize the each tf value in the training doc vector.
5.	Similarly, for the testing document, create the doc vector corresponding to each of the classes.
6.	So, for each testing document we have 5 vectors each corresponding to each of the classes.
7.	Normalize each of the document vector in the aforementioned manner.
8.	Calculate the Euclidean distance of each of the testing document vector with each of the training document present in the same class.
9.	For each testing document, we get the array of Euclidean distances the length of the array being the number of training documents.
10.	Find the minimum K distances and assign the label to the testing document same as the majority label present in the selected minimum.

##### PREPROCESSING STEPS:
1.	Tokenization
2.	Punctuation Removal
3.	Lemmatization
4.  Stopword Removal
