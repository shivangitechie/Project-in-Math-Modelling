import re
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('punkt')

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Combine contents of the three files into 'all_articles.txt'
file_names = ['american_football_glossary.txt', 'all_weeks_usage_notes.txt', 'transcription.txt']

with open('all_articles.txt', 'w') as all_articles:
    for file_name in file_names:
        with open(file_name, 'r') as file:
            content = file.read()
            all_articles.write(content + "\n\n")  # Add two newlines between each file's content

# Read the combined text file
with open('all_articles.txt', 'r') as file:
    text = file.read()

# Function for text cleaning
def clean_text(text):
    # Remove special characters and numbers
    text = re.sub(r'[^A-Za-z\s]', '', text)
    # Convert text to lowercase
    text = text.lower()
    # Tokenize text
    words = word_tokenize(text)
    # Remove stopwords
    words = [word for word in words if word not in stopwords.words('english')]
    return words

# Function for lemmatization and NER
def lemmatize_and_ner(words):
    doc = nlp(" ".join(words))
    # Lemmatization
    lemmatized_words = [token.lemma_ for token in doc]
    # Named Entity Recognition (NER)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    return lemmatized_words, entities

# Clean the text
cleaned_words = clean_text(text)

# Lemmatization and NER
lemmatized_words, entities = lemmatize_and_ner(cleaned_words)

# Print the results
print("Lemmatized Words:\n", lemmatized_words)
print("\nNamed Entities:\n", entities)

# Optional: Save results to a file
with open('preprocessed_text.txt', 'w') as file:
    file.write("Lemmatized Words:\n")
    file.write(" ".join(lemmatized_words))
    file.write("\n\nNamed Entities:\n")
    for entity, label in entities:
        file.write(f"{entity} ({label})\n")
