# Structured recipe from unstructured corpus
Group id: 16

Group Members: 
1.  Suryank Tiwari (MT19019)
2.  Rose Verma (MT19052)
3.  Prateek Agarwal (MT19070)

## Datasets:

1.  NYT ingredient data present in the folder as nyt-ingredients-snapshot-2015.csv
2.  Epirecipes data present as full_format_recipes.json under the folder data.

## Configuration:

1.  In roundtrip.sh file, provide the path to the crf_learn and crf_test as provided in the current roundtrip.sh file.
2.  If you do not want to configure this, model_file has already been provided under the tmp folder so that you can continue with the Step 5 of "How to Run the program".

## How to Run the program:

1.  Unzip the folder
2.  To run the model on dataset 1, run the script.py file with three command line arguments namely 
    - Number of training rows
    - Number of testing rows
    - Number of ingredient lines from the end of the input csv file you want to test upon
    - P.S. This model was tested with maximum 20000 training rows, 2000 testing rows and 2000 ingredient lines
3.  This will generate the intermediate "model_file" under the tmp folder which is used to generate the resultant json file named as "results.json".
4.  Step 2 is important and Step 5 is optional.
5.  If you want to run the model on dataset 2, run the parseJson.py dile with one command line argument namely
    - The number of recipes to run the model on.
    - P.S. The dataset contains more than 20k recipes and it may take time if we run on whole length data. Prescribed number of recipes would be upto 500.
6.  This results in the resultant file named as final.json. This is the structured data with respect to each of the recipe title.
7.  After getting the structured data from either the Step 2 or Step 5, run the KGB.py file with one command line argument
    - Name of the json file using which wou want to create the graph.
8.  Upon running this will show a graph of the whole system containing the input json file recipes as well as community graph of the recipe. Also, you will have an option to generate the query specific sub-knowledge graph for the entered query.
9.  To exit this, enter the response to "Enter Query" as "exit" (without double quotes).

##### PREPROCESSING STEPS:
1.	Tokenization
2.	Punctuation Removal
3.	Lemmatization
4.  Stopword Removal
5.  Leading and trailing space removal
6.  Lowercase conversion
