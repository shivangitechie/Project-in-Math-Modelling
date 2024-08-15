# **README for unstructured_text_preprocessing.py**

## **Overview**

This script combines text from multiple sources into a single file, performs text cleaning, lemmatization, and Named Entity Recognition (NER) using SpaCy and NLTK, and then saves the processed results.

### **Functionality**

**Combine Text Files:**

Merges the contents of three text files (american_football_glossary.txt, all_weeks_usage_notes.txt, and transcription.txt) into a single file, all_articles.txt, with each file's content separated by two newlines.

**Text Cleaning:**

Removes special characters and numbers.

Converts text to lowercase.

Tokenizes the text into individual words.

Removes common English stopwords.

Lemmatization and Named Entity Recognition (NER):

Uses SpaCy for lemmatization, reducing words to their base forms.

Extracts named entities and their types (e.g., person, organization) using SpaCy's NER capabilities.

### **Output:**


Prints the lemmatized words and named entities.

Optionally saves the processed results to preprocessed_text.txt.

### **Requirements**

Python 3.x

nltk library

spacy library

SpaCy model: en_core_web_sm

### **Installation**

Install the required libraries and SpaCy model using pip:

*pip install nltk spacy*

*python -m spacy download en_core_web_sm*

Additionally, download NLTK resources:

import nltk

nltk.download('stopwords')

nltk.download('punkt')

### **Usage**

Place the text files (american_football_glossary.txt, all_weeks_usage_notes.txt, transcription.txt) in the same directory as the script.


**Run the script to combine and preprocess the text:**

python text_preprocessing.py

Review the printed lemmatized words and named entities. Check preprocessed_text.txt for saved results.
