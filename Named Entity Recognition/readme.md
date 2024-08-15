# Named Entity Recognition (NER) using Pre-trained Transformer Models

## Overview

This script uses a pre-trained Named Entity Recognition (NER) model from the Hugging Face Transformers library to identify and classify named entities within text data.

File: ner_extraction.py

**Dependencies**

Python 3.x

Transformers (transformers)

Pandas (pandas)

NumPy (numpy)

**Installation**

Before running the script, make sure the necessary libraries are installed:

pip install transformers pandas numpy

**Code Explanation**

**Loading the Pre-trained NER Model:**

from transformers import pipeline

ner_pipeline = pipeline("ner", grouped_entities=True)

The pipeline() function from the Transformers library loads a pre-trained NER model. The grouped_entities=True parameter is used to group together tokens that belong to the same entity.

**Loading Preprocessed Text Data:**

with open('preprocessed_text.txt', 'r') as file:

    text = file.read()
    
The script loads preprocessed text data from a file named preprocessed_text.txt.

**Processing Text Data:**

lines = text.split('\n')

The text is split into individual lines based on newline characters for easier processing.

**Applying NER to Each Line:**

ner_results = []

for line in lines:

    if line.strip():
    
        ner_results.append(ner_pipeline(line))
        
For each line in the text, the NER model is applied if the line contains non-empty text. The results are stored in the ner_results list.

**Combining NER Results into a DataFrame:**

ner_df = pd.DataFrame(ner_results)

print(ner_df.head())

The NER results are organized into a Pandas DataFrame for easier viewing and analysis.


**Output**

The script prints out the first few rows of the DataFrame containing the identified named entities and their corresponding classifications.

**How to Run**

Ensure that you have preprocessed text data saved as preprocessed_text.txt.

**Run the script:**

python ner_extraction.py

This script is useful for extracting entities like player names, teams, and other relevant terms from articles or reports in a fantasy football application.

**Next Steps**

Extend the script to handle more complex text data.

Integrate the NER results into downstream tasks like player classification or sentiment analysis.
